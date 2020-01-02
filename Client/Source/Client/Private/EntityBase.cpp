// Fill out your copyright notice in the Description page of Project Settings.


#include "EntityBase.h"
#include "Engine/KBEngine.h"
#include "Engine/Entity.h"

// Sets default values
AEntityBase::AEntityBase()
{
 	// Set this character to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
	PrimaryActorTick.bCanEverTick = true;
	entityID = 0;
	moveSpeed = 0.f;
	isOnGround = false;

	if (isPlayer())
	{
		AutoPossessPlayer = EAutoReceiveInput::Player0;
	}

}

// Called when the game starts or when spawned
void AEntityBase::BeginPlay()
{
	Super::BeginPlay();

	// 由于UE4可视化实体创建要晚于KBE的插件的逻辑实体，而KBE插件实体先前可能已经触发了一些属性设置事件
	// 因此此时我们可能已经错过了一些事件，我们只能在此补救必要的触发了， 例如：名称和血量属性值
	KBEngine::Entity* pEntity = KBEngine::KBEngineApp::getSingleton().findEntity(entityID);
	if (pEntity) {
		pEntity->callPropertysSetMethods();
	}
}

// Called every frame
void AEntityBase::Tick(float DeltaTime)
{
	Super::Tick(DeltaTime);
	if (!isPlayer())
	{
		updateLocation(DeltaTime);
	}

}

// Called to bind functionality to input
void AEntityBase::SetupPlayerInputComponent(UInputComponent* PlayerInputComponent)
{
	Super::SetupPlayerInputComponent(PlayerInputComponent);

}

void AEntityBase::updateLocation(float DeltaTime)
{
	const FVector& currLocation = GetActorLocation();

	//Direction from Self to targetPos
	FVector vectorDirection = targetLocation - currLocation;

	//由于服务端脚本moveSpeed的单位是厘米，这里需要转换为UE4单位毫米
	float deltaSpeed = (moveSpeed * 10.f ) * DeltaTime;
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

