#include "AvatarBase.h"
#include "KBVar.h"
#include "EntityDef.h"
#include "ScriptModule.h"
#include "Property.h"
#include "Method.h"
#include "DataTypes.h"
#include "CustomDataTypes.h"
#include "MemoryStream.h"
#include "EntityComponent.h"

namespace KBEngine
{



void AvatarBase::onComponentsEnterworld()
{
}

void AvatarBase::onComponentsLeaveworld()
{
}

void AvatarBase::onGetBase()
{
	if(pBaseEntityCall)
		delete pBaseEntityCall;

	pBaseEntityCall = new EntityBaseEntityCall_AvatarBase(id(), className());
}

void AvatarBase::onGetCell()
{
	if(pCellEntityCall)
		delete pCellEntityCall;

	pCellEntityCall = new EntityCellEntityCall_AvatarBase(id(), className());
}

void AvatarBase::onLoseCell()
{
	delete pCellEntityCall;
	pCellEntityCall = NULL;
}

EntityCall* AvatarBase::getBaseEntityCall()
{
	return pBaseEntityCall;
}

EntityCall* AvatarBase::getCellEntityCall()
{
	return pCellEntityCall;
}

void AvatarBase::onRemoteMethodCall(MemoryStream& stream)
{
	ScriptModule* sm = *EntityDef::moduledefs.Find("Avatar");
	uint16 methodUtype = 0;
	uint16 componentPropertyUType = 0;

	if (sm->usePropertyDescrAlias)
	{
		componentPropertyUType = stream.readUint8();
	}
	else
	{
		componentPropertyUType = stream.readUint16();
	}

	if (sm->useMethodDescrAlias)
	{
		methodUtype = stream.read<uint8>();
	}
	else
	{
		methodUtype = stream.read<uint16>();
	}

	if(componentPropertyUType > 0)
	{
		KBE_ASSERT(false);

		return;
	}

	Method* pMethod = sm->idmethods[methodUtype];

	switch(pMethod->methodUtype)
	{
		case 12:
		{
			onJump();
			break;
		}
		default:
			break;
	};
}

void AvatarBase::onUpdatePropertys(MemoryStream& stream)
{
	ScriptModule* sm = *EntityDef::moduledefs.Find("Avatar");

	while(stream.length() > 0)
	{
		uint16 componentPropertyUType = 0;
		uint16 properUtype = 0;

		if (sm->usePropertyDescrAlias)
		{
			componentPropertyUType = stream.readUint8();
			properUtype = stream.read<uint8>();
		}
		else
		{
			componentPropertyUType = stream.readUint16();
			properUtype = stream.read<uint16>();
		}

		if(componentPropertyUType > 0)
		{
			KBE_ASSERT(false);

			return;
		}

		Property* pProp = sm->idpropertys[properUtype];

		switch(pProp->properUtype)
		{
			case 40001:
			{
				FVector oldval_direction = direction;
				direction = stream.readVector3();

				if(pProp->isBase())
				{
					if(inited())
						onDirectionChanged(oldval_direction);
				}
				else
				{
					if(inWorld())
						onDirectionChanged(oldval_direction);
				}

				break;
			}
			case 5:
			{
				uint16 oldval_level = level;
				level = stream.readUint16();

				if(pProp->isBase())
				{
					if(inited())
						onLevelChanged(oldval_level);
				}
				else
				{
					if(inWorld())
						onLevelChanged(oldval_level);
				}

				break;
			}
			case 41006:
			{
				uint32 oldval_modelID = modelID;
				modelID = stream.readUint32();

				if(pProp->isBase())
				{
					if(inited())
						onModelIDChanged(oldval_modelID);
				}
				else
				{
					if(inWorld())
						onModelIDChanged(oldval_modelID);
				}

				break;
			}
			case 41007:
			{
				uint8 oldval_modelScale = modelScale;
				modelScale = stream.readUint8();

				if(pProp->isBase())
				{
					if(inited())
						onModelScaleChanged(oldval_modelScale);
				}
				else
				{
					if(inWorld())
						onModelScaleChanged(oldval_modelScale);
				}

				break;
			}
			case 9:
			{
				uint8 oldval_moveSpeed = moveSpeed;
				moveSpeed = stream.readUint8();

				if(pProp->isBase())
				{
					if(inited())
						onMoveSpeedChanged(oldval_moveSpeed);
				}
				else
				{
					if(inWorld())
						onMoveSpeedChanged(oldval_moveSpeed);
				}

				break;
			}
			case 41003:
			{
				FString oldval_name = name;
				name = stream.readUnicode();

				if(pProp->isBase())
				{
					if(inited())
						onNameChanged(oldval_name);
				}
				else
				{
					if(inWorld())
						onNameChanged(oldval_name);
				}

				break;
			}
			case 6:
			{
				uint16 oldval_own_val = own_val;
				own_val = stream.readUint16();

				if(pProp->isBase())
				{
					if(inited())
						onOwn_valChanged(oldval_own_val);
				}
				else
				{
					if(inWorld())
						onOwn_valChanged(oldval_own_val);
				}

				break;
			}
			case 40000:
			{
				FVector oldval_position = position;
				position = stream.readVector3();

				if(pProp->isBase())
				{
					if(inited())
						onPositionChanged(oldval_position);
				}
				else
				{
					if(inWorld())
						onPositionChanged(oldval_position);
				}

				break;
			}
			case 40002:
			{
				stream.readUint32();
				break;
			}
			case 41001:
			{
				uint32 oldval_spaceUType = spaceUType;
				spaceUType = stream.readUint32();

				if(pProp->isBase())
				{
					if(inited())
						onSpaceUTypeChanged(oldval_spaceUType);
				}
				else
				{
					if(inWorld())
						onSpaceUTypeChanged(oldval_spaceUType);
				}

				break;
			}
			case 41004:
			{
				uint32 oldval_uid = uid;
				uid = stream.readUint32();

				if(pProp->isBase())
				{
					if(inited())
						onUidChanged(oldval_uid);
				}
				else
				{
					if(inWorld())
						onUidChanged(oldval_uid);
				}

				break;
			}
			case 41005:
			{
				uint32 oldval_utype = utype;
				utype = stream.readUint32();

				if(pProp->isBase())
				{
					if(inited())
						onUtypeChanged(oldval_utype);
				}
				else
				{
					if(inWorld())
						onUtypeChanged(oldval_utype);
				}

				break;
			}
			default:
				break;
		};
	}
}

void AvatarBase::callPropertysSetMethods()
{
	ScriptModule* sm = EntityDef::moduledefs["Avatar"];
	TMap<uint16, Property*>& pdatas = sm->idpropertys;

	FVector oldval_direction = direction;
	Property* pProp_direction = pdatas[2];
	if(pProp_direction->isBase())
	{
		if(inited() && !inWorld())
			onDirectionChanged(oldval_direction);
	}
	else
	{
		if(inWorld())
		{
			if(pProp_direction->isOwnerOnly() && !isPlayer())
			{
			}
			else
			{
				onDirectionChanged(oldval_direction);
			}
		}
	}

	uint16 oldval_level = level;
	Property* pProp_level = pdatas[4];
	if(pProp_level->isBase())
	{
		if(inited() && !inWorld())
			onLevelChanged(oldval_level);
	}
	else
	{
		if(inWorld())
		{
			if(pProp_level->isOwnerOnly() && !isPlayer())
			{
			}
			else
			{
				onLevelChanged(oldval_level);
			}
		}
	}

	uint32 oldval_modelID = modelID;
	Property* pProp_modelID = pdatas[5];
	if(pProp_modelID->isBase())
	{
		if(inited() && !inWorld())
			onModelIDChanged(oldval_modelID);
	}
	else
	{
		if(inWorld())
		{
			if(pProp_modelID->isOwnerOnly() && !isPlayer())
			{
			}
			else
			{
				onModelIDChanged(oldval_modelID);
			}
		}
	}

	uint8 oldval_modelScale = modelScale;
	Property* pProp_modelScale = pdatas[6];
	if(pProp_modelScale->isBase())
	{
		if(inited() && !inWorld())
			onModelScaleChanged(oldval_modelScale);
	}
	else
	{
		if(inWorld())
		{
			if(pProp_modelScale->isOwnerOnly() && !isPlayer())
			{
			}
			else
			{
				onModelScaleChanged(oldval_modelScale);
			}
		}
	}

	uint8 oldval_moveSpeed = moveSpeed;
	Property* pProp_moveSpeed = pdatas[7];
	if(pProp_moveSpeed->isBase())
	{
		if(inited() && !inWorld())
			onMoveSpeedChanged(oldval_moveSpeed);
	}
	else
	{
		if(inWorld())
		{
			if(pProp_moveSpeed->isOwnerOnly() && !isPlayer())
			{
			}
			else
			{
				onMoveSpeedChanged(oldval_moveSpeed);
			}
		}
	}

	FString oldval_name = name;
	Property* pProp_name = pdatas[8];
	if(pProp_name->isBase())
	{
		if(inited() && !inWorld())
			onNameChanged(oldval_name);
	}
	else
	{
		if(inWorld())
		{
			if(pProp_name->isOwnerOnly() && !isPlayer())
			{
			}
			else
			{
				onNameChanged(oldval_name);
			}
		}
	}

	uint16 oldval_own_val = own_val;
	Property* pProp_own_val = pdatas[9];
	if(pProp_own_val->isBase())
	{
		if(inited() && !inWorld())
			onOwn_valChanged(oldval_own_val);
	}
	else
	{
		if(inWorld())
		{
			if(pProp_own_val->isOwnerOnly() && !isPlayer())
			{
			}
			else
			{
				onOwn_valChanged(oldval_own_val);
			}
		}
	}

	FVector oldval_position = position;
	Property* pProp_position = pdatas[1];
	if(pProp_position->isBase())
	{
		if(inited() && !inWorld())
			onPositionChanged(oldval_position);
	}
	else
	{
		if(inWorld())
		{
			if(pProp_position->isOwnerOnly() && !isPlayer())
			{
			}
			else
			{
				onPositionChanged(oldval_position);
			}
		}
	}

	uint32 oldval_spaceUType = spaceUType;
	Property* pProp_spaceUType = pdatas[10];
	if(pProp_spaceUType->isBase())
	{
		if(inited() && !inWorld())
			onSpaceUTypeChanged(oldval_spaceUType);
	}
	else
	{
		if(inWorld())
		{
			if(pProp_spaceUType->isOwnerOnly() && !isPlayer())
			{
			}
			else
			{
				onSpaceUTypeChanged(oldval_spaceUType);
			}
		}
	}

	uint32 oldval_uid = uid;
	Property* pProp_uid = pdatas[11];
	if(pProp_uid->isBase())
	{
		if(inited() && !inWorld())
			onUidChanged(oldval_uid);
	}
	else
	{
		if(inWorld())
		{
			if(pProp_uid->isOwnerOnly() && !isPlayer())
			{
			}
			else
			{
				onUidChanged(oldval_uid);
			}
		}
	}

	uint32 oldval_utype = utype;
	Property* pProp_utype = pdatas[12];
	if(pProp_utype->isBase())
	{
		if(inited() && !inWorld())
			onUtypeChanged(oldval_utype);
	}
	else
	{
		if(inWorld())
		{
			if(pProp_utype->isOwnerOnly() && !isPlayer())
			{
			}
			else
			{
				onUtypeChanged(oldval_utype);
			}
		}
	}

}

AvatarBase::AvatarBase():
	Entity(),
	pBaseEntityCall(NULL),
	pCellEntityCall(NULL),
	level((uint16)FCString::Atoi64(TEXT("0"))),
	modelID((uint32)FCString::Atoi64(TEXT("0"))),
	modelScale((uint8)FCString::Atoi64(TEXT("30"))),
	moveSpeed((uint8)FCString::Atoi64(TEXT("50"))),
	name(TEXT("")),
	own_val((uint16)FCString::Atoi64(TEXT("0"))),
	spaceUType((uint32)FCString::Atoi64(TEXT("0"))),
	uid((uint32)FCString::Atoi64(TEXT("0"))),
	utype((uint32)FCString::Atoi64(TEXT("0")))
{
}

AvatarBase::~AvatarBase()
{
	if(pBaseEntityCall)
		delete pBaseEntityCall;

	if(pCellEntityCall)
		delete pCellEntityCall;

}

void AvatarBase::attachComponents()
{
}

void AvatarBase::detachComponents()
{
}

}