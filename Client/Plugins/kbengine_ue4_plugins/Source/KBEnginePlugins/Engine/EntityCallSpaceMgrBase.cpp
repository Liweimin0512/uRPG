#include "EntityCallSpaceMgrBase.h"
#include "Bundle.h"

namespace KBEngine
{

EntityBaseEntityCall_SpaceMgrBase::EntityBaseEntityCall_SpaceMgrBase(int32 eid, const FString& ename) : EntityCall(eid, ename)
{
	type = ENTITYCALL_TYPE_BASE;
}

EntityBaseEntityCall_SpaceMgrBase::~EntityBaseEntityCall_SpaceMgrBase()
{
}



EntityCellEntityCall_SpaceMgrBase::EntityCellEntityCall_SpaceMgrBase(int32 eid, const FString& ename) : EntityCall(eid, ename)
{
	type = ENTITYCALL_TYPE_CELL;
}

EntityCellEntityCall_SpaceMgrBase::~EntityCellEntityCall_SpaceMgrBase()
{
}


}