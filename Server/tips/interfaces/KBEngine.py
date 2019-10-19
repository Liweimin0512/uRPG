def addTimer( initialOffset, repeatOffset=0, callbackObj=None ):
	"""	
	功能说明：
	注册一个定时器，定时器由回调函数callbackObj触发，回调函数将在"initialOffset"秒后被执行第1次，而后将每间隔"repeatOffset"秒执行1次。
	
	例子:
	
	# 这里是使用addTimer的一个例子
	        import KBEngine
	 
	        # 增加一个定时器，5秒后执行第1次，而后每1秒执行1次，用户参数是9
	        KBEngine.addTimer( 5, 1, onTimer_Callbackfun )
	 
	        # 增加一个定时器，1秒后执行，用户参数缺省是0
	        KBEngine.addTimer( 1, onTimer_Callbackfun )
	 
	    def onTimer_Callbackfun( id ):
	        print "onTimer_Callbackfun called: id %i" % ( id )
	        # if 这是不断重复的定时器，当不再需要该定时器的时候，调用下面函数移除:
	        #     KBEngine.delTimer( id )
	
	
	
	参数：
	
	
	@initialOffset
	float，指定定时器从注册到第一次回调的时间间隔（秒）。
	
	
	@repeatOffset
	float，指定第一次回调执行后每次执行的时间间隔（秒）。必须用函数delTimer移除定时器，否则它会一直重复下去。值小于等于0将被忽略。
	
	
	@callbackObj
	function，指定的回调函数对象。
	
	
	
	
	
	返回:
	
	integer，该函数返回timer的内部id，这个id可用于delTimer移除定时器。
	
	
	
	
	
	

	"""
	pass

def accountLoginResponse( commitName, realAccountName, extraDatas, errorCode ):
	"""	
	功能说明：
	在onRequestAccountLogin被回调后，脚本需要调用此接口给出登陆处理结果。
	
	
	参数：
	
	
	@commitName
	string，客户端请求时所提交的名称。
	
	
	@realAccountName
	string，返回真实的账号名称（没有特殊要求通常就是commitName，使用各种别名账号登陆时可用到）。
	
	
	@extraDatas
	bytes，客户端请求时所附带的数据，可将数据转发第三方平台，在此提供对其进行修改的机会。该参数可以通过base实体的getClientDatas接口在脚本读取。
	
	
	@errorCode
	integer，错误码。如果需要中断用户的行为可在此设置错误码，错误码可参考（KBEngine.SERVER_ERROR_*， 描述在kbengine/kbe/res/server/server_errors.xml），否则提交KBEngine.SERVER_SUCCESS代表允许此处登陆。
	
	
	
	
	
	

	"""
	pass

def createAccountResponse( commitName, realAccountName, extraDatas, errorCode ):
	"""	
	功能说明：
	在onRequestCreateAccount被回调后，脚本需要调用此接口给出账号创建处理结果。
	
	
	参数：
	
	
	@commitName
	string，客户端请求时所提交的名称。
	
	
	@realAccountName
	string，返回真实的账号名称（没有特殊要求通常就是commitName，使用各种别名账号登陆时可用到）。
	
	
	@extraDatas
	bytes，客户端请求时所附带的数据，可将数据转发第三方平台，在此提供对其进行修改的机会。该参数可以通过base实体的getClientDatas接口在脚本读取。
	
	
	@errorCode
	integer，错误码。如果需要中断用户的行为可在此设置错误码，错误码可参考（KBEngine.SERVER_ERROR_*， 描述在kbengine/kbe/res/server/server_errors.xml），否则提交KBEngine.SERVER_SUCCESS代表允许此处登陆。
	
	
	
	
	
	

	"""
	pass

def chargeResponse( orderID, extraDatas, errorCode ):
	"""	
	功能说明：
	在onRequestCharge被回调后，脚本需要调用此接口给出计费处理结果。
	
	
	参数：
	
	
	@ordersID
	uint64，订单的ID。
	
	
	@extraDatas
	bytes，客户端请求时所附带的数据，可将数据转发第三方平台，在此提供对其进行修改的机会。该参数可以通过base实体的getClientDatas接口在脚本读取。
	
	
	@errorCode
	integer，错误码。如果需要中断用户的行为可在此设置错误码，错误码可参考（KBEngine.SERVER_ERROR_*， 描述在kbengine/kbe/res/server/server_errors.xml），否则提交KBEngine.SERVER_SUCCESS代表允许此处登陆。
	
	
	
	
	
	

	"""
	pass

def delTimer( id ):
	"""	
	功能说明：
	函数delTimer用于移除一个注册的定时器，移除后的定时器不再执行。只执行1次的定时器在执行回调后自动移除，不必要使用delTimer移除。
	如果delTimer函数使用一个无效的id（例如已经移除），将会产生错误。
	
	到KBEngine.addTimer参考定时器的一个使用例子。
	
	
	参数：
	
	
	@id
	integer，它指定要移除的定时器id。
	
	
	
	
	
	
	
	

	"""
	pass

def onInterfaceAppReady(  ):
	"""	
	功能说明：
	当前进程已经准备好的时候回调此函数。
	注意：该回调接口必须实现在入口模块(kbengine_defaults.xml->entryScriptFile)中。
	
	
	

	"""
	pass

def onInterfaceAppShutDown(  ):
	"""	
	功能说明：
	进程关闭会回调此函数。
	注意：该回调接口必须实现在入口模块(kbengine_defaults.xml->entryScriptFile)中。
	
	
	

	"""
	pass

def onRequestCreateAccount( registerName, password, datas ):
	"""	
	功能说明：
	当客户端请求服务器创建账号时，该回调被调用。
	
	可在此函数内数据进行检查和修改，将最终结果通过KBEngine.createAccountResponse提交给引擎。
	
	注意：该回调接口必须实现在入口模块(kbengine_defaults.xml->entryScriptFile)中。
	
	
	参数：
	
	
	@registerName
	string，客户端请求时所提交的名称。
	
	
	@password
	string，密码。
	
	
	@datas
	bytes，客户端请求时所附带的数据，可将数据转发第三方平台。
	
	
	
	
	

	"""
	pass

def onRequestAccountLogin( loginName, password, datas ):
	"""	
	功能说明：
	当客户端请求服务器登陆账号时，该回调被调用。
	可在此函数内数据进行检查和修改，将最终结果通过KBEngine.accountLoginResponse提交给引擎。
	
	注意：该回调接口必须实现在入口模块(kbengine_defaults.xml->entryScriptFile)中。
	
	
	参数：
	
	
	@loginName
	string，客户端请求时所提交的名称。
	
	
	@password
	string，密码。
	
	
	@datas
	bytes，客户端请求时所附带的数据，可将数据转发第三方平台。
	
	
	
	
	

	"""
	pass

def onRequestCharge( ordersID, entityDBID, datas ):
	"""	
	功能说明：
	当请求计费时（通常是baseapp上调用了KBEngine.charge），该回调被调用。
	可在此函数内数据进行检查和修改，将最终结果通过KBEngine.chargeResponse提交给引擎。
	
	注意：该回调接口必须实现在入口模块(kbengine_defaults.xml->entryScriptFile)中。
	
	
	参数：
	
	
	@ordersID
	uint64，订单的ID。
	
	
	@entityDBID
	uint64，提交订单的实体DBID。
	
	
	@datas
	bytes，客户端请求时所附带的数据，可将数据转发第三方平台。
	
	
	
	
	
	
	
	

	"""
	pass

