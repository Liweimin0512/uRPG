/*
	Generated by KBEngine!
	Please do not modify this file!
	
	tools = kbcmd
*/

#pragma once

#include "KBECommon.h"
#include "EntityCall.h"
#include "KBETypes.h"
#include "CustomDataTypes.h"


// defined in */scripts/entity_defs/Test.def

namespace KBEngine
{

class KBENGINEPLUGINS_API EntityBaseEntityCall_TestBase : public EntityCall
{
public:
	uint16 entityComponentPropertyID;

	EntityBaseEntityCall_TestBase(uint16 ecpID, int32 eid);

	virtual ~EntityBaseEntityCall_TestBase();
	void say(int32 arg1);
};

class KBENGINEPLUGINS_API EntityCellEntityCall_TestBase : public EntityCall
{
public:
	uint16 entityComponentPropertyID;

	EntityCellEntityCall_TestBase(uint16 ecpID, int32 eid);

	virtual ~EntityCellEntityCall_TestBase();
	void hello(int32 arg1);
};

}