-- MySQL dump 10.13  Distrib 5.7.20, for Linux (x86_64)
--
-- Host: localhost    Database: stockdb
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
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add permission',3,'add_permission'),(8,'Can change permission',3,'change_permission'),(9,'Can delete permission',3,'delete_permission'),(10,'Can add content type',4,'add_contenttype'),(11,'Can change content type',4,'change_contenttype'),(12,'Can delete content type',4,'delete_contenttype'),(13,'Can add session',5,'add_session'),(14,'Can change session',5,'change_session'),(15,'Can delete session',5,'delete_session'),(16,'Can add 持仓信息',6,'add_hold'),(17,'Can change 持仓信息',6,'change_hold'),(18,'Can delete 持仓信息',6,'delete_hold'),(19,'Can add 股票信息',7,'add_stock'),(20,'Can change 股票信息',7,'change_stock'),(21,'Can delete 股票信息',7,'delete_stock'),(22,'Can add 用户信息',8,'add_user'),(23,'Can change 用户信息',8,'change_user'),(24,'Can delete 用户信息',8,'delete_user'),(25,'Can add 友情链接',9,'add_link'),(26,'Can change 友情链接',9,'change_link'),(27,'Can delete 友情链接',9,'delete_link'),(28,'Can add 交易记录',10,'add_deal'),(29,'Can change 交易记录',10,'change_deal'),(30,'Can delete 交易记录',10,'delete_deal');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
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
  KEY `django_admin_log_user_id_c564eba6_fk_stockapp_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_stockapp_user_id` FOREIGN KEY (`user_id`) REFERENCES `stockapp_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2017-12-25 07:52:19.137689','1','中国黄金',1,'[{\"added\": {}}]',7,1),(2,'2017-12-25 07:52:36.252419','1','中国黄金',2,'[{\"changed\": {\"fields\": [\"impressum\"]}}]',7,1),(3,'2017-12-25 07:57:03.058347','1','admin',2,'[{\"changed\": {\"fields\": [\"last_login\", \"gender\", \"profession\", \"money\"]}}]',8,1),(4,'2017-12-28 02:08:59.966223','2','华能水电',1,'[{\"added\": {}}]',7,1),(5,'2017-12-28 02:09:43.671739','3','中国平安',1,'[{\"added\": {}}]',7,1),(6,'2017-12-28 02:10:46.665236','4','中国中车',1,'[{\"added\": {}}]',7,1),(7,'2017-12-28 02:10:58.796109','2','华能水电',2,'[{\"changed\": {\"fields\": [\"impressum\"]}}]',7,1),(8,'2017-12-28 02:10:58.802051','3','中国平安',2,'[{\"changed\": {\"fields\": [\"impressum\"]}}]',7,1),(9,'2017-12-28 02:10:58.808678','4','中国中车',2,'[{\"changed\": {\"fields\": [\"impressum\"]}}]',7,1);
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
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(2,'auth','group'),(3,'auth','permission'),(4,'contenttypes','contenttype'),(5,'sessions','session'),(10,'stockapp','deal'),(6,'stockapp','hold'),(9,'stockapp','link'),(7,'stockapp','stock'),(8,'stockapp','user');
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
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2017-12-25 06:31:32.743180'),(2,'contenttypes','0002_remove_content_type_name','2017-12-25 06:31:32.802053'),(3,'auth','0001_initial','2017-12-25 06:31:32.986793'),(4,'auth','0002_alter_permission_name_max_length','2017-12-25 06:31:33.023960'),(5,'auth','0003_alter_user_email_max_length','2017-12-25 06:31:33.034826'),(6,'auth','0004_alter_user_username_opts','2017-12-25 06:31:33.043245'),(7,'auth','0005_alter_user_last_login_null','2017-12-25 06:31:33.054113'),(8,'auth','0006_require_contenttypes_0002','2017-12-25 06:31:33.059143'),(9,'stockapp','0001_initial','2017-12-25 06:31:33.623882'),(10,'admin','0001_initial','2017-12-25 06:31:33.727897'),(11,'admin','0002_logentry_remove_auto_add','2017-12-25 06:31:33.750510'),(12,'auth','0007_alter_validators_add_error_messages','2017-12-25 06:31:33.765647'),(13,'auth','0008_alter_user_username_max_length','2017-12-25 06:31:33.778734'),(14,'sessions','0001_initial','2017-12-25 06:31:33.817434'),(15,'stockapp','0002_auto_20171108_1602','2017-12-25 06:31:34.171971'),(16,'stockapp','0003_auto_20171109_1719','2017-12-25 06:31:34.192602'),(17,'stockapp','0004_auto_20171110_1021','2017-12-25 06:31:34.250425'),(18,'stockapp','0005_auto_20171117_1417','2017-12-25 06:31:34.307225'),(19,'stockapp','0006_auto_20171120_1531','2017-12-25 06:31:34.326465'),(20,'stockapp','0007_auto_20171225_1431','2017-12-25 06:31:34.414883');
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
INSERT INTO `django_session` VALUES ('cbz508rzia4ets25heltps62jvlmxacf','OTExNDE2N2QwZTgyODlmOWRhNTJmNjkxMTkwNTNmYjU1YjU4ODA0ZTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiMTE5ZDBiYzVmMTlhYThiMGQ1NzJiMDQ5OWYxNjRmNTQ3ZDBiZTU4MiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2018-01-08 07:55:35.562406'),('hp6b7lm1fm344jb8pirhgtahun0j1nzg','NzlkNWY5NjUzOTdmNDA3YWExNzJmMGQxNjg0NTQ3NzBlYWEwYzAyMzp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNjFhZGNjZGU0MGU3NTM2MTlmOTUwMTQ4N2EzNTUyM2YxNDk5NDJhZSIsIl9hdXRoX3VzZXJfaWQiOiIzIn0=','2018-01-11 03:35:16.929460'),('wjscwb5wh6cd0b56xli8lm8u1yyaw4b5','ZTIzMTI0YTcxMDljMGMzZmViNDBlMzI0OWMwZmJlYTVmOTBiZTNjZTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYmMxOWU4MzBkMzE0YTM5ZDNmYjFlNTg3NTdiYTQyNjZjNTU0YWMzNCIsIl9hdXRoX3VzZXJfaWQiOiIyIn0=','2018-01-11 03:32:33.393902');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stockapp_deal`
--

DROP TABLE IF EXISTS `stockapp_deal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stockapp_deal` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `genre` tinyint(1) NOT NULL,
  `number` int(11) NOT NULL,
  `amount` int(11) NOT NULL,
  `figure` double NOT NULL,
  `time` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `stockapp_deal_user_id_473c0e47_fk` (`user_id`),
  CONSTRAINT `stockapp_deal_user_id_473c0e47_fk` FOREIGN KEY (`user_id`) REFERENCES `stockapp_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stockapp_deal`
--

LOCK TABLES `stockapp_deal` WRITE;
/*!40000 ALTER TABLE `stockapp_deal` DISABLE KEYS */;
/*!40000 ALTER TABLE `stockapp_deal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stockapp_hold`
--

DROP TABLE IF EXISTS `stockapp_hold`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stockapp_hold` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `number` int(11) NOT NULL,
  `amount` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `stockapp_hold_user_id_f06ee3a0_fk_stockapp_user_id` (`user_id`),
  CONSTRAINT `stockapp_hold_user_id_f06ee3a0_fk_stockapp_user_id` FOREIGN KEY (`user_id`) REFERENCES `stockapp_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stockapp_hold`
--

LOCK TABLES `stockapp_hold` WRITE;
/*!40000 ALTER TABLE `stockapp_hold` DISABLE KEYS */;
/*!40000 ALTER TABLE `stockapp_hold` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stockapp_link`
--

DROP TABLE IF EXISTS `stockapp_link`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stockapp_link` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) NOT NULL,
  `callback_url` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stockapp_link`
--

LOCK TABLES `stockapp_link` WRITE;
/*!40000 ALTER TABLE `stockapp_link` DISABLE KEYS */;
/*!40000 ALTER TABLE `stockapp_link` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stockapp_stock`
--

DROP TABLE IF EXISTS `stockapp_stock`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stockapp_stock` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `number` int(11) NOT NULL,
  `company_name` varchar(64) NOT NULL,
  `flow_in` double NOT NULL,
  `flow_out` double NOT NULL,
  `impressum` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stockapp_stock`
--

LOCK TABLES `stockapp_stock` WRITE;
/*!40000 ALTER TABLE `stockapp_stock` DISABLE KEYS */;
INSERT INTO `stockapp_stock` VALUES (1,600489,'中国黄金',456,236,'四好农村路”建设取得了实实在在的成效，为农村特别是贫困地区带去了人气、财气，也为党在基层凝聚了民心。\r\n\r\n　　习近平指出，交通运输部等有关部门和各地区要认真贯彻落实党的十九大精神，从实施乡村振兴战略、打赢脱贫攻坚战的高度，进一步深化对建设农村公路重要意义的认识，聚焦突出问题，完善政策机制，既要把农村公路建好，更要管好、护好、运营好，为广大农民致富奔小康、为加快推进农业农村现代化提供更好保障'),(2,600025,'华能水电',123123,3254324,'习近平指出，交通运输部等有关部门和各地区要认真贯彻落实党的十九大精神，从实施乡村振兴战略、打赢脱贫攻坚战的高度，进一步深化对建设农村公路重要意义的认识，聚焦突出问题，完善政策机制，既要把农村公路建好，更要管好、护好、运营好，为广大农民致富奔小康、为加快推进农业农村现代化提供更好保障'),(3,601318,'中国平安',3242,345646,'习近平指出，交通运输部等有关部门和各地区要认真贯彻落实党的十九大精神，从实施乡村振兴战略、打赢脱贫攻坚战的高度，进一步深化对建设农村公路重要意义的认识，聚焦突出问题，完善政策机制，既要把农村公路建好，更要管好、护好、运营好，为广大农民致富奔小康、为加快推进农业农村现代化提供更好保障'),(4,601766,'中国中车',123,324,'习近平指出，交通运输部等有关部门和各地区要认真贯彻落实党的十九大精神，从实施乡村振兴战略、打赢脱贫攻坚战的高度，进一步深化对建设农村公路重要意义的认识，聚焦突出问题，完善政策机制，既要把农村公路建好，更要管好、护好、运营好，为广大农民致富奔小康、为加快推进农业农村现代化提供更好保障');
/*!40000 ALTER TABLE `stockapp_stock` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stockapp_stock_user`
--

DROP TABLE IF EXISTS `stockapp_stock_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stockapp_stock_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `stock_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `stockapp_stock_user_stock_id_user_id_9d3f98bf_uniq` (`stock_id`,`user_id`),
  KEY `stockapp_stock_user_user_id_32cfed72_fk_stockapp_user_id` (`user_id`),
  CONSTRAINT `stockapp_stock_user_stock_id_a5c7c8b6_fk_stockapp_stock_id` FOREIGN KEY (`stock_id`) REFERENCES `stockapp_stock` (`id`),
  CONSTRAINT `stockapp_stock_user_user_id_32cfed72_fk_stockapp_user_id` FOREIGN KEY (`user_id`) REFERENCES `stockapp_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stockapp_stock_user`
--

LOCK TABLES `stockapp_stock_user` WRITE;
/*!40000 ALTER TABLE `stockapp_stock_user` DISABLE KEYS */;
INSERT INTO `stockapp_stock_user` VALUES (1,1,1),(2,2,1),(3,3,1),(6,3,3),(4,4,1),(5,4,3);
/*!40000 ALTER TABLE `stockapp_stock_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stockapp_user`
--

DROP TABLE IF EXISTS `stockapp_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stockapp_user` (
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
  `gender` varchar(1) NOT NULL,
  `age` int(11) DEFAULT NULL,
  `profession` varchar(128) NOT NULL,
  `qq` varchar(20) DEFAULT NULL,
  `mobile` varchar(11) DEFAULT NULL,
  `money` double DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `mobile` (`mobile`),
  UNIQUE KEY `money` (`money`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stockapp_user`
--

LOCK TABLES `stockapp_user` WRITE;
/*!40000 ALTER TABLE `stockapp_user` DISABLE KEYS */;
INSERT INTO `stockapp_user` VALUES (1,'pbkdf2_sha256$36000$9ijAIUpcsUam$vQeKGF3W5Zv2IqdTHJUlk8in+4Sl+43EDUAI0TtfbBo=','2017-12-28 02:58:15.015294',1,'admin','','','',1,1,'2017-12-25 07:50:00.000000','0',NULL,'理财',NULL,NULL,100000),(2,'pbkdf2_sha256$36000$yYkJUdHkI0Jv$6k5Pyzlu+eXm3SXyLvX6Mc6ZO6kk1ahiE4vztS3NTrM=','2017-12-28 03:32:33.390590',0,'特朗普','','','1111111111@qq.com',0,1,'2017-12-28 03:32:33.374747','0',20,'student','123456','123456',NULL),(3,'pbkdf2_sha256$36000$1MkCRp7VDJkr$28R54VTtqSSoDaWKg8grT4iO2qZUnI14vujz9W0Ky80=','2017-12-28 03:35:16.926031',0,'cainiao','','','123@123.com',0,1,'2017-12-28 03:35:16.900769','0',43,'工程师','1234567','11111111111',NULL);
/*!40000 ALTER TABLE `stockapp_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stockapp_user_groups`
--

DROP TABLE IF EXISTS `stockapp_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stockapp_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `stockapp_user_groups_user_id_group_id_7a3641b0_uniq` (`user_id`,`group_id`),
  KEY `stockapp_user_groups_group_id_a3618adb_fk_auth_group_id` (`group_id`),
  CONSTRAINT `stockapp_user_groups_group_id_a3618adb_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `stockapp_user_groups_user_id_1c3c64fc_fk_stockapp_user_id` FOREIGN KEY (`user_id`) REFERENCES `stockapp_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stockapp_user_groups`
--

LOCK TABLES `stockapp_user_groups` WRITE;
/*!40000 ALTER TABLE `stockapp_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `stockapp_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stockapp_user_user_permissions`
--

DROP TABLE IF EXISTS `stockapp_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stockapp_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `stockapp_user_user_permi_user_id_permission_id_2d15db01_uniq` (`user_id`,`permission_id`),
  KEY `stockapp_user_user_p_permission_id_919f5559_fk_auth_perm` (`permission_id`),
  CONSTRAINT `stockapp_user_user_p_permission_id_919f5559_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `stockapp_user_user_p_user_id_8ec629a8_fk_stockapp_` FOREIGN KEY (`user_id`) REFERENCES `stockapp_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stockapp_user_user_permissions`
--

LOCK TABLES `stockapp_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `stockapp_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `stockapp_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-12-28 12:00:46
