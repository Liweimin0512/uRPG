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


}