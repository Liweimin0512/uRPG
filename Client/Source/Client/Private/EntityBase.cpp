// Fill out your copyright notice in the Description page of Project Settings.


#include "EntityBase.h"
#include "Client.h"
#include "Engine/KBEngine.h"
#include "MainGameModeBase.h"
#include "Engine/Entity.h"

 //Sets default values
AEntityBase::AEntityBase(const FObjectInitializer& ObjectInitializer) : Super(ObjectInitializer)
{
	// Set this character to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
	PrimaryActorTick.bCanEverTick = true;
	entityID = 0;
	moveSpeed = 0.f;
	isOnGround = false;
	isPlayerCharacter = false;
}

// Called when the game starts or when spawned
void AEntityBase::BeginPlay()
{
	Super::BeginPlay();

	auto XGameMode = Cast<AMainGameModeBase>(UGameplayStatics::GetGameMode(this));

	if (XGameMode)
	{
		// 把自己注册到AMainGameModeBase，方便后面查找
		XGameMode->addGameEntity(this->entityID, this);
		KBEngine::Entity* pEntity = KBEngine::KBEngineApp::getSingleton().findEntity(entityID);

		// 由于UE4可视化实体创建要晚于KBE的插件的逻辑实体，而KBE插件实体先前可能已经触发了一些属性设置事件
		// 因此此时我们可能已经错过了一些事件，我们只能在此补救必要的触发了， 例如：名称和血量属性值
		if (pEntity)
			pEntity->callPropertysSetMethods();
	}
}

void AEntityBase::Destroyed()
{
	Super::Destroyed();

	auto XGameMode = Cast<AMainGameModeBase>(UGameplayStatics::GetGameMode(this));

	if (XGameMode)
	{
		// 把自己注册到AMainGameModeBase，方便后面查找
		XGameMode->removeGameEntity(this->entityID);
	}
}

void AEntityBase::updateLocation(float DeltaTime)
{
	const FVector& currLocation = GetActorLocation();

	//Direction from Self to targetPos
	FVector vectorDirection = targetLocation - currLocation;

	float deltaSpeed = (moveSpeed * 10.f /*由于服务端脚本moveSpeed的单位是厘米，这里需要转换为UE4单位毫米*/) * DeltaTime;
	if (vectorDirection.Size() > deltaSpeed)
	{
		//Normalize Vector so it is just a direction
		vectorDirection.Normalize();

		//Move moveSpeed units toward the player, per tick
		SetActorLocation(currLocation + (vectorDirection * deltaSpeed));
	}
	else
	{
		SetActorLocation(targetLocation);
	}

	FaceRotation(targetRotator, DeltaTime);
}

// Called every frame
void AEntityBase::Tick(float DeltaTime)
{
	Super::Tick(DeltaTime);

	if (!isPlayerCharacter)
	{
		updateLocation(DeltaTime);
	}
}

// Called to bind functionality to input
void AEntityBase::SetupPlayerInputComponent(class UInputComponent* inputComponent)
{
	Super::SetupPlayerInputComponent(inputComponent);

}

void AEntityBase::FaceRotation(FRotator NewRotation, float DeltaTime)
{
	FRotator CurrentRotation = FMath::RInterpTo(GetActorRotation(), NewRotation, DeltaTime, 8.0f);

	Super::FaceRotation(CurrentRotation, DeltaTime);
}

void AEntityBase::setModelID(int modelID)
{
	this->modelID = modelID;

	if (this->modelID == ModelID_Avatar)
	{
		this->createAvatar();
	}
	else
	{
		this->createMonster();
	}
}

void AEntityBase::createAvatar()
{
	//TArray<UActorComponent*> components = this->GetComponents().Array();
	//for (int i = 0; i < components.Num(); i++)
	//{
	//	if (components[i]->GetName() == "Scene")  //调整血条位置
	//	{
	//		UWidgetComponent* pWidget = (UWidgetComponent*)components[i];
	//		pWidget->SetRelativeLocation(FVector(0.f, 0.f, 50.f));
	//	}

	//	if (components[i]->GetName() == "Sphere")	//隐藏整球
	//	{
	//		USphereComponent* pSphere = (USphereComponent*)components[i];
	//		pSphere->SetActive(false);
	//		pSphere->SetVisibility(false);
	//	}

	//	if (components[i]->GetName() == "Cone")		//隐藏圆锥体
	//	{
	//		UStaticMeshComponent* pCone = (UStaticMeshComponent*)components[i];
	//		pCone->SetActive(false);
	//		pCone->SetVisibility(false);
	//	}
	//}
}

void AEntityBase::createMonster()
{
	//USkeletalMeshComponent* SkeletalMesh = this->GetMesh();
	//SkeletalMesh->SetActive(false);
	//SkeletalMesh->SetVisibility(false);
}

