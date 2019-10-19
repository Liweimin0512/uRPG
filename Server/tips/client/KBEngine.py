class Entity:
	def baseCall( self, methodName, methodArgs ):
		"""		
		功能说明：
		调用该实体的base部分的方法。
		注意：实体在服务端必须有base部分，在客户端只有客户端控制的玩家实体才可以访问该方法。
		
		
		例子：
		js插件: entity.baseCall("reqCreateAvatar", roleType, name);
		c#插件: entity.baseCall("reqCreateAvatar", new object[]{roleType, name});
		
		
		参数：
		
		
		@methodName
		string，方法名称。
		
		
		@methodArgs
		objects，方法参数列表。
		
		
		
		
		
		返回：
		
		
		由于是远程调用，不可能阻塞等待返回，因此无返回值。
		
		
		
		
		
		

		"""
		pass

	def cellCall( self, methodName, methodArgs ):
		"""		
		功能说明：
		调用该实体的cell部分的方法。
		注意：实体在服务端必须有cell部分，在客户端只有客户端控制的玩家实体才可以访问该方法。
		
		
		例子：
		js插件: entity.cellCall("xxx", roleType, name);
		c#插件: entity.cellCall("xxx", new object[]{roleType, name});
		
		
		参数：
		
		
		@methodName
		string，方法名称。
		
		
		@methodArgs
		objects，方法参数列表。
		
		
		
		
		
		返回：
		
		
		由于是远程调用，不可能阻塞等待返回，因此无返回值。
		
		
		
		
		
		
		
		
		

		"""
		pass

	def onDestroy( self ):
		"""		实体被销毁时调用。
		
		

		"""
		pass

	def onEnterWorld( self ):
		"""		如果实体非客户端控制实体，则表明实体进入了服务端上客户端控制的实体的View范围，此时客户端可以看见这个实体了。
		如果实体是客户端控制的实体则表明该实体已经在服务端创建了cell并进入了space。
		
		
		

		"""
		pass

	def onLeaveWorld( self ):
		"""		如果实体非客户端控制实体，则表明实体离开了服务端上客户端控制的实体的View范围，此时客户端看不见这个实体了。
		如果实体是客户端控制的实体则表明该实体已经在服务端销毁了cell并离开了space。
		
		
		

		"""
		pass

	def onEnterSpace( self ):
		"""		客户端控制的实体进入了一个新的space。
		
		
		

		"""
		pass

	def onLeaveSpace( self ):
		"""		客户端控制的实体离开了当前的space。
		
		
		
		

		"""
		pass

	@property
	def className( self ):

		"""		实体的类名。 

		"""
		pass

	@property
	def position( self ):

		"""		这个实体在世界空间中的坐标(x, y, z)，数据由服务端同步到客户端。
		
		
		

		"""
		pass

	@property
	def direction( self ):

		"""		这个属性描述的是Entity在世界空间中的朝向，数据由服务端同步到客户端。

		"""
		pass

	@property
	def isOnGround( self ):

		"""		如果这个属性的值为True，Entity在地面上，否则为False。
		如果是客户端控制的实体该属性将会在改变时同步到服务端，其他实体则由服务端同步到客户端，客户端可以判断这个值来强制贴地避免精度带来的影响。

		"""
		pass

def login( username, password  ):
	"""	
	功能说明：
	登录账号到KBEngine服务端。
	注意：如果插件与UI层使用事件交互模式，在UI层不要直接调用，请触发一个"login"事件给插件，事件附带数据username和password。
	
	
	
	参数：
	
	
	@username
	string，用户名。
	
	
	@password
	string，密码。
	
	
	
	
	

	"""
	pass

def createAccount( username, password  ):
	"""	
	功能说明：
	请求向KBEngine服务端创建一个登录账号。
	注意：如果插件与UI层使用事件交互模式，在UI层不要直接调用，请触发一个"createAccount"事件给插件，事件附带数据username和password。
	
	
	
	参数：
	
	
	@username
	string，用户名。
	
	
	@password
	string，密码。
	
	
	
	
	

	"""
	pass

def reloginBaseapp(   ):
	"""	
	功能说明：
	请求重登录到KBEngine服务端(通常在掉线之后希望更及时的连接到服务端并继续控制服务端角色时使用)。
	注意：如果插件与UI层使用事件交互模式，在UI层不要直接调用，请触发一个"reloginBaseapp"事件给插件，事件附带数据为空。
	
	
	
	

	"""
	pass

def player(  ):
	"""	
	功能说明：
	获得当前客户端所控制的实体。
	
	
	
	返回：
	
	
	Entity，返回控制的实体, 如果不存在(如：未能连接到服务端)则返回空。
	
	
	
	
	
	

	"""
	pass

def resetPassword( username ):
	"""	
	功能说明：
	请求loginapp重置账号的密码, 服务端将会向该账号绑定的邮箱发送一封重置密码邮件(通常是忘记密码功能使用)。
	
	
	
	参数：
	
	
	@username
	string，用户名。
	
	
	
	
	

	"""
	pass

def bindAccountEmail( emailaddress ):
	"""	
	功能说明：
	请求baseapp绑定账号的email地址。
	
	
	
	参数：
	
	
	@emailaddress
	string，邮箱地址。
	
	
	
	
	

	"""
	pass

def newPassword( oldpassword, newpassword ):
	"""	
	功能说明：
	请求设置账号的新密码。
	
	
	
	参数：
	
	
	@oldpassword
	string，旧密码。
	
	@newpassword
	string，新密码。
	
	
	
	
	

	"""
	pass

def findEntity( entityID  ):
	"""	
	功能说明：
	通过实体的ID查找实体的实例对象。
	
	
	参数：
	
	
	@entityID
	int32，实体ID。
	
	
	
	
	返回：
	
	
	Entity，存在返回实体实例，不存在返回空。
	
	
	
	
	
	

	"""
	pass

def getSpaceData( key  ):
	"""	
	功能说明：
	获取指定key的space数据。
	
	space数据由用户在服务端通过setSpaceData设置。
	
	
	参数：
	
	
	@key
	string，一个字符串关键字。
	
	
	
	
	返回：
	
	
	string，指定key的字符串数据。
	
	
	
	
	

	"""
	pass

@property
def component():

	"""	
	说明：
	这是正运行在当前脚本环境的组件。（至今为止）可能值有'cell', 'base', 'client', 'database', 'bot' 和 'editor'。

	"""
	pass

@property
def entities():

	"""	
	说明：
	entities是一个字典对象，包含当前进程上所有的实体。

	"""
	pass

@property
def entity_uuid():

	"""	
	说明：
	实体的uuid，改ID与实体本次登录绑定。当使用重登陆功能时服务端会与此ID进行比对，判断合法性。

	"""
	pass

@property
def entity_id():

	"""	
	说明：
	当前客户端所控制的实体的ID。

	"""
	pass

@property
def spaceID():

	"""	
	说明：
	当前客户端控制的实体所在的空间ID(也可以理解为所在对应的场景、房间、副本)。

	"""
	pass

