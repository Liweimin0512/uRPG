// Copyright 1998-2019 Epic Games, Inc. All Rights Reserved.

using UnrealBuildTool;

public class Client : ModuleRules
{
	public Client(ReadOnlyTargetRules Target) 
		: base(Target)
	{
		//PrivatePCHHeaderFile = "Public/Client.h";
		PCHUsage = PCHUsageMode.UseExplicitOrSharedPCHs;
	
		PublicDependencyModuleNames.AddRange(
			new string[] {
				"Core",
				"CoreUObject",
				"Engine"
			}
		);

		PrivateDependencyModuleNames.AddRange(
			new string[] {
				"InputCore",
				"KBEnginePlugins",
				"VictoryBPLibrary",
				"GameplayAbilities",
				"GameplayTags",
				"GameplayTasks"
			}
		);
	}
}
