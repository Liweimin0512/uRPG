// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "Client.h"
#include "GameFramework/Character.h"
#include "AbilitySystemInterface.h"
#include "Abilities/RPGAbilitySystemComponent.h"
#include "Abilities/CoreAttributeSet.h"
#include "EntityBase.generated.h"

const int ModelID_NPC = 1002;
const int ModelID_Monster1 = 1003;
const int ModelID_Monster2 = 1004;
const int ModelID_Gate = 40001001;
const int ModelID_Avatar = 90000001;

UCLASS()
class CLIENT_API AEntityBase : public ACharacter,public IAbilitySystemInterface
{
	GENERATED_UCLASS_BODY()

public:

	// AEntityBase();

	virtual void PossessedBy(AController* NewController) override;
	virtual void UnPossessed() override;
	virtual void OnRep_Controller() override;
	virtual void GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& OutLifetimeProps) const override;

	// Implement IAbilitySystemInterface
	UPROPERTY()
	URPGAbilitySystemComponent* AbilitySystemComponent;

	/** Returns current health, will be 0 if dead */
	UFUNCTION(BlueprintCallable)
	virtual float GetHealth() const;

	/** Returns maximum health, health will never be greater than this */
	UFUNCTION(BlueprintCallable)
	virtual float GetMaxHealth() const;

	/** Returns current mana */
	UFUNCTION(BlueprintCallable)
	virtual float GetMana() const;

	/** Returns maximum mana, mana will never be greater than this */
	UFUNCTION(BlueprintCallable)
	virtual float GetMaxMana() const;

	/** Returns current movement speed */
	UFUNCTION(BlueprintCallable)
	virtual float GetMoveSpeed() const;

	/** Returns the character level that is passed to the ability system */
	UFUNCTION(BlueprintCallable)
	virtual int32 GetCharacterLevel() const;

	/** Modifies the character level, this may change abilities. Returns true on success */
	UFUNCTION(BlueprintCallable)
	virtual bool SetCharacterLevel(int32 NewLevel);






	// Called when the game starts or when spawned
	virtual void BeginPlay() override;

	/** Called once this actor has been deleted */
	virtual void Destroyed() override;

	// Called every frame
	virtual void Tick(float DeltaSeconds) override;

	// Called to bind functionality to input
	virtual void SetupPlayerInputComponent(class UInputComponent* inputComponent) override;

	UFUNCTION(BlueprintCallable, Category = "KBEngine")
		virtual void FaceRotation(FRotator NewRotation, float DeltaTime = 0.f) override;

	UFUNCTION(BlueprintCallable, Category = "KBEngine")
		void updateLocation(float DeltaTime);

	UFUNCTION(BlueprintCallable, Category = "KBEngine")
		void setTargetLocation(const FVector& loc)
	{
		targetLocation = loc;
	}

	UFUNCTION(BlueprintCallable, Category = "KBEngine")
		void setTargetRotator(const FRotator& rot)
	{
		targetRotator = rot;
	}

	UFUNCTION(BlueprintCallable, Category = "KBEngine")
		void setIsOnGround(bool onGround)
	{
		isOnGround = onGround;
	}

	UFUNCTION(BlueprintCallable, Category = "KBEngine")
		virtual void setModelID(int modelID);

	//UFUNCTION(BlueprintCallable, Category = "KBEngine")
	//	virtual bool isPlayer() {
	//	return false;
	//}

private:
	void createAvatar();
	void createMonster();

public:
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = KBEngine)
		float modelScale;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = KBEngine)
		int modelID;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = KBEngine)
		float moveSpeed;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = KBEngine)
		int entityID;

	// ʵ�彫Ҫ�ƶ�����Ŀ�ĵ�λ��
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = KBEngine)
		FVector targetLocation;

	// ʵ�彫Ҫ�ƶ�����Ŀ�ĳ���
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = KBEngine)
		FRotator targetRotator;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = KBEngine)
		bool isOnGround;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = KBEngine)
		bool isPlayerCharacter;


protected:
	/** The level of this character, should not be modified directly once it has already spawned */
	UPROPERTY(EditAnywhere, Replicated, Category = Abilities)
	int32 CharacterLevel;

	/** List of attributes modified by the ability system */
	UPROPERTY()
	UCoreAttributeSet* AttributeSet;

	/** If true we have initialized our abilities */
	UPROPERTY()
	int32 bAbilitiesInitialized;


	/**
	 * Called when character takes damage, which may have killed them
	 *
	 * @param DamageAmount Amount of damage that was done, not clamped based on current health
	 * @param HitInfo The hit info that generated this damage
	 * @param DamageTags The gameplay tags of the event that did the damage
	 * @param InstigatorCharacter The character that initiated this damage
	 * @param DamageCauser The actual actor that did the damage, might be a weapon or projectile
	 */
	UFUNCTION(BlueprintImplementableEvent)
	void OnDamaged(float DamageAmount, const FHitResult& HitInfo, const struct FGameplayTagContainer& DamageTags, AEntityBase* InstigatorCharacter, AActor* DamageCauser);

	/**
	 * Called when health is changed, either from healing or from being damaged
	 * For damage this is called in addition to OnDamaged/OnKilled
	 *
	 * @param DeltaValue Change in health value, positive for heal, negative for cost. If 0 the delta is unknown
	 * @param EventTags The gameplay tags of the event that changed mana
	 */
	UFUNCTION(BlueprintImplementableEvent)
	void OnHealthChanged(float DeltaValue, const struct FGameplayTagContainer& EventTags);

	/**
	 * Called when mana is changed, either from healing or from being used as a cost
	 *
	 * @param DeltaValue Change in mana value, positive for heal, negative for cost. If 0 the delta is unknown
	 * @param EventTags The gameplay tags of the event that changed mana
	 */
	UFUNCTION(BlueprintImplementableEvent)
	void OnManaChanged(float DeltaValue, const struct FGameplayTagContainer& EventTags);

	/**
	 * Called when movement speed is changed
	 *
	 * @param DeltaValue Change in move speed
	 * @param EventTags The gameplay tags of the event that changed mana
	 */
	UFUNCTION(BlueprintImplementableEvent)
	void OnMoveSpeedChanged(float DeltaValue, const struct FGameplayTagContainer& EventTags);



	/** Apply the startup gameplay abilities and effects */
	void AddStartupGameplayAbilities();

	/** Attempts to remove any startup gameplay abilities */
	void RemoveStartupGameplayAbilities();



	// Called from RPGAttributeSet, these call BP events above
	virtual void HandleDamage(float DamageAmount, const FHitResult& HitInfo, const struct FGameplayTagContainer& DamageTags, AEntityBase* InstigatorCharacter, AActor* DamageCauser);
	virtual void HandleHealthChanged(float DeltaValue, const struct FGameplayTagContainer& EventTags);
	virtual void HandleManaChanged(float DeltaValue, const struct FGameplayTagContainer& EventTags);
	virtual void HandleMoveSpeedChanged(float DeltaValue, const struct FGameplayTagContainer& EventTags);
};