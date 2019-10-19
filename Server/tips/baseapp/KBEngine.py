class Entity:
	def addTimer( self, initialOffset, repeatOffset=0, userArg=0 ):
		"""		
		功能说明：
		注册一个定时器，定时器由回调函数onTimer触发，回调函数将在"initialOffset"秒后被执行第1次，而后将每间隔"repeatOffset"秒执行1次，可设定一个用户参数"userArg"（仅限integer类型）。
		
		onTimer 函数必须在entity的base部分被定义，且带有2个参数，第1个integer类型的是timer的id（可用于移除timer的"delTimer"函数），第2个是用户参数"userArg"。
		
		例子:
		
		# 这里是使用addTimer的一个例子
		import KBEngine
		 
		class MyBaseEntity( KBEngine.Entity ):
		 
		    def __init__( self ):
		        KBEngine.Entity.__init__( self )
		 
		        # 增加一个定时器，5秒后执行第1次，而后每1秒执行1次，用户参数是9
		        self.addTimer( 5, 1, 9 )
		 
		        # 增加一个定时器，1秒后执行，用户参数缺省是0
		        self.addTimer( 1 )
		 
		    # Entity的定时器回调"onTimer"被调用
		    def onTimer( self, id, userArg ):
		        print "MyBaseEntity.onTimer called: id %i, userArg: %i" % ( id, userArg )
		        # if 这是不断重复的定时器，当不再需要该定时器的时候，调用下面函数移除:
		        #     self.delTimer( id )
		
		
		
		参数：
		
		
		@initialOffset
		float，指定定时器从注册到第一次回调的时间间隔（秒）。
		
		
		@repeatOffset
		float，指定第一次回调执行后每次执行的时间间隔（秒）。必须用函数delTimer移除定时器，否则它会一直重复下去。值小于等于0将被忽略。
		
		
		@userArg
		integer，指定底层回调"onTimer"时的userArg参数值。
		
		
		
		
		
		返回:
		
		integer，该函数返回timer的内部id，这个id可用于delTimer移除定时器。
		
		
		
		

		"""
		pass

	def createCellEntity( self, cellEntityMB ):
		"""		
		功能说明：
		请求在一个cell里面创建一个关联的实体。
		
		用于创建cell实体的信息被存储在该实体的属性cellData里。这个属性是一个字典，对应实体的.def文件里的默认值，同时还包括用于表示
		实体位置和方向(roll, pitch, yaw)的"position", "direction" 和 "spaceID"。
		
		
		参数：
		
		
		@cellEntityMB
		一个可选的CellEntityCall参数，
		指定哪个空间里创建这个cell实体的。
		
		只能使用一个直接的CellEntityCall。如果你有一个实体的BaseEntityCall，你不可以使用baseEntityCall.cell传给这个函数。
		你必须在这个实体的base上创建一个新的函数来回传这个直接的CellEntityCall。
		
		例如：
		baseEntityCallOfNearbyEntity.createCellNearSelf( self )
		在实体的base上：
		def createCellNearSelf( self, baseEntityCall ):
		    baseEntityCall.createCellNearHere( self.cell )
		在原实体的base上调用createCellNearSelf()方法：
		def createCellNearHere( self. cellEntityCall ):
		    self.createCellEntity( cellEntityCall )
		
		
		
		

		"""
		pass

	def createCellEntityInNewSpace( self, cellappIndex ):
		"""		
		功能说明：
		在cellapp上创建一个空间(space)并且将该实体的cell创建到这个新的空间中，它请求通过cellappmgr来完成。
		
		用于创建cell实体的信息被存储在该实体的属性cellData里。这个属性是一个字典，对应实体的.def文件里的默认值同时还包括用于表示
		实体位置和方向(roll, pitch, yaw)的"position", "direction" 和 "spaceID"。
		
		
		参数：
		
		
		@cellappIndex
		integer，为None或者0则由引擎负载均衡进行动态选择，如果大于0则在指定的cellapp中创建space。
		例子：假如预期会开启4个cellapp，那么cellappIndex需要指定时索引可以是1、2、3、4，
		如果实际运行的cellapp不足4个，例如只有3个，那么cellappIndex输入4时由于数量溢出4代表1，如果输入5则代表2。
		提示：此功能可以结合KBngine.setAppFlags(KBEngine.APP_FLAGS_NOT_PARTCIPATING_LOAD_BALANCING)来使用，例如：将大地图space放到几个固定的cellapp中，并将这些cellapp设置为不参与负载均衡，其他cellapp用于放置副本space。
		创建副本space时cellappIndex设置为0或者None，副本地图的消耗将不会影响到大地图进程，从而保证了主场景的流畅。
		
		
		
		
		

		"""
		pass

	def delTimer( self, id ):
		"""		
		功能说明：
		函数delTimer用于移除一个注册的定时器，移除后的定时器不再执行。只执行1次的定时器在执行回调后自动移除，不必要使用delTimer移除。
		如果delTimer函数使用一个无效的id（例如已经移除），将会产生错误。
		
		到Entity.addTimer参考定时器的一个使用例子。
		
		
		参数：
		
		
		@id
		integer，它指定要移除的定时器id。
		
		
		
		

		"""
		pass

	def destroy( self, deleteFromDB, writeToDB ):
		"""		
		功能说明：
		这个函数销毁该实体的base部分。如果实体存在cell部分，那么用户必须先销毁cell部分，否则将会产生错误。要销毁实体的cell部分，调用Entity.destroyCellEntity。
		
		也许在onLoseCell回调里调用self.destroy更为恰当。这能保证实体的base部分被销毁。
		
		
		参数：
		
		
		@deleteFromDB
		如果是True，在数据库里与这个实体有关联的条目将会被删除，该参数默认为False。
		
		
		@writeToDB
		如果是True，与这个实体相关联的存档属性将会写入数据库。只有在这个实体是从数据库读取的或者是使用过Entity.writeToDB写入数据库才会被执行。这个参数默认为True，但当deleteFromDB为True的时候它将被忽略。
		
		
		
		

		"""
		pass

	def destroyCellEntity( self ):
		"""		
		功能说明：
		destroyCellEntity请求销毁关联的cell实体。如果没有关联的cell实体该方法将会产生错误。
		

		"""
		pass

	def teleport( self, baseEntityMB ):
		"""		
		功能说明：
		teleport会瞬移这个实体的cell部分到参数指定的实体所在的空间。
		
		在抵达新的空间后，Entity.onTeleportSuccess被调用。这可以用来在新的空间里移动该实体到合适的位置。
		
		
		参数：
		
		
		@baseEntityMB
		实体应该移到的指定实体所在的空间，baseEntityMB即指定实体的EntityCall。当成功的时候，与此参数相关联的cell实体会被传入到Entity.onTeleportSuccess函数。
		
		
		
		

		"""
		pass

	def writeToDB( self, callback, shouldAutoLoad, dbInterfaceName ):
		"""		
		功能说明：
		该函数保存这个实体的存档属性到数据库，使得以后需要的时候可以重新从数据库加载。
		
		实体也可以被标记为自动加载，这样当服务启动后实体将会被重新创建。
		
		
		参数：
		
		
		@callback
		这个可选参数是当数据库操作完成后的回调函数。
		它有两个参数。第一个是boolean类型标志成功或失败，第二个是base实体。
		
		
		@shouldAutoLoad
		这个可选参数指定这个实体在服务启动的时候是否需要从数据库加载。
		注意：服务器启动时自动加载实体，底层默认将会调用createEntityAnywhereFromDBID将实体创建到一个负载最小的baseapp上，整个过程将会在第一个启动的baseapp调用onBaseAppReady之前完成。
		脚本层可以在个性化脚本(kbengine_defaults.xml->baseapp->entryScriptFile定义)中重新实现实体的创建方法，例如：
		def onAutoLoadEntityCreate(entityType, dbid): 
		          KBEngine.createEntityFromDBID(entityType, dbid)
		
		
		@dbInterfaceName
		string，可选参数，指定由某个数据库接口来完成, 默认使用"default"接口。数据库接口由kbengine_defaults.xml->dbmgr->databaseInterfaces中定义。
		
		
		
		
		

		"""
		pass

	def onCreateCellFailure( self ):
		"""		
		功能说明：
		如果这个函数在脚本中有实现，这个函数在cell实体创建失败的时候被调用。
		这个函数没有参数。
		

		"""
		pass

	def onDestroy( self ):
		"""		
		功能说明：
		如果这个函数在脚本中有实现，这个函数在调用Entity.destroy()后，在实际销毁之前被调用。
		这个函数没有参数。
		

		"""
		pass

	def onGetCell( self ):
		"""		
		功能说明：
		如果这个函数在脚本中有实现，这个函数在它获得cell实体的时候被调用。
		这个函数没有参数。
		

		"""
		pass

	def onLoseCell( self ):
		"""		
		功能说明：
		如果这个函数在脚本中有实现，这个函数在它关联的cell实体销毁之后被调用。
		这个函数没有参数。
		

		"""
		pass

	def onPreArchive( self ):
		"""		
		功能说明：
		如果这个函数在脚本中有实现，这个函数在该实体自动写入数据库之前被调用。这个回调在Entity.onWriteToDB回调之前被调用。
		如果该回调返回False，该归档操作中止。这个回调应该返回True使得操作继续。如果这个回调不存在，则归档操作继续进行。
		

		"""
		pass

	def onRestore( self ):
		"""		
		功能说明：
		如果这个函数在脚本中有实现，这个函数在Entity应用程序崩溃后在其它Entity应用程序上
		重新创建该实体时被调用。
		这个函数没有参数。
		

		"""
		pass

	def onTimer( self, timerHandle, userData ):
		"""		
		功能说明：
		这个函数当一个与此实体关联的定时器触发的时候被调用。
		一个定时器可以使用Entity.addTimer函数添加。
		
		
		参数：
		
		
		@timerHandle
		定时器的id。
		
		
		@userData
		传进Entity.addTimer的integer用户数据。
		
		
		
		

		"""
		pass

	def onWriteToDB( self, cellData ):
		"""		
		功能说明：
		如果这个函数在脚本中有实现，这个函数在实体数据将要写进数据库的时候被调用。
		
		需要注意的是在该回调里调用writeToDB会导致无限循环。
		
		
		参数：
		
		
		@cellData
		包含将要存进数据库的cell属性。
		cellData是一个字典。
		
		
		
		
		

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
	def client( self ):

		"""		
		说明：
		client是用于联系客户端的EntityCall。这个属性是只读的，且如果这个base实体没有关联的客户端时属性是None。

		"""
		pass

	@property
	def databaseID( self ):

		"""		
		说明：
		databaseID是实体的永久ID(数据库id)。这个id是uint64类型且大于0，如果是0则表示该实体不是永久的。

		"""
		pass

	@property
	def databaseInterfaceName( self ):

		"""		
		说明：
		databaseInterfaceName是实体持久化所在的数据库接口名称，该接口名称在kbengine_defaults->dbmgr中配置。实体必须持久化过（databaseID>0）该属性才可用，否则返回空字符串。

		"""
		pass

	@property
	def id( self ):

		"""		
		说明：
		id是实体的对象id。这个id是一个整型，在base，cell和client相关联的实体之间是相同的。
		这个属性是只读的。

		"""
		pass

	@property
	def isDestroyed( self ):

		"""		
		说明：
		如果该Entity实体已经被销毁了，这个属性为True。

		"""
		pass

	@property
	def shouldAutoArchive( self ):

		"""		
		说明：
		这个属性决定了自动存档的策略。如果设为True，自动存档将可用，如果设为False，自动存档将不可用。
		如果设为KBEngine.NEXT_ONLY，自动存档将在下一个预定的时间可用，
		在下一次存档后，这个属性将置为False。

		"""
		pass

	@property
	def shouldAutoBackup( self ):

		"""		
		说明：
		这个属性决定了自动备份的策略。如果设为True，自动备份将可用，如果设为False，自动备份将不可用。
		如果设为KBEngine.NEXT_ONLY，自动备份将在下一个预定的时间可用，
		在下一次备份后，这个属性将置为False。

		"""
		pass

class Proxy(Entity):
	def disconnect( self ):
		"""		
		断开客户端连接。
		
		
		

		"""
		pass

	def getClientType( self ):
		"""		
		功能说明：
		这个函数返回客户端类型。
		
		
		返回:
		
		
		UNKNOWN_CLIENT_COMPONENT_TYPE	= 0,
		CLIENT_TYPE_MOBILE				= 1,	// 手机类
		CLIENT_TYPE_WIN					= 2,	// pc， 一般都是exe客户端
		CLIENT_TYPE_LINUX				= 3		// Linux Application program
		CLIENT_TYPE_MAC					= 4		// Mac Application program
		CLIENT_TYPE_BROWSER				= 5,	// web应用， html5，flash
		CLIENT_TYPE_BOTS				= 6,	// bots
		CLIENT_TYPE_MINI				= 7,	// Mini-Client
		CLIENT_TYPE_END					= 8		// end
		
		
		
		
		

		"""
		pass

	def getClientDatas( self ):
		"""		
		功能说明：
		这个函数返回客户端登录时和注册时所附带的数据。
		此数据可用于运营系统扩展，如果连接了第三方账号服务，此数据会经过interfaces进程发往第三方服务系统。
		
		
		返回:
		
		
		tuple, 固定为2个元素的tuple(登陆数据bytes，注册数据bytes)，第一个元素为登陆时客户端调用登陆时传入的datas参数，
		第二个元素为注册时客户端调用注册所传入的datas参数。由于可以存储任意二进制数据，因此他们都是以bytes类型存在。
		
		
		
		
		

		"""
		pass

	def giveClientTo( self, proxy ):
		"""		
		功能说明：
		将客户端的控制器转交给另一个Proxy，当前的Proxy必须有一个客户端而目标Proxy则必须没有关联客户端，否则将会提示错误。
		
		
		参看：
		
		Proxy.onGiveClientToFailure
		
		
		
		参数：
		
		
		proxy
		控制权将转交给这个实体。
		
		
		
		
		

		"""
		pass

	def streamFileToClient( self, resourceName, desc="", id=-1 ):
		"""		
		功能说明：
		这个函数类似于streamStringToClient()，将一个资源文件发送给客户端。发送过程在不同的线程上操作，因此不会危及主线程。
		
		
		参看：
		
		Proxy.onStreamComplete
		
		
		
		参数：
		
		
		resourceName
		要发送的资源名称，包含路径。
		
		
		desc
		一个可选的字符串，发送给客户端的资源描述。
		
		
		id
		一个16位的id，它的值完全取决于调用者。如果传入-1系统将会在队列里面选择一个没有在用的id。可以在客户端根据这个id做资源判断。
		
		
		
		
		
		
		返回：
		
		
		与这个下载关联的id。
		
		
		
		

		"""
		pass

	def streamStringToClient( self, data, desc="", id=-1 ):
		"""		
		功能说明：
		发送一些数据到当前实体绑定的客户端。如果客户端端口则数据被清除，
		当客户端再次绑定到实体的时候才可调用这个函数。16位的id完全取决于调用者。
		
		如果调用者没有指定这个ID则系统会分配一个未用过的id。可以在客户端根据这个id做资源判断。
		
		你可以在Proxy的派生类中定义回调函数（onStreamComplete），所有数据成功发送给客户端时或下载失败时会调用这个回调函数。
		
		参看：Proxy.onStreamComplete与客户端实体Entity.onStreamDataStarted和
		Entity.onStreamDataRecv还有Entity.onStreamDataCompleted。
		
		
		参数：
		
		
		@data
		要发送的字符串。
		
		
		@desc
		一个可选的字符串，发送给客户端的描述。
		
		
		@id
		一个16位的id，它的值完全取决于调用者。如果传入-1系统将会在队列里面选择一个没有在用的id。
		
		
		
		
		
		返回：
		
		
		与这个下载关联的id。
		
		
		
		
		

		"""
		pass

	def onClientDeath( self ):
		"""		如果在脚本中实现了此回调，这个方法将在客户端断开连接时被调用。 这个方法没有参数。
		

		"""
		pass

	def onClientGetCell( self ):
		"""		如果在脚本中实现了此回调，当客户端能够调用实体的cell属性时，该回调被调用。
		

		"""
		pass

	def onClientEnabled( self ):
		"""		如果在脚本中实现了此回调，当实体可用时（ 各种初始化完毕并且可以与客户端通讯 ）该回调被调用。 这个方法没有参数。
		注意：giveClientTo将控制权赋给了该实体时也会导致该回调被调用。
		

		"""
		pass

	def onGiveClientToFailure( self ):
		"""		
		如果在脚本中实现了此回调，当实体调用giveClientTo失败时，该回调被调用。这个方法没有参数。
		
		

		"""
		pass

	def onLogOnAttempt( self, ip, port, password ):
		"""		如果在脚本中实现了此回调，这个函数在客户端尝试使用当前账号实体进行登录时触发回调。
		这种情况通常是实体存在于内存中处于有效状态，最明显的例子是用户A使用此账号登录了，用户B使用同一账号进行登录，此时回调触发。
		
		这个回调函数可以返回如下常量值： 
		KBEngine.LOG_ON_ACCEPT：允许新的客户端与实体进行绑定，如果实体已经绑定了一个客户端，之前的客户端将被踢出。
		KBEngine.LOG_ON_REJECT：拒绝新的客户端与实体绑定。 
		KBEngine.LOG_ON_WAIT_FOR_DESTROY：等待实体销毁后再进行客户端绑定。
		
		
		
		参数：
		
		
		@ip 尝试登录的客户端IP地址。
		
		
		@port 尝试登录的客户端连接的端口。
		
		
		@password 用户登录时使用的MD5密码。
		
		
		
		

		"""
		pass

	def onStreamComplete( self, id, success ):
		"""		如果在脚本中实现了此回调，当用户使用Proxy.streamStringToClient()或Proxy.streamFileToClient()完成时，该回调被调用。
		
		
		
		
		参数：
		
		
		@id 与下载关联的id。
		
		
		@success 成功与否。
		
		
		
		
		

		"""
		pass

	@property
	def __ACCOUNT_NAME__( self ):

		"""		
		说明：
		如果proxy是帐号则可以访问__ACCOUNT_NAME__得到帐号名。

		"""
		pass

	@property
	def __ACCOUNT_PASSWORD__( self ):

		"""		
		说明：
		如果proxy是帐号则可以访问__ACCOUNT_PASSWORD__得到帐号MD5密码。

		"""
		pass

	@property
	def clientAddr( self ):

		"""		这是一个tuple对象，包含了客户端的ip与端口。

		"""
		pass

	@property
	def clientEnabled( self ):

		"""		实体是否已经可用。在实体可用之前脚本不能与客户端进行通讯。

		"""
		pass

	@property
	def hasClient( self ):

		"""		Proxy是否绑定了一个客户端连接。

		"""
		pass

	@property
	def roundTripTime( self ):

		"""		在一段时间内服务器与这个Proxy绑定的客户端通讯平均往返时间。这个属性只在Linux下生效。

		"""
		pass

	@property
	def timeSinceHeardFromClient( self ):

		"""		最后一次收到客户端数据包时到目前为止所过去的时间（秒）。

		"""
		pass

def addWatcher( path, dataType, getFunction ):
	"""	
	功能说明：
	与调试监视系统交互，允许用户向监视系统注册一个监视变量。
	
	例：
	
	
	
	>>> def countPlayers( ):
	>>>     i = 0
	>>>     for e in KBEngine.entities.values():
	>>>     	if e.__class__.__name__ == "Avatar":
	>>>     		i += 1
	>>>     return i
	>>>
	>>> KBEngine.addWatcher( "players", "UINT32", countPlayers )
	
	
	这个函数添加一个监视变量在"scripts/players"监视路径之下。函数countPlayers在观察者观察时被调用。
	
	
	参数：
	
	
	@path
	创建监视的路径。
	
	
	@dataType
	监视变量的值类型。参考: 基本类型
	
	
	@getFunction
	这个函数当观察者检索该变量时调用。
	这个函数不带参数返回一个代表监视变量的值。
	
	
	
	
	
	

	"""
	pass

def address(  ):
	"""	
	功能说明：
	返回内部网络接口的地址。
	
	
	
	

	"""
	pass

def MemoryStream(  ):
	"""	
	功能说明：
	返回一个新的MemoryStream对象。
	
	MemoryStream对象存储的是二进制信息，提供这个类型是为了让用户能够方便的序列化与反序列化Python基本类型同时能与KBEngine底层序列化规则相同。
	
	例如：你可以使用这个对象构造一个KBEngine能解析的网络数据包。
	
	用法：
	
	>>> s = KBEngine.MemoryStream()
	>>> s
	>>> b''
	>>> s.append("UINT32", 1)
	>>> s.pop("UINT32")
	>>> 1
	
	
	目前MemoryStream能够支持的类型仅为基本数据类型。参考: 基本类型
	
	
	

	"""
	pass

def charge( ordersID, dbID, byteDatas, pycallback ):
	"""	
	功能说明：
	计费接口。
	
	
	参数：
	
	
	@ordersID
	string，订单ID。
	
	
	@dbID
	uint64，实体的databaseID。
	
	
	@byteDatas
	bytes，附带数据，由开发者自己解析和定义。
	
	
	@pycallback
	计费回调。
	计费回调原型: (当在interfaces中调用KBEngine.chargeResponse后，如果某个订单设置过回调则该回调被调用)
	def on**ChargeCB(self, orderID, dbID, success, datas):
	ordersID：string，订单ID
	dbID：uint64，通常为entity的databaseID
	success：bool，是否成功
	datas：bytes，附带数据，由开发者自己解析和定义
	
	
	
	

	"""
	pass

def createEntity(  ):
	"""	
	功能说明：
	KBEngine.createEntityLocally的别名.
	

	"""
	pass

def createEntityAnywhere( entityType, params, callback ):
	"""	
	功能说明：
	创建一个新的Entity实体，
	服务端可能选择任何的Baseapp来创建Entity实体。
	
	这个方法应作为KBEngine.createEntityLocally的首选，
	这样服务端会灵活地选择一个合适的Baseapp来创建实体。
	
	函数参数需要提供创建的实体的类型，还有一个Python字典作为参数来初始化实体的值。
	
	这个Python字典不需要用户提供所有的属性，没有提供的属性默认为实体定义文件".def"提供的默认值。
	
	例子：
	
	params = {
		"name" : "kbe", # base, BASE_AND_CLIENT
		"HP" : 100,	# cell, ALL_CLIENT, in cellData
		"tmp" : "tmp"	# baseEntity.tmp
	}
	
	def onCreateEntityCallback(entity)
		print(entity)
	
	createEntityAnywhere("Avatar", params, onCreateEntityCallback)
	
	
	
	
	参数：
	
	
	@entityType
	string，指定要创建的Entity实体的类型。有效的实体类型在/scripts/entities.xml列出。
	
	
	@params
	可选参数, 一个Python字典对象。
	如果一个指定的键是一个Entity属性，他的值会用来初始化这个Entity实体的属性。
	如果这个键是一个Cell属性，它会被添加到Entity实体的'cellData'属性，这个'cellData'属性是一个Python字典，
	然后在后面会用来初始化cell实体的属性。
	
	
	@callback
	callback是一个可选的回调函数，当实体完成创建时被调用。回调函数带有一个参数，当成功的时候是Entity实体的entityCall，失败时是None。
	
	
	
	
	
	返回：
	
	
	通过回调返回Entity实体的entityCall。
	
	
	
	
	
	

	"""
	pass

def createEntityRemotely( entityType, baseMB, params, callback ):
	"""	
	功能说明：
	通过baseMB参数在一个指定的baseapp上创建一个新的Entity实体。
	
	应该将KBEngine.createEntityAnywhere方法作为首选。
	
	函数参数需要提供创建的实体的类型，还有一个Python字典作为参数来初始化实体的值。
	
	这个Python字典不需要用户提供所有的属性，没有提供的属性默认为实体定义文件".def"提供的默认值。
	
	例子：
	
	params = {
		"name" : "kbe", # base, BASE_AND_CLIENT
		"HP" : 100,	# cell, ALL_CLIENT, in cellData
		"tmp" : "tmp"	# baseEntity.tmp
	}
	
	def onCreateEntityCallback(entity)
		print(entity)
	
	createEntityRemotely("Avatar", baseEntityCall, params, onCreateEntityCallback)
	
	
	
	
	参数：
	
	
	@entityType
	string，指定要创建的Entity实体的类型。有效的实体类型在/scripts/entities.xml列出。
	
	
	@baseMB
	BaseEntityCall，这是一个Entity的EntityCall。实体将被创建在该Entity对应的Baseapp进程上。
	
	
	@params
	可选参数, 一个Python字典对象。
	如果一个指定的键是一个Entity属性，他的值会用来初始化这个Entity实体的属性。
	如果这个键是一个Cell属性，它会被添加到Entity实体的'cellData'属性，这个'cellData'属性是一个Python字典，
	然后在后面会用来初始化cell实体的属性。
	
	
	@callback
	callback是一个可选的回调函数，当实体完成创建时被调用。回调函数带有一个参数，当成功的时候是Entity实体的entityCall，失败时是None。
	
	
	
	
	
	返回：
	
	
	通过回调返回Entity实体的entityCall。
	
	
	
	
	
	

	"""
	pass

def createEntityFromDBID( entityType, dbID, callback, dbInterfaceName ):
	"""	
	功能说明：
	从数据库里加载数据创建一个Entity实体。
	这个新的Entity实体会在调用这个函数的Baseapp上创建。
	如果该实体已经从数据库检出，那么将返回这个存在的Entity实体的引用。
	
	
	参数：
	
	
	@entityType
	string，指定要加载的Entity实体类型。实体类型在/scripts/entities.xml列出。
	
	
	@dbID
	指定要创建的实体的数据库ID。这个实体的数据库ID存储在该实体的databaseID属性。
	
	
	@callback
	这是一个可选的回调函数，当操作完成的时候它会被调用。回调函数带有3个参数：baseRef，databaseID和wasActive。
	如果操作成功，baseRef会是一个entityCall或者是新创建的Entity实体的直接引用，databaseID会是实体的数据库ID，无论该实体是否已经激活
	wasActive都会有所指示，如果wasActive是True则baseRef是已经存在的实体的引用(已经从数据库检出)。如果操作失败这三个参数的值，baseRef将会是None，databaseID将会是0，wasActive将会是False。
	失败最常见的原因是实体在数据库里不存在，但偶尔也会出现其它错误比如说超时或者是分配ID失败。
	
	
	@dbInterfaceName
	string，可选参数，指定由某个数据库接口来完成, 默认使用"default"接口。数据库接口由kbengine_defaults.xml->dbmgr->databaseInterfaces中定义。
	
	
	
	
	

	"""
	pass

def createEntityAnywhereFromDBID( entityType, dbID, callback, dbInterfaceName ):
	"""	
	功能说明：
	从数据库里加载数据创建一个Entity实体。
	服务端可能选择任何的Baseapp来创建Entity实体。
	
	使用这个函数将有助于BaseApps负载平衡。
	
	如果该实体已经从数据库检出，那么将返回这个存在的Entity实体的引用。
	
	
	参数：
	
	
	@entityType
	string，指定要创建的Entity实体的类型。有效的实体类型在/scripts/entities.xml列出。
	
	
	@dbID
	这是一个指定要创建的实体的数据库ID。这个实体的数据库ID存储在该实体的databaseID属性。
	
	
	@callback
	这是一个可选的回调函数，当操作完成的时候它会被调用。回调函数带有3个参数：baseRef，databaseID和wasActive。
	如果操作成功，baseRef会是一个entityCall或者是新创建的Entity实体的直接引用，databaseID会是实体的数据库ID，无论该实体是否已经激活
	wasActive都会有所指示，如果wasActive是True则baseRef是已经存在的实体的引用(已经从数据库检出)。如果操作失败这三个参数的值，baseRef将会是None，databaseID将会是0，wasActive将会是False。
	失败最常见的原因是实体在数据库里不存在，但偶尔也会出现其它错误比如说超时或者是分配ID失败。
	
	
	@dbInterfaceName
	string，可选参数，指定由某个数据库接口来完成, 默认使用"default"接口。数据库接口由kbengine_defaults.xml->dbmgr->databaseInterfaces中定义。
	
	
	
	
	
	返回：
	
	
	通过回调返回Entity实体的entityCall。
	
	
	
	
	

	"""
	pass

def createEntityRemotelyFromDBID( entityType, dbID, baseMB, callback, dbInterfaceName ):
	"""	
	功能说明：
	从数据库里加载数据并通过baseMB参数在一个指定的baseapp上创建一个Entity实体。
	
	如果该实体已经从数据库检出，那么将返回这个存在的Entity实体的引用。
	
	
	参数：
	
	
	@entityType
	string，指定要创建的Entity实体的类型。有效的实体类型在/scripts/entities.xml列出。
	
	
	@dbID
	这是一个指定要创建的实体的数据库ID。这个实体的数据库ID存储在该实体的databaseID属性。
	
	
	@baseMB
	BaseEntityCall，这是一个Entity的EntityCall。实体将被创建在该Entity对应的Baseapp进程上。
	
	
	@callback
	这是一个可选的回调函数，当操作完成的时候它会被调用。回调函数带有3个参数：baseRef，databaseID和wasActive。
	如果操作成功，baseRef会是一个entityCall或者是新创建的Entity实体的直接引用，databaseID会是实体的数据库ID，无论该实体是否已经激活
	wasActive都会有所指示，如果wasActive是True则baseRef是已经存在的实体的引用(已经从数据库检出)。如果操作失败这三个参数的值，baseRef将会是None，databaseID将会是0，wasActive将会是False。
	失败最常见的原因是实体在数据库里不存在，但偶尔也会出现其它错误比如说超时或者是分配ID失败。
	
	
	@dbInterfaceName
	string，可选参数，指定由某个数据库接口来完成, 默认使用"default"接口。数据库接口由kbengine_defaults.xml->dbmgr->databaseInterfaces中定义。
	
	
	
	
	
	返回：
	
	
	通过回调返回Entity实体的entityCall。
	
	
	
	
	
	

	"""
	pass

def createEntityLocally( entityType, params ):
	"""	
	功能说明：
	创建一个新的Entity实体。
	函数参数需要提供创建的实体的类型，还有一个Python字典作为参数来初始化实体的值。
	
	这个Python字典不需要用户提供所有的属性，没有提供的属性默认为实体定义文件".def"提供的默认值。
	
	KBEngine.createEntityAnywhere应该作为这个方法的首选，因为服务端可以灵活地
	在合适的Baseapp上创建实体。
	
	例子：
	
	params = {
		"name" : "kbe", # base, BASE_AND_CLIENT
		"HP" : 100,	# cell, ALL_CLIENT, in cellData
		"tmp" : "tmp"	# baseEntity.tmp
	}
	
	baseEntity = createEntityLocally("Avatar", params)
	
	
	
	参数：
	
	
	@entityType
	string，指定要创建的Entity实体的类型。有效的实体类型在/scripts/entities.xml列出。
	
	
	@params
	可选参数, 一个Python字典对象。
	如果一个指定的键是一个Entity属性，他的值会用来初始化这个Entity实体的属性。
	如果这个键是一个Cell属性，它会被添加到Entity实体的'cellData'属性，这个'cellData'属性是一个Python字典，
	然后在后面会用来初始化cell实体的属性。
	
	
	
	
	
	返回：
	
	新创建的Entity实体（参考Entity）
	
	
	
	
	
	
	

	"""
	pass

def debugTracing(  ):
	"""	
	功能说明：
	输出当前KBEngine追踪的Python扩展对象计数器。
	扩展对象包括：固定字典、固定数组、Entity、EntityCall...
	在服务端正常关闭时如果计数器不为零，此时说明泄露已存在，日志将会输出错误信息。
	ERROR cellapp [0x0000cd64] [2014-11-12 00:38:07,300] - PyGC::debugTracing(): FixedArray : leaked(128)
	ERROR cellapp [0x0000cd64] [2014-11-12 00:38:07,300] - PyGC::debugTracing(): EntityCall : leaked(8)
	
	
	参数：
	
	
	@path
	要删除的变量的路径。
	
	
	
	
	
	

	"""
	pass

def delWatcher( path ):
	"""	
	功能说明：
	与调试监视系统交互，允许用户在脚本删除监视的变量。
	
	
	参数：
	
	
	@path
	要删除的变量的路径。
	
	
	
	
	

	"""
	pass

def deleteEntityByDBID( entityType, dbID, callback, dbInterfaceName ):
	"""	
	功能说明：
	从数据库删除指定的实体（包括属性所产生的子表数据），如果实体没有从数据库检出则删除成功，
	如果实体已经从数据库检出那么KBEngine服务系统将会删除失败，并且从回调中返回
	Entity实体的entityCall。
	
	
	参数：
	
	
	@entityType
	string，指定要删除的Entity实体的类型。有效的实体类型在/scripts/entities.xml列出。
	
	
	@dbID
	指定要删除的实体的数据库ID。这个实体的数据库ID存储在该实体的databaseID属性。
	
	
	@callback
	callback是一个可选的回调函数，只有一个参数，当实体没有从数据库检出时将会成功删除数据，参数是True。如果实体已经从数据库检出那么参数是Entity实体的entityCall。
	
	
	@dbInterfaceName
	string，可选参数，指定由某个数据库接口来完成, 默认使用"default"接口。数据库接口由kbengine_defaults.xml->dbmgr->databaseInterfaces中定义。
	
	
	
	
	
	

	"""
	pass

def deregisterReadFileDescriptor( fileDescriptor ):
	"""	
	功能说明：
	注销已经通过KBEngine.registerReadFileDescriptor注册的回调。
	
	
	例子:
	http://www.kbengine.org/assets/other/py/Poller.py
	
	
	参数：
	
	
	@fileDescriptor
	socket描述符/文件描述符。
	
	
	
	

	"""
	pass

def deregisterWriteFileDescriptor( fileDescriptor ):
	"""	
	功能说明：
	注销已经通过KBEngine.registerWriteFileDescriptor注册的回调。
	
	
	例子:
	http://www.kbengine.org/assets/other/py/Poller.py
	
	
	参数：
	
	
	@fileDescriptor
	socket描述符/文件描述符。
	
	
	
	
	
	

	"""
	pass

def executeRawDatabaseCommand( command, callback, threadID, dbInterfaceName ):
	"""	
	功能说明：
	这个脚本函数在数据库上执行原始数据库命令，该命令将直接由相关数据库进行解析。
	
	请注意使用该函数修改实体数据可能不生效，因为如果实体已经检出，被修改过的实体数据将仍会被实体存档而导致覆盖。
	强烈不推荐这个函数用于读取或修改实体数据。
	
	
	参数：
	
	
	@command
	这个数据库命令将会因为不同数据库配置方案而不同。对于方案为MySQL数据库它是一个SQL查询语句。
	
	
	@callback
	
	  可选参数，带有命令执行结果的回调对象（比如说是一个函数）。这个回调带有4个参数：结果集合，影响的行数，自増长值，错误信息。
	  
	  声明样例：
	  def 
	  sqlcallback(result, rows, insertid, error):
	    print(result, rows, insertid, error)  
	    
	    如同上面的例子所示，result参数对应的就是&ldquo;结果集合&rdquo;，这个结果集合参数是一个行列表。
	    每一行是一个包含字段值的字符串列表。
	    命令执行没有返回结果集合（比如说是DELETE命令），
	    或者
	    命令执行有错误时这个结果集合为None。
	    
	    rows参数则是&ldquo;影响的行数&rdquo;，它是一个整数，表示命令执行受影响的行数。这个参数只和不返回结果结合的命令（如DELETE）相关。
	    如果有结果集合返回或者命令执行有错误时这个参数为None。
	    
	  insertid对应的是&ldquo;自増长值&rdquo;，类似于实体的databaseID，当成功的向一张带有自増长类型字段的表中插入数据时，它返回该数据在插入时自増长字段所被赋于的值。
	    更多的信息可以参阅mysql的mysql_insert_id()方法。另外，此参数仅在数据库类型为mysql时有意义。
	    
	    error则对应了&ldquo;错误信息&rdquo;，当命令执行有错误时，这个参数是一个描述错误的字符串。命令执行没有发生错误时这个参数为None。
	  
	
	@threadID
	int32，可选参数，指定一个线程来处理本条命令。用户可以通过这个参数控制某一类命令的执行先后顺序（dbmgr是多线程处理的），默认是不指定，如果threadID是实体的ID，
	那么将加入到该实体的存档队列中由线程逐条写入。
	
	
	@dbInterfaceName
	string，可选参数，指定由某个数据库接口来完成, 默认使用"default"接口。数据库接口由kbengine_defaults.xml->dbmgr->databaseInterfaces中定义。
	
	
	
	
	
	

	"""
	pass

def genUUID64(  ):
	"""	
	功能说明：
	该函数生成一个64位的唯一ID。
	注意：这个函数依赖于Baseapps服务进程启动参数gus，请正确设置启动参数保持唯一性。
	另外如果gus超过65535则该函数只能在当前进程上保持唯一性。
	
	
	用途：
	多个服务进程上产生唯一物品ID并且在合服时不会产生冲突。
	多个服务进程上产生一个房间ID，不需要进行唯一性校验。
	
	
	返回：
	
	
	返回一个64位的integer。
	
	
	
	

	"""
	pass

def getResFullPath( res ):
	"""	
	功能说明：
	获取资源的绝对路径。
	注意：资源必须在KBE_RES_PATH之下才可以访问到。 
	
	
	参数：
	
	
	@res
	string，资源的相对路径。
	
	
	
	
	
	返回：
	
	
	string，如果存在返回资源的绝对路径，否则返回空。
	
	
	
	
	

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

def getAppFlags(  ):
	"""	
	功能说明：
	获取当前引擎APP的标记, 参考:KBEngine.setAppFlags。
	
	
	
	返回：
	
	
	KBEngine.APP_FLAGS_*。
	
	
	
	
	

	"""
	pass

def hasRes( res ):
	"""	
	功能说明：
	使用这个接口可以判断一个相对路径的资源是否存在。
	注意：资源必须在KBE_RES_PATH之下才可以访问到。
	
	
	例子:
	
	
	>>>KBEngine.hasRes("scripts/entities.xml")
	
	True
	
	
	参数：
	
	
	@res
	string，资源的相对路径。
	
	
	
	
	返回：
	
	
	BOOL, 存在返回True，否则返回False。
	
	
	
	
	
	
	
	

	"""
	pass

def isShuttingDown(  ):
	"""	
	功能说明：
	返回服务端是否正在关闭中。
	在onBaseAppShutDown(state=0)回调函数被调用后，这个函数返回True。
	
	
	返回：
	
	
	系统正在关闭返回True，否则返回False。
	
	
	
	

	"""
	pass

def listPathRes( path, extension ):
	"""	
	功能说明：
	获得一个资源目录下的资源列表。
	注意：资源必须在KBE_RES_PATH之下才可以访问到。
	
	
	例子:
	
	
	>>>KBEngine.listPathRes("scripts/cell/interfaces")
	
	('/home/kbe/kbengine/demo/res/scripts/cell/interfaces/AI.py', '/home/kbe/kbengine/demo/res/scripts/cell/interfaces/新建文本文档.txt')
	
	>>>KBEngine.listPathRes("scripts/cell/interfaces", "txt")
	
	('/home/kbe/kbengine/demo/res/scripts/cell/interfaces/新建文本文档.txt')
	
	>>>KBEngine.listPathRes("scripts/cell/interfaces", "txt|py")
	
	('/home/kbe/kbengine/demo/res/scripts/cell/interfaces/AI.py', '/home/kbe/kbengine/demo/res/scripts/cell/interfaces/新建文本文档.txt')
	
	>>>KBEngine.listPathRes("scripts/cell/interfaces", ("txt", "py"))
	
	('/home/kbe/kbengine/demo/res/scripts/cell/interfaces/AI.py', '/home/kbe/kbengine/demo/res/scripts/cell/interfaces/新建文本文档.txt')
	
	
	参数：
	
	
	@res
	string，资源的相对路径。
	
	
	@extension
	string，可选参数，扩展名。
	
	
	
	
	返回：
	
	
	Tuple, 资源列表。
	
	
	
	
	
	

	"""
	pass

def lookUpEntityByDBID( entityType, dbID, callback, dbInterfaceName ):
	"""	
	功能说明：
	查询一个实体是否从数据库检出，
	如果实体已经从数据库检出那么KBEngine服务系统将从回调中返回Entity实体的entityCall。
	
	
	参数：
	
	
	@entityType
	string，指定要查询的Entity实体的类型。有效的实体类型在/scripts/entities.xml列出。
	
	
	@dbID
	指定要查询的Entity实体的数据库ID。这个实体的数据库ID存储在该实体的databaseID属性。
	
	
	@callback
	callback只有一个参数，当实体没有从数据库检出时将会返回True。如果实体已经从数据库检出那么将返回Entity实体的entityCall, 其他任何情况返回False。
	
	
	@dbInterfaceName
	string，可选参数，指定由某个数据库接口来完成, 默认使用"default"接口。数据库接口由kbengine_defaults.xml->dbmgr->databaseInterfaces中定义。
	
	
	
	
	
	

	"""
	pass

def matchPath( res ):
	"""	
	功能说明：
	使用相对路径的资源获得资源的绝对路径。
	注意：资源必须在KBE_RES_PATH之下才可以访问到。
	
	
	例子:
	
	
	>>>KBEngine.matchPath("scripts/entities.xml")
	'/home/kbe/kbengine/demo/res/scripts/entities.xml'
	
	
	参数：
	
	
	@res
	string，资源的相对路径(包括资源名称)。
	
	
	
	
	返回：
	
	
	string, 资源的绝对路径。
	
	
	
	
	
	
	

	"""
	pass

def open( res, mode ):
	"""	
	功能说明：
	使用这个接口可以使用相对路径来打开相关资源。
	注意：资源必须在KBE_RES_PATH之下才可以访问到。
	
	
	参数：
	
	
	@res
	string，资源的相对路径。
	
	
	@mode
	string，文件操作模式：
	w     以写方式打开，
	a     以追加模式打开 (从 EOF 开始, 必要时创建新文件)
	r+     以读写模式打开
	w+     以读写模式打开 (参见 w )
	a+     以读写模式打开 (参见 a )
	rb     以二进制读模式打开
	wb     以二进制写模式打开 (参见 w )
	ab     以二进制追加模式打开 (参见 a )
	rb+    以二进制读写模式打开 (参见 r+ )
	wb+    以二进制读写模式打开 (参见 w+ )
	ab+    以二进制读写模式打开 (参见 a+ )
	
	
	
	

	"""
	pass

def publish(  ):
	"""	
	功能说明：
	这个接口返回当前服务端发行模式。
	
	
	返回：
	
	
	int8，0：debug，1：release，其它可自定义。
	
	
	

	"""
	pass

def quantumPassedPercent(  ):
	"""	
	功能说明：
	返回取得当前tick占用一个时钟周期的百分比。
	
	
	返回：
	
	
	返回取得当前tick占用一个时钟周期的百分比。
	
	
	
	
	

	"""
	pass

def registerReadFileDescriptor( fileDescriptor, callback ):
	"""	
	功能说明：
	注册一个回调函数，这个回调函数当文件描述符可读时被调用。
	
	
	例子:
	http://www.kbengine.org/assets/other/py/Poller.py
	
	
	参数：
	
	
	@fileDescriptor
	socket描述符/文件描述符。
	
	
	@callback
	一个回调函数，socket描述符/文件描述符作为它的唯一参数。
	
	
	
	

	"""
	pass


	"""	
	功能说明：
	注册一个回调函数，这个回调函数当socket描述符/文件描述符可写时被调用。
	
	
	例子:
	http://www.kbengine.org/assets/other/py/Poller.py
	
	
	参数：
	
	
	@fileDescriptor
	socket描述符/文件描述符。
	
	
	@callback
	一个回调函数，socket描述符/文件描述符作为它的唯一参数。
	
	
	
	
	
	

	"""
	pass

def reloadScript( fullReload ):
	"""	
	功能说明：
	重新加载与实体和自定义数据类型相关的Python模块。当前实体类会设置为新加载的类。
	这个方法应该只用于开发模式，对于产品模式不合适。下面几点应该注意：
	
	1）重载脚本仅仅能在Baseapp上执行， 用户应该确保所有的服务端组件加载完成。
	
	2）自定义类型在脚本重载后应该确保内存中已经实例化的对象也被更新，下面是一个例子:
	
	
	for e in KBEngine.entities.values():
	   if type( e ) is Avatar.Avatar:
	      e.customData.__class__ = CustomClass
	
	当这个方法完成时 KBEngine.onInit( True ) 被调用。
	
	
	参数：
	
	
	@fullReload
	可选的boolean参数，指定是否同时重新加载实体定义。如果这个参数为False，则实体定义不会被重新加载。默认为True。
	
	
	
	
	
	返回：
	
	重新加载成功返回True，否则返回False。
	
	
	
	
	
	
	

	"""
	pass

def scriptLogType( logType ):
	"""	
	功能说明：
	设置当前Python.print输出的信息类型(参考: KBEngine.LOG_TYPE_*)。
	
	
	

	"""
	pass

def setAppFlags( flags ):
	"""	
	功能说明：
	设置当前引擎APP的标记。
	
	
	KBEngine.APP_FLAGS_NONE // 默认的(未设置标记)
	KBEngine.APP_FLAGS_NOT_PARTCIPATING_LOAD_BALANCING //不参与负载均衡
	
	例如：
	KBEngine.setAppFlags(KBEngine.APP_FLAGS_NOT_PARTCIPATING_LOAD_BALANCING | KBEngine.APP_FLAGS_*)
	
	

	"""
	pass

def time(  ):
	"""	
	功能说明：
	这个方法返回当前游戏的时间（周期数）。
	
	
	返回：
	
	
	uint32，当前游戏的时间，这里指周期数，周期受频率影响，频率由配置文件kbengine.xml或者kbengine_defaults.xml->gameUpdateHertz决定。
	
	
	
	

	"""
	pass

def onBaseAppReady( isBootstrap ):
	"""	
	功能说明：
	当前Baseapp进程已经准备好的时候回调此函数。
	注意：该回调接口必须实现在入口模块(kbengine_defaults.xml->entryScriptFile)中。
	
	
	参数：
	
	
	@isBootstrap
	bool，是否为第一个启动的Baseapp。
	
	
	
	

	"""
	pass

def onBaseAppShutDown( state ):
	"""	
	功能说明：
	Baseapp关闭过程会回调此函数。
	注意：该回调接口必须实现在入口模块(kbengine_defaults.xml->entryScriptFile)中。
	
	
	参数：
	
	
	@state
	如果state为0，意指在断开所有客户端之前，如果state为1，意指在将所有实体写入数据库之前，如果state为2，意指在所有实体被写入数据库之后。
	
	
	
	

	"""
	pass

def onCellAppDeath( addr ):
	"""	
	功能说明：
	某个cellapp死亡会回调此函数。
	注意：该回调接口必须实现在入口模块(kbengine_defaults.xml->entryScriptFile)中。
	
	
	参数：
	
	
	@addr
	死亡的cellapp地址。
	tuple:(ip, port) 网络字节序
	
	
	
	

	"""
	pass

def onFini(  ):
	"""	
	功能说明：
	引擎正式关闭后回调此函数。
	注意：该回调接口必须实现在入口模块kbengine_defaults.xml->entryScriptFile)中。
	

	"""
	pass

def onBaseAppData( key, value ):
	"""	
	功能说明：
	KBEngine.baseAppData有改变时回调此函数。
	注意：该回调接口必须实现在入口模块(kbengine_defaults.xml->entryScriptFile)中。
	
	
	参数：
	
	
	@key
	被改变数据的键。
	
	
	@value
	被改变数据的值。
	
	
	
	

	"""
	pass

def onBaseAppDataDel( key ):
	"""	
	功能说明：
	KBEngine.baseAppData有删除的时候回调此函数。
	注意：该回调接口必须实现在入口模块(kbengine_defaults.xml->entryScriptFile)中。
	
	
	参数：
	
	
	@key
	被删除数据的键。
	
	
	
	

	"""
	pass

def onGlobalData( key, value ):
	"""	
	功能说明：
	KBEngine.globalData有改变的时候回调此函数。
	注意：该回调接口必须实现在入口模块(kbengine_defaults.xml->entryScriptFile)中。
	
	
	参数：
	
	
	@key
	被改变数据的键。
	
	
	@value
	被改变数据的值。
	
	
	
	

	"""
	pass

def onGlobalDataDel( key ):
	"""	
	功能说明：
	KBEngine.globalData有删除的时候回调此函数。
	注意：该回调接口必须实现在入口模块(kbengine_defaults.xml->entryScriptFile)中。
	
	
	参数：
	
	
	@key
	被删除数据的键。
	
	
	
	

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

def onLoseChargeCB( orderID, dbID, success, datas ):
	"""	
	功能说明：
	当在interfaces中调用KBEngine.chargeResponse后，如果该订单丢失或者是不明interfaces未被记录的订单会收到此回调通知。
	注意：该回调接口必须实现在入口模块(kbengine_defaults.xml->entryScriptFile)中。
	
	
	参数：
	
	
	@ordersID
	string，订单ID。
	
	
	@dbID
	uint64，实体的数据库ID, 参见: Entity.databaseID。
	
	
	@success
	bool，是否成功。
	
	
	@datas
	bytes，附带信息。
	
	
	

	"""
	pass

def onReadyForLogin( isBootstrap ):
	"""	
	功能说明：
	当引擎启动并初始化完成后会一直调用此接口询问脚本层是否准备完毕，如果脚本层准备完毕则loginapp允许客户端登录。
	注意：该回调接口必须实现在入口模块(kbengine_defaults.xml->entryScriptFile)中。
	
	
	参数：
	
	
	@isBootstrap
	bool，是否为第一个启动的Baseapp。
	
	
	
	
	
	
	
	返回：
	
	返回值大于等于1.0则脚本层准备完成，否则返回准备的进度值0.0~1.0。
	
	
	
	
	
	

	"""
	pass

def onReadyForShutDown(  ):
	"""	
	功能说明：
	如果这个函数在脚本中有实现，当进程准备退出时，该回调函数被调用。
	
	可以通过该回调控制进程退出的时机。
	注意：该回调接口必须实现在入口模块(kbengine_defaults.xml->entryScriptFile)中。
	
	
	返回：
	
	
	bool，如果返回True，则允许进入进程退出流程，返回其它值则进程会过一段时间后再次询问。
	
	
	
	
	

	"""
	pass

def onAutoLoadEntityCreate( entityType, dbID ):
	"""	
	功能说明：
	自动加载的实体创建时的回调，如果脚本层实现此回调，那么实体由脚本层创建，否则引擎默认使用createEntityAnywhereFromDBID来创建实体。
	这个回调被调用是由于Entity.writeToDB时设置了实体自动加载。
	注：该回调优先于onBaseAppReady执行，可在onBaseAppReady时检查是否已加载实体。
	
	
	参数：
	
	
	@entityType
	string，指定要查询的Entity实体的类型。有效的实体类型在/scripts/entities.xml列出。
	
	
	@dbID
	指定要查询的Entity实体的数据库ID。这个实体的数据库ID存储在该实体的databaseID属性。
	
	
	
	
	
	
	
	
	
	

	"""
	pass

@property
def LOG_ON_ACCEPT():

	"""	
	说明：
	这个常量由Proxy.onLogOnAttempt返回，意指允许新的client与一个Proxy实体绑定。
	如果Proxy实体已经存在一个client绑定关系，那么将踢出之前的client。

	"""
	pass

@property
def LOG_ON_REJECT():

	"""	
	说明：
	这个常量由Proxy.onLogOnAttempt返回，意指拒绝当前client与Proxy实体绑定。

	"""
	pass

@property
def LOG_ON_WAIT_FOR_DESTROY():

	"""	
	说明：
	这个常量由Proxy.onLogOnAttempt返回，当前请求client将会等待直到Proxy实体完全销毁，底层再完成后续绑定过程。
	在这返回之前Proxy.destroy或者Proxy.destroyCellEntity
	应该被调用。

	"""
	pass

@property
def LOG_TYPE_DBG():

	"""	
	说明：
	日志输出类型为调试类型。
	由scriptLogType设置。

	"""
	pass

@property
def LOG_TYPE_ERR():

	"""	
	说明：
	日志输出类型为错误类型。
	由scriptLogType设置。

	"""
	pass

@property
def LOG_TYPE_INFO():

	"""	
	说明：
	日志输出类型为常规信息类型。
	由scriptLogType设置。

	"""
	pass

@property
def LOG_TYPE_NORMAL():

	"""	
	说明：
	日志输出类型为常规类型。
	由scriptLogType设置。

	"""
	pass

@property
def LOG_TYPE_WAR():

	"""	
	说明：
	日志输出类型为警告类型。
	由scriptLogType设置。

	"""
	pass

@property
def NEXT_ONLY():

	"""	
	说明：
	这个常量用于Entity.shouldAutoBackup和Entity.shouldAutoArchive属性。这个值意指在下一次认为可以的时候自动备份该实体，然后这个属性自动设为False（0）。

	"""
	pass

@property
def component():

	"""	
	说明：
	这是正运行在当前Python环境的组件。（至今为止）可能值有'cell', 'base', 'client', 'database', 'bot' 和 'editor'。

	"""
	pass

@property
def entities():

	"""	
	说明：
	entities是一个字典对象，包含当前进程上所有的实体。
	
	调试泄露的实体（调用过destroy却没有释放内存的实体，通常是由于被引用导致无法释放）：
	
	>>> KBEngine.entities.garbages.items()
	[(1025, Avatar object at 0x7f92431ceae8.)]
	
	>>> e = _[0][1]
	>>> import gc
	>>> gc.get_referents(e)
	[{'spacesIsOk': True, 'bootstrapIdx': 1}, ]
	
	
	调试泄露的KBEngine封装的Python对象：
	KBEngine.debugTracing

	"""
	pass

@property
def baseAppData():

	"""	
	说明：
	这个属性包含一个类字典的对象，这个对象会在所有的BaseApps之间自动同步。
	当字典的一个值被修改，这个修改会广播到所有的BaseApps。
	
	
	例子：
	
	KBEngine.baseAppData[ "hello" ] = "there"
	
	
	其余BaseApps可以访问下面的：
	
	print KBEngine.baseAppData[ "hello" ]
	
	
	键和值可以是任意类型，但这些类型必须在所有目标组件上能够被封装和被拆封。
	
	当一个值被改变或被删除，一个回调函数会在所有组件被调用。
	参看：KBEngine.onBaseAppData和KBEngine.onDelBaseAppData。
	
	注意：只有顶层的值才会被广播，如果你有一个值（比如一个列表），它改变了内部的值（比如只是改变一个数），这个信息不会被广播。
	
	不要进行下面的操作：
	
	KBEngine.baseAppData[ "list" ] = [1, 2, 3]
	KBEngine.baseAppData[ "list" ][1] = 7
	
	这样，本地访问是[1, 7, 3]，远程访问是[1, 2, 3]。

	"""
	pass

@property
def globalData():

	"""	
	说明：
	这个属性包含一个类字典的对象，这个对象会在所有的BaseApps和CellApps之间自动同步。
	当字典的一个值被修改，这个修改会广播到所有的BaseApps和CellApps。
	
	例子：
	
	KBEngine.globalData[ "hello" ] = "there"
	
	
	其余Baseapp或者Cellapp可以访问下面的：
	
	print KBEngine.globalData[ "hello" ]
	
	
	键和值可以是任意类型，但这些类型必须在所有目标组件上能够被封装和被拆封。
	
	当一个值被改变或被删除，一个回调函数会在所有组件被调用。
	参看：KBEngine.onGlobalData和KBEngine.onGlobalDataDel。
	
	注意：只有顶层的值才会被广播，如果你有一个值（比如一个列表），它改变了内部的值（比如只是改变一个数），这个信息不会被广播。
	
	不要进行下面的操作：
	
	KBEngine.globalData[ "list" ] = [1, 2, 3]
	KBEngine.globalData[ "list" ][1] = 7
	
	这样，本地访问是[1, 7, 3]，远程访问是[1, 2, 3]。

	"""
	pass

