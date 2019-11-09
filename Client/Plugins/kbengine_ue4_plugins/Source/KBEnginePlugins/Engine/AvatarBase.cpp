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
			case 6:
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
			case 5:
			{
				uint8 oldval_raceTypeCell = raceTypeCell;
				raceTypeCell = stream.readUint8();

				if(pProp->isBase())
				{
					if(inited())
						onRaceTypeCellChanged(oldval_raceTypeCell);
				}
				else
				{
					if(inWorld())
						onRaceTypeCellChanged(oldval_raceTypeCell);
				}

				break;
			}
			case 40002:
			{
				stream.readUint32();
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

	uint8 oldval_raceTypeCell = raceTypeCell;
	Property* pProp_raceTypeCell = pdatas[5];
	if(pProp_raceTypeCell->isBase())
	{
		if(inited() && !inWorld())
			onRaceTypeCellChanged(oldval_raceTypeCell);
	}
	else
	{
		if(inWorld())
		{
			if(pProp_raceTypeCell->isOwnerOnly() && !isPlayer())
			{
			}
			else
			{
				onRaceTypeCellChanged(oldval_raceTypeCell);
			}
		}
	}

}

AvatarBase::AvatarBase():
	Entity(),
	pBaseEntityCall(NULL),
	pCellEntityCall(NULL),
	level((uint16)FCString::Atoi64(TEXT("0"))),
	raceTypeCell((uint8)FCString::Atoi64(TEXT("0")))
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