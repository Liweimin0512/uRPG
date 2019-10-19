class Entity:
	def moveToPoint( self, destination, velocity, distance, userData, faceMovement, moveVertically ):
		"""		
		功能说明：
		直线移动Entity到给定的坐标点，成功或失败会调用回调函数。
		任何实体，在任意时刻只能有一个移动控制器，重复调用任何移动函数将终止之前的移动控制器。
		返回一个可以用于取消这次移动的控制器ID。
		
		例如：
		Entity.cancelController( movementID )。
		移动取消还可以调用Entity.cancelController( "Movement" )。当移动被取消之后通知方法将
		不被调用。
		
		回调函数如下定义：
		
			def onMove( self, controllerID, userData ):
			def onMoveOver( self, controllerID, userData ):
			def onMoveFailure( self, controllerID, userData ):
		
		
		
		参看：
		
		Entity.cancelController
		
		
		
		参数：
		
		
		destination
		Vector3，Entity要移动到的目标位置点
		
		velocity
		float，Entity的移动速度，单位m/s
		
		distance
		float，距离目标小于该值停止移动，如果该值为0则移动到目标位置。
		
		
		userData
		object，传给通知函数的数据
		
		
		faceMovement
		bool，如果实体面向移动方向则为true。如果是其它机制则为false。
		
		
		moveVertically
		bool，设为true指移动为直线移动，设为false指贴着地面移动。
		
		
		
		
		
		
		返回：
		
		
		int，新创建的控制器ID。
		
		
		
		
		
		

		"""
		pass

	def cancelController( self, controllerID ):
		"""		
		功能说明：
		函数cancelController停止一个控制器对Entity的影响。它只能在一个real实体上被调用。
		
		
		参数：
		
		
		@controllerID
		controllerID是要取消的控制器的索引，它是一个整型。一个专用的控制器类型的字符串也可以作为它的类型。
		例如，一次只有一个移动/导航控制器可以被激活，这可以用entity.cancelController( "Movement" )取消。
		
		
		
		
		
		
		

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
	def base( self ):

		"""		base是用于联系Entity实体的entityCall。这个属性是只读的，且如果这个实体没有关联的Entity实体时属性是None。

		"""
		pass

	@property
	def cell( self ):

		"""		
		说明：
		cell是用于联系cell实体的ENTITYCALL。这个属性是只读的，且如果这个base实体没有关联的cell时属性是None。
		

		"""
		pass

	@property
	def cellData( self ):

		"""		
		说明：
		cellData是一个字典属性。每当base实体没有创建它的cell实体时，cell实体的属性会保存在这里。
		
		如果cell实体被创建，这些用到的值和cellData属性将被删除。除了cell实体在实体定义文件里指定的属性外，它还包含position, direction and
		spaceID。

		"""
		pass

	@property
	def className( self ):

		"""		
		说明：
		实体的类名。

		"""
		pass

	@property
	def clientapp( self ):

		"""		
		说明：
		当前实体所属的客户端（对象）。

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

class PyClientApp:
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
	def entities( self ):

		"""		
		说明：
		entities是一个字典对象，包含当前进程上所有的实体。

		"""
		pass

def addBots( reqCreateAndLoginTotalCount, reqCreateAndLoginTickCount=0, reqCreateAndLoginTickTime=0 ):
	"""	
	功能说明：
	向服务端添加机器人。
	
	例子:
	
	# 这里是使用addBots的一个例子
	        import KBEngine
	 
	        # 一次性向服务器添加5个机器人（瞬时完成）
	        KBEngine.addBots( 5 )
	 
	        # 一共向服务器添加1000个机器人，每次添加5个，每次添加所用时间(s)
	        KBEngine.addBots( 1000, 5, 10 )
	
	
	
	
	参数：
	
	
	@reqCreateAndLoginTotalCount
	integer，向服务器添加的机器人总数。
	
	
	@reqCreateAndLoginTickCount
	integer，每次向服务器添加的机器人数量。
	
	
	@reqCreateAndLoginTickTime
	integer，每次添加所用时间(秒)。
	
	
	
	
	
	
	

	"""
	pass

def callback( initialOffset, callbackObj ):
	"""	
	功能说明：
	注册一个回调，回调函数callbackObj触发，回调函数将在"initialOffset"秒后被执行。
	
	例子:
	
	# 这里是使用callback的一个例子
	        import KBEngine
	 
	        # 增加一个定时器，1秒后执行
	        KBEngine.callback( 1, onCallbackfun )
	 
	    def onCallbackfun( ):
	        print "onCallbackfun called“
		
	
	
	
	参数：
	
	
	@initialOffset
	float，指定回调从注册到回调的时间间隔（秒）。
	
	
	@callbackObj
	function，指定的回调函数对象。
	
	
	
	
	
	返回:
	
	integer，该函数返回callback的内部id，这个id可用于cancelCallback移除回调。
	
	
	
	
	
	

	"""
	pass

def cancelCallback( id ):
	"""	
	功能说明：
	函数cancelCallback用于移除一个注册但还未触发的回调，移除后的回调不再执行。
	如果cancelCallback函数使用一个无效的id（例如已经移除），将会产生错误。
	
	到KBEngine.callback参考回调的一个使用例子。
	
	
	参数：
	
	
	@id
	integer，它指定要移除的回调id。
	
	
	
	
	
	

	"""
	pass

def genUUID64(  ):
	"""	
	功能说明：
	该函数生成一个64位的唯一ID。
	注意：这个函数依赖于Cellapps服务进程启动参数gus，请正确设置启动参数保持唯一性。
	另外如果gus超过65535则该函数只能在当前进程上保持唯一性。
	
	
	用途：
	多个服务进程上产生唯一物品ID并且在合服时不会产生冲突。
	多个服务进程上产生一个房间ID，不需要进行唯一性校验。
	
	
	返回：
	
	
	返回一个64位的integer。
	
	
	
	
	

	"""
	pass

def getWatcher( path ):
	"""	
	功能说明：
	从KBEngine调试系统中获取一个监视变量的值。
	
	
	例子：在baseapp1的Python命令行输入:
	>>>KBEngine.getWatcher("/root/stats/runningTime")
	
	12673648533
	
	
	>>>KBEngine.getWatcher("/root/scripts/players")
	
	32133
	
	
	参数：
	
	
	@path
	string，该变量的绝对路径包括变量名(可以在GUIConsole的watcher页查看)。
	
	
	
	
	
	返回：
	
	
	该变量的值。
	
	
	
	
	
	

	"""
	pass

def getWatcherDir( path ):
	"""	
	功能说明：
	从KBEngine调试系统中获取一个监视目录下的元素列表(目录、变量名)。
	
	
	例子：在baseapp1的Python命令行输入:
	>>>KBEngine.getWatcher("/root")
	
	('stats', 'objectPools', 'network', 'syspaths', 'ThreadPool', 'cprofiles', 'scripts', 'numProxices', 'componentID', 'componentType', 'uid', 'numClients', 'globalOrder', 'username', 'load', 'gametime', 'entitiesSize', 'groupOrder')
	
	
	参数：
	
	
	@path
	string，该变量的绝对路径(可以在GUIConsole的watcher页查看)。
	
	
	
	
	
	返回：
	
	
	监视目录下的元素列表(目录、变量名)。
	
	
	
	
	
	

	"""
	pass

def scriptLogType( logType ):
	"""	
	功能说明：
	设置当前Python.print输出的信息类型(参考: KBEngine.LOG_TYPE_*)。
	
	
	
	

	"""
	pass

def onInit( isReload ):
	"""	
	功能说明：
	当引擎启动后初始化完所有的脚本后这个接口被调用。
	注意：该回调接口必须实现在入口模块(kbengine_defaults.xml->entryScriptFile)中。
	
	
	参数：
	
	
	@isReload
	bool，是否是被重写加载脚本后触发的。
	
	
	
	
	
	

	"""
	pass

def onFinish(  ):
	"""	
	功能说明：
	进程关闭会回调此函数。
	注意：该回调接口必须实现在入口模块(kbengine_defaults.xml->entryScriptFile)中。
	
	
	
	
	

	"""
	pass

@property
def bots():

	"""	
	说明：
	bots是一个字典对象，包含当前进程上所有的客户端对象。

	"""
	pass

@property
def component():

	"""	
	说明：
	这是正运行在当前脚本环境的组件。（至今为止）可能值有'cell', 'base', 'client', 'database', 'bot' 和 'editor'。

	"""
	pass

