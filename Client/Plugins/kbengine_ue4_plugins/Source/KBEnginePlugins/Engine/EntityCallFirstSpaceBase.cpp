#include "EntityCallFirstSpaceBase.h"
#include "Bundle.h"

namespace KBEngine
{

EntityBaseEntityCall_FirstSpaceBase::EntityBaseEntityCall_FirstSpaceBase(int32 eid, const FString& ename) : EntityCall(eid, ename)
{
	type = ENTITYCALL_TYPE_BASE;
}

EntityBaseEntityCall_FirstSpaceBase::~EntityBaseEntityCall_FirstSpaceBase()
{
}



EntityCellEntityCall_FirstSpaceBase::EntityCellEntityCall_FirstSpaceBase(int32 eid, const FString& ename) : EntityCall(eid, ename)
{
	type = ENTITYCALL_TYPE_CELL;
}

EntityCellEntityCall_FirstSpaceBase::~EntityCellEntityCall_FirstSpaceBase()
{
}


}