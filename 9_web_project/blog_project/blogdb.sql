-- MySQL dump 10.13  Distrib 5.7.20, for Linux (x86_64)
--
-- Host: localhost    Database: blogdb
-- ------------------------------------------------------
-- Server version	5.7.20-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add content type',4,'add_contenttype'),(11,'Can change content type',4,'change_contenttype'),(12,'Can delete content type',4,'delete_contenttype'),(13,'Can add session',5,'add_session'),(14,'Can change session',5,'change_session'),(15,'Can delete session',5,'delete_session'),(16,'Can add 评论',6,'add_comment'),(17,'Can change 评论',6,'change_comment'),(18,'Can delete 评论',6,'delete_comment'),(19,'Can add 用户',7,'add_user'),(20,'Can change 用户',7,'change_user'),(21,'Can delete 用户',7,'delete_user'),(22,'Can add 分类',8,'add_category'),(23,'Can change 分类',8,'change_category'),(24,'Can delete 分类',8,'delete_category'),(25,'Can add 标签',9,'add_tag'),(26,'Can change 标签',9,'change_tag'),(27,'Can delete 标签',9,'delete_tag'),(28,'Can add 文章',10,'add_article'),(29,'Can change 文章',10,'change_article'),(30,'Can delete 文章',10,'delete_article'),(31,'Can add 友情链接',11,'add_links'),(32,'Can change 友情链接',11,'change_links'),(33,'Can delete 友情链接',11,'delete_links'),(34,'Can add 广告',12,'add_ad'),(35,'Can change 广告',12,'change_ad'),(36,'Can delete 广告',12,'delete_ad');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_ad`
--

DROP TABLE IF EXISTS `blog_ad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog_ad` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) NOT NULL,
  `description` varchar(200) NOT NULL,
  `image_url` varchar(100) NOT NULL,
  `callback_url` varchar(200) DEFAULT NULL,
  `date_publish` datetime(6) NOT NULL,
  `index` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_ad`
--

LOCK TABLES `blog_ad` WRITE;
/*!40000 ALTER TABLE `blog_ad` DISABLE KEYS */;
INSERT INTO `blog_ad` VALUES (1,'达内','达内教育','ad/2017/12/af8b77cc93ef1276f7a87388adb334e0_660_200.jpg','http://bj.tedu.cn','2017-12-25 07:30:55.159493',999),(2,'soho','soho出售','ad/2017/12/网站加载.png','http://www.python.org','2017-12-25 07:32:08.413616',999);
/*!40000 ALTER TABLE `blog_ad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_article`
--

DROP TABLE IF EXISTS `blog_article`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog_article` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) NOT NULL,
  `desc` varchar(50) NOT NULL,
  `content` longtext NOT NULL,
  `click_count` int(11) NOT NULL,
  `is_recommend` tinyint(1) NOT NULL,
  `date_publish` datetime(6) NOT NULL,
  `category_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `blog_article_category_id_7e38f15e_fk_blog_category_id` (`category_id`),
  KEY `blog_article_user_id_5beb0cc1_fk_blog_user_id` (`user_id`),
  CONSTRAINT `blog_article_category_id_7e38f15e_fk_blog_category_id` FOREIGN KEY (`category_id`) REFERENCES `blog_category` (`id`),
  CONSTRAINT `blog_article_user_id_5beb0cc1_fk_blog_user_id` FOREIGN KEY (`user_id`) REFERENCES `blog_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_article`
--

LOCK TABLES `blog_article` WRITE;
/*!40000 ALTER TABLE `blog_article` DISABLE KEYS */;
INSERT INTO `blog_article` VALUES (1,'习近平：把农村公路建好管好护好运营好','中共中央总书记、国家主席、中央军委主席习近平近日对“四好农村路”建设作出重要指示','他强调，近年来，“四好农村路”建设取得了实实在在的成效，为农村特别是贫困地区带去了人气、财气，也为党在基层凝聚了民心。<br />\r\n<br />\r\n习近平指出，交通运输部等有关部门和各地区要认真贯彻落实党的十九大精神，从实施乡村振兴战略、打赢脱贫攻坚战的高度，进一步深化对建设农村公路重要意义的认识，聚焦突出问题，完善政策机制，既要把农村公路建好，更要管好、护好、运营好，为广大农民致富奔小康、为加快推进农业农村现代化提供更好保障。<br />\r\n<br />\r\n中共中央政治局常委、国务院总理李克强作出批示，要求认真总结地方经验，进一步完善政策和工作机制，注重发挥地方、基层和农民的积极性，有效提升农村公路建设、管护和运营水平，为实施乡村振兴战略、推动农民脱贫致富和加快农业农村现代化提供有力支撑。<br />\r\n<br />\r\n12月25日，交通运输部召开全国交通运输工作会议，传达学习习近平重要指示和李克强批示精神，研究部署贯彻落实相关工作。会议强调，习近平总书记的重要指示，既是充分肯定、极大鼓舞，更是殷切期望、巨大鞭策。要认真贯彻落实党的十九大精神和习近平新时代中国特色社会主义思想，聚焦突出问题，完善政策机制，推动“四好农村路”迈入高质量发展的新阶段。<br />\r\n<br />\r\n党的十八大以来，习近平对农村公路建设高度重视，多次作出重要指示，要求建好、管好、护好、运营好农村公路。交通运输部等部门和各级党委政府认真贯彻落实习近平重要指示精神，扎实推进“四好农村路”建设并取得明显成效。5年来，全国新建改建农村公路127.5万公里，99.24%的乡镇和98.34%的建制村通上了沥青路、水泥路，乡镇和建制村通客车率分别达到99.1%和96.5%以上，城乡运输一体化水平接近80%，农村“出行难”问题得到有效解决，交通扶贫精准化水平不断提高，农村物流网络不断完善，广大农民群众得到了实实在在的获得感、幸福感。',45,1,'2017-12-25 07:36:10.165719',3,1);
/*!40000 ALTER TABLE `blog_article` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_article_tag`
--

DROP TABLE IF EXISTS `blog_article_tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog_article_tag` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `article_id` int(11) NOT NULL,
  `tag_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `blog_article_tag_article_id_tag_id_818e752b_uniq` (`article_id`,`tag_id`),
  KEY `blog_article_tag_tag_id_f2afe66b_fk_blog_tag_id` (`tag_id`),
  CONSTRAINT `blog_article_tag_article_id_8db2395e_fk_blog_article_id` FOREIGN KEY (`article_id`) REFERENCES `blog_article` (`id`),
  CONSTRAINT `blog_article_tag_tag_id_f2afe66b_fk_blog_tag_id` FOREIGN KEY (`tag_id`) REFERENCES `blog_tag` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_article_tag`
--

LOCK TABLES `blog_article_tag` WRITE;
/*!40000 ALTER TABLE `blog_article_tag` DISABLE KEYS */;
INSERT INTO `blog_article_tag` VALUES (1,1,1);
/*!40000 ALTER TABLE `blog_article_tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_category`
--

DROP TABLE IF EXISTS `blog_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `index` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_category`
--

LOCK TABLES `blog_category` WRITE;
/*!40000 ALTER TABLE `blog_category` DISABLE KEYS */;
INSERT INTO `blog_category` VALUES (1,'技术交流',999),(2,'娱乐文化',999),(3,'我的生活',999);
/*!40000 ALTER TABLE `blog_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_comment`
--

DROP TABLE IF EXISTS `blog_comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog_comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` longtext NOT NULL,
  `username` varchar(30) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `url` varchar(100) DEFAULT NULL,
  `date_publish` datetime(6) NOT NULL,
  `article_id` int(11) DEFAULT NULL,
  `pid_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `blog_comment_article_id_3d58bca6_fk_blog_article_id` (`article_id`),
  KEY `blog_comment_pid_id_2a2b4cc4_fk_blog_comment_id` (`pid_id`),
  KEY `blog_comment_user_id_59a54155_fk_blog_user_id` (`user_id`),
  CONSTRAINT `blog_comment_article_id_3d58bca6_fk_blog_article_id` FOREIGN KEY (`article_id`) REFERENCES `blog_article` (`id`),
  CONSTRAINT `blog_comment_pid_id_2a2b4cc4_fk_blog_comment_id` FOREIGN KEY (`pid_id`) REFERENCES `blog_comment` (`id`),
  CONSTRAINT `blog_comment_user_id_59a54155_fk_blog_user_id` FOREIGN KEY (`user_id`) REFERENCES `blog_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_comment`
--

LOCK TABLES `blog_comment` WRITE;
/*!40000 ALTER TABLE `blog_comment` DISABLE KEYS */;
INSERT INTO `blog_comment` VALUES (1,'习大大好棒','admin','123@123.com','http://www.baidu.com','2017-12-25 07:38:03.859845',1,NULL,1),(2,'确实好棒','cainiao','123@123.com','http://xiaocainiao.com','2017-12-25 07:41:29.185399',1,3,2),(3,'我要吃庆丰包子','朱鹏辉','zhupenghui@123.com',NULL,'2017-12-25 08:29:44.787169',1,1,NULL),(4,'巴拉拉小魔仙','balala','123@123.com','http://www.baidu.com','2017-12-25 08:30:41.918434',1,NULL,3),(5,'庆丰包子is棒棒哒','balabala','123@123.com','','2017-12-25 08:31:20.130422',1,NULL,4),(6,'你的顺丰快递已在天津炸毁','kkkk','12@123.com',NULL,'2017-12-25 08:32:42.398529',1,1,NULL),(7,'asdsadsads','艾斯','1@1.com','https://艾斯.ic','2017-12-25 09:42:03.550296',1,NULL,NULL),(8,'GAME OVER','GG','GG@GG.COM','https://艾斯.ic','2017-12-25 09:42:35.357533',1,NULL,NULL),(9,'???/WHAT HAPPEN?','???','A@A.COM','http://A.COM','2017-12-25 09:43:36.765590',1,NULL,NULL),(10,'0.0\r\n老铁\r\n双击666','老铁','0@0.0.com','http://0.0.com','2017-12-25 09:44:56.037559',1,NULL,NULL);
/*!40000 ALTER TABLE `blog_comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_links`
--

DROP TABLE IF EXISTS `blog_links`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog_links` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) NOT NULL,
  `description` varchar(200) NOT NULL,
  `callback_url` varchar(200) NOT NULL,
  `date_publish` datetime(6) NOT NULL,
  `index` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_links`
--

LOCK TABLES `blog_links` WRITE;
/*!40000 ALTER TABLE `blog_links` DISABLE KEYS */;
INSERT INTO `blog_links` VALUES (1,'百度','百度主页','http://www.baidu.com','2017-12-25 07:26:08.659241',999),(2,'python','python 官网','http://www.python.org','2017-12-25 07:27:34.695600',999);
/*!40000 ALTER TABLE `blog_links` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_tag`
--

DROP TABLE IF EXISTS `blog_tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog_tag` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_tag`
--

LOCK TABLES `blog_tag` WRITE;
/*!40000 ALTER TABLE `blog_tag` DISABLE KEYS */;
INSERT INTO `blog_tag` VALUES (1,'民生'),(2,'体育'),(3,'django');
/*!40000 ALTER TABLE `blog_tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_user`
--

DROP TABLE IF EXISTS `blog_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `avatar` varchar(200) DEFAULT NULL,
  `qq` varchar(20) DEFAULT NULL,
  `mobile` varchar(11) DEFAULT NULL,
  `url` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `mobile` (`mobile`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_user`
--

LOCK TABLES `blog_user` WRITE;
/*!40000 ALTER TABLE `blog_user` DISABLE KEYS */;
INSERT INTO `blog_user` VALUES (1,'pbkdf2_sha256$36000$o8B3WtnfJBWf$2XXWNRgujvYiyTblVUhI+GX1R1S5wSdZqZbRpdkw1AQ=','2017-12-27 01:55:30.920807',1,'admin','','','',1,1,'2017-12-25 07:22:50.824471','avatar/default.png',NULL,NULL,NULL),(2,'pbkdf2_sha256$36000$Bn8n8M1Hyowh$e0eBGiFGMXO08lATRejCxwax7OZnPfZSunxjKsD0Y+I=','2017-12-25 07:41:00.000000',0,'cainiao','','','123@123.com',0,1,'2017-12-25 07:41:00.000000','avatar/2017/12/网站加载.png',NULL,NULL,'http://xiaocainiao.com'),(3,'pbkdf2_sha256$36000$Glf6P1PTYM2O$Fbl47B1hUzZGBeuyBxxf7/w2/b/r4dWYVAqDdIf7s9s=','2017-12-25 08:30:31.203502',0,'balala','','','123@123.com',0,1,'2017-12-25 08:30:31.184775','avatar/default.png',NULL,NULL,'http://www.baidu.com'),(4,'pbkdf2_sha256$36000$jWuGIHvDWkxw$XweuutTLa5faN6yvTR5tFQD0VNXFTMYAz/DtCJ1svi4=','2017-12-25 08:30:40.469999',0,'balabala','','','123@123.com',0,1,'2017-12-25 08:30:40.449218','avatar/default.png',NULL,NULL,''),(5,'pbkdf2_sha256$36000$R5XS9eiEhVwa$Wb1X0bTimxawDSPTOgE7dqf+SBYB8zIim+cuTmbGfPM=','2017-12-26 03:13:37.941782',0,'superstar','','','superstar@163.com',0,1,'2017-12-26 03:13:37.908294','avatar/default.png',NULL,NULL,'');
/*!40000 ALTER TABLE `blog_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_user_groups`
--

DROP TABLE IF EXISTS `blog_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `blog_user_groups_user_id_group_id_9046f296_uniq` (`user_id`,`group_id`),
  KEY `blog_user_groups_group_id_29990e74_fk_auth_group_id` (`group_id`),
  CONSTRAINT `blog_user_groups_group_id_29990e74_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `blog_user_groups_user_id_4e1acb48_fk_blog_user_id` FOREIGN KEY (`user_id`) REFERENCES `blog_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_user_groups`
--

LOCK TABLES `blog_user_groups` WRITE;
/*!40000 ALTER TABLE `blog_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `blog_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_user_user_permissions`
--

DROP TABLE IF EXISTS `blog_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `blog_user_user_permissions_user_id_permission_id_1d3c1311_uniq` (`user_id`,`permission_id`),
  KEY `blog_user_user_permi_permission_id_95ca6010_fk_auth_perm` (`permission_id`),
  CONSTRAINT `blog_user_user_permi_permission_id_95ca6010_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `blog_user_user_permissions_user_id_379a1502_fk_blog_user_id` FOREIGN KEY (`user_id`) REFERENCES `blog_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_user_user_permissions`
--

LOCK TABLES `blog_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `blog_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `blog_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_blog_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_blog_user_id` FOREIGN KEY (`user_id`) REFERENCES `blog_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2017-12-25 07:23:54.708578','1','技术交流',1,'[{\"added\": {}}]',8,1),(2,'2017-12-25 07:24:09.114359','2','娱乐文化',1,'[{\"added\": {}}]',8,1),(3,'2017-12-25 07:24:23.784406','3','我的生活',1,'[{\"added\": {}}]',8,1),(4,'2017-12-25 07:26:08.660362','1','百度',1,'[{\"added\": {}}]',11,1),(5,'2017-12-25 07:27:34.697194','2','python',1,'[{\"added\": {}}]',11,1),(6,'2017-12-25 07:30:55.163818','1','达内',1,'[{\"added\": {}}]',12,1),(7,'2017-12-25 07:32:08.414908','2','soho',1,'[{\"added\": {}}]',12,1),(8,'2017-12-25 07:36:06.307953','1','民生',1,'[{\"added\": {}}]',9,1),(9,'2017-12-25 07:36:10.173550','1','习近平：把农村公路建好管好护好运营好',1,'[{\"added\": {}}]',10,1),(10,'2017-12-25 07:39:19.390523','2','体育',1,'[{\"added\": {}}]',9,1),(11,'2017-12-25 07:39:31.617113','3','django',1,'[{\"added\": {}}]',9,1),(12,'2017-12-25 07:42:08.043267','2','cainiao',2,'[{\"changed\": {\"fields\": [\"last_login\", \"avatar\"]}}]',7,1),(13,'2017-12-27 01:56:23.771752','3','我要吃庆丰包子',2,'[{\"changed\": {\"fields\": [\"pid\"]}}]',6,1),(14,'2017-12-27 02:22:47.365838','6','你的顺丰快递已在天津炸毁',2,'[{\"changed\": {\"fields\": [\"pid\"]}}]',6,1),(15,'2017-12-27 02:23:11.492747','2','确实好棒',2,'[{\"changed\": {\"fields\": [\"pid\"]}}]',6,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(12,'blog','ad'),(10,'blog','article'),(8,'blog','category'),(6,'blog','comment'),(11,'blog','links'),(9,'blog','tag'),(7,'blog','user'),(4,'contenttypes','contenttype'),(5,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2017-12-25 06:27:25.359260'),(2,'contenttypes','0002_remove_content_type_name','2017-12-25 06:27:25.447621'),(3,'auth','0001_initial','2017-12-25 06:27:25.736087'),(4,'auth','0002_alter_permission_name_max_length','2017-12-25 06:27:25.779471'),(5,'auth','0003_alter_user_email_max_length','2017-12-25 06:27:25.791407'),(6,'auth','0004_alter_user_username_opts','2017-12-25 06:27:25.801135'),(7,'auth','0005_alter_user_last_login_null','2017-12-25 06:27:25.810473'),(8,'auth','0006_require_contenttypes_0002','2017-12-25 06:27:25.815048'),(9,'blog','0001_initial','2017-12-25 06:27:26.666524'),(10,'admin','0001_initial','2017-12-25 06:27:26.777309'),(11,'admin','0002_logentry_remove_auto_add','2017-12-25 06:27:26.804643'),(12,'auth','0007_alter_validators_add_error_messages','2017-12-25 06:27:26.819368'),(13,'auth','0008_alter_user_username_max_length','2017-12-25 06:27:26.832540'),(14,'blog','0002_auto_20171225_1427','2017-12-25 06:27:26.882351'),(15,'sessions','0001_initial','2017-12-25 06:27:26.919922');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('2jptf4plt3xzudee7znjx214j0d2atc4','MGFiY2MzMjMzMGIwNzNjZjEwM2IwZDg3MTJhMzVjNGMxZWZkMTkwMzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzNDViYTYxZTlkODQ4ZmZjNTZiZDg4M2QwOWFmYzA5ZWZiNjg5ZDk4In0=','2018-01-09 08:06:13.089405'),('7ps96otg860cutgfqmi8yzujroozo5cp','YTc1MjQ0YjQ5YzQ5ZjBlOWYyNGIzYWI1MTg4MjY0MzI1YmFkZGJmNDp7Il9hdXRoX3VzZXJfaGFzaCI6IjY5ODA0OGMyNzgyYjg4Mzg3Zjc5NWVjMzU1NzYwYTI0N2IwYzgzMTAiLCJfYXV0aF91c2VyX2lkIjoiMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2018-01-08 08:30:31.207821'),('8dcjicrxg1i6a61u5sq0ykoif8748qss','NjNkNzM1YWQ0ODMyNjc1YjA1ZjViYmViOWFhYjQ2Yzg5YWM2MTMxMzp7Il9hdXRoX3VzZXJfaWQiOiI1IiwiX2F1dGhfdXNlcl9oYXNoIjoiOWNlYzhhZGRmYmM4YTE4YzQ4NDA1Yzk1NDBmZWNjODE1MTQyNWUzNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2018-01-09 03:13:37.948066'),('rzfa1bb5s3f9esgtxju7kvtlkxflibmu','MTQ0OWEzMWQwZDIzYzBjMzZjYjRiNjkxYmFhYTg2MWI0ZmI0ODNlMDp7Il9hdXRoX3VzZXJfaGFzaCI6IjM0NWJhNjFlOWQ4NDhmZmM1NmJkODgzZDA5YWZjMDllZmI2ODlkOTgiLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2018-01-08 07:41:46.828169'),('t3oxwz9g0368wegrty6a20topiw3ce5i','MTQ0OWEzMWQwZDIzYzBjMzZjYjRiNjkxYmFhYTg2MWI0ZmI0ODNlMDp7Il9hdXRoX3VzZXJfaGFzaCI6IjM0NWJhNjFlOWQ4NDhmZmM1NmJkODgzZDA5YWZjMDllZmI2ODlkOTgiLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2018-01-10 01:55:30.935575'),('tmgemg12ztpwzuct8xvuszmuym2xgn9a','ZTIyYjdlYWY1YmQzNDc5MzU3ZDIxNWQ0NzJlNzQxMTJkZTdlM2ZiOTp7Il9hdXRoX3VzZXJfaGFzaCI6ImFjNzJmYjI5YmM5ODI3NTZjN2Q5ZWJlMDlkOTE0NWNiZmI4M2ZlNjUiLCJfYXV0aF91c2VyX2lkIjoiNCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2018-01-08 08:30:40.473980');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-12-27 10:24:01
