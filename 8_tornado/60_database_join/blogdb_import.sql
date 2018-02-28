-- MySQL dump 10.13  Distrib 5.7.19, for Linux (x86_64)
--
-- Host: localhost    Database: blogdb
-- ------------------------------------------------------
-- Server version	5.7.19-0ubuntu0.16.04.1

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
-- Table structure for table `a`
--

DROP TABLE IF EXISTS `a`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `a` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `a`
--

LOCK TABLES `a` WRITE;
/*!40000 ALTER TABLE `a` DISABLE KEYS */;
INSERT INTO `a` VALUES (1,'f'),(2,'a'),(3,'e'),(4,'g'),(5,'h');
/*!40000 ALTER TABLE `a` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `b`
--

DROP TABLE IF EXISTS `b`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `b` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `b`
--

LOCK TABLES `b` WRITE;
/*!40000 ALTER TABLE `b` DISABLE KEYS */;
INSERT INTO `b` VALUES (1,'a'),(2,'b'),(3,'c'),(4,'d'),(5,'e');
/*!40000 ALTER TABLE `b` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `table1`
--

DROP TABLE IF EXISTS `table1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `table1` (
  `customer_id` varchar(20) NOT NULL,
  `city` varchar(20) NOT NULL,
  PRIMARY KEY (`customer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `table1`
--

LOCK TABLES `table1` WRITE;
/*!40000 ALTER TABLE `table1` DISABLE KEYS */;
INSERT INTO `table1` VALUES ('baidu','hangzhou'),('jd','shanghai'),('tedu','hangzhou'),('tx','hangzhou');
/*!40000 ALTER TABLE `table1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `table2`
--

DROP TABLE IF EXISTS `table2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `table2` (
  `order_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`order_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `table2`
--

LOCK TABLES `table2` WRITE;
/*!40000 ALTER TABLE `table2` DISABLE KEYS */;
INSERT INTO `table2` VALUES (1,'tedu'),(2,'jd'),(3,'jd'),(4,'jd'),(5,'tx'),(6,NULL);
/*!40000 ALTER TABLE `table2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_blog`
--

DROP TABLE IF EXISTS `tb_blog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_blog` (
  `blog_id` int(11) NOT NULL AUTO_INCREMENT,
  `blog_title` varchar(128) NOT NULL,
  `blog_content` varchar(1024) NOT NULL,
  `blog_user_id` int(11) NOT NULL,
  `blog_create_data` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `blog_update_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`blog_id`),
  KEY `tb_blog_tb_user_user_id_fk` (`blog_user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_blog`
--

LOCK TABLES `tb_blog` WRITE;
/*!40000 ALTER TABLE `tb_blog` DISABLE KEYS */;
INSERT INTO `tb_blog` VALUES (1,'我是要成为海贼王的男人','我是要成为海贼王的男人!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!',2,'2017-12-21 09:04:59','2017-12-21 09:04:59'),(2,'我是要成为海贼王的男人','我是要成为海贼王的男人,我是要成为海贼王的男人,我是要成为海贼王的男人',2,'2017-12-21 09:04:59','2017-12-21 09:04:59'),(3,'还是喜欢过夏天','还是喜欢过夏天',1,'2017-12-21 09:04:59','2017-12-21 09:04:59'),(4,'超像真人的蜡像，一出门被吓了一个大跳。','超像真人的蜡像，一出门被吓了一个大跳。',1,'2017-12-21 09:04:59','2017-12-21 09:04:59'),(5,'哈哈哈，哈哈哈哈哈哈，哈哈哈哈哈哈哈哈，哈哈哈哈哈哈哈，杀青','哈哈哈，哈哈哈哈哈哈，哈哈哈哈哈哈哈哈，哈哈哈哈哈哈哈，杀青',3,'2017-12-21 09:04:59','2017-12-21 09:04:59'),(6,'[ 慢一拍的感謝回覆 ]  “我的名字不好聽”，“不好聽也沒事，妳就告訴我吧”，”牛愛花！<- -  這段害我差點嗆到  ⁄(⁄ ⁄ ⁄ω⁄ ⁄ ⁄)⁄  謝謝祝福 ','[ 慢一拍的感謝回覆 ]  “我的名字不好聽”，“不好聽也沒事，妳就告訴我吧”，”牛愛花！<- -  這段害我差點嗆到  ⁄(⁄ ⁄ ⁄ω⁄ ⁄ ⁄)⁄  謝謝祝福 ',5,'2017-12-21 09:04:59','2017-12-21 09:04:59');
/*!40000 ALTER TABLE `tb_blog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_blog_tag`
--

DROP TABLE IF EXISTS `tb_blog_tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_blog_tag` (
  `rel_id` int(11) NOT NULL AUTO_INCREMENT,
  `rel_blog_id` int(11) NOT NULL,
  `rel_tag_id` int(11) NOT NULL,
  PRIMARY KEY (`rel_id`),
  KEY `tb_blog_tag_tb_blog_blog_id_fk` (`rel_blog_id`),
  KEY `tb_blog_tag_tb_tag_tag_id_fk` (`rel_tag_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_blog_tag`
--

LOCK TABLES `tb_blog_tag` WRITE;
/*!40000 ALTER TABLE `tb_blog_tag` DISABLE KEYS */;
INSERT INTO `tb_blog_tag` VALUES (1,1,1),(2,2,1),(3,5,3),(4,6,2);
/*!40000 ALTER TABLE `tb_blog_tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_comment`
--

DROP TABLE IF EXISTS `tb_comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_comment` (
  `comment_id` int(11) NOT NULL AUTO_INCREMENT,
  `comment_content` varchar(1024) NOT NULL,
  `comment_user_id` int(11) NOT NULL,
  `comment_blog_id` int(11) NOT NULL,
  `comment_create_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `comment_udpate_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`comment_id`),
  KEY `tb_comment_tb_blog_blog_id_fk` (`comment_blog_id`),
  KEY `tb_comment_tb_user_user_id_fk` (`comment_user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_comment`
--

LOCK TABLES `tb_comment` WRITE;
/*!40000 ALTER TABLE `tb_comment` DISABLE KEYS */;
INSERT INTO `tb_comment` VALUES (1,'加油',1,1,'2017-12-21 09:13:36','2017-12-21 09:27:32'),(2,'我看好你',1,1,'2017-12-21 09:13:36','2017-12-21 09:27:32'),(3,'强强强',1,2,'2017-12-21 09:13:36','2017-12-21 09:27:32'),(4,'前排表白热巴热巴！！',7,3,'2017-12-21 09:13:36','2017-12-22 04:57:51'),(5,'啊啊啊,老婆',6,3,'2017-12-21 09:13:36','2017-12-22 05:00:24'),(6,'心',1,4,'2017-12-21 09:13:36','2017-12-21 09:27:32'),(7,'喜欢你',5,4,'2017-12-21 09:13:36','2017-12-22 05:00:24'),(8,'哈哈哈哈哈哈哈',1,5,'2017-12-21 09:13:36','2017-12-21 09:27:32'),(9,'感谢',1,6,'2017-12-21 09:27:32','2017-12-21 09:27:32');
/*!40000 ALTER TABLE `tb_comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_tag`
--

DROP TABLE IF EXISTS `tb_tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_tag` (
  `tag_id` int(11) NOT NULL AUTO_INCREMENT,
  `tag_name` varchar(5) NOT NULL,
  PRIMARY KEY (`tag_id`),
  UNIQUE KEY `tb_tag_tag_name_uindex` (`tag_name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_tag`
--

LOCK TABLES `tb_tag` WRITE;
/*!40000 ALTER TABLE `tb_tag` DISABLE KEYS */;
INSERT INTO `tb_tag` VALUES (1,'动漫'),(2,'演唱会'),(3,'电视剧');
/*!40000 ALTER TABLE `tb_tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_user`
--

DROP TABLE IF EXISTS `tb_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(10) NOT NULL,
  `user_password` varchar(50) NOT NULL,
  `user_avatar` varchar(256) DEFAULT NULL,
  `user_city` varchar(10) NOT NULL,
  `user_create_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `user_update_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `tb_user_user_name_uindex` (`user_name`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_user`
--

LOCK TABLES `tb_user` WRITE;
/*!40000 ALTER TABLE `tb_user` DISABLE KEYS */;
INSERT INTO `tb_user` VALUES (1,'迪丽热巴','aa','<null>','乌鲁木齐','2017-12-21 08:53:36','2017-12-22 01:38:00'),(2,'蒙奇·D·路飞','aa','<null>','风车村','2017-12-21 08:33:36','2017-12-22 01:38:00'),(3,'黄渤','aa',NULL,'青岛市','2017-12-21 07:43:36','2017-12-22 01:38:00'),(4,'陈奕迅','aa',NULL,'香港','2017-12-21 08:42:36','2017-12-22 01:38:00'),(5,'陈信宏','aa',NULL,'台北市','2017-12-21 08:43:39','2017-12-22 01:38:00'),(6,'路人甲','aa',NULL,'北京','2017-12-22 01:42:03','2017-12-22 01:42:43'),(7,'路人乙','aa',NULL,'北京','2017-12-22 01:42:44','2017-12-22 01:42:44'),(14,'aa','4124bc0a9335c27f086f24ba207a4912','1514020266.4037883工牌.svg','beijing','2017-12-23 09:11:06','2017-12-23 09:11:06');
/*!40000 ALTER TABLE `tb_user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-12-23 17:29:52
