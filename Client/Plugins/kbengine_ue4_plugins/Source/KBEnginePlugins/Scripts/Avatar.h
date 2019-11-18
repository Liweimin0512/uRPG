#pragma once
#include "Engine/KBECommon.h"
#include "Engine/AvatarBase.h"

namespace KBEngine 
{

	class Avatar :
		public AvatarBase
	{
	public:
		Avatar();
		virtual ~Avatar();

		virtual void __init__() override;

	//public:
	//	virtual void onDestroy() override;
	//	virtual void onEnterWorld() override;
	//	virtual void onLeaveWorld() override;
	//	virtual void onEnterSpace() override;
	//	virtual void onLeaveSpace() override;


	};


}