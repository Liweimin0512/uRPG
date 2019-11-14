// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "RPGGameModeBase.h"
#include "SelectAvatarGameModeBase.generated.h"

/**
 * 
 */
UCLASS()
class CLIENT_API ASelectAvatarGameModeBase : public ARPGGameModeBase
{
	GENERATED_UCLASS_BODY()

public:
	virtual void installEvents() override;

	UFUNCTION(BlueprintNativeEvent, BlueprintCallable, Category = "KBEngine")
	void onReqAvatarList(const UKBEventData* pEventData);
	
	UFUNCTION(BlueprintNativeEvent, BlueprintCallable, Category = "KBEngine")
	void onCreateAvatarResult(const UKBEventData* pEventData);

	UFUNCTION(BlueprintNativeEvent, BlueprintCallable, Category = "KBEngine")
	void addSpaceGeometryMapping(const UKBEventData* pEventData);

	UFUNCTION(BlueprintNativeEvent, BlueprintCallable, Category = "KBEngine")
		void onRemoveAvatar(const UKBEventData* pEventData);

	UFUNCTION(BlueprintCallable, Category = KBEngine)
		void reqCreateAvatar(uint8 raceType, const FString& name);
	UFUNCTION(BlueprintCallable, Category = KBEngine)
		void reqRemoveAvatar(const FAVATAR_INFOS& avatarInfos);
	UFUNCTION(BlueprintCallable, Category = KBEngine)
		void reqEnterGame(const FAVATAR_INFOS& avatarInfos);
};
