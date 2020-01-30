// Fill out your copyright notice in the Description page of Project Settings.


#include "SelectAvatarGameModeBase.h"
#include "Client.h"
#include "Engine/KBEngine.h"


ASelectAvatarGameModeBase::ASelectAvatarGameModeBase(const FObjectInitializer& ObjectInitializer) : Super(ObjectInitializer)
{
	// Set this character to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
	PrimaryActorTick.bCanEverTick = true;
}

void ASelectAvatarGameModeBase::installEvents()
{
	Super::installEvents();

	// select-avatars(register by scripts)
	KBENGINE_REGISTER_EVENT("onReqAvatarList", onReqAvatarList);
	KBENGINE_REGISTER_EVENT("onCreateAvatarResult", onCreateAvatarResult);
	KBENGINE_REGISTER_EVENT("onRemoveAvatar", onRemoveAvatar);

	// begin enterworld
	// 这个事件触发时我们需要切换地图到游戏世界地图
	KBENGINE_REGISTER_EVENT("addSpaceGeometryMapping", addSpaceGeometryMapping);
}

void ASelectAvatarGameModeBase::onReqAvatarList_Implementation(const UKBEventData* pEventData)
{
}

void ASelectAvatarGameModeBase::onCreateAvatarResult_Implementation(const UKBEventData* pEventData)
{
}

void ASelectAvatarGameModeBase::onRemoveAvatar_Implementation(const UKBEventData* pEventData)
{
}

void ASelectAvatarGameModeBase::addSpaceGeometryMapping_Implementation(const UKBEventData* pEventData)
{

}

void ASelectAvatarGameModeBase::reqCreateAvatar(uint8 raceType, const FString& name)
{
	// 由于Account实体注册了该事件， 如果此时Account实体存在那么必然会执行到该事件 
	UKBEventData_reqCreateAvatar* pEventData = NewObject<UKBEventData_reqCreateAvatar>();
	pEventData->roleType = raceType;
	pEventData->name = name;
	KBENGINE_EVENT_FIRE("reqCreateAvatar", pEventData);
}

void ASelectAvatarGameModeBase::reqRemoveAvatar(const FAVATAR_INFOS& avatarInfos)
{
	// 由于Account实体注册了该事件， 如果此时Account实体存在那么必然会执行到该事件 
	UKBEventData_reqRemoveAvatar* pEventData = NewObject<UKBEventData_reqRemoveAvatar>();
	pEventData->avatarInfos = avatarInfos;
	FAVATAR_INFOS event_avatar;
	KBENGINE_EVENT_FIRE("reqRemoveAvatar", pEventData);
}

void ASelectAvatarGameModeBase::reqEnterGame(const FAVATAR_INFOS& avatarInfos)
{
	// 由于Account实体注册了该事件， 如果此时Account实体存在那么必然会执行到该事件 
	UKBEventData_selectAvatarGame* pEventData = NewObject<UKBEventData_selectAvatarGame>();
	pEventData->avatarInfos = avatarInfos;
	KBENGINE_EVENT_FIRE("selectAvatarGame", pEventData);
}

