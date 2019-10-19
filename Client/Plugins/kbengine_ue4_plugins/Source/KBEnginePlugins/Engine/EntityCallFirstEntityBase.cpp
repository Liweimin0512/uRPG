#include "EntityCallFirstEntityBase.h"
#include "Bundle.h"

namespace KBEngine
{

EntityBaseEntityCall_FirstEntityBase::EntityBaseEntityCall_FirstEntityBase(int32 eid, const FString& ename) : EntityCall(eid, ename)
{
	type = ENTITYCALL_TYPE_BASE;
}

EntityBaseEntityCall_FirstEntityBase::~EntityBaseEntityCall_FirstEntityBase()
{
}



EntityCellEntityCall_FirstEntityBase::EntityCellEntityCall_FirstEntityBase(int32 eid, const FString& ename) : EntityCall(eid, ename)
{
	type = ENTITYCALL_TYPE_CELL;
}

EntityCellEntityCall_FirstEntityBase::~EntityCellEntityCall_FirstEntityBase()
{
}

void EntityCellEntityCall_FirstEntityBase::say(const FString& arg1)
{
	Bundle* pBundleRet = newCall("say", 0);
	if(!pBundleRet)
		return;

	pBundleRet->writeUnicode(arg1);
	sendCall(NULL);
}


}