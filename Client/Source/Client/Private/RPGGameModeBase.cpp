// Fill out your copyright notice in the Description page of Project Settings.

#include "Public/RPGGameModeBase.h"
#include "Client.h"
#include "Engine/KBEngine.h"

ARPGGameModeBase::ARPGGameModeBase(const FObjectInitializer& ObjectInitializer)
	: Super(ObjectInitializer)
{
	// Set this character to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
	PrimaryActorTick.bCanEverTick = true;
}

void ARPGGameModeBase::InitGame(const FString& MapName, const FString& Options, FString& ErrorMessage)
{
	Super::InitGame(MapName, Options, ErrorMessage);
}

// Called when the game starts or when spawned
void ARPGGameModeBase::BeginPlay()
{
	Super::BeginPlay();
	installEvents();
}


void ARPGGameModeBase::EndPlay(const EEndPlayReason::Type EndPlayReason)
{
	Super::EndPlay(EndPlayReason);
	KBENGINE_DEREGISTER_ALL_EVENT();
}

void ARPGGameModeBase::Logout(AController* Exiting)
{
	Super::Logout(Exiting);

	// 可以在这里理解为玩家编辑器Stop游戏或者离开了这个场景
	if (Exiting)
	{
		KBENGINE_DEREGISTER_ALL_EVENT();
	}
}

void ARPGGameModeBase::installEvents()
{
	// common
	KBENGINE_REGISTER_EVENT(KBEngine::KBEventTypes::onKicked, onKicked);
	KBENGINE_REGISTER_EVENT(KBEngine::KBEventTypes::onDisconnected, onDisconnected);
	KBENGINE_REGISTER_EVENT(KBEngine::KBEventTypes::onConnectionState, onConnectionState);
	KBENGINE_REGISTER_EVENT(KBEngine::KBEventTypes::onReloginBaseappSuccessfully, onReloginBaseappSuccessfully);
	KBENGINE_REGISTER_EVENT(KBEngine::KBEventTypes::onReloginBaseappFailed, onReloginBaseappFailed);
}

void ARPGGameModeBase::fire(const FString& eventName, UKBEventData* pEventData)
{
	KBENGINE_EVENT_FIRE(eventName, pEventData);
}

void ARPGGameModeBase::onKicked_Implementation(const UKBEventData* pEventData)
{
}

void ARPGGameModeBase::onDisconnected_Implementation(const UKBEventData* pEventData)
{

}

void ARPGGameModeBase::onConnectionState_Implementation(const UKBEventData* pEventData)
{

}

void ARPGGameModeBase::onReloginBaseappSuccessfully_Implementation(const UKBEventData* pEventData)
{
}

void ARPGGameModeBase::onReloginBaseappFailed_Implementation(const UKBEventData* pEventData)
{
}

void ARPGGameModeBase::startReloginBaseappTimer()
{
	if (!timerHandle.IsValid())
		GetWorldTimerManager().SetTimer(timerHandle, this, &ARPGGameModeBase::onReloginBaseappTimer, 1.0f, false, 1.0f);
}

void ARPGGameModeBase::stopReloginBaseappTimer()
{
	GetWorldTimerManager().ClearTimer(timerHandle);
}

void ARPGGameModeBase::onReloginBaseappTimer()
{
	KBEngine::KBEngineApp::getSingleton().reloginBaseapp();

	if (timerHandle.IsValid())
		GetWorldTimerManager().SetTimer(timerHandle, this, &ARPGGameModeBase::onReloginBaseappTimer, 1.0f, false, 3.0f);
}


