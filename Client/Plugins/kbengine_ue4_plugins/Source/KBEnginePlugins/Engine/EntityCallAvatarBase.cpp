#include "EntityCallAvatarBase.h"
#include "Bundle.h"

namespace KBEngine
{

EntityBaseEntityCall_AvatarBase::EntityBaseEntityCall_AvatarBase(int32 eid, const FString& ename) : EntityCall(eid, ename)
{
	type = ENTITYCALL_TYPE_BASE;
}

EntityBaseEntityCall_AvatarBase::~EntityBaseEntityCall_AvatarBase()
{
}



EntityCellEntityCall_AvatarBase::EntityCellEntityCall_AvatarBase(int32 eid, const FString& ename) : EntityCall(eid, ename)
{
	type = ENTITYCALL_TYPE_CELL;
}

EntityCellEntityCall_AvatarBase::~EntityCellEntityCall_AvatarBase()
{
}

void EntityCellEntityCall_AvatarBase::jump()
{
	Bundle* pBundleRet = newCall("jump", 0);
	if(!pBundleRet)
		return;

	sendCall(NULL);
}

void EntityCellEntityCall_AvatarBase::relive(uint8 arg1)
{
	Bundle* pBundleRet = newCall("relive", 0);
	if(!pBundleRet)
		return;

	pBundleRet->writeUint8(arg1);
	sendCall(NULL);
}


}