#include "CustomDataTypes.h"
#include "EntityDef.h"
#include "KBDebug.h"
#include "DataTypes.h"
#include "Runtime/Core/Public/Misc/Variant.h"

namespace KBEngine
{

void DATATYPE_AVATAR_INFO::createFromStreamEx(MemoryStream& stream, AVATAR_INFO& datas)
{
	datas.dbid = stream.readUint64();
	datas.name = stream.readUnicode();
	datas.roleType = stream.readUint8();
	datas.level = stream.readUint16();
}

void DATATYPE_AVATAR_INFO::addToStreamEx(Bundle& stream, const AVATAR_INFO& v)
{
	stream.writeUint64(v.dbid);
	stream.writeUnicode(v.name);
	stream.writeUint8(v.roleType);
	stream.writeUint16(v.level);
}

void DATATYPE_AVATAR_INFO_LIST::createFromStreamEx(MemoryStream& stream, AVATAR_INFO_LIST& datas)
{
	values_DataType.createFromStreamEx(stream, datas.values);
}

void DATATYPE_AVATAR_INFO_LIST::addToStreamEx(Bundle& stream, const AVATAR_INFO_LIST& v)
{
	values_DataType.addToStreamEx(stream, v.values);
}


}