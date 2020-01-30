// Fill out your copyright notice in the Description page of Project Settings.


#include "MainGameModeBase.h"
#include "Client.h"
#include "Engine/KBEngine.h"
#include "Engine/Entity.h"
#include "EntityBase.h"



AMainGameModeBase::AMainGameModeBase(const FObjectInitializer& ObjectInitializer) : Super(ObjectInitializer)
{
	// Set this character to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
	PrimaryActorTick.bCanEverTick = true;
}


void AMainGameModeBase::installEvents()
{
	Super::installEvents();

	// in world
	// 这个事件触发时我们需要切换地图到游戏世界地图
	KBENGINE_REGISTER_EVENT(KBEngine::KBEventTypes::addSpaceGeometryMapping, addSpaceGeometryMapping);
	KBENGINE_REGISTER_EVENT(KBEngine::KBEventTypes::onEnterWorld, onEnterWorld);
	KBENGINE_REGISTER_EVENT(KBEngine::KBEventTypes::onLeaveWorld, onLeaveWorld);
	KBENGINE_REGISTER_EVENT(KBEngine::KBEventTypes::onEnterSpace, onEnterSpace);
	KBENGINE_REGISTER_EVENT(KBEngine::KBEventTypes::onLeaveSpace, onLeaveSpace);
	KBENGINE_REGISTER_EVENT(KBEngine::KBEventTypes::set_position, set_position);
	KBENGINE_REGISTER_EVENT(KBEngine::KBEventTypes::set_direction, set_direction);
	KBENGINE_REGISTER_EVENT(KBEngine::KBEventTypes::updatePosition, updatePosition);
	KBENGINE_REGISTER_EVENT(KBEngine::KBEventTypes::onControlled, onControlled);

	// in world(register by scripts)
	KBENGINE_REGISTER_EVENT("set_HP", set_HP);
	KBENGINE_REGISTER_EVENT("set_MP", set_MP);
	KBENGINE_REGISTER_EVENT("set_HP_Max", set_HP_Max);
	KBENGINE_REGISTER_EVENT("set_MP_Max", set_MP_Max);
	KBENGINE_REGISTER_EVENT("set_level", set_level);
	KBENGINE_REGISTER_EVENT("set_name", set_name);
	KBENGINE_REGISTER_EVENT("set_moveSpeed", set_moveSpeed);
	KBENGINE_REGISTER_EVENT("set_modelScale", set_modelScale);
	KBENGINE_REGISTER_EVENT("set_modelID", set_modelID);
	KBENGINE_REGISTER_EVENT("set_entityNO", set_entityNO);
	KBENGINE_REGISTER_EVENT("set_flags", set_flags);
	KBENGINE_REGISTER_EVENT("set_state", set_state);
	KBENGINE_REGISTER_EVENT("set_subState", set_subState);
	KBENGINE_REGISTER_EVENT("set_forbids", set_forbids);
	KBENGINE_REGISTER_EVENT("recvDamage", recvDamage);
	KBENGINE_REGISTER_EVENT("otherAvatarOnJump", otherAvatarOnJump);
	KBENGINE_REGISTER_EVENT("onAddSkill", onAddSkill);
}

// Called when the game starts or when spawned
void AMainGameModeBase::BeginPlay()
{
	Super::BeginPlay();

	check(KBEngine::KBEngineApp::getSingleton().isInitialized());

	// 如果已经有被创建的实体，说明他们在上一个场景未来得及跳转之前已经通知创建了，但由于我们的world场景并没有来得及创建，这部分实体进入世界事件已经漏掉
	// 此时我们需要再次触发一次onEnterWorld，让表现层能够在游戏场景中创建出所有的实体
	KBEngine::KBEngineApp::ENTITIES_MAP& entities = KBEngine::KBEngineApp::getSingleton().entities();
	for (auto& item : entities)
	{
		KBEngine::Entity* pEntity = item.Value;

		UKBEventData_onEnterWorld* pEventData = NewObject<UKBEventData_onEnterWorld>();
		pEventData->entityID = pEntity->id();
		pEventData->spaceID = KBEngine::KBEngineApp::getSingleton().spaceID();
		KBPos2UE4Pos(pEventData->position, pEntity->position);
		pEventData->direction = pEntity->direction;
		pEventData->moveSpeed = pEntity->velocity();
		pEventData->isOnGround = pEntity->isOnGround();
		pEventData->isPlayer = pEntity->isPlayer();
		pEventData->entityClassName = pEntity->className();
		pEventData->res = TEXT("");
		KBENGINE_EVENT_FIRE(KBEngine::KBEventTypes::onEnterWorld, pEventData);
	}
}

void AMainGameModeBase::reqRelive(int reliveType)
{
	// 由于玩家的Avatar实体注册了该事件， 如果此时Avatar实体存在那么必然会执行到该事件 
	UKBEventData_reqRelive* pEventData = NewObject<UKBEventData_reqRelive>();
	pEventData->reliveType = reliveType;
	KBENGINE_EVENT_FIRE("relive", pEventData);
}

AEntityBase* AMainGameModeBase::findGameEntity(int entityID)
{
	AEntityBase** pGameEntity = gameEntities.Find(entityID);
	if (pGameEntity)
		return *pGameEntity;

	return NULL;
}

void AMainGameModeBase::addGameEntity(int entityID, AEntityBase* entity)
{
	gameEntities.Add(entityID, entity);
}

void AMainGameModeBase::removeGameEntity(int entityID)
{
	gameEntities.Remove(entityID);
}

void AMainGameModeBase::addSpaceGeometryMapping_Implementation(const UKBEventData* pEventData)
{

}

void AMainGameModeBase::onEnterWorld_Implementation(const UKBEventData* pEventData)
{
	const UKBEventData_onEnterWorld* pData = Cast<UKBEventData_onEnterWorld>(pEventData);

	FRotator Rot(0.f, 0.f, 0.f);
	KBDir2UE4Dir(Rot, pData->direction);
	FTransform SpawnTransform(Rot, pData->position);

	if (pData->isPlayer)
	{
		TSubclassOf<class AEntityBase>& APlayerCharacterClass = GameEntityClassArray[1];
		auto DeferredActor = Cast<AEntityBase>(UGameplayStatics::BeginDeferredActorSpawnFromClass(this, APlayerCharacterClass, SpawnTransform));
		if (DeferredActor != nullptr)
		{
			DeferredActor->entityID = pData->entityID;
			DeferredActor->moveSpeed = pData->moveSpeed;
			auto myPlayerController = UGameplayStatics::GetPlayerController(GWorld, 0);
			myPlayerController->Possess(DeferredActor);
			UGameplayStatics::FinishSpawningActor(DeferredActor, SpawnTransform);
		}

	}
	else
	{
		TSubclassOf<class AEntityBase>& AEntityBaseClass = GameEntityClassArray[0];
		auto DeferredActor = Cast<AEntityBase>(UGameplayStatics::BeginDeferredActorSpawnFromClass(this, AEntityBaseClass, SpawnTransform));
		if (DeferredActor != nullptr)
		{
			DeferredActor->entityID = pData->entityID;
			DeferredActor->moveSpeed = pData->moveSpeed;
			UGameplayStatics::FinishSpawningActor(DeferredActor, SpawnTransform);
		}
	}
}

void AMainGameModeBase::onLeaveWorld_Implementation(const UKBEventData* pEventData)
{
	const UKBEventData_onLeaveWorld* pData = Cast<UKBEventData_onLeaveWorld>(pEventData);
	AEntityBase* pAEntityBase = findGameEntity(pData->entityID);

	if (pAEntityBase)
	{
		pAEntityBase->Destroy();
	}
}

void AMainGameModeBase::onEnterSpace_Implementation(const UKBEventData* pEventData)
{
	const UKBEventData_onEnterSpace* pData = Cast<UKBEventData_onEnterSpace>(pEventData);

	FRotator Rot(0.f, 0.f, 0.f);
	KBDir2UE4Dir(Rot, pData->direction);
	FTransform SpawnTransform(Rot, pData->position);

	if (pData->isPlayer)
	{
		TSubclassOf<class AEntityBase>& APlayerCharacterClass = GameEntityClassArray[1];
		auto DeferredActor = Cast<AEntityBase>(UGameplayStatics::BeginDeferredActorSpawnFromClass(this, APlayerCharacterClass, SpawnTransform));
		if (DeferredActor != nullptr)
		{
			DeferredActor->entityID = pData->entityID;
			DeferredActor->moveSpeed = pData->moveSpeed;
			UGameplayStatics::FinishSpawningActor(DeferredActor, SpawnTransform);
		}
	}
	else
	{
		check(false);
	}
}

void AMainGameModeBase::onLeaveSpace_Implementation(const UKBEventData* pEventData)
{
	const UKBEventData_onLeaveSpace* pData = Cast<UKBEventData_onLeaveSpace>(pEventData);
	AEntityBase* pAEntityBase = findGameEntity(pData->entityID);

	if (pAEntityBase)
	{
		pAEntityBase->Destroy();
	}
}

void AMainGameModeBase::set_position_Implementation(const UKBEventData* pEventData)
{
	const UKBEventData_set_position* pData = Cast<UKBEventData_set_position>(pEventData);
	AEntityBase* pAEntityBase = findGameEntity(pData->entityID);

	if (pAEntityBase)
	{
		pAEntityBase->SetActorLocation(pData->position);
		pAEntityBase->setTargetLocation(pData->position);
		pAEntityBase->setIsOnGround(pData->isOnGround);
	}
}

void AMainGameModeBase::set_direction_Implementation(const UKBEventData* pEventData)
{
	const UKBEventData_set_direction* pData = Cast<UKBEventData_set_direction>(pEventData);
	AEntityBase* pAEntityBase = findGameEntity(pData->entityID);

	if (pAEntityBase)
	{
		pAEntityBase->setTargetRotator(pData->direction);
	}
}

void AMainGameModeBase::updatePosition_Implementation(const UKBEventData* pEventData)
{
	const UKBEventData_updatePosition* pData = Cast<UKBEventData_updatePosition>(pEventData);
	AEntityBase* pAEntityBase = findGameEntity(pData->entityID);

	if (pAEntityBase)
	{
		pAEntityBase->setTargetLocation(pData->position);
		pAEntityBase->setIsOnGround(pData->isOnGround);
	}
}

void AMainGameModeBase::onControlled_Implementation(const UKBEventData* pEventData)
{

}

void AMainGameModeBase::set_HP_Implementation(const UKBEventData* pEventData)
{

}

void AMainGameModeBase::set_MP_Implementation(const UKBEventData* pEventData)
{

}

void AMainGameModeBase::set_HP_Max_Implementation(const UKBEventData* pEventData)
{

}

void AMainGameModeBase::set_MP_Max_Implementation(const UKBEventData* pEventData)
{

}

void AMainGameModeBase::set_level_Implementation(const UKBEventData* pEventData)
{

}

void AMainGameModeBase::set_name_Implementation(const UKBEventData* pEventData)
{

}

void AMainGameModeBase::set_moveSpeed_Implementation(const UKBEventData* pEventData)
{
	const UKBEventData_set_moveSpeed* pData = Cast<UKBEventData_set_moveSpeed>(pEventData);
	AEntityBase* pAEntityBase = findGameEntity(pData->entityID);

	if (pAEntityBase)
		pAEntityBase->moveSpeed = pData->moveSpeed;
}

void AMainGameModeBase::set_modelScale_Implementation(const UKBEventData* pEventData)
{
	const UKBEventData_set_modelScale* pData = Cast<UKBEventData_set_modelScale>(pEventData);
	AEntityBase* pAEntityBase = findGameEntity(pData->entityID);

	if (pAEntityBase)
		pAEntityBase->modelScale = (float)(pData->modelScale / 100.0f);
}

void AMainGameModeBase::set_modelID_Implementation(const UKBEventData* pEventData)
{
	const UKBEventData_set_modelID* pData = Cast<UKBEventData_set_modelID>(pEventData);
	AEntityBase* pAEntityBase = findGameEntity(pData->entityID);
	if (pAEntityBase)
		pAEntityBase->setModelID(pData->modelID);
}

void AMainGameModeBase::set_entityNO_Implementation(const UKBEventData* pEventData)
{

}

void AMainGameModeBase::set_flags_Implementation(const UKBEventData* pEventData)
{

}

void AMainGameModeBase::set_state_Implementation(const UKBEventData* pEventData)
{

}

void AMainGameModeBase::set_subState_Implementation(const UKBEventData* pEventData)
{

}

void AMainGameModeBase::set_forbids_Implementation(const UKBEventData* pEventData)
{

}

void AMainGameModeBase::recvDamage_Implementation(const UKBEventData* pEventData)
{

}

void AMainGameModeBase::otherAvatarOnJump_Implementation(const UKBEventData* pEventData)
{

}

void AMainGameModeBase::onAddSkill_Implementation(const UKBEventData* pEventData)
{

}
