// Fill out your copyright notice in the Description page of Project Settings.

#include "LoginGameModeBase.h"
#include "Client.h"
#include "Engine/KBEngine.h"

ALoginGameModeBase::ALoginGameModeBase(const FObjectInitializer& ObjectInitializer) 
	: Super(ObjectInitializer)
{
	// Set this character to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
	PrimaryActorTick.bCanEverTick = true;
}

void ALoginGameModeBase::installEvents()
{
	Super::installEvents();

	// login
	KBENGINE_REGISTER_EVENT(KBEngine::KBEventTypes::onCreateAccountResult, onCreateAccountResult);
	KBENGINE_REGISTER_EVENT(KBEngine::KBEventTypes::onLoginFailed, onLoginFailed);
	KBENGINE_REGISTER_EVENT(KBEngine::KBEventTypes::onVersionNotMatch, onVersionNotMatch);
	KBENGINE_REGISTER_EVENT(KBEngine::KBEventTypes::onScriptVersionNotMatch, onScriptVersionNotMatch);
	KBENGINE_REGISTER_EVENT(KBEngine::KBEventTypes::onLoginBaseappFailed, onLoginBaseappFailed);
	KBENGINE_REGISTER_EVENT(KBEngine::KBEventTypes::onLoginBaseapp, onLoginBaseapp);
	KBENGINE_REGISTER_EVENT("onLoginSuccessfully", onLoginSuccessfully);
	KBENGINE_REGISTER_EVENT("Loginapp_importClientMessages", Loginapp_importClientMessages);
	KBENGINE_REGISTER_EVENT("Baseapp_importClientMessages", Baseapp_importClientMessages);
	KBENGINE_REGISTER_EVENT("Baseapp_importClientEntityDef", Baseapp_importClientEntityDef);

}

// Called when the game starts or when spawned
void ALoginGameModeBase::BeginPlay()
{
	// 每次进入到这个界面时对KBE做一次清理，否则KBE插件内缓存的内容将一直存在
	KBEngine::KBEngineApp::getSingleton().reset();

	Super::BeginPlay();
}


bool ALoginGameModeBase::validEmail(FString strEmail)
{
	return KBEngine::KBEngineApp::getSingleton().validEmail(strEmail);
}

void ALoginGameModeBase::onCreateAccountResult_Implementation(const UKBEventData* pEventData)
{
}

void ALoginGameModeBase::onLoginFailed_Implementation(const UKBEventData* pEventData)
{
}

void ALoginGameModeBase::onVersionNotMatch_Implementation(const UKBEventData* pEventData)
{
}

void ALoginGameModeBase::onScriptVersionNotMatch_Implementation(const UKBEventData* pEventData)
{
}

void ALoginGameModeBase::onLoginBaseappFailed_Implementation(const UKBEventData* pEventData)
{
}

void ALoginGameModeBase::onLoginSuccessfully_Implementation(const UKBEventData* pEventData)
{
}

void ALoginGameModeBase::onLoginBaseapp_Implementation(const UKBEventData* pEventData)
{
}

void ALoginGameModeBase::Loginapp_importClientMessages_Implementation(const UKBEventData* pEventData)
{
}

void ALoginGameModeBase::Baseapp_importClientMessages_Implementation(const UKBEventData* pEventData)
{
}

void ALoginGameModeBase::Baseapp_importClientEntityDef_Implementation(const UKBEventData* pEventData)
{
}