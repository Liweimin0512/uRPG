#include "EntityDef.h"
#include "DataTypes.h"
#include "CustomDataTypes.h"
#include "ScriptModule.h"
#include "Property.h"
#include "Method.h"
#include "KBVar.h"
#include "Entity.h"

#include "Scripts/Account.h"
#include "Scripts/Avatar.h"

namespace KBEngine
{

TMap<FString, uint16> EntityDef::datatype2id;
TMap<FString, DATATYPE_BASE*> EntityDef::datatypes;
TMap<uint16, DATATYPE_BASE*> EntityDef::id2datatypes;
TMap<FString, int32> EntityDef::entityclass;
TMap<FString, ScriptModule*> EntityDef::moduledefs;
TMap<uint16, ScriptModule*> EntityDef::idmoduledefs;

bool EntityDef::initialize()
{
	initDataTypes();
	initDefTypes();
	initScriptModules();
	return true;
}

bool EntityDef::reset()
{
	clear();
	return initialize();
}

void EntityDef::clear()
{
	TArray<DATATYPE_BASE*> deleted_datatypes;
	for (auto& item : EntityDef::datatypes)
	{
		int32 idx = deleted_datatypes.Find(item.Value);
		if (idx != INDEX_NONE)
			continue;

		deleted_datatypes.Add(item.Value);
		delete item.Value;
	}

	for (auto& item : EntityDef::moduledefs)
		delete item.Value;

	datatype2id.Empty();
	datatypes.Empty();
	id2datatypes.Empty();
	entityclass.Empty();
	moduledefs.Empty();
	idmoduledefs.Empty();
}

void EntityDef::initDataTypes()
{
	datatypes.Add(TEXT("UINT8"), new DATATYPE_UINT8());
	datatypes.Add(TEXT("UINT16"), new DATATYPE_UINT16());
	datatypes.Add(TEXT("UINT32"), new DATATYPE_UINT32());
	datatypes.Add(TEXT("UINT64"), new DATATYPE_UINT64());

	datatypes.Add(TEXT("INT8"), new DATATYPE_INT8());
	datatypes.Add(TEXT("INT16"), new DATATYPE_INT16());
	datatypes.Add(TEXT("INT32"), new DATATYPE_INT32());
	datatypes.Add(TEXT("INT64"), new DATATYPE_INT64());

	datatypes.Add(TEXT("FLOAT"), new DATATYPE_FLOAT());
	datatypes.Add(TEXT("DOUBLE"), new DATATYPE_DOUBLE());

	datatypes.Add(TEXT("STRING"), new DATATYPE_STRING());
	datatypes.Add(TEXT("VECTOR2"), new DATATYPE_VECTOR2());

	datatypes.Add(TEXT("VECTOR3"), new DATATYPE_VECTOR3());

	datatypes.Add(TEXT("VECTOR4"), new DATATYPE_VECTOR4());
	datatypes.Add(TEXT("PYTHON"), new DATATYPE_PYTHON());

	datatypes.Add(TEXT("UNICODE"), new DATATYPE_UNICODE());
	datatypes.Add(TEXT("ENTITYCALL"), new DATATYPE_ENTITYCALL());

	datatypes.Add(TEXT("BLOB"), new DATATYPE_BLOB());
}

Entity* EntityDef::createEntity(int utype)
{
	Entity* pEntity = NULL;

	switch(utype)
	{
		case 1:
			pEntity = new Account();
			break;
		case 2:
			pEntity = new Avatar();
			break;
		default:
			SCREEN_ERROR_MSG("EntityDef::createEntity() : entity(%d) not found!", utype);
			break;
	};

	return pEntity;
}

void EntityDef::initScriptModules()
{
	ScriptModule* pAccountModule = new ScriptModule("Account", 1);
	EntityDef::moduledefs.Add(TEXT("Account"), pAccountModule);
	EntityDef::idmoduledefs.Add(1, pAccountModule);

	Property* pAccount_position = new Property();
	pAccount_position->name = TEXT("position");
	pAccount_position->properUtype = 40000;
	pAccount_position->properFlags = 4;
	pAccount_position->aliasID = 1;
	KBVar* pAccount_position_defval = new KBVar(FVector());
	pAccount_position->pDefaultVal = pAccount_position_defval;
	pAccountModule->propertys.Add(TEXT("position"), pAccount_position); 

	pAccountModule->usePropertyDescrAlias = true;
	pAccountModule->idpropertys.Add((uint16)pAccount_position->aliasID, pAccount_position);

	//DEBUG_MSG("EntityDef::initScriptModules: add(Account), property(position / 40000).");

	Property* pAccount_direction = new Property();
	pAccount_direction->name = TEXT("direction");
	pAccount_direction->properUtype = 40001;
	pAccount_direction->properFlags = 4;
	pAccount_direction->aliasID = 2;
	KBVar* pAccount_direction_defval = new KBVar(FVector());
	pAccount_direction->pDefaultVal = pAccount_direction_defval;
	pAccountModule->propertys.Add(TEXT("direction"), pAccount_direction); 

	pAccountModule->usePropertyDescrAlias = true;
	pAccountModule->idpropertys.Add((uint16)pAccount_direction->aliasID, pAccount_direction);

	//DEBUG_MSG("EntityDef::initScriptModules: add(Account), property(direction / 40001).");

	Property* pAccount_spaceID = new Property();
	pAccount_spaceID->name = TEXT("spaceID");
	pAccount_spaceID->properUtype = 40002;
	pAccount_spaceID->properFlags = 16;
	pAccount_spaceID->aliasID = 3;
	KBVar* pAccount_spaceID_defval = new KBVar((uint32)FCString::Atoi64(TEXT("")));
	pAccount_spaceID->pDefaultVal = pAccount_spaceID_defval;
	pAccountModule->propertys.Add(TEXT("spaceID"), pAccount_spaceID); 

	pAccountModule->usePropertyDescrAlias = true;
	pAccountModule->idpropertys.Add((uint16)pAccount_spaceID->aliasID, pAccount_spaceID);

	//DEBUG_MSG("EntityDef::initScriptModules: add(Account), property(spaceID / 40002).");

	Property* pAccount_lastSelCharacter = new Property();
	pAccount_lastSelCharacter->name = TEXT("lastSelCharacter");
	pAccount_lastSelCharacter->properUtype = 2;
	pAccount_lastSelCharacter->properFlags = 32;
	pAccount_lastSelCharacter->aliasID = 4;
	KBVar* pAccount_lastSelCharacter_defval = new KBVar((uint64)FCString::Atoi64(TEXT("0")));
	pAccount_lastSelCharacter->pDefaultVal = pAccount_lastSelCharacter_defval;
	pAccountModule->propertys.Add(TEXT("lastSelCharacter"), pAccount_lastSelCharacter); 

	pAccountModule->usePropertyDescrAlias = true;
	pAccountModule->idpropertys.Add((uint16)pAccount_lastSelCharacter->aliasID, pAccount_lastSelCharacter);

	//DEBUG_MSG("EntityDef::initScriptModules: add(Account), property(lastSelCharacter / 2).");

	TArray<DATATYPE_BASE*> Account_onCreateAvatarResult_args;
	Account_onCreateAvatarResult_args.Add(EntityDef::id2datatypes[2]);
	Account_onCreateAvatarResult_args.Add(EntityDef::id2datatypes[25]);

	Method* pAccount_onCreateAvatarResult = new Method();
	pAccount_onCreateAvatarResult->name = TEXT("onCreateAvatarResult");
	pAccount_onCreateAvatarResult->methodUtype = 7;
	pAccount_onCreateAvatarResult->aliasID = 1;
	pAccount_onCreateAvatarResult->args = Account_onCreateAvatarResult_args;

	pAccountModule->methods.Add(TEXT("onCreateAvatarResult"), pAccount_onCreateAvatarResult); 
	pAccountModule->useMethodDescrAlias = true;
	pAccountModule->idmethods.Add((uint16)pAccount_onCreateAvatarResult->aliasID, pAccount_onCreateAvatarResult);

	//DEBUG_MSG("EntityDef::initScriptModules: add(Account), method(onCreateAvatarResult / 7).");

	TArray<DATATYPE_BASE*> Account_onRemoveAvatar_args;
	Account_onRemoveAvatar_args.Add(EntityDef::id2datatypes[5]);

	Method* pAccount_onRemoveAvatar = new Method();
	pAccount_onRemoveAvatar->name = TEXT("onRemoveAvatar");
	pAccount_onRemoveAvatar->methodUtype = 8;
	pAccount_onRemoveAvatar->aliasID = 2;
	pAccount_onRemoveAvatar->args = Account_onRemoveAvatar_args;

	pAccountModule->methods.Add(TEXT("onRemoveAvatar"), pAccount_onRemoveAvatar); 
	pAccountModule->useMethodDescrAlias = true;
	pAccountModule->idmethods.Add((uint16)pAccount_onRemoveAvatar->aliasID, pAccount_onRemoveAvatar);

	//DEBUG_MSG("EntityDef::initScriptModules: add(Account), method(onRemoveAvatar / 8).");

	TArray<DATATYPE_BASE*> Account_onReqAvatarList_args;
	Account_onReqAvatarList_args.Add(EntityDef::id2datatypes[26]);

	Method* pAccount_onReqAvatarList = new Method();
	pAccount_onReqAvatarList->name = TEXT("onReqAvatarList");
	pAccount_onReqAvatarList->methodUtype = 6;
	pAccount_onReqAvatarList->aliasID = 3;
	pAccount_onReqAvatarList->args = Account_onReqAvatarList_args;

	pAccountModule->methods.Add(TEXT("onReqAvatarList"), pAccount_onReqAvatarList); 
	pAccountModule->useMethodDescrAlias = true;
	pAccountModule->idmethods.Add((uint16)pAccount_onReqAvatarList->aliasID, pAccount_onReqAvatarList);

	//DEBUG_MSG("EntityDef::initScriptModules: add(Account), method(onReqAvatarList / 6).");

	TArray<DATATYPE_BASE*> Account_reqAvatarList_args;

	Method* pAccount_reqAvatarList = new Method();
	pAccount_reqAvatarList->name = TEXT("reqAvatarList");
	pAccount_reqAvatarList->methodUtype = 1;
	pAccount_reqAvatarList->aliasID = -1;
	pAccount_reqAvatarList->args = Account_reqAvatarList_args;

	pAccountModule->methods.Add(TEXT("reqAvatarList"), pAccount_reqAvatarList); 
	pAccountModule->base_methods.Add(TEXT("reqAvatarList"), pAccount_reqAvatarList);

	pAccountModule->idbase_methods.Add(pAccount_reqAvatarList->methodUtype, pAccount_reqAvatarList);

	//DEBUG_MSG("EntityDef::initScriptModules: add(Account), method(reqAvatarList / 1).");

	TArray<DATATYPE_BASE*> Account_reqCreateAvatar_args;
	Account_reqCreateAvatar_args.Add(EntityDef::id2datatypes[12]);
	Account_reqCreateAvatar_args.Add(EntityDef::id2datatypes[2]);

	Method* pAccount_reqCreateAvatar = new Method();
	pAccount_reqCreateAvatar->name = TEXT("reqCreateAvatar");
	pAccount_reqCreateAvatar->methodUtype = 2;
	pAccount_reqCreateAvatar->aliasID = -1;
	pAccount_reqCreateAvatar->args = Account_reqCreateAvatar_args;

	pAccountModule->methods.Add(TEXT("reqCreateAvatar"), pAccount_reqCreateAvatar); 
	pAccountModule->base_methods.Add(TEXT("reqCreateAvatar"), pAccount_reqCreateAvatar);

	pAccountModule->idbase_methods.Add(pAccount_reqCreateAvatar->methodUtype, pAccount_reqCreateAvatar);

	//DEBUG_MSG("EntityDef::initScriptModules: add(Account), method(reqCreateAvatar / 2).");

	TArray<DATATYPE_BASE*> Account_reqEnterGame_args;
	Account_reqEnterGame_args.Add(EntityDef::id2datatypes[5]);

	Method* pAccount_reqEnterGame = new Method();
	pAccount_reqEnterGame->name = TEXT("reqEnterGame");
	pAccount_reqEnterGame->methodUtype = 3;
	pAccount_reqEnterGame->aliasID = -1;
	pAccount_reqEnterGame->args = Account_reqEnterGame_args;

	pAccountModule->methods.Add(TEXT("reqEnterGame"), pAccount_reqEnterGame); 
	pAccountModule->base_methods.Add(TEXT("reqEnterGame"), pAccount_reqEnterGame);

	pAccountModule->idbase_methods.Add(pAccount_reqEnterGame->methodUtype, pAccount_reqEnterGame);

	//DEBUG_MSG("EntityDef::initScriptModules: add(Account), method(reqEnterGame / 3).");

	TArray<DATATYPE_BASE*> Account_reqRemoveAvatar_args;
	Account_reqRemoveAvatar_args.Add(EntityDef::id2datatypes[12]);

	Method* pAccount_reqRemoveAvatar = new Method();
	pAccount_reqRemoveAvatar->name = TEXT("reqRemoveAvatar");
	pAccount_reqRemoveAvatar->methodUtype = 4;
	pAccount_reqRemoveAvatar->aliasID = -1;
	pAccount_reqRemoveAvatar->args = Account_reqRemoveAvatar_args;

	pAccountModule->methods.Add(TEXT("reqRemoveAvatar"), pAccount_reqRemoveAvatar); 
	pAccountModule->base_methods.Add(TEXT("reqRemoveAvatar"), pAccount_reqRemoveAvatar);

	pAccountModule->idbase_methods.Add(pAccount_reqRemoveAvatar->methodUtype, pAccount_reqRemoveAvatar);

	//DEBUG_MSG("EntityDef::initScriptModules: add(Account), method(reqRemoveAvatar / 4).");

	TArray<DATATYPE_BASE*> Account_reqRemoveAvatarDBID_args;
	Account_reqRemoveAvatarDBID_args.Add(EntityDef::id2datatypes[5]);

	Method* pAccount_reqRemoveAvatarDBID = new Method();
	pAccount_reqRemoveAvatarDBID->name = TEXT("reqRemoveAvatarDBID");
	pAccount_reqRemoveAvatarDBID->methodUtype = 5;
	pAccount_reqRemoveAvatarDBID->aliasID = -1;
	pAccount_reqRemoveAvatarDBID->args = Account_reqRemoveAvatarDBID_args;

	pAccountModule->methods.Add(TEXT("reqRemoveAvatarDBID"), pAccount_reqRemoveAvatarDBID); 
	pAccountModule->base_methods.Add(TEXT("reqRemoveAvatarDBID"), pAccount_reqRemoveAvatarDBID);

	pAccountModule->idbase_methods.Add(pAccount_reqRemoveAvatarDBID->methodUtype, pAccount_reqRemoveAvatarDBID);

	//DEBUG_MSG("EntityDef::initScriptModules: add(Account), method(reqRemoveAvatarDBID / 5).");

	ScriptModule* pAvatarModule = new ScriptModule("Avatar", 2);
	EntityDef::moduledefs.Add(TEXT("Avatar"), pAvatarModule);
	EntityDef::idmoduledefs.Add(2, pAvatarModule);

	Property* pAvatar_position = new Property();
	pAvatar_position->name = TEXT("position");
	pAvatar_position->properUtype = 40000;
	pAvatar_position->properFlags = 4;
	pAvatar_position->aliasID = 1;
	KBVar* pAvatar_position_defval = new KBVar(FVector());
	pAvatar_position->pDefaultVal = pAvatar_position_defval;
	pAvatarModule->propertys.Add(TEXT("position"), pAvatar_position); 

	pAvatarModule->usePropertyDescrAlias = true;
	pAvatarModule->idpropertys.Add((uint16)pAvatar_position->aliasID, pAvatar_position);

	//DEBUG_MSG("EntityDef::initScriptModules: add(Avatar), property(position / 40000).");

	Property* pAvatar_direction = new Property();
	pAvatar_direction->name = TEXT("direction");
	pAvatar_direction->properUtype = 40001;
	pAvatar_direction->properFlags = 4;
	pAvatar_direction->aliasID = 2;
	KBVar* pAvatar_direction_defval = new KBVar(FVector());
	pAvatar_direction->pDefaultVal = pAvatar_direction_defval;
	pAvatarModule->propertys.Add(TEXT("direction"), pAvatar_direction); 

	pAvatarModule->usePropertyDescrAlias = true;
	pAvatarModule->idpropertys.Add((uint16)pAvatar_direction->aliasID, pAvatar_direction);

	//DEBUG_MSG("EntityDef::initScriptModules: add(Avatar), property(direction / 40001).");

	Property* pAvatar_spaceID = new Property();
	pAvatar_spaceID->name = TEXT("spaceID");
	pAvatar_spaceID->properUtype = 40002;
	pAvatar_spaceID->properFlags = 16;
	pAvatar_spaceID->aliasID = 3;
	KBVar* pAvatar_spaceID_defval = new KBVar((uint32)FCString::Atoi64(TEXT("")));
	pAvatar_spaceID->pDefaultVal = pAvatar_spaceID_defval;
	pAvatarModule->propertys.Add(TEXT("spaceID"), pAvatar_spaceID); 

	pAvatarModule->usePropertyDescrAlias = true;
	pAvatarModule->idpropertys.Add((uint16)pAvatar_spaceID->aliasID, pAvatar_spaceID);

	//DEBUG_MSG("EntityDef::initScriptModules: add(Avatar), property(spaceID / 40002).");

	Property* pAvatar_level = new Property();
	pAvatar_level->name = TEXT("level");
	pAvatar_level->properUtype = 5;
	pAvatar_level->properFlags = 8;
	pAvatar_level->aliasID = 4;
	KBVar* pAvatar_level_defval = new KBVar((uint16)FCString::Atoi64(TEXT("")));
	pAvatar_level->pDefaultVal = pAvatar_level_defval;
	pAvatarModule->propertys.Add(TEXT("level"), pAvatar_level); 

	pAvatarModule->usePropertyDescrAlias = true;
	pAvatarModule->idpropertys.Add((uint16)pAvatar_level->aliasID, pAvatar_level);

	//DEBUG_MSG("EntityDef::initScriptModules: add(Avatar), property(level / 5).");

	Property* pAvatar_modelID = new Property();
	pAvatar_modelID->name = TEXT("modelID");
	pAvatar_modelID->properUtype = 41006;
	pAvatar_modelID->properFlags = 4;
	pAvatar_modelID->aliasID = 5;
	KBVar* pAvatar_modelID_defval = new KBVar((uint32)FCString::Atoi64(TEXT("0")));
	pAvatar_modelID->pDefaultVal = pAvatar_modelID_defval;
	pAvatarModule->propertys.Add(TEXT("modelID"), pAvatar_modelID); 

	pAvatarModule->usePropertyDescrAlias = true;
	pAvatarModule->idpropertys.Add((uint16)pAvatar_modelID->aliasID, pAvatar_modelID);

	//DEBUG_MSG("EntityDef::initScriptModules: add(Avatar), property(modelID / 41006).");

	Property* pAvatar_modelScale = new Property();
	pAvatar_modelScale->name = TEXT("modelScale");
	pAvatar_modelScale->properUtype = 41007;
	pAvatar_modelScale->properFlags = 4;
	pAvatar_modelScale->aliasID = 6;
	KBVar* pAvatar_modelScale_defval = new KBVar((uint8)FCString::Atoi64(TEXT("30")));
	pAvatar_modelScale->pDefaultVal = pAvatar_modelScale_defval;
	pAvatarModule->propertys.Add(TEXT("modelScale"), pAvatar_modelScale); 

	pAvatarModule->usePropertyDescrAlias = true;
	pAvatarModule->idpropertys.Add((uint16)pAvatar_modelScale->aliasID, pAvatar_modelScale);

	//DEBUG_MSG("EntityDef::initScriptModules: add(Avatar), property(modelScale / 41007).");

	Property* pAvatar_moveSpeed = new Property();
	pAvatar_moveSpeed->name = TEXT("moveSpeed");
	pAvatar_moveSpeed->properUtype = 9;
	pAvatar_moveSpeed->properFlags = 4;
	pAvatar_moveSpeed->aliasID = 7;
	KBVar* pAvatar_moveSpeed_defval = new KBVar((uint8)FCString::Atoi64(TEXT("50")));
	pAvatar_moveSpeed->pDefaultVal = pAvatar_moveSpeed_defval;
	pAvatarModule->propertys.Add(TEXT("moveSpeed"), pAvatar_moveSpeed); 

	pAvatarModule->usePropertyDescrAlias = true;
	pAvatarModule->idpropertys.Add((uint16)pAvatar_moveSpeed->aliasID, pAvatar_moveSpeed);

	//DEBUG_MSG("EntityDef::initScriptModules: add(Avatar), property(moveSpeed / 9).");

	Property* pAvatar_name = new Property();
	pAvatar_name->name = TEXT("name");
	pAvatar_name->properUtype = 41003;
	pAvatar_name->properFlags = 4;
	pAvatar_name->aliasID = 8;
	KBVar* pAvatar_name_defval = new KBVar(FString());
	pAvatar_name->pDefaultVal = pAvatar_name_defval;
	pAvatarModule->propertys.Add(TEXT("name"), pAvatar_name); 

	pAvatarModule->usePropertyDescrAlias = true;
	pAvatarModule->idpropertys.Add((uint16)pAvatar_name->aliasID, pAvatar_name);

	//DEBUG_MSG("EntityDef::initScriptModules: add(Avatar), property(name / 41003).");

	Property* pAvatar_own_val = new Property();
	pAvatar_own_val->name = TEXT("own_val");
	pAvatar_own_val->properUtype = 6;
	pAvatar_own_val->properFlags = 16;
	pAvatar_own_val->aliasID = 9;
	KBVar* pAvatar_own_val_defval = new KBVar((uint16)FCString::Atoi64(TEXT("")));
	pAvatar_own_val->pDefaultVal = pAvatar_own_val_defval;
	pAvatarModule->propertys.Add(TEXT("own_val"), pAvatar_own_val); 

	pAvatarModule->usePropertyDescrAlias = true;
	pAvatarModule->idpropertys.Add((uint16)pAvatar_own_val->aliasID, pAvatar_own_val);

	//DEBUG_MSG("EntityDef::initScriptModules: add(Avatar), property(own_val / 6).");

	Property* pAvatar_spaceUType = new Property();
	pAvatar_spaceUType->name = TEXT("spaceUType");
	pAvatar_spaceUType->properUtype = 41001;
	pAvatar_spaceUType->properFlags = 8;
	pAvatar_spaceUType->aliasID = 10;
	KBVar* pAvatar_spaceUType_defval = new KBVar((uint32)FCString::Atoi64(TEXT("")));
	pAvatar_spaceUType->pDefaultVal = pAvatar_spaceUType_defval;
	pAvatarModule->propertys.Add(TEXT("spaceUType"), pAvatar_spaceUType); 

	pAvatarModule->usePropertyDescrAlias = true;
	pAvatarModule->idpropertys.Add((uint16)pAvatar_spaceUType->aliasID, pAvatar_spaceUType);

	//DEBUG_MSG("EntityDef::initScriptModules: add(Avatar), property(spaceUType / 41001).");

	Property* pAvatar_uid = new Property();
	pAvatar_uid->name = TEXT("uid");
	pAvatar_uid->properUtype = 41004;
	pAvatar_uid->properFlags = 4;
	pAvatar_uid->aliasID = 11;
	KBVar* pAvatar_uid_defval = new KBVar((uint32)FCString::Atoi64(TEXT("0")));
	pAvatar_uid->pDefaultVal = pAvatar_uid_defval;
	pAvatarModule->propertys.Add(TEXT("uid"), pAvatar_uid); 

	pAvatarModule->usePropertyDescrAlias = true;
	pAvatarModule->idpropertys.Add((uint16)pAvatar_uid->aliasID, pAvatar_uid);

	//DEBUG_MSG("EntityDef::initScriptModules: add(Avatar), property(uid / 41004).");

	Property* pAvatar_utype = new Property();
	pAvatar_utype->name = TEXT("utype");
	pAvatar_utype->properUtype = 41005;
	pAvatar_utype->properFlags = 4;
	pAvatar_utype->aliasID = 12;
	KBVar* pAvatar_utype_defval = new KBVar((uint32)FCString::Atoi64(TEXT("0")));
	pAvatar_utype->pDefaultVal = pAvatar_utype_defval;
	pAvatarModule->propertys.Add(TEXT("utype"), pAvatar_utype); 

	pAvatarModule->usePropertyDescrAlias = true;
	pAvatarModule->idpropertys.Add((uint16)pAvatar_utype->aliasID, pAvatar_utype);

	//DEBUG_MSG("EntityDef::initScriptModules: add(Avatar), property(utype / 41005).");

	TArray<DATATYPE_BASE*> Avatar_onJump_args;

	Method* pAvatar_onJump = new Method();
	pAvatar_onJump->name = TEXT("onJump");
	pAvatar_onJump->methodUtype = 12;
	pAvatar_onJump->aliasID = 1;
	pAvatar_onJump->args = Avatar_onJump_args;

	pAvatarModule->methods.Add(TEXT("onJump"), pAvatar_onJump); 
	pAvatarModule->useMethodDescrAlias = true;
	pAvatarModule->idmethods.Add((uint16)pAvatar_onJump->aliasID, pAvatar_onJump);

	//DEBUG_MSG("EntityDef::initScriptModules: add(Avatar), method(onJump / 12).");

	TArray<DATATYPE_BASE*> Avatar_jump_args;

	Method* pAvatar_jump = new Method();
	pAvatar_jump->name = TEXT("jump");
	pAvatar_jump->methodUtype = 10;
	pAvatar_jump->aliasID = -1;
	pAvatar_jump->args = Avatar_jump_args;

	pAvatarModule->methods.Add(TEXT("jump"), pAvatar_jump); 
	pAvatarModule->cell_methods.Add(TEXT("jump"), pAvatar_jump);

	pAvatarModule->idcell_methods.Add(pAvatar_jump->methodUtype, pAvatar_jump);

	//DEBUG_MSG("EntityDef::initScriptModules: add(Avatar), method(jump / 10).");

	TArray<DATATYPE_BASE*> Avatar_relive_args;
	Avatar_relive_args.Add(EntityDef::id2datatypes[2]);

	Method* pAvatar_relive = new Method();
	pAvatar_relive->name = TEXT("relive");
	pAvatar_relive->methodUtype = 9;
	pAvatar_relive->aliasID = -1;
	pAvatar_relive->args = Avatar_relive_args;

	pAvatarModule->methods.Add(TEXT("relive"), pAvatar_relive); 
	pAvatarModule->cell_methods.Add(TEXT("relive"), pAvatar_relive);

	pAvatarModule->idcell_methods.Add(pAvatar_relive->methodUtype, pAvatar_relive);

	//DEBUG_MSG("EntityDef::initScriptModules: add(Avatar), method(relive / 9).");

}

void EntityDef::initDefTypes()
{
	{
		uint16 utype = 2;
		FString typeName = TEXT("ENTITY_SUBSTATE");
		FString name = TEXT("UINT8");
		DATATYPE_BASE** fPtr = EntityDef::datatypes.Find(name);
		DATATYPE_BASE* pVal = fPtr != NULL ? *fPtr : NULL;
		EntityDef::datatypes.Add(typeName, pVal);
		EntityDef::id2datatypes.Add(utype, EntityDef::datatypes[typeName]);
		EntityDef::datatype2id.Add(typeName, utype);
	}

	{
		uint16 utype = 3;
		FString typeName = TEXT("UINT16");
		FString name = TEXT("UINT16");
		DATATYPE_BASE** fPtr = EntityDef::datatypes.Find(name);
		DATATYPE_BASE* pVal = fPtr != NULL ? *fPtr : NULL;
		EntityDef::datatypes.Add(typeName, pVal);
		EntityDef::id2datatypes.Add(utype, EntityDef::datatypes[typeName]);
		EntityDef::datatype2id.Add(typeName, utype);
	}

	{
		uint16 utype = 5;
		FString typeName = TEXT("UID");
		FString name = TEXT("UINT64");
		DATATYPE_BASE** fPtr = EntityDef::datatypes.Find(name);
		DATATYPE_BASE* pVal = fPtr != NULL ? *fPtr : NULL;
		EntityDef::datatypes.Add(typeName, pVal);
		EntityDef::id2datatypes.Add(utype, EntityDef::datatypes[typeName]);
		EntityDef::datatype2id.Add(typeName, utype);
	}

	{
		uint16 utype = 4;
		FString typeName = TEXT("ENTITY_UTYPE");
		FString name = TEXT("UINT32");
		DATATYPE_BASE** fPtr = EntityDef::datatypes.Find(name);
		DATATYPE_BASE* pVal = fPtr != NULL ? *fPtr : NULL;
		EntityDef::datatypes.Add(typeName, pVal);
		EntityDef::id2datatypes.Add(utype, EntityDef::datatypes[typeName]);
		EntityDef::datatype2id.Add(typeName, utype);
	}

	{
		uint16 utype = 6;
		FString typeName = TEXT("ENTITY_STATE");
		FString name = TEXT("INT8");
		DATATYPE_BASE** fPtr = EntityDef::datatypes.Find(name);
		DATATYPE_BASE* pVal = fPtr != NULL ? *fPtr : NULL;
		EntityDef::datatypes.Add(typeName, pVal);
		EntityDef::id2datatypes.Add(utype, EntityDef::datatypes[typeName]);
		EntityDef::datatype2id.Add(typeName, utype);
	}

	{
		uint16 utype = 7;
		FString typeName = TEXT("INT16");
		FString name = TEXT("INT16");
		DATATYPE_BASE** fPtr = EntityDef::datatypes.Find(name);
		DATATYPE_BASE* pVal = fPtr != NULL ? *fPtr : NULL;
		EntityDef::datatypes.Add(typeName, pVal);
		EntityDef::id2datatypes.Add(utype, EntityDef::datatypes[typeName]);
		EntityDef::datatype2id.Add(typeName, utype);
	}

	{
		uint16 utype = 8;
		FString typeName = TEXT("ENTITY_FORBIDS");
		FString name = TEXT("INT32");
		DATATYPE_BASE** fPtr = EntityDef::datatypes.Find(name);
		DATATYPE_BASE* pVal = fPtr != NULL ? *fPtr : NULL;
		EntityDef::datatypes.Add(typeName, pVal);
		EntityDef::id2datatypes.Add(utype, EntityDef::datatypes[typeName]);
		EntityDef::datatype2id.Add(typeName, utype);
	}

	{
		uint16 utype = 9;
		FString typeName = TEXT("INT64");
		FString name = TEXT("INT64");
		DATATYPE_BASE** fPtr = EntityDef::datatypes.Find(name);
		DATATYPE_BASE* pVal = fPtr != NULL ? *fPtr : NULL;
		EntityDef::datatypes.Add(typeName, pVal);
		EntityDef::id2datatypes.Add(utype, EntityDef::datatypes[typeName]);
		EntityDef::datatype2id.Add(typeName, utype);
	}

	{
		uint16 utype = 1;
		FString typeName = TEXT("STRING");
		FString name = TEXT("STRING");
		DATATYPE_BASE** fPtr = EntityDef::datatypes.Find(name);
		DATATYPE_BASE* pVal = fPtr != NULL ? *fPtr : NULL;
		EntityDef::datatypes.Add(typeName, pVal);
		EntityDef::id2datatypes.Add(utype, EntityDef::datatypes[typeName]);
		EntityDef::datatype2id.Add(typeName, utype);
	}

	{
		uint16 utype = 12;
		FString typeName = TEXT("UNICODE");
		FString name = TEXT("UNICODE");
		DATATYPE_BASE** fPtr = EntityDef::datatypes.Find(name);
		DATATYPE_BASE* pVal = fPtr != NULL ? *fPtr : NULL;
		EntityDef::datatypes.Add(typeName, pVal);
		EntityDef::id2datatypes.Add(utype, EntityDef::datatypes[typeName]);
		EntityDef::datatype2id.Add(typeName, utype);
	}

	{
		uint16 utype = 13;
		FString typeName = TEXT("FLOAT");
		FString name = TEXT("FLOAT");
		DATATYPE_BASE** fPtr = EntityDef::datatypes.Find(name);
		DATATYPE_BASE* pVal = fPtr != NULL ? *fPtr : NULL;
		EntityDef::datatypes.Add(typeName, pVal);
		EntityDef::id2datatypes.Add(utype, EntityDef::datatypes[typeName]);
		EntityDef::datatype2id.Add(typeName, utype);
	}

	{
		uint16 utype = 14;
		FString typeName = TEXT("DOUBLE");
		FString name = TEXT("DOUBLE");
		DATATYPE_BASE** fPtr = EntityDef::datatypes.Find(name);
		DATATYPE_BASE* pVal = fPtr != NULL ? *fPtr : NULL;
		EntityDef::datatypes.Add(typeName, pVal);
		EntityDef::id2datatypes.Add(utype, EntityDef::datatypes[typeName]);
		EntityDef::datatype2id.Add(typeName, utype);
	}

	{
		uint16 utype = 10;
		FString typeName = TEXT("UID1");
		FString name = TEXT("PYTHON");
		DATATYPE_BASE** fPtr = EntityDef::datatypes.Find(name);
		DATATYPE_BASE* pVal = fPtr != NULL ? *fPtr : NULL;
		EntityDef::datatypes.Add(typeName, pVal);
		EntityDef::id2datatypes.Add(utype, EntityDef::datatypes[typeName]);
		EntityDef::datatype2id.Add(typeName, utype);
	}

	{
		uint16 utype = 10;
		FString typeName = TEXT("PY_DICT");
		FString name = TEXT("PY_DICT");
		DATATYPE_BASE** fPtr = EntityDef::datatypes.Find(name);
		DATATYPE_BASE* pVal = fPtr != NULL ? *fPtr : NULL;
		EntityDef::datatypes.Add(typeName, pVal);
		EntityDef::id2datatypes.Add(utype, EntityDef::datatypes[typeName]);
		EntityDef::datatype2id.Add(typeName, utype);
	}

	{
		uint16 utype = 10;
		FString typeName = TEXT("PY_TUPLE");
		FString name = TEXT("PY_TUPLE");
		DATATYPE_BASE** fPtr = EntityDef::datatypes.Find(name);
		DATATYPE_BASE* pVal = fPtr != NULL ? *fPtr : NULL;
		EntityDef::datatypes.Add(typeName, pVal);
		EntityDef::id2datatypes.Add(utype, EntityDef::datatypes[typeName]);
		EntityDef::datatype2id.Add(typeName, utype);
	}

	{
		uint16 utype = 10;
		FString typeName = TEXT("PY_LIST");
		FString name = TEXT("PY_LIST");
		DATATYPE_BASE** fPtr = EntityDef::datatypes.Find(name);
		DATATYPE_BASE* pVal = fPtr != NULL ? *fPtr : NULL;
		EntityDef::datatypes.Add(typeName, pVal);
		EntityDef::id2datatypes.Add(utype, EntityDef::datatypes[typeName]);
		EntityDef::datatype2id.Add(typeName, utype);
	}

	{
		uint16 utype = 20;
		FString typeName = TEXT("ENTITYCALL");
		FString name = TEXT("ENTITYCALL");
		DATATYPE_BASE** fPtr = EntityDef::datatypes.Find(name);
		DATATYPE_BASE* pVal = fPtr != NULL ? *fPtr : NULL;
		EntityDef::datatypes.Add(typeName, pVal);
		EntityDef::id2datatypes.Add(utype, EntityDef::datatypes[typeName]);
		EntityDef::datatype2id.Add(typeName, utype);
	}

	{
		uint16 utype = 11;
		FString typeName = TEXT("BLOB");
		FString name = TEXT("BLOB");
		DATATYPE_BASE** fPtr = EntityDef::datatypes.Find(name);
		DATATYPE_BASE* pVal = fPtr != NULL ? *fPtr : NULL;
		EntityDef::datatypes.Add(typeName, pVal);
		EntityDef::id2datatypes.Add(utype, EntityDef::datatypes[typeName]);
		EntityDef::datatype2id.Add(typeName, utype);
	}

	{
		uint16 utype = 15;
		FString typeName = TEXT("VECTOR2");
		FString name = TEXT("VECTOR2");
		DATATYPE_BASE** fPtr = EntityDef::datatypes.Find(name);
		DATATYPE_BASE* pVal = fPtr != NULL ? *fPtr : NULL;
		EntityDef::datatypes.Add(typeName, pVal);
		EntityDef::id2datatypes.Add(utype, EntityDef::datatypes[typeName]);
		EntityDef::datatype2id.Add(typeName, utype);
	}

	{
		uint16 utype = 16;
		FString typeName = TEXT("DIRECTION3D");
		FString name = TEXT("VECTOR3");
		DATATYPE_BASE** fPtr = EntityDef::datatypes.Find(name);
		DATATYPE_BASE* pVal = fPtr != NULL ? *fPtr : NULL;
		EntityDef::datatypes.Add(typeName, pVal);
		EntityDef::id2datatypes.Add(utype, EntityDef::datatypes[typeName]);
		EntityDef::datatype2id.Add(typeName, utype);
	}

	{
		uint16 utype = 17;
		FString typeName = TEXT("VECTOR4");
		FString name = TEXT("VECTOR4");
		DATATYPE_BASE** fPtr = EntityDef::datatypes.Find(name);
		DATATYPE_BASE* pVal = fPtr != NULL ? *fPtr : NULL;
		EntityDef::datatypes.Add(typeName, pVal);
		EntityDef::id2datatypes.Add(utype, EntityDef::datatypes[typeName]);
		EntityDef::datatype2id.Add(typeName, utype);
	}

	{
		uint16 utype = 22;
		FString typeName = TEXT("ENTITY_FORBID_COUNTER");
		DATATYPE_ENTITY_FORBID_COUNTER* pDatatype = new DATATYPE_ENTITY_FORBID_COUNTER();
		EntityDef::datatypes.Add(typeName, (DATATYPE_BASE*)pDatatype);
		EntityDef::id2datatypes.Add(utype, EntityDef::datatypes[typeName]);
		EntityDef::datatype2id.Add(typeName, utype);
	}

	{
		uint16 utype = 23;
		FString typeName = TEXT("ENTITYID_LIST");
		DATATYPE_ENTITYID_LIST* pDatatype = new DATATYPE_ENTITYID_LIST();
		EntityDef::datatypes.Add(typeName, (DATATYPE_BASE*)pDatatype);
		EntityDef::id2datatypes.Add(utype, EntityDef::datatypes[typeName]);
		EntityDef::datatype2id.Add(typeName, utype);
	}

	{
		uint16 utype = 24;
		FString typeName = TEXT("AVATAR_DATA");
		DATATYPE_AVATAR_DATA* pDatatype = new DATATYPE_AVATAR_DATA();
		EntityDef::datatypes.Add(typeName, (DATATYPE_BASE*)pDatatype);
		EntityDef::id2datatypes.Add(utype, EntityDef::datatypes[typeName]);
		EntityDef::datatype2id.Add(typeName, utype);
	}

	{
		uint16 utype = 25;
		FString typeName = TEXT("AVATAR_INFOS");
		DATATYPE_AVATAR_INFOS* pDatatype = new DATATYPE_AVATAR_INFOS();
		EntityDef::datatypes.Add(typeName, (DATATYPE_BASE*)pDatatype);
		EntityDef::id2datatypes.Add(utype, EntityDef::datatypes[typeName]);
		EntityDef::datatype2id.Add(typeName, utype);
	}

	{
		uint16 utype = 26;
		FString typeName = TEXT("AVATAR_INFOS_LIST");
		DATATYPE_AVATAR_INFOS_LIST* pDatatype = new DATATYPE_AVATAR_INFOS_LIST();
		EntityDef::datatypes.Add(typeName, (DATATYPE_BASE*)pDatatype);
		EntityDef::id2datatypes.Add(utype, EntityDef::datatypes[typeName]);
		EntityDef::datatype2id.Add(typeName, utype);
	}

	for(auto& Elem : EntityDef::datatypes)
	{
		if(Elem.Value)
		{
			Elem.Value->bind();
		}
	}
}


}