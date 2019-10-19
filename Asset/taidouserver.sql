# Host: 127.0.0.1  (Version: 5.6.23-log)
# Date: 2015-07-09 15:22:20
# Generator: MySQL-Front 5.3  (Build 4.214)

/*!40101 SET NAMES utf8 */;

#
# Structure for table "serverproperty"
#

DROP TABLE IF EXISTS `serverproperty`;
CREATE TABLE `serverproperty` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `ip` varchar(255) DEFAULT NULL,
  `count` int(11) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;

#
# Data for table "serverproperty"
#

INSERT INTO `serverproperty` VALUES (1,'一区 中国','127.0.0.1',10),(2,'二区 沃尔玛','127.0.0.1',200),(3,'三区 水帘洞','127.0.0.1',30),(4,'四去 北京','127.0.0.1',40),(5,'五区 上海','127.0.0.1',50),(6,'三区 水帘洞','127.0.0.1',60),(7,'三区 水帘洞','127.0.0.1',200),(8,'三区 水帘洞','127.0.0.1',150),(9,'三区 水帘洞','127.0.0.1',30),(10,'三区 水帘洞','127.0.0.1',40),(11,'三区 水帘洞','127.0.0.1',300),(12,'三区 水帘洞','127.0.0.1',60),(13,'三区 水帘洞','127.0.0.1',10),(14,'三区 水帘洞','127.0.0.1',100),(15,'三区 水帘洞','127.0.0.1',30),(16,'三区 水帘洞','127.0.0.1',40),(17,'三区 水帘洞','127.0.0.1',50),(18,'三区 水帘洞','127.0.0.1',60),(19,'三区 水帘洞','127.0.0.1',10),(20,'三区 水帘洞','127.0.0.1',20),(21,'三区 水帘洞','127.0.0.1',100),(22,'三区 水帘洞','127.0.0.1',40),(23,'三区 水帘洞','127.0.0.1',150),(24,'三区 水帘洞','127.0.0.1',60);

#
# Structure for table "user"
#

DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

#
# Data for table "user"
#

INSERT INTO `user` VALUES (2,'siki','81DC9BDB52D04DC20036DBD8313ED055'),(3,'taikr','81DC9BDB52D04DC20036DBD8313ED055'),(4,'siki1','81DC9BDB52D04DC20036DBD8313ED055'),(5,'siki3','81DC9BDB52D04DC20036DBD8313ED055'),(6,'1234','81DC9BDB52D04DC20036DBD8313ED055'),(7,'qwer','1CE22BFE558FC8D77EAC6D824827A3D1'),(8,'asdf','81DC9BDB52D04DC20036DBD8313ED055'),(9,'siki2','81DC9BDB52D04DC20036DBD8313ED055');

#
# Structure for table "role"
#

DROP TABLE IF EXISTS `role`;
CREATE TABLE `role` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `level` int(11) DEFAULT NULL,
  `isman` bit(1) DEFAULT NULL,
  `userid` int(11) DEFAULT NULL,
  `exp` int(11) DEFAULT NULL,
  `diamond` int(11) DEFAULT NULL,
  `coin` int(11) DEFAULT NULL,
  `energy` int(11) DEFAULT NULL,
  `toughen` int(11) DEFAULT NULL,
  PRIMARY KEY (`Id`),
  KEY `fk_userid` (`userid`),
  CONSTRAINT `fk_userid` FOREIGN KEY (`userid`) REFERENCES `user` (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;

#
# Data for table "role"
#

INSERT INTO `role` VALUES (5,'siki',10,b'1',2,0,10,97171,100,50),(6,'siki1',1,b'1',4,0,1000,20000,100,50),(7,'siki1',1,b'1',4,0,1000,20000,100,50),(8,'sdf',1,b'0',4,0,1000,20000,100,50),(9,'siki1',1,b'1',4,0,1000,20000,100,50),(10,'siki3',1,b'1',5,0,1000,20000,100,50),(11,'sdf',1,b'1',6,0,1000,20000,100,50),(12,'asd',1,b'1',7,0,1000,20000,100,50),(13,'SIKI',1,b'1',8,0,1000,20000,100,50),(14,'134',1,b'1',9,0,1000,20000,100,50);

#
# Structure for table "taskdb"
#

DROP TABLE IF EXISTS `taskdb`;
CREATE TABLE `taskdb` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `taskid` int(11) DEFAULT NULL,
  `state` tinyint(3) DEFAULT NULL,
  `type` tinyint(3) DEFAULT NULL,
  `roleid` int(11) DEFAULT NULL,
  `lastupdatetime` datetime DEFAULT NULL,
  PRIMARY KEY (`Id`),
  KEY `fk_roleid` (`roleid`),
  CONSTRAINT `fk_roleid` FOREIGN KEY (`roleid`) REFERENCES `role` (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

#
# Data for table "taskdb"
#

INSERT INTO `taskdb` VALUES (1,1001,3,0,5,'0001-01-01 00:00:00'),(2,1002,1,1,5,'0001-01-01 00:00:00'),(3,1003,1,2,10,'0001-01-01 00:00:00'),(4,1003,1,2,6,'0001-01-01 00:00:00');

#
# Structure for table "skilldb"
#

DROP TABLE IF EXISTS `skilldb`;
CREATE TABLE `skilldb` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `skillid` int(11) DEFAULT NULL,
  `roleid` int(11) DEFAULT NULL,
  `level` int(11) DEFAULT NULL,
  PRIMARY KEY (`Id`),
  KEY `fk_skillid_roleid` (`roleid`),
  CONSTRAINT `fk_skillid_roleid` FOREIGN KEY (`roleid`) REFERENCES `role` (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

#
# Data for table "skilldb"
#

INSERT INTO `skilldb` VALUES (1,1002,5,3),(2,1003,5,3),(3,1004,5,5);

#
# Structure for table "inventoryitemdb"
#

DROP TABLE IF EXISTS `inventoryitemdb`;
CREATE TABLE `inventoryitemdb` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `inventoryid` int(11) DEFAULT NULL,
  `count` int(11) DEFAULT NULL,
  `level` int(11) DEFAULT NULL,
  `isdressed` bit(1) DEFAULT NULL,
  `roleid` int(11) DEFAULT NULL,
  PRIMARY KEY (`Id`),
  KEY `fk_inventory_roleid` (`roleid`),
  CONSTRAINT `fk_inventory_roleid` FOREIGN KEY (`roleid`) REFERENCES `role` (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;

#
# Data for table "inventoryitemdb"
#

INSERT INTO `inventoryitemdb` VALUES (1,1019,1,9,b'0',5),(2,1001,1,8,b'1',5),(3,1008,1,1,b'1',5),(4,1002,1,6,b'0',5),(5,1017,3,7,b'0',5),(6,1018,1,5,b'0',5),(7,1012,1,2,b'1',5),(8,1005,1,7,b'0',5),(9,1002,1,9,b'0',5),(10,1005,1,6,b'0',5),(11,1005,1,6,b'0',5);
