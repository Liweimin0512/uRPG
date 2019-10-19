class Entity:
	def accelerate( self, accelerateType, acceleration ):
		"""		
		功能说明：
		加速实体当前运动。
		
		
		可影响的运动包括：
		
		Entity.moveToEntity
		Entity.moveToPoint
		Entity.navigate
		Entity.addYawRotator
		
		
		
		参数：
		
		
		accelerateType
		string，影响的运动类型，如：Movement、Turn。
		
		
		velocity
		float，每秒的加速度，如果传入的是负值则表示减速度。
		
		
		
		
		
		
		返回：
		
		
		影响后的实体当前速度。
		
		
		
		
		
		

		"""
		pass

	def addYawRotator( self, targetYaw, velocity, userArg ):
		"""		
		功能说明：
		控制实体绕yaw旋转，旋转完成将会通过Entity.onTurn通知。
		
		使用Entity.cancelController带上控制器ID或者使用Entity.cancelController("Movement")来删除它。
		
		
		参看：
		
		Entity.cancelController
		
		
		
		参数：
		
		
		targetYaw
		float，给定的目标yaw弧度。
		
		
		velocity
		float，旋转时每秒的弧度。
		
		
		userArg
		是一个可选的整型，所有控制器共有。如果这个值不为0则传给回调函数。建议
		在回调原型里设置默认值为0。
		
		
		
		
		
		
		
		

		"""
		pass

	def addProximity( self, rangeXZ, rangeY, userArg ):
		"""		
		功能说明：
		创建一个范围触发器，当有其它实体进入或离开这个触发器区域的时候会通知这个Entity。这个区域是一个方形（为了效率）。如果
		其它实体在x轴和z轴上均在给定的距离里面，则实体被视为在这个范围里面。这个Entity通过onEnterTrap和onLeaveTrap函数被
		通知，这两个函数可以如下定义：
		
		
			def onEnterTrap( self, entityEntering, rangeXZ, rangeY, controllerID, userArg = 0 ):
			def onLeaveTrap( self, entityLeaving, rangeXZ, rangeY, controllerID, userArg = 0 ):
		
		
		由于这个范围触发器是一个控制器，使用Entity.cancelController带上控制器ID来删除它。
		
		需要注意的是回调有可能会立刻被触发，即使在addProximity()调用返回之前。
		
		
		参看：
		
		Entity.cancelController
		
		
		
		参数：
		
		
		rangeXZ
		float，给定触发器xz轴区域的大小，必须大于等于0。
		
		
		rangeY
		float，给定触发器y轴高度，必须大于等于0。
		需要注意的是，这个参数要生效必须开放kbengine_defaults.xml->cellapp->coordinate_system->rangemgr_y
		
		开放y轴管理会带来一些消耗，因为一些游戏大量的实体都在同一y轴高度或者在差不多水平线高度，此时碰撞变得非常密集。
		3D太空类游戏或者小房间类实体较少的游戏比较适合开放此选项。
		
		
		userArg
		是一个可选的整型，所有控制器共有。如果这个值不为0则传给回调函数。建议
		在回调原型里设置默认值为0。
		
		
		
		
		
		
		返回：
		
		
		返回创建控制器的id。
		
		
		
		

		"""
		pass

	def addTimer( self, start, interval=0.0, userData=0 ):
		"""		
		功能说明：
		注册一个定时器，定时器由回调函数onTimer触发，回调函数将在"initialOffset"秒后被执行第1次，而后将每间隔"repeatOffset"秒执行1次，可设定一个用户参数"userArg"（仅限integer类型）。
		
		onTimer 函数必须在entity的cell部分被定义，且带有2个参数，第1个integer类型的是timer的id（可用于移除timer的"delTimer"函数），第2个是用户参数"userArg"。
		
		例子:
		
		# 这里是使用addTimer的一个例子
		import KBEngine
		 
		class MyCellEntity( KBEngine.Entity ):
		 
		    def __init__( self ):
		        KBEngine.Entity.__init__( self )
		 
		        # 增加一个定时器，5秒后执行第1次，而后每1秒执行1次，用户参数是9
		        self.addTimer( 5, 1, 9 )
		 
		        # 增加一个定时器，1秒后执行，用户参数缺省是0
		        self.addTimer( 1 )
		 
		    # Entity的定时器回调"onTimer"被调用
		    def onTimer( self, id, userArg ):
		        print "MyCellEntity.onTimer called: id %i, userArg: %i" % ( id, userArg )
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

	def clientEntity( self, destID ):
		"""		
		功能说明：
		通过这个方法可以访问自己客户端（当前实体必须绑定了客户端）中某个实体的方法，只有在View范围内的实体才会同步到客户端。它只能在一个real实体上被调用。
		
		
		参数：
		
		
		@destID
		目标实体的ID。
		
		
		
		
		
		

		"""
		pass

	def canNavigate( self ):
		"""		
		功能说明：
		通过这个方法判断当前实体是否可以使用导航（Entity.navigate）功能。它只能在一个real实体上被调用。
		通常当实体所在Space使用Entity.addSpaceGeometryMapping加载过有效的导航用的碰撞数据（Navmesh或者2D的tile数据）并且实体在有效导航区域该功能可用。
		
		
		返回：
		
		bool， 如果实体可在当前Space中使用导航功能返回True，否则返回False。
		
		
		
		
		

		"""
		pass

	def debugView( self ):
		"""		
		功能说明：
		debugView输出Entity的View的详细信息到cell的调试日志。
		一份View系统工作的描述可以在Entity类文档中找到。
		
		一份样品信息如下：
		
		  INFO cellapp [0x00001a1c] [2014-11-04 00:28:41,409] - Avatar::debugView: 100 size=4, Seen=4, Pending=0, ViewRadius=50.000, ViewHyst=5.000
		  INFO cellapp [0x00001a1c] [2014-11-04 00:28:41,409] - Avatar::debugView: 100 Avatar(102), position(771.586.211.002.776.55), dist=0
		  INFO cellapp [0x00001a1c] [2014-11-04 00:28:41,409] - Avatar::debugView: 100 Monster(1028), position(820.834.211.635.768.749), dist=49.8659
		  INFO cellapp [0x00001a1c] [2014-11-04 00:28:41,409] - Avatar::debugView: 100 NPC(1025), position(784.024.210.95.782.273), dist=13.6915
		  INFO cellapp [0x00001a1c] [2014-11-04 00:28:41,409] - Avatar::debugView: 100 Avatar(106), position(771.586.211.002.776.55), dist=0
		
		信息的第一行告诉我们：
		
		实体#1000的数据
		有4个实体在它的View区域并且已经同步给客户端。
		有0个实体在它的View区域，正在等待同步到客户端。
		View的半径是 50.000
		View的滞后区域向外延伸了5.000
		
		

		"""
		pass

	def delTimer( self, id ):
		"""		
		功能说明：
		函数delTimer用于移除一个注册的定时器，移除后的定时器不再执行。只执行1次的定时器在执行回调后自动移除，不必要使用delTimer移除。
		如果delTimer函数使用一个无效的id（例如已经移除），将会产生错误。
		
		
		参数：
		
		
		@id
		integer，它指定要移除的定时器id。
		
		
		
		

		"""
		pass

	def destroy( self ):
		"""		
		功能说明：
		这个函数销毁它的本地Entity实例，如果实体在其他进程上存在ghost部分也会同时通知销毁。
		这个函数最好由实体自己调用，如果这个实体是一个ghost则会抛出一个异常。如果回调函数onDestroy()被实现则被调用。
		

		"""
		pass

	def destroySpace( self ):
		"""		
		功能说明：
		销毁这个实体所在的空间。
		

		"""
		pass

	def entitiesInView( self ):
		"""		
		功能说明：
		获得这个实体的View范围内的实体列表。
		

		"""
		pass

	def entitiesInRange( self, range, entityType=None, position=None ):
		"""		
		功能说明：
		在给定的距离内搜索实体。这是一个球形的搜索，3个轴的距离
		都要测量。这可以找到在这个实体的View范围之外的实体，但不能找到其他cell的实体。
		例子：
		
		  self.entitiesInRange( 100, 'Creature', (100, 0, 100) )
		
		搜索到‘Creature’类型的实体列表（‘Creature’的子类实例化的实体）。中心点是(100, 0, 100)，搜索半径是100米。
		
		  [ e for e in self.entitiesInRange( 100, None, (100,0,100) ) if isinstance( e, BaseType ) ]
		
		将给出一个来自‘BaseType’或‘BaseType’的子类实例化的实体列表。
		
		
		参数：
		
		
		@range
		围绕这个实体搜索的距离，float类型
		
		
		@entityType
		一个可选的字符串参数，实体的类型名称，用于匹配实体。如果实体类型是一个有效的类名（ 有效的实体类型在/scripts/entities.xml列出 ），
		则只有这个类型的实体会被返回，否则将这个范围的所有实体都返回。
		
		
		@position
		一个可选的Vector3类型参数，作为搜索半径的中心, 默认以实体自身为中心。
		
		
		
		
		
		返回：
		
		
		在给定范围内的Entity对象列表。
		
		
		
		

		"""
		pass

	def isReal( self ):
		"""		
		功能说明：
		这个函数返回这个Entity是real的还是一个ghost的。
		
		这个函数很少被用到但对调试很有用。
		
		
		返回：
		
		bool， 如果是real实体返回True，否则返回False。
		
		
		

		"""
		pass

	def moveToEntity( self, destEntityID, velocity, distance, userData, faceMovement, moveVertically ):
		"""		
		功能说明：
		直线移动实体到另一个Entity位置。
		任何实体，在任意时刻只能有一个移动控制器，重复调用任何移动函数将终止之前的移动控制器。
		调用后函数将返回一个可以用于取消这次移动的控制器ID。
		
		例如，Entity.cancelController( movementID )。
		移动取消还可以调用Entity.cancelController( "Movement" )。当移动被取消之后回调通知方法将不被调用。
		
		
			def onMove( self, controllerID, userData ):
			def onMoveOver( self, controllerID, userData ):
			def onMoveFailure( self, controllerID, userData ):
		
		
		
		参考:
		
		Entity.cancelController
		
		
		
		参数：
		
		
		destEntityID
		int，目标Entity的ID
		
		
		velocity
		float，Entity移动的速度，单位m/s
		
		
		distance
		float，距离目标小于该值停止移动，如果该值为0则移动到目标位置。
		
		
		userData
		object，可选参数，回调通知被调用时其中userData参数将为此值。
		
		
		faceMovement
		bool，可选参数，如果实体面向移动方向则为true。如果是其它机制则为false。
		
		
		moveVertically
		bool，可选参数，设为True指移动为直线移动，设为False指贴着地面直线移动。
		
		
		
		
		
		
		返回：
		
		
		int，新创建的控制器ID。
		
		
		
		

		"""
		pass

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

	def getViewRadius( self ):
		"""		
		功能说明：
		这个函数返回这个Entity当前的View半径值。
		
		数据可以通过
		Entity.setViewRadius( radius, hyst )设置。
		
		
		返回：
		
		float， View半径。
		
		
		
		
		

		"""
		pass

	def getViewHystArea( self ):
		"""		
		功能说明：
		这个函数返回这个Entity的View当前滞后区域值。
		
		数据可以通过
		Entity.setViewRadius( radius, hyst )设置。
		
		
		返回：
		
		float， View当前滞后区域值。
		
		
		
		
		

		"""
		pass

	def getRandomPoints( self, centerPos, maxRadius, maxPoints, layer ):
		"""		
		功能说明：
		这个函数用于获取以某个坐标点为中心一定区域内Entity.navigate可到达的随机坐标点。
		
		
		参数：
		
		
		@centerPos
		Vector3，Entity中心坐标点
		
		
		@maxRadius
		float，最大的搜索半径
		
		
		@maxPoints
		uint32，最多返回的随机坐标点数量。
		
		
		@layer
		int8，使用某个层的navmesh来搜索。
		
		
		
		
		
		返回：
		
		
		tuple，包含一个或者多个坐标的数组。 
		
		
		
		
		
		

		"""
		pass

	def navigate( self, destination, velocity, distance, maxMoveDistance, maxSearchDistance, faceMovement, layer, userData ):
		"""		
		功能说明：
		使用导航系统来使这个Entity向一个目标点移动，成功或失败会调用回调函数。
		KBEngine可以有数个预先生成好的导航网格，不同的网格大小（会导致不同的导航路径）。
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
		Vector3，Entity移向的目标点。
		
		
		velocity
		float，Entity的移动速度，单位m/s
		
		
		distance
		float，距离目标小于该值停止移动，如果该值为0则移动到目标位置。
		
		
		maxMoveDistance
		float，最大的移动距离。
		
		
		maxSearchDistance
		float，从导航数据中最大搜索距离。
		
		
		faceMovement
		bool，如果实体面向移动方向则为true（默认）。如果是其它机制则为false。
		
		
		layer
		int8，使用某个层的navmesh来寻路。
		
		
		userData
		object，传给通知函数的数据。
		
		
		
		
		
		
		返回：
		
		
		int，新创建的控制器ID。 
		
		
		
		
		
		
		

		"""
		pass

	def navigatePathPoints( self, destination, maxSearchDistance, layer ):
		"""		
		功能说明：
		这个函数返回有当前Entity的位置到destination位置所经过的路径点列表。
		
		
		
		参数：
		
		
		@destination
		Vector3，Entity移向的目标点
		
		
		@maxSearchDistance
		float，最大的搜索距离
		
		
		@layer
		int8，使用某个层的navmesh来查找路径列表。
		
		
		
		
		
		

		"""
		pass

	def setViewRadius( self, radius, hyst=5 ):
		"""		
		功能说明：
		指定Entity的感兴趣的区域大小。
		
		这个函数只能用于有Witness关联的实体。
		
		注意：
		你可以通过设置kbengine.xml配置选项'cellapp/defaultViewRadius'来设置默认的View半径。
		
		数据可以通过
		Entity.getViewRadius( )与Entity.getViewHystArea( )获得。
		
		
		参数：
		
		
		@radius
		float，radius指定View区域的半径
		
		
		@hyst
		float，指定超过View区域的滞后区域的大小。合理的设定滞后区域将能够降低View碰撞的敏感度从而提高CPU执行效率。
		一个实体进入另一个实体的View必须跨越View半径区域，但实体离开View区域则需要移出View半径区域包括滞后区域。
		
		
		
		
		
		返回：
		
		
		None
		
		
		
		

		"""
		pass

	def teleport( self, nearbyMBRef, position, direction ):
		"""		
		功能说明：
		瞬间移动一个Entity到一个指定的空间。这个函数允许指定实体移动后的位置与朝向。
		如果需要在不同空间跳转（ 通常用于不同场景或者房间跳转 ），可以传一个CellEntityCall给这个函数（ 这个entityCall所对应的实体必须在目的空间中 ）。
		
		这个函数只能在real的实体上被调用。
		
		
		参数：
		
		
		@nearbyMBRef
		一个决定Entity跳往哪个Space的CellEntityCall（ 这个entityCall所对应的实体必须在目的Space中 ），它被认为是传送目的地。
		这个可以设为None，在这种情形下它会在当前的cell完成瞬移。
		
		
		@position
		Entity瞬移后的坐标，是一个有3个float(x, y, z)组成的序列。
		
		
		@direction
		Entity瞬移后的朝向，是一个由3个float组成的序列(roll,pitch, yaw)。
		
		
		
		
		
		
		

		"""
		pass

	def writeToDB( self, shouldAutoLoad, dbInterfaceName ):
		"""		
		功能说明：
		这个函数保存与这个实体相关的数据到数据库，包括base实体的数据。在数据确认传到数据库之前base实体的onWriteToDB函数会被调用。
		
		cell实体的数据同时备份在base实体，确保遇到灾难恢复数据时数据是最新的。
		
		这个函数只能在real实体且实体必须存在base部分时才允许被调用。
		
		
		参数：
		
		
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

	def onDestroy( self ):
		"""		如果这个函数在脚本中有实现，这个函数在调用Entity.destroy()后，在实际销毁之前被调用。
		这个函数没有参数。
		

		"""
		pass

	def onEnterTrap( self, entity, rangeXZ, rangeY, controllerID, userArg ):
		"""		当注册了使用Entity.addProximity注册了一个范围触发器，有其他实体进入触发器时，该回调函数被调用。
		
		
		参数：
		
		
		@entity 已经进入了范围的实体。
		
		
		@rangeXZ
		float，给定触发器xz轴区域的大小，必须大于等于0。
		
		
		@rangeY
		float，给定触发器y轴高度，必须大于等于0。
		需要注意的是，这个参数要生效必须开放kbengine_defaults.xml->cellapp->coordinate_system->rangemgr_y
		
		开放y轴管理会带来一些消耗，因为一些游戏大量的实体都在同一y轴高度或者在差不多水平线高度，此时碰撞变得非常密集。
		3D太空类游戏或者小房间类实体较少的游戏比较适合开放此选项。
		
		
		@controllerID 这个触发器的控制器id。
		
		
		@userArg 这个参数的值由用户调用addProximity时给出，用户可以根据此参数对当前行为做一些判断。
		
		
		
		

		"""
		pass

	def onEnteredView( self, entity ):
		"""		如果这个函数在脚本中有实现，当一个实体进入了当前实体的View范围，该回调被触发。
		
		
		参数：
		
		
		@entity 进入View范围的实体。
		
		
		
		
		

		"""
		pass

	def onGetWitness( self ):
		"""		如果这个函数在脚本中有实现，当实体绑定了Witness时被调用。
		也可以访问实体属性Entity.hasWitness得到实体当前的状态。
		
		

		"""
		pass

	def onLeaveTrap( self, entity, rangeXZ, rangeY, controllerID, userArg ):
		"""		如果这个函数在脚本中有实现，当实体离开了当前实体注册的范围触发器区域时被触发，范围触发器由Entity.addProximity注册。
		
		
		参数：
		
		
		@entity 已经离开触发器区域的实体。
		
		
		@rangeXZ
		float，给定触发器xz轴区域的大小，必须大于等于0。
		
		
		@rangeY
		float，给定触发器y轴高度，必须大于等于0。
		需要注意的是，这个参数要生效必须开放kbengine_defaults.xml->cellapp->coordinate_system->rangemgr_y
		
		开放y轴管理会带来一些消耗，因为一些游戏大量的实体都在同一y轴高度或者在差不多水平线高度，此时碰撞变得非常密集。
		3D太空类游戏或者小房间类实体较少的游戏比较适合开放此选项。
		
		
		@controllerID 这个触发器的控制器ID。
		
		
		@userArg 这个参数的值由用户调用addProximity时给出，用户可以根据此参数对当前行为做一些判断。
		
		
		
		
		
		

		"""
		pass

	def onLoseControlledBy( self, id ):
		"""		如果这个函数在脚本中有实现，当Entity.controlledBy 所关联的实体丢失时改回调方法被调用。
		
		
		参数：
		
		
		@id controlledBy实体的ID。
		
		
		
		
		
		

		"""
		pass

	def onLoseWitness( self ):
		"""		如果这个函数在脚本中有实现，当实体解除Witness时，该回调被触发。
		也可以访问实体属性Entity.hasWitness得到实体当前的状态。
		

		"""
		pass

	def onMove( self, controllerID, userData ):
		"""		如果这个函数在脚本中有实现，相关的Entity.moveToPoint与Entity.moveToEntity还有Entity.navigate方法被调用并且成功后底层每帧移动都会回调此函数。
		
		
		
		参数：
		
		
		@controllerID 与某个移动相关的控制器ID。
		
		
		@userData 这个参数值由用户在请求移动相关接口时给出。
		
		
		
		
		
		

		"""
		pass

	def onMoveOver( self, controllerID, userData ):
		"""		如果这个函数在脚本中有实现，相关的Entity.moveToPoint与Entity.moveToEntity还有Entity.navigate方法被调用后到达指定目标点时会回调此函数。
		
		
		参数：
		
		
		@controllerID 与某个移动相关的控制器ID。
		
		
		@userData 这个参数值由用户在请求移动相关接口时给出。
		
		
		
		
		
		

		"""
		pass

	def onMoveFailure( self, controllerID, userData ):
		"""		如果这个函数在脚本中有实现，相关的Entity.moveToPoint与Entity.moveToEntity还有Entity.navigate方法被调用并且失败时会回调此函数。
		
		
		参数：
		
		
		@controllerID 与某个移动相关的控制器ID。
		
		
		@userData 这个参数值由用户在请求移动相关接口时给出。
		
		
		
		
		
		
		

		"""
		pass

	def onRestore( self ):
		"""		如果这个函数在脚本中有实现，这个函数在Cell应用程序崩溃后在其它Cell应用程序上重新创建该实体时被调用。这个函数没有参数。 
		
		

		"""
		pass

	def onSpaceGone( self ):
		"""		如果这个函数在脚本中有实现，当前实体所在的Space将要销毁时触发 。这个函数没有参数。 
		
		
		

		"""
		pass

	def onTurn( self, controllerID, userData ):
		"""		如果这个函数在脚本中有实现，相关的Entity.addYawRotator方法被调用后到达指定yaw时会回调此函数。
		
		
		参数：
		
		
		@controllerID Entity.addYawRotator返回的控制器ID。
		
		
		@userData 这个参数值由用户在请求移动相关接口时给出。
		
		
		
		
		

		"""
		pass

	def onTeleport( self ):
		"""		如果这个函数在脚本中有实现，在通过baseapp的Entity.teleport调用发生的实体传送中，实体(Real entity)被传送之前的时刻此方法会被调用。
		请注意，在cell上调用实体的teleport并不会回调此接口，如果你需要这个功能请在Entity.teleport之后调用此回调。
		
		
		

		"""
		pass

	def onTeleportFailure( self ):
		"""		如果这个函数在脚本中有实现，当用户调用Entity.teleport失败时该回调被调用。
		
		

		"""
		pass

	def onTeleportSuccess( self, nearbyEntity ):
		"""		如果这个函数在脚本中有实现，当用户调用Entity.teleport成功时该回调被调用。
		
		
		参数：
		
		
		@nearbyEntity 这个参数由用户调用
			Entity.teleport时给出。这是一个real实体。
		
		
		
		

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

	def onUpdateBegin( self ):
		"""		当同步一帧开始时被调用。
		
		
		

		"""
		pass

	def onUpdateEnd( self ):
		"""		当同步一帧结束时被调用。
		
		
		

		"""
		pass

	def onWitnessed( self, isWitnessed ):
		"""		如果这个函数在脚本中有实现，如果当前实体进入了另一个绑定了Witness的实体的View范围（也可以理解为一个实体被观察者观察到了），则该实体的回调函数被调用。
		可以利用这个函数在实体被观察时激活实体的AI，实体停止被观察时可以停止AI的执行，这样可以降低服务端的计算量从而提升效率。
		
		
		
		
		参数：
		
		
		@isWitnessed bool，实体被观察时为True，实体被停止观察时是False。
		也可以访问实体属性Entity.isWitnessed得到实体当前的状态。
		
		
		
		

		"""
		pass

	def onWriteToDB( self ):
		"""		如果这个函数在脚本中有实现，这个函数在实体将要存档到数据库时被调用。
		
		

		"""
		pass

	@property
	def allClients( self ):

		"""		通过这个属性调用实体的客户端远程方法，引擎会将这个消息广播给实体View范围内所有的其他绑定了客户端的实体(包括自己的客户端，绑定了客户端的实体通常为玩家)。
		例子：
		avatar的View范围内有玩家A和玩家B以及怪物C。
		avatar.allClients.attack(monsterID，skillID, damage)
		此时，玩家自己和玩家A还有玩家B的客户端都会调用到该实体attack方法，在他们的客户端可以调用指定技能的攻击动作做表现。

		"""
		pass

	@property
	def base( self ):

		"""		base是用于联系Entity实体的entityCall。这个属性是只读的，且如果这个实体没有关联的Entity实体时属性是None。

		"""
		pass

	@property
	def className( self ):

		"""		实体的类名。 

		"""
		pass

	@property
	def client( self ):

		"""		client是用于联系客户端的entityCall。这个属性是只读的，且如果这个实体没有关联的客户端时属性是None。

		"""
		pass

	@property
	def controlledBy( self ):

		"""		该属性如果设置为某个客户端所关联的服务端实体的BaseEntityCall，那么该实体由对应的客户端来控制移动，如果该属性为None则实体由服务端移动。
		当客户端登陆后调用giveClientTo到该实体时，该属性会自动的设置为自己的BaseEntityCall。
		
		脚本可以灵活的控制该实体由服务端控制移动或是由客户端（自己的客户端或是其他客户端）控制移动。

		"""
		pass

	@property
	def direction( self ):

		"""		这个属性描述的是Entity在世界空间中的朝向，用户可以改变这个属性，数据会同步到客户端。

		"""
		pass

	@property
	def hasWitness( self ):

		"""		这个只读属性如果为True，表示实体已经绑定了一个Witness，绑定了Witness的实体则客户端可以通过实体获得实体View范围内的信息。否则为False。

		"""
		pass

	@property
	def id( self ):

		"""		id是Entity的对象id。这个id是一个整型，在base，cell和client相关联的实体之间是相同的。 这个属性是只读的。 

		"""
		pass

	@property
	def isDestroyed( self ):

		"""		如果这个属性的值为True，Entity则已经被销毁了。

		"""
		pass

	@property
	def isOnGround( self ):

		"""		如果这个属性的值为True，Entity在地面上，否则为False。

		"""
		pass

	@property
	def isWitnessed( self ):

		"""		如果当前实体进入了另一个绑定了Witness的实体的View范围（也可以理解为一个实体被观察者观察到了, 这个属性值为True，否则为False。
		
		参考：
		Entity.onWitnessed

		"""
		pass

	@property
	def layer( self ):

		"""		一个space可以同时加载多个navmesh数据，不同的navmesh在不同的layer中，不同的layer可被抽象成地面、水面等等。
		通过这个属性决定一个实体存在于哪个layer中。
		
		参考：
		KBEngine.addSpaceGeometryMapping

		"""
		pass

	@property
	def otherClients( self ):

		"""		通过这个属性调用实体的客户端远程方法，引擎会将这个消息广播给实体View范围内所有的其他绑定了客户端的实体(不包括自己的客户端，绑定了客户端的实体通常为玩家)。
		例子：
		avatar的View范围内有玩家A和玩家B以及怪物C。
		avatar.otherClients.attack(monsterID，skillID, damage)
		此时，玩家A与玩家B的客户端都会调用到该实体attack方法，在他们的客户端可以调用指定技能的攻击动作做表现。

		"""
		pass

	@property
	def position( self ):

		"""		这个实体在世界空间中的坐标(x, y, z)，这个属性可以被用户改变，改变后会同步到客户端。
		需要注意的是，不要引用这个属性，引用这个属性很有可能错误的修改了实体的真实坐标。
		
		
		例子：
		self.position.y = 10.0
		
		
		如果你想拷贝这个属性值可以使用如下方式：
		
		
			import Math
			self.copyPosition = Math.Vector3( self.position )
		

		"""
		pass

	@property
	def spaceID( self ):

		"""		这个属性是实体所在的空间的ID，cell与客户端这个值都保持一致。

		"""
		pass

	@property
	def topSpeed( self ):

		"""		实体的最大xz轴移动速度（米/秒），这个属性通常要比实际移动速度要大一些，服务端通过这个属性检查客户端的移动合法性，如果移动距离超出速度限制则被强制拉回上一个坐标位置。

		"""
		pass

	@property
	def topSpeedY( self ):

		"""		实体的最大y轴移动速度（米/秒），这个属性通常要比实际移动速度要大一些，服务端通过这个属性检查客户端的移动合法性，如果移动距离超出速度限制则被强制拉回上一个坐标位置。

		"""
		pass

	@property
	def volatileInfo( self ):

		"""		这个属性指定Entity的易变类数据同步到客户端的策略。
		易变类数据包括实体的坐标position和实体的朝向direction，易变类数据由于极易改变的特性，引擎底层使用了一套优化的方案将其同步到客户端。
		这个属性是四个float（position，yaw，pitch，roll）代表距离值，当一个实体靠近当前实体达到距离则服务端向其同步相关数据。如果距离值大于View半径则代表总是同步。
		还有一个特殊的bool属性optimized，它的作用是控制服务器同步时是否进行优化，目前主要的优化是Y轴。
		如果为true，在一些行为(如：navigate)导致服务器能确定实体在地面时，服务器不同步实体的Y轴坐标，当同步大量实体时能节省大量带宽，默认为true。
		
		用户也可以在.def制定不同实体的同步策略：
		
		〈Volatile〉
		    〈position/〉           〈!-- 总是同步 --〉
		    〈yaw/〉                〈!-- 总是同步 --〉
		    〈pitch〉20〈/pitch〉     〈!-- 相距20米或以内同步     --〉
		    〈optimized〉 true 〈/optimized〉   
		〈/Volatile〉               〈!-- roll未指明则总是同步  --〉
		
		

		"""
		pass

def addSpaceGeometryMapping( spaceID, mapper, path, shouldLoadOnServer, params ):
	"""	
	功能说明：
	关联一个给定空间的几何映射，函数调用之后服务端和客户端都会加载相应的几何体数据。
	
	在服务端上，从给定目录里加载所有的几何数据到指定的空间。这些数据可能被分成很多区块，不同区块是异步加载的，当所有的几何数据加载
	完成的时候下面的通知方法会被调用：
		def onAllSpaceGeometryLoaded( self, spaceID, mappingName ):
	
	
	
	服务端仅加载场景的几何数据提供给导航和碰撞功能使用，客户端除了几何数据外还会加载纹理等数据。
	
	3D场景当前默认使用的是recastnavigation插件所导出的数据，2D场景当前默认使用的是MapEditor编辑器导出的数据。
	
	
	有一种可能会导致onAllSpaceGeometryLoaded()不被调用，就是如果在某一个
	时刻多个CellApp同时调用这个方法来添加几何到相同的空间的时候CellAppMgr崩溃了。
	
	
	参数：
	
	
	spaceID
	uint32，空间的ID，指定在哪个空间操作
	
	
	mapper
	目前填None
	
	
	path
	包含几何数据的目录路径
	
	
	shouldLoadOnServer
	可选的boolean参数，指定是否在服务端上加载几何。默认为True
	
	
	params
	可选的PyDict参数，指定不同layer所使用的navmesh，例如：
	KBEngine.addSpaceGeometryMapping(self.spaceID, None, resPath, True, {0 : "srv_xinshoucun_1.navmesh", 1 : "srv_xinshoucun.navmesh"})
	
	
	
	
	

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

def createEntity( entityType, spaceID, position, direction, params ):
	"""	
	功能说明：
	createEntity在当前进程指定space中创建一个新的实体。
	这个函数需要指定要创建的实体的类别，位置和方向，还可以选择性地设置实体的任意属性（属性在实体的.def文件里描述）。
	
	例子：
	
	# 创建一个打开的门的实体与"thing"实体的位置一样
	direction = ( 0, 0, thing.yaw )
	properties = { "open":1 }
	KBEngine.createEntity( "Door", thing.space, thing.position, direction,
	                       properties )
	
	
	
	参数：
	
	
	@entityType
	string，要创建的实体名称，在/scripts/entities.xml文件里声明。
	
	
	@spaceID
	int32，要放置实体的空间的ID。
	
	
	@position
	由3个float组成的序列，指定新实体的出生点，在世界中的坐标。
	
	
	@direction
	由3个float组成的序列，指定新实体的初始朝向(roll, pitch, yaw)，相对于世界坐标系。
	
	
	@params
	可选参数, 一个Python字典对象。
	如果一个指定的键是一个Entity属性，他的值会用来初始化这个Entity实体的属性。
	
	
	
	
	
	返回：
	
	
	新实体。
	
	
	
	
	
	

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
	
	

	"""
	pass

def delSpaceData( spaceID, key  ):
	"""	
	功能说明：
	删除指定key的space数据（如果space分割成多个部分，将进行同步删除）。
	
	space数据由用户通过setSpaceData设置。
	
	
	参数：
	
	
	@spaceID
	int32，空间的ID。
	
	
	@key
	string，一个字符串关键字。
	
	
	
	
	

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
	
	
	@callback可选参数，带有命令执行结果的回调对象（比如说是一个函数）。这个回调带有4个参数：结果集合，影响的行数，自増长值，错误信息。 
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
	注意：这个函数依赖于Cellapps服务进程启动参数gus，请正确设置启动参数保持唯一性。
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
	string，如果存在返回资源的绝对路径，否则返回空。
	
	
	
	
	
	返回：
	
	
	string，资源的绝对路径。
	
	
	
	
	
	

	"""
	pass

def getSpaceData( spaceID, key  ):
	"""	
	功能说明：
	获取指定key的space数据。
	
	space数据由用户通过setSpaceData设置。
	
	
	参数：
	
	
	@spaceID
	int32，空间的ID。
	
	
	@key
	string，一个字符串关键字。
	
	
	
	
	返回：
	
	
	string，指定key的字符串数据。
	
	
	
	
	

	"""
	pass

def getSpaceGeometryMapping( spaceID ):
	"""	
	功能说明：
	返回一个指定空间的几何映射名称。
	
	
	参数：
	
	
	@spaceID
	要查询的空间的id。
	
	
	
	
	
	返回：
	
	
	string，几何映射名称。
	
	
	
	
	
	
	

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
	返回服务端是否正在关闭中。在onBaseAppShuttingDown回调函数被调用后，这个函数返回True。
	
	
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

def raycast( spaceID, layer, src, dst ):
	"""	
	功能说明：
	在指定的space中指定的layer中由源坐标向目的坐标射出一道射线，返回碰撞到的坐标点。
	
	注意：space必须使用addSpaceGeometryMapping加载过几何数据。
	
	下面是一个例子:
	
	
		>>> KBEngine.raycast( spaceID, entity.layer, (0, 10, 0), (0,-10,0) )
		((0.0000, 0.0000, 0.0000), ( (0.0000, 0.0000, 0.0000),
		(4.0000, 0.0000, 0.0000), (4.0000, 0.0000, 4.0000)), 0)
	
	
	
	参数：
	
	
	@spaceID
	int32, space的id。
	
	
	@layer
	int8，几何层。一个space可以同时加载多个navmesh数据，不同的navmesh在不同的layer中，不同的layer可被抽象成地面、水面等等。
	
	
	
	
	
	返回：
	
	list， 碰撞到的坐标点列表。
	
	
	
	
	
	

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
	
	1）重载脚本仅仅能在Cellapp上执行， 用户应该确保所有的服务端组件加载完成。
	
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

def setSpaceData( spaceID, key, value  ):
	"""	
	功能说明：
	设置指定key的space数据。
	
	space数据可以通过getSpaceData获取。
	
	
	参数：
	
	
	@spaceID
	int32，空间的ID。
	
	
	@key
	string，一个字符串关键字。
	
	
	@value
	string，字符串值。
	
	
	
	
	
	

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

def onCellAppData( key, value ):
	"""	
	功能说明：
	KBEngine.cellAppData有改变时回调此函数。
	注意：该回调接口必须实现在入口模块(kbengine_defaults.xml->entryScriptFile)中。
	
	
	参数：
	
	
	@key
	被改变数据的键。
	
	
	@value
	被改变数据的值。
	
	
	
	

	"""
	pass

def onCellAppDataDel( key ):
	"""	
	功能说明：
	KBEngine.cellAppData有删除的时候回调此函数。
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

def onSpaceData( spaceID, key, value ):
	"""	
	功能说明：
	当space数据有改变的时候被调用。
	space数据由用户通过setSpaceData设置。
	
	
	参数：
	
	
	@spaceID
	空间的ID。
	
	
	@key
	被改变数据的键。
	
	
	@value
	被改变数据的值。
	
	
	
	
	
	
	
	

	"""
	pass

def onSpaceGeometryLoaded( spaceID, mapping ):
	"""	
	功能说明：
	空间所需求的网格碰撞等数据加载完毕。
	由用户通过addSpaceGeometryMapping设置。
	
	
	参数：
	
	
	@spaceID
	空间的ID。
	
	
	@mapping
	网格碰撞数据的映射值。
	
	
	
	
	
	
	
	
	

	"""
	pass

def onAllSpaceGeometryLoaded( spaceID, isBootstrap, mapping ):
	"""	
	功能说明：
	空间所需求的网格碰撞等数据全部加载完毕。
	由用户通过addSpaceGeometryMapping设置。
	
	
	参数：
	
	
	@spaceID
	空间的ID。
	
	
	@isBootstrap
	如果一个空间被分割由多个cell共同负载，那么isBootstrap描述的是是否为加载请求的发起cell。
	
	
	@mapping
	网格碰撞数据的映射值。
	
	
	
	
	
	
	
	
	

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
	这个常量目前在Cellapp未被使用。

	"""
	pass

@property
def cellAppData():

	"""	
	说明：
	这个属性包含一个类字典的对象，这个对象会在所有的CellApps之间自动同步。
	当字典的一个值被修改，这个修改会广播到所有的CellApps。
	
	
	例子：
	
	KBEngine.cellAppData[ "hello" ] = "there"
	
	
	其余CellApp可以访问下面的：
	
	print KBEngine.cellAppData[ "hello" ]
	
	
	键和值可以是任意类型，但这些类型必须在所有目标组件上能够被封装和被拆封。
	
	当一个值被改变或被删除，一个回调函数会在所有组件被调用。
	参看：KBEngine.onCellAppData和KBEngine.onDelCellAppData。
	
	注意：只有顶层的值才会被广播，如果你有一个值（比如一个列表），它改变了内部的值（比如只是改变一个数），这个信息不会被广播。
	
	不要进行下面的操作：
	
	KBEngine.cellAppData[ "list" ] = [1, 2, 3]
	KBEngine.cellAppData[ "list" ][1] = 7
	
	这样，本地访问是[1, 7, 3]，远程访问是[1, 2, 3]。

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
	entities是一个字典对象，包含当前进程上所有的实体，包括ghost实体。
	
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
def globalData():

	"""	
	说明：
	这个属性包含一个类字典的对象，这个对象会在所有的BaseApps和CellApps之间自动复制。
	当字典的一个值被修改，这个修改会广播到所有的BaseApps和CellApps。CellAppMgr解决竞争条件，保证信息复制的权威性。
	
	例子：
	
	KBEngine.globalData[ "hello" ] = "there"
	
	
	其余Cellapp或者Baseapp可以访问下面的：
	
	print KBEngine.globalData[ "hello" ]
	
	
	键和值可以是任意类型，但这些类型必须在所有目标组件上能够被封装和被拆封。
	
	当一个值被改变或被删除，一个回调函数会在所有组件被调用。
	参看：KBEngine.onGlobalData和KBEngine.onGlobalDataDel。
	
	注意：只有顶层的值才会被广播，如果你有一个易变的值（比如一个列表），它改变了内部的值（比如只是改变一个数），这个信息不会被广播。
	
	不要进行下面的操作：
	
	KBEngine.globalData[ "list" ] = [1, 2, 3]
	KBEngine.globalData[ "list" ][1] = 7
	
	这样，本地访问是[1, 7, 3]，远程访问是[1, 2, 3]。

	"""
	pass

