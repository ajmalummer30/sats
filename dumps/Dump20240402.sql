-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: sats
-- ------------------------------------------------------
-- Server version	8.3.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `accounts_customuser`
--

DROP TABLE IF EXISTS `accounts_customuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_customuser` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `age` int unsigned DEFAULT NULL,
  `phone_number` varchar(20) DEFAULT NULL,
  `station_name_id` bigint DEFAULT NULL,
  `employee_id` varchar(20) NOT NULL,
  `manager_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  KEY `accounts_customuser_manager_id_6b37f368_fk_accounts_` (`manager_id`),
  KEY `accounts_customuser_station_name_id_36ffa5a0_fk_accounts_` (`station_name_id`),
  CONSTRAINT `accounts_customuser_manager_id_6b37f368_fk_accounts_` FOREIGN KEY (`manager_id`) REFERENCES `accounts_customuser` (`id`),
  CONSTRAINT `accounts_customuser_station_name_id_36ffa5a0_fk_accounts_` FOREIGN KEY (`station_name_id`) REFERENCES `accounts_station` (`id`),
  CONSTRAINT `accounts_customuser_chk_1` CHECK ((`age` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_customuser`
--

LOCK TABLES `accounts_customuser` WRITE;
/*!40000 ALTER TABLE `accounts_customuser` DISABLE KEYS */;
INSERT INTO `accounts_customuser` VALUES (1,'pbkdf2_sha256$600000$9RLRzdvrrKFKqjZ1a6VVHx$w3NN+JjoYJQi99EP2S2JCZTRCxq1jjU9LlAbi/Lf3ck=','2024-02-25 17:10:15.529906',1,'admin','','','',1,1,'2024-02-25 17:09:48.182979',NULL,NULL,NULL,'SSA10010019',NULL),(2,'pbkdf2_sha256$600000$DjqkV9w9mWAEQP2dny8I3u$wYIMzFfltMFYZmgxXW9pDluavG1axwl8IQJU3u32uwI=','2024-02-29 12:59:32.337139',1,'root','','','',1,1,'2024-02-26 17:37:58.569165',NULL,NULL,NULL,'SSA10010019',NULL),(3,'pbkdf2_sha256$600000$jKTWXz0cZzfchMnTnwVT8G$N3bnH72YliddTSMvLmNdHkU8CbjZhFqdHoTvmjqZ9TQ=','2024-03-26 12:14:12.393172',0,'ajmalummer','Ajmal','Ummer','ajmalummer30@gmail.com',0,1,'2024-02-26 17:45:05.000000',NULL,NULL,1,'SSA10010019',8),(4,'pbkdf2_sha256$600000$UI0AY2BeOIvNb2Zl9DPhs4$HcaWVYzGTkC3lz9r9mMy0IRQ1I6gbzPYb5r8lFaxV2A=','2024-03-07 14:18:34.197019',0,'lazimmohammed','lazim','mohammed','lazim.mohammed@sats.com.sa',0,1,'2024-02-27 08:57:31.000000',NULL,'0539483153',1,'2537546794',3),(5,'Welcome2s',NULL,0,'hassan.rana','Hassan','Rana','hassan.rana@sats.com.sa',0,1,'2024-02-27 09:13:30.000000',NULL,NULL,2,'SSA10010063',NULL),(6,'pbkdf2_sha256$600000$recDRaWIeCud8xcKomghNi$YBCuVBwYLtsR5UWFe1EsoF3dqfc9IgdmOx4N/WJnmKI=','2024-03-27 14:47:45.767386',0,'masud.ahmed','Mohammad Masud','Ahmed','masud.ahmed@sats.com.sa',0,1,'2024-02-27 09:18:12.000000',NULL,NULL,1,'SSA10010034',5),(7,'pbkdf2_sha256$600000$BI5Xh2ioYb8hjd6f5ofLJG$SLQsZGo67yMQ2ylOtKSPWqCWyu95iTcVN9tgvL6lQsg=','2024-03-26 11:08:04.994315',0,'mohammed.asif','Mohammed','Asif','dmmfacilities@sats.com.sa',0,1,'2024-02-27 09:19:58.000000',NULL,NULL,1,'SSA10010053',5),(8,'Welcome2s',NULL,0,'shareefbm','Mohammed','Shareef','a@g.com',0,1,'2024-02-28 14:18:37.000000',NULL,NULL,2,'SSA1001003',NULL);
/*!40000 ALTER TABLE `accounts_customuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_customuser_groups`
--

DROP TABLE IF EXISTS `accounts_customuser_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_customuser_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `accounts_customuser_groups_customuser_id_group_id_c074bdcb_uniq` (`customuser_id`,`group_id`),
  KEY `accounts_customuser_groups_group_id_86ba5f9e_fk_auth_group_id` (`group_id`),
  CONSTRAINT `accounts_customuser__customuser_id_bc55088e_fk_accounts_` FOREIGN KEY (`customuser_id`) REFERENCES `accounts_customuser` (`id`),
  CONSTRAINT `accounts_customuser_groups_group_id_86ba5f9e_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_customuser_groups`
--

LOCK TABLES `accounts_customuser_groups` WRITE;
/*!40000 ALTER TABLE `accounts_customuser_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_customuser_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_customuser_user_permissions`
--

DROP TABLE IF EXISTS `accounts_customuser_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_customuser_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `accounts_customuser_user_customuser_id_permission_9632a709_uniq` (`customuser_id`,`permission_id`),
  KEY `accounts_customuser__permission_id_aea3d0e5_fk_auth_perm` (`permission_id`),
  CONSTRAINT `accounts_customuser__customuser_id_0deaefae_fk_accounts_` FOREIGN KEY (`customuser_id`) REFERENCES `accounts_customuser` (`id`),
  CONSTRAINT `accounts_customuser__permission_id_aea3d0e5_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_customuser_user_permissions`
--

LOCK TABLES `accounts_customuser_user_permissions` WRITE;
/*!40000 ALTER TABLE `accounts_customuser_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_customuser_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_department`
--

DROP TABLE IF EXISTS `accounts_department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_department` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `Name` varchar(30) NOT NULL,
  `Dept_Head_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `accounts_department_Dept_Head_id_718db190_fk_accounts_` (`Dept_Head_id`),
  CONSTRAINT `accounts_department_Dept_Head_id_718db190_fk_accounts_` FOREIGN KEY (`Dept_Head_id`) REFERENCES `accounts_customuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_department`
--

LOCK TABLES `accounts_department` WRITE;
/*!40000 ALTER TABLE `accounts_department` DISABLE KEYS */;
INSERT INTO `accounts_department` VALUES (1,'IT',3),(2,'FACILITY & SERVICES',5);
/*!40000 ALTER TABLE `accounts_department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_profile`
--

DROP TABLE IF EXISTS `accounts_profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_profile` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `location` varchar(30) NOT NULL,
  `birth_date` date DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `accounts_profile_user_id_49a85d32_fk_accounts_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_customuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_profile`
--

LOCK TABLES `accounts_profile` WRITE;
/*!40000 ALTER TABLE `accounts_profile` DISABLE KEYS */;
INSERT INTO `accounts_profile` VALUES (1,'',NULL,1),(2,'',NULL,2),(3,'',NULL,3),(4,'',NULL,4),(5,'',NULL,5),(6,'',NULL,6),(7,'',NULL,7),(8,'',NULL,8);
/*!40000 ALTER TABLE `accounts_profile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_station`
--

DROP TABLE IF EXISTS `accounts_station`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_station` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `Name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_station`
--

LOCK TABLES `accounts_station` WRITE;
/*!40000 ALTER TABLE `accounts_station` DISABLE KEYS */;
INSERT INTO `accounts_station` VALUES (1,'DMM'),(2,'RUH'),(3,'JED');
/*!40000 ALTER TABLE `accounts_station` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=161 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add user',1,'add_customuser'),(2,'Can change user',1,'change_customuser'),(3,'Can delete user',1,'delete_customuser'),(4,'Can view user',1,'view_customuser'),(5,'Can add profile',2,'add_profile'),(6,'Can change profile',2,'change_profile'),(7,'Can delete profile',2,'delete_profile'),(8,'Can view profile',2,'view_profile'),(9,'Can add department',3,'add_department'),(10,'Can change department',3,'change_department'),(11,'Can delete department',3,'delete_department'),(12,'Can view department',3,'view_department'),(13,'Can add station',4,'add_station'),(14,'Can change station',4,'change_station'),(15,'Can delete station',4,'delete_station'),(16,'Can view station',4,'view_station'),(17,'Can add log entry',5,'add_logentry'),(18,'Can change log entry',5,'change_logentry'),(19,'Can delete log entry',5,'delete_logentry'),(20,'Can view log entry',5,'view_logentry'),(21,'Can add permission',6,'add_permission'),(22,'Can change permission',6,'change_permission'),(23,'Can delete permission',6,'delete_permission'),(24,'Can view permission',6,'view_permission'),(25,'Can add group',7,'add_group'),(26,'Can change group',7,'change_group'),(27,'Can delete group',7,'delete_group'),(28,'Can view group',7,'view_group'),(29,'Can add content type',8,'add_contenttype'),(30,'Can change content type',8,'change_contenttype'),(31,'Can delete content type',8,'delete_contenttype'),(32,'Can view content type',8,'view_contenttype'),(33,'Can add session',9,'add_session'),(34,'Can change session',9,'change_session'),(35,'Can delete session',9,'delete_session'),(36,'Can view session',9,'view_session'),(37,'Can add general question',10,'add_generalquestion'),(38,'Can change general question',10,'change_generalquestion'),(39,'Can delete general question',10,'delete_generalquestion'),(40,'Can view general question',10,'view_generalquestion'),(41,'Can add checklist details',11,'add_checklistdetails'),(42,'Can change checklist details',11,'change_checklistdetails'),(43,'Can delete checklist details',11,'delete_checklistdetails'),(44,'Can view checklist details',11,'view_checklistdetails'),(45,'Can add sub question response',12,'add_subquestionresponse'),(46,'Can change sub question response',12,'change_subquestionresponse'),(47,'Can delete sub question response',12,'delete_subquestionresponse'),(48,'Can view sub question response',12,'view_subquestionresponse'),(49,'Can add gen question response',13,'add_genquestionresponse'),(50,'Can change gen question response',13,'change_genquestionresponse'),(51,'Can delete gen question response',13,'delete_genquestionresponse'),(52,'Can view gen question response',13,'view_genquestionresponse'),(53,'Can add fuel',14,'add_fuel'),(54,'Can change fuel',14,'change_fuel'),(55,'Can delete fuel',14,'delete_fuel'),(56,'Can view fuel',14,'view_fuel'),(57,'Can add workpermit',15,'add_workpermit'),(58,'Can change workpermit',15,'change_workpermit'),(59,'Can delete workpermit',15,'delete_workpermit'),(60,'Can view workpermit',15,'view_workpermit'),(61,'Can add excel file',16,'add_excelfile'),(62,'Can change excel file',16,'change_excelfile'),(63,'Can delete excel file',16,'delete_excelfile'),(64,'Can view excel file',16,'view_excelfile'),(65,'Can add equipment',17,'add_equipment'),(66,'Can change equipment',17,'change_equipment'),(67,'Can delete equipment',17,'delete_equipment'),(68,'Can view equipment',17,'view_equipment'),(69,'Can add equipment specific question',18,'add_equipmentspecificquestion'),(70,'Can change equipment specific question',18,'change_equipmentspecificquestion'),(71,'Can delete equipment specific question',18,'delete_equipmentspecificquestion'),(72,'Can view equipment specific question',18,'view_equipmentspecificquestion'),(73,'Can add nature of injury',19,'add_natureofinjury'),(74,'Can change nature of injury',19,'change_natureofinjury'),(75,'Can delete nature of injury',19,'delete_natureofinjury'),(76,'Can view nature of injury',19,'view_natureofinjury'),(77,'Can add incident',20,'add_incident'),(78,'Can change incident',20,'change_incident'),(79,'Can delete incident',20,'delete_incident'),(80,'Can view incident',20,'view_incident'),(81,'Can add expense',21,'add_expense'),(82,'Can change expense',21,'change_expense'),(83,'Can delete expense',21,'delete_expense'),(84,'Can view expense',21,'view_expense'),(85,'Can add expense item',22,'add_expenseitem'),(86,'Can change expense item',22,'change_expenseitem'),(87,'Can delete expense item',22,'delete_expenseitem'),(88,'Can view expense item',22,'view_expenseitem'),(89,'Can add travel claim',23,'add_travelclaim'),(90,'Can change travel claim',23,'change_travelclaim'),(91,'Can delete travel claim',23,'delete_travelclaim'),(92,'Can view travel claim',23,'view_travelclaim'),(93,'Can add it_ brand',24,'add_it_brand'),(94,'Can change it_ brand',24,'change_it_brand'),(95,'Can delete it_ brand',24,'delete_it_brand'),(96,'Can view it_ brand',24,'view_it_brand'),(97,'Can add it_ category',25,'add_it_category'),(98,'Can change it_ category',25,'change_it_category'),(99,'Can delete it_ category',25,'delete_it_category'),(100,'Can view it_ category',25,'view_it_category'),(101,'Can add it_ device_ status',26,'add_it_device_status'),(102,'Can change it_ device_ status',26,'change_it_device_status'),(103,'Can delete it_ device_ status',26,'delete_it_device_status'),(104,'Can view it_ device_ status',26,'view_it_device_status'),(105,'Can add it_ prodcuts',27,'add_it_prodcuts'),(106,'Can change it_ prodcuts',27,'change_it_prodcuts'),(107,'Can delete it_ prodcuts',27,'delete_it_prodcuts'),(108,'Can view it_ prodcuts',27,'view_it_prodcuts'),(109,'Can add allocation_status',28,'add_allocation_status'),(110,'Can change allocation_status',28,'change_allocation_status'),(111,'Can delete allocation_status',28,'delete_allocation_status'),(112,'Can view allocation_status',28,'view_allocation_status'),(113,'Can add it asset allocation',29,'add_itassetallocation'),(114,'Can change it asset allocation',29,'change_itassetallocation'),(115,'Can delete it asset allocation',29,'delete_itassetallocation'),(116,'Can view it asset allocation',29,'view_itassetallocation'),(117,'Can add custom history',30,'add_customhistory'),(118,'Can change custom history',30,'change_customhistory'),(119,'Can delete custom history',30,'delete_customhistory'),(120,'Can view custom history',30,'view_customhistory'),(121,'Can add in_ body parts',31,'add_in_bodyparts'),(122,'Can change in_ body parts',31,'change_in_bodyparts'),(123,'Can delete in_ body parts',31,'delete_in_bodyparts'),(124,'Can view in_ body parts',31,'view_in_bodyparts'),(125,'Can add in_ category',32,'add_in_category'),(126,'Can change in_ category',32,'change_in_category'),(127,'Can delete in_ category',32,'delete_in_category'),(128,'Can view in_ category',32,'view_in_category'),(129,'Can add in_ incident type',33,'add_in_incidenttype'),(130,'Can change in_ incident type',33,'change_in_incidenttype'),(131,'Can delete in_ incident type',33,'delete_in_incidenttype'),(132,'Can view in_ incident type',33,'view_in_incidenttype'),(133,'Can add in_ nature of injury',34,'add_in_natureofinjury'),(134,'Can change in_ nature of injury',34,'change_in_natureofinjury'),(135,'Can delete in_ nature of injury',34,'delete_in_natureofinjury'),(136,'Can view in_ nature of injury',34,'view_in_natureofinjury'),(137,'Can add in_ surface condition',35,'add_in_surfacecondition'),(138,'Can change in_ surface condition',35,'change_in_surfacecondition'),(139,'Can delete in_ surface condition',35,'delete_in_surfacecondition'),(140,'Can view in_ surface condition',35,'view_in_surfacecondition'),(141,'Can add in_ visibility',36,'add_in_visibility'),(142,'Can change in_ visibility',36,'change_in_visibility'),(143,'Can delete in_ visibility',36,'delete_in_visibility'),(144,'Can view in_ visibility',36,'view_in_visibility'),(145,'Can add whether condition',37,'add_whethercondition'),(146,'Can change whether condition',37,'change_whethercondition'),(147,'Can delete whether condition',37,'delete_whethercondition'),(148,'Can view whether condition',37,'view_whethercondition'),(149,'Can add in_ incidents',38,'add_in_incidents'),(150,'Can change in_ incidents',38,'change_in_incidents'),(151,'Can delete in_ incidents',38,'delete_in_incidents'),(152,'Can view in_ incidents',38,'view_in_incidents'),(153,'Can add employeesinvolved',39,'add_employeesinvolved'),(154,'Can change employeesinvolved',39,'change_employeesinvolved'),(155,'Can delete employeesinvolved',39,'delete_employeesinvolved'),(156,'Can view employeesinvolved',39,'view_employeesinvolved'),(157,'Can add driver involved',40,'add_driverinvolved'),(158,'Can change driver involved',40,'change_driverinvolved'),(159,'Can delete driver involved',40,'delete_driverinvolved'),(160,'Can view driver involved',40,'view_driverinvolved');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_accounts_customuser_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_accounts_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_customuser` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2024-02-26 17:45:30.909627','1','dmm',1,'[{\"added\": {}}]',4,2),(2,'2024-02-26 17:45:40.470681','3','ajmal ummer',1,'[{\"added\": {}}]',1,2),(3,'2024-02-27 08:57:12.882903','2','RUH',1,'[{\"added\": {}}]',4,2),(4,'2024-02-27 08:57:18.133152','3','JED',1,'[{\"added\": {}}]',4,2),(5,'2024-02-27 08:58:53.856453','4','lazim mohammed',1,'[{\"added\": {}}]',1,2),(6,'2024-02-27 09:00:31.979968','1','DMM',2,'[{\"changed\": {\"fields\": [\"Name\"]}}]',4,2),(7,'2024-02-27 09:00:51.139921','3','Ajmal Ummer',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\"]}}]',1,2),(8,'2024-02-27 09:18:06.195617','5','Hassan Rana',1,'[{\"added\": {}}]',1,2),(9,'2024-02-27 09:19:45.416438','6','Mohammad Masud Ahmed',1,'[{\"added\": {}}]',1,2),(10,'2024-02-27 09:23:48.136342','7','Mohammed Asif',1,'[{\"added\": {}}]',1,2),(11,'2024-02-27 09:24:06.783624','1','HP',1,'[{\"added\": {}}]',24,2),(12,'2024-02-27 09:24:13.900484','2','Dell',1,'[{\"added\": {}}]',24,2),(13,'2024-02-27 09:24:21.116340','3','Lenovo',1,'[{\"added\": {}}]',24,2),(14,'2024-02-27 09:24:28.954303','4','Xerox',1,'[{\"added\": {}}]',24,2),(15,'2024-02-27 09:25:08.147394','1','Computer',1,'[{\"added\": {}}]',25,2),(16,'2024-02-27 09:25:17.342987','2','Laptop',1,'[{\"added\": {}}]',25,2),(17,'2024-02-27 09:25:26.210905','3','Printer',1,'[{\"added\": {}}]',25,2),(18,'2024-02-27 09:25:31.223937','4','CCTV',1,'[{\"added\": {}}]',25,2),(19,'2024-02-27 09:25:43.472418','5','Monitor',1,'[{\"added\": {}}]',25,2),(20,'2024-02-27 09:26:00.602624','4','CCTV Cameras',2,'[{\"changed\": {\"fields\": [\"Category\"]}}]',25,2),(21,'2024-02-27 09:26:14.119966','6','IP Phones',1,'[{\"added\": {}}]',25,2),(22,'2024-02-27 09:31:48.679822','1','active',1,'[{\"added\": {}}]',26,2),(23,'2024-02-27 09:31:55.162859','2','inactive',1,'[{\"added\": {}}]',26,2),(24,'2024-02-27 09:32:03.667101','3','Obsolute',1,'[{\"added\": {}}]',26,2),(25,'2024-02-27 09:32:15.244171','4','Damaged',1,'[{\"added\": {}}]',26,2),(26,'2024-02-27 09:32:22.225970','2','Inactive',2,'[{\"changed\": {\"fields\": [\"Status\"]}}]',26,2),(27,'2024-02-27 09:32:28.942033','1','Active',2,'[{\"changed\": {\"fields\": [\"Status\"]}}]',26,2),(28,'2024-02-27 09:40:41.247023','1','IT',1,'[{\"added\": {}}]',3,2),(29,'2024-02-27 09:41:05.027124','2','FACILITY & SERVICES',1,'[{\"added\": {}}]',3,2),(30,'2024-02-28 10:24:05.730498','6','Mohammad Masud Ahmed',2,'[{\"changed\": {\"fields\": [\"Email address\"]}}]',1,2),(31,'2024-02-28 10:24:31.684825','7','Mohammed Asif',2,'[{\"changed\": {\"fields\": [\"Email address\"]}}]',1,2),(32,'2024-02-28 12:09:49.362161','7','Mohammed Asif',2,'[]',1,2),(33,'2024-02-28 12:10:53.298891','7','Mohammed Asif',2,'[{\"changed\": {\"fields\": [\"Password\"]}}]',1,2),(34,'2024-02-28 14:19:31.646554','8','Mohammed Shareef',1,'[{\"added\": {}}]',1,2),(35,'2024-02-28 14:19:42.084036','3','Ajmal Ummer',2,'[{\"changed\": {\"fields\": [\"Manager\"]}}]',1,2),(36,'2024-02-28 14:45:01.854565','7','Mohammed Asif',2,'[{\"changed\": {\"fields\": [\"Email address\"]}}]',1,2),(37,'2024-02-29 12:59:49.052685','7','Mohammed Asif',2,'[]',1,2);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'accounts','customuser'),(3,'accounts','department'),(2,'accounts','profile'),(4,'accounts','station'),(5,'admin','logentry'),(7,'auth','group'),(6,'auth','permission'),(8,'contenttypes','contenttype'),(28,'itassets','allocation_status'),(30,'itassets','customhistory'),(24,'itassets','it_brand'),(25,'itassets','it_category'),(26,'itassets','it_device_status'),(27,'itassets','it_prodcuts'),(29,'itassets','itassetallocation'),(21,'pettycash','expense'),(22,'pettycash','expenseitem'),(23,'pettycash','travelclaim'),(11,'polls','checklistdetails'),(17,'polls','equipment'),(18,'polls','equipmentspecificquestion'),(16,'polls','excelfile'),(14,'polls','fuel'),(10,'polls','generalquestion'),(13,'polls','genquestionresponse'),(20,'polls','incident'),(19,'polls','natureofinjury'),(12,'polls','subquestionresponse'),(15,'polls','workpermit'),(40,'quality','driverinvolved'),(39,'quality','employeesinvolved'),(31,'quality','in_bodyparts'),(32,'quality','in_category'),(38,'quality','in_incidents'),(33,'quality','in_incidenttype'),(34,'quality','in_natureofinjury'),(35,'quality','in_surfacecondition'),(36,'quality','in_visibility'),(37,'quality','whethercondition'),(9,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=269 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'polls','0001_initial','2024-02-25 17:05:53.867063'),(2,'polls','0002_checklistdetails_subquestionresponse_and_more','2024-02-25 17:05:54.032897'),(3,'contenttypes','0001_initial','2024-02-25 17:05:54.070337'),(4,'contenttypes','0002_remove_content_type_name','2024-02-25 17:05:54.100331'),(5,'auth','0001_initial','2024-02-25 17:05:54.261763'),(6,'auth','0002_alter_permission_name_max_length','2024-02-25 17:05:54.286853'),(7,'auth','0003_alter_user_email_max_length','2024-02-25 17:05:54.286853'),(8,'auth','0004_alter_user_username_opts','2024-02-25 17:05:54.286853'),(9,'auth','0005_alter_user_last_login_null','2024-02-25 17:05:54.299242'),(10,'auth','0006_require_contenttypes_0002','2024-02-25 17:05:54.301330'),(11,'auth','0007_alter_validators_add_error_messages','2024-02-25 17:05:54.301330'),(12,'auth','0008_alter_user_username_max_length','2024-02-25 17:05:54.301330'),(13,'auth','0009_alter_user_last_name_max_length','2024-02-25 17:05:54.301330'),(14,'auth','0010_alter_group_name_max_length','2024-02-25 17:05:54.315887'),(15,'auth','0011_update_proxy_permissions','2024-02-25 17:05:54.318087'),(16,'auth','0012_alter_user_first_name_max_length','2024-02-25 17:05:54.318087'),(17,'accounts','0001_initial','2024-02-25 17:05:54.497610'),(18,'polls','0003_alter_checklistdetails_user','2024-02-25 17:05:54.628363'),(19,'polls','0004_checklistdetails_time','2024-02-25 17:05:54.633363'),(20,'polls','0005_subject_brand_subject_capacity_and_more','2024-02-25 17:05:54.699290'),(21,'polls','0006_station_alter_checklistdetails_time','2024-02-25 17:05:54.700491'),(22,'polls','0007_subject_station_name_alter_checklistdetails_time','2024-02-25 17:05:54.767469'),(23,'polls','0008_alter_checklistdetails_time','2024-02-25 17:05:54.767469'),(24,'polls','0009_alter_checklistdetails_time','2024-02-25 17:05:54.767469'),(25,'polls','0010_alter_checklistdetails_time_and_more','2024-02-25 17:05:54.833656'),(26,'polls','0011_fuel_alter_checklistdetails_time','2024-02-25 17:05:54.850855'),(27,'polls','0012_alter_checklistdetails_time','2024-02-25 17:05:54.850855'),(28,'polls','0013_subject_fueltype_alter_checklistdetails_time','2024-02-25 17:05:54.902663'),(29,'polls','0014_subjectspecificquestion_fueltype_and_more','2024-02-25 17:05:54.983628'),(30,'polls','0015_remove_subjectspecificquestion_subject_and_more','2024-02-25 17:05:55.090496'),(31,'polls','0016_alter_checklistdetails_time_and_more','2024-02-25 17:05:55.096497'),(32,'polls','0017_alter_checklistdetails_time','2024-02-25 17:05:55.102139'),(33,'polls','0018_alter_checklistdetails_time','2024-02-25 17:05:55.102139'),(34,'polls','0019_alter_checklistdetails_time','2024-02-25 17:05:55.102139'),(35,'polls','0020_alter_checklistdetails_time','2024-02-25 17:05:55.116044'),(36,'polls','0021_alter_checklistdetails_time','2024-02-25 17:05:55.116044'),(37,'polls','0022_alter_checklistdetails_time','2024-02-25 17:05:55.116044'),(38,'polls','0023_alter_checklistdetails_time','2024-02-25 17:05:55.116044'),(39,'polls','0024_alter_checklistdetails_time','2024-02-25 17:05:55.132729'),(40,'polls','0025_alter_checklistdetails_time','2024-02-25 17:05:55.132729'),(41,'polls','0026_alter_checklistdetails_time_workpermit','2024-02-25 17:05:55.184076'),(42,'polls','0027_alter_checklistdetails_time_delete_workpermit','2024-02-25 17:05:55.200227'),(43,'polls','0028_alter_checklistdetails_time_workpermit','2024-02-25 17:05:55.235798'),(44,'polls','0029_alter_checklistdetails_time_alter_subject_brand_and_more','2024-02-25 17:05:55.250988'),(45,'polls','0030_alter_checklistdetails_time_and_more','2024-02-25 17:05:55.250988'),(46,'polls','0031_alter_checklistdetails_time_and_more','2024-02-25 17:05:55.267472'),(47,'polls','0032_excelfile_alter_checklistdetails_time_and_more','2024-02-25 17:05:55.267472'),(48,'polls','0033_alter_checklistdetails_time_and_more','2024-02-25 17:05:55.282777'),(49,'polls','0034_alter_checklistdetails_time_and_more','2024-02-25 17:05:55.282777'),(50,'polls','0035_alter_checklistdetails_time_and_more','2024-02-25 17:05:55.333108'),(51,'polls','0036_alter_checklistdetails_time_and_more','2024-02-25 17:05:55.348614'),(52,'polls','0037_alter_checklistdetails_time_and_more','2024-02-25 17:05:55.351498'),(53,'polls','0038_alter_checklistdetails_time_and_more','2024-02-25 17:05:55.351498'),(54,'polls','0039_alter_checklistdetails_time_and_more','2024-02-25 17:05:55.365966'),(55,'polls','0040_alter_checklistdetails_time_and_more','2024-02-25 17:05:55.366708'),(56,'polls','0041_alter_checklistdetails_time_and_more','2024-02-25 17:05:55.366708'),(57,'polls','0042_alter_checklistdetails_time_and_more','2024-02-25 17:05:55.382720'),(58,'polls','0043_alter_checklistdetails_time_and_more','2024-02-25 17:05:55.382720'),(59,'polls','0044_alter_checklistdetails_time_and_more','2024-02-25 17:05:55.382720'),(60,'polls','0045_alter_checklistdetails_time_and_more','2024-02-25 17:05:55.399378'),(61,'polls','0046_alter_checklistdetails_time_and_more','2024-02-25 17:05:55.399378'),(62,'polls','0047_alter_checklistdetails_time_and_more','2024-02-25 17:05:55.399378'),(63,'polls','0048_alter_checklistdetails_time_and_more','2024-02-25 17:05:55.418077'),(64,'polls','0049_alter_checklistdetails_time_and_more','2024-02-25 17:05:55.418077'),(65,'polls','0050_alter_checklistdetails_time_and_more','2024-02-25 17:05:55.432404'),(66,'polls','0051_alter_checklistdetails_time_and_more','2024-02-25 17:05:55.433671'),(67,'polls','0052_alter_checklistdetails_time_and_more','2024-02-25 17:05:55.433671'),(68,'polls','0053_alter_checklistdetails_time_and_more','2024-02-25 17:05:55.449321'),(69,'polls','0054_alter_checklistdetails_time_and_more','2024-02-25 17:05:55.449321'),(70,'polls','0055_alter_checklistdetails_time_and_more','2024-02-25 17:05:55.449321'),(71,'polls','0056_alter_checklistdetails_time_and_more','2024-02-25 17:05:55.468029'),(72,'polls','0057_alter_checklistdetails_time_and_more','2024-02-25 17:05:55.468029'),(73,'polls','0058_alter_checklistdetails_time_and_more','2024-02-25 17:05:55.481577'),(74,'polls','0059_alter_checklistdetails_time_and_more','2024-02-25 17:05:55.484591'),(75,'polls','0060_alter_checklistdetails_time_and_more','2024-02-25 17:05:55.484591'),(76,'polls','0061_alter_checklistdetails_time_and_more','2024-02-25 17:05:55.499644'),(77,'polls','0062_alter_checklistdetails_time_and_more','2024-02-25 17:05:55.499644'),(78,'polls','0063_alter_checklistdetails_time_and_more','2024-02-25 17:05:55.499644'),(79,'polls','0064_alter_checklistdetails_time_and_more','2024-02-25 17:05:55.516275'),(80,'polls','0065_alter_checklistdetails_time_and_more','2024-02-25 17:05:55.516275'),(81,'polls','0066_alter_checklistdetails_time_and_more','2024-02-25 17:05:55.532458'),(82,'polls','0067_alter_checklistdetails_time_and_more','2024-02-25 17:05:55.532827'),(83,'polls','0068_alter_checklistdetails_time_and_more','2024-02-25 17:05:55.532827'),(84,'polls','0069_alter_checklistdetails_time_and_more','2024-02-25 17:05:55.549634'),(85,'polls','0070_alter_checklistdetails_time_and_more','2024-02-25 17:05:55.549634'),(86,'polls','0071_alter_checklistdetails_time_and_more','2024-02-25 17:05:55.549634'),(87,'polls','0072_alter_checklistdetails_time_and_more','2024-02-25 17:05:55.566144'),(88,'polls','0073_alter_checklistdetails_time_and_more','2024-02-25 17:05:55.566144'),(89,'polls','0074_alter_checklistdetails_time_and_more','2024-02-25 17:05:55.582966'),(90,'polls','0075_alter_checklistdetails_time_and_more','2024-02-25 17:05:55.583801'),(91,'polls','0076_alter_checklistdetails_time_and_more','2024-02-25 17:05:55.583801'),(92,'polls','0077_alter_checklistdetails_time_and_more','2024-02-25 17:05:55.599605'),(93,'polls','0078_alter_checklistdetails_time_and_more','2024-02-25 17:05:55.599605'),(94,'polls','0079_subjectspecificquestion_subject_and_more','2024-02-25 17:05:56.395925'),(95,'polls','0080_alter_checklistdetails_time_and_more','2024-02-25 17:05:56.395925'),(96,'accounts','0002_customuser_phone_number','2024-02-25 17:05:56.416233'),(97,'accounts','0003_alter_customuser_phone_number','2024-02-25 17:05:56.450223'),(98,'accounts','0004_profile','2024-02-25 17:05:56.501414'),(99,'accounts','0005_customuser_station_name','2024-02-25 17:05:56.549701'),(100,'accounts','0006_alter_customuser_station_name','2024-02-25 17:05:56.600021'),(101,'accounts','0007_customuser_employee_id','2024-02-25 17:05:56.618600'),(102,'accounts','0008_alter_customuser_employee_id','2024-02-25 17:05:56.683506'),(103,'accounts','0009_customuser_manager','2024-02-25 17:05:56.718698'),(104,'accounts','0010_alter_customuser_manager','2024-02-25 17:05:56.718698'),(105,'accounts','0011_alter_customuser_station_name','2024-02-25 17:05:56.799885'),(106,'accounts','0012_department','2024-02-25 17:05:56.799885'),(107,'accounts','0013_department_dept_head','2024-02-25 17:05:56.835484'),(108,'accounts','0014_station','2024-02-25 17:05:56.835484'),(109,'accounts','0015_alter_customuser_station_name','2024-02-25 17:05:56.900836'),(110,'admin','0001_initial','2024-02-25 17:05:56.981374'),(111,'admin','0002_logentry_remove_auto_add','2024-02-25 17:05:56.986695'),(112,'admin','0003_logentry_add_action_flag_choices','2024-02-25 17:05:56.990425'),(113,'itassets','0001_initial','2024-02-25 17:05:57.167484'),(114,'itassets','0002_it_prodcuts_asset_tag','2024-02-25 17:05:57.167484'),(115,'itassets','0003_alter_it_prodcuts_supplier_and_more','2024-02-25 17:05:57.253599'),(116,'itassets','0004_alter_it_prodcuts_model','2024-02-25 17:05:57.283907'),(117,'itassets','0005_allocation_status_it_prodcuts_allocation_status','2024-02-25 17:05:57.332501'),(118,'itassets','0006_it_prodcuts_station_name','2024-02-25 17:05:57.391060'),(119,'itassets','0007_it_prodcuts_created_date','2024-02-25 17:05:57.399198'),(120,'itassets','0008_it_prodcuts_file','2024-02-25 17:05:57.427370'),(121,'itassets','0009_alter_it_prodcuts_file','2024-02-25 17:05:57.465756'),(122,'itassets','0010_it_prodcuts_image','2024-02-25 17:05:57.485937'),(123,'itassets','0011_alter_it_prodcuts_file_itassetallocation','2024-02-25 17:05:57.616503'),(124,'itassets','0012_itassetallocation_deallocation_date','2024-02-25 17:05:57.632177'),(125,'itassets','0013_alter_itassetallocation_allocation_date','2024-02-25 17:05:57.667665'),(126,'itassets','0014_it_prodcuts_current_allocation','2024-02-25 17:05:57.716060'),(127,'itassets','0015_alter_itassetallocation_allocation_date','2024-02-25 17:05:57.716060'),(128,'itassets','0016_alter_itassetallocation_allocation_date','2024-02-25 17:05:57.716060'),(129,'itassets','0017_alter_itassetallocation_allocation_date','2024-02-25 17:05:57.734141'),(130,'itassets','0018_alter_it_prodcuts_allocation_status','2024-02-25 17:05:57.881556'),(131,'itassets','0019_alter_it_prodcuts_station_name','2024-02-25 17:05:57.937722'),(132,'itassets','0020_alter_it_prodcuts_created_date_and_more','2024-02-25 17:05:58.002075'),(133,'itassets','0021_alter_it_prodcuts_created_date','2024-02-25 17:05:58.002075'),(134,'itassets','0022_alter_it_prodcuts_image','2024-02-25 17:05:58.002075'),(135,'itassets','0023_alter_it_prodcuts_created_date','2024-02-25 17:05:58.017586'),(136,'itassets','0024_it_prodcuts_asset_remarks','2024-02-25 17:05:58.032075'),(137,'itassets','0025_historicalit_prodcuts','2024-02-25 17:05:58.145506'),(138,'itassets','0026_customhistory','2024-02-25 17:05:58.182774'),(139,'itassets','0027_natureofinjury_and_more','2024-02-25 17:05:58.201140'),(140,'itassets','0028_delete_natureofinjury','2024-02-25 17:05:58.201140'),(141,'itassets','0029_alter_historicalit_prodcuts_created_date_and_more','2024-02-25 17:05:58.219912'),(142,'itassets','0030_delete_historicalit_prodcuts','2024-02-25 17:05:58.229995'),(143,'itassets','0031_alter_it_prodcuts_created_date','2024-02-25 17:05:58.234947'),(144,'itassets','0032_alter_it_prodcuts_created_date','2024-02-25 17:05:58.234947'),(145,'itassets','0033_alter_it_prodcuts_created_date','2024-02-25 17:05:58.234947'),(146,'pettycash','0001_initial','2024-02-25 17:05:58.316980'),(147,'pettycash','0002_alter_expense_employee_delete_employee','2024-02-25 17:05:58.364429'),(148,'pettycash','0003_alter_expense_total_amount','2024-02-25 17:05:58.368646'),(149,'pettycash','0004_alter_expense_total_amount','2024-02-25 17:05:58.368646'),(150,'pettycash','0005_alter_expense_total_amount','2024-02-25 17:05:58.383111'),(151,'pettycash','0006_expense_claimant_alter_expense_date','2024-02-25 17:05:58.401196'),(152,'pettycash','0007_alter_expense_claimant','2024-02-25 17:05:58.401196'),(153,'pettycash','0008_expense_station_name','2024-02-25 17:05:58.449827'),(154,'pettycash','0009_alter_expense_station_name','2024-02-25 17:05:58.543835'),(155,'pettycash','0010_travelclaim','2024-02-25 17:05:58.633800'),(156,'pettycash','0011_alter_travelclaim_upload_bill','2024-02-25 17:05:58.665998'),(157,'pettycash','0012_alter_travelclaim_accommodation_and_more','2024-02-25 17:05:58.683948'),(158,'pettycash','0013_remove_travelclaim_station','2024-02-25 17:05:58.721228'),(159,'pettycash','0014_travelclaim_total_amount','2024-02-25 17:05:58.739597'),(160,'pettycash','0015_alter_travelclaim_total_amount','2024-02-25 17:05:58.739597'),(161,'pettycash','0016_travelclaim_status','2024-02-25 17:05:58.755254'),(162,'pettycash','0017_alter_travelclaim_status','2024-02-25 17:05:58.789376'),(163,'pettycash','0018_travelclaim_approved_date','2024-02-25 17:05:58.804365'),(164,'pettycash','0019_travelclaim_created_date','2024-02-25 17:05:58.818045'),(165,'pettycash','0020_alter_travelclaim_created_date','2024-02-25 17:05:58.818045'),(166,'pettycash','0021_alter_travelclaim_approved_date_and_more','2024-02-25 17:05:58.835487'),(167,'pettycash','0022_alter_travelclaim_created_date','2024-02-25 17:05:58.835487'),(168,'pettycash','0023_expense_approved_status_and_more','2024-02-25 17:05:58.865416'),(169,'pettycash','0024_expense_upload_bill_alter_travelclaim_created_date','2024-02-25 17:05:58.884778'),(170,'pettycash','0025_expense_approved_date_alter_travelclaim_created_date','2024-02-25 17:05:58.901196'),(171,'pettycash','0026_alter_travelclaim_created_date','2024-02-25 17:05:58.901196'),(172,'pettycash','0027_alter_travelclaim_created_date','2024-02-25 17:05:58.917399'),(173,'pettycash','0028_alter_travelclaim_created_date','2024-02-25 17:05:58.919314'),(174,'pettycash','0029_alter_travelclaim_created_date','2024-02-25 17:05:58.919314'),(175,'pettycash','0030_alter_travelclaim_created_date','2024-02-25 17:05:58.934195'),(176,'pettycash','0031_alter_expense_date_alter_travelclaim_created_date','2024-02-25 17:05:58.934195'),(177,'pettycash','0032_alter_expense_date_alter_travelclaim_created_date','2024-02-25 17:05:58.984751'),(178,'pettycash','0033_alter_expense_date_alter_travelclaim_created_date_and_more','2024-02-25 17:05:59.049592'),(179,'pettycash','0034_alter_expense_date_alter_travelclaim_created_date','2024-02-25 17:05:59.066423'),(180,'pettycash','0035_alter_expense_date_alter_travelclaim_created_date','2024-02-25 17:05:59.074615'),(181,'pettycash','0036_remove_travelclaim_approved_date_and_more','2024-02-25 17:05:59.133760'),(182,'pettycash','0037_travelclaim_end_date_travelclaim_start_date','2024-02-25 17:05:59.149930'),(183,'pettycash','0038_travelclaim_approved_date','2024-02-25 17:05:59.167774'),(184,'pettycash','0039_alter_expense_station_name','2024-02-25 17:05:59.217554'),(185,'pettycash','0040_alter_travelclaim_status','2024-02-25 17:05:59.217554'),(186,'pettycash','0041_alter_travelclaim_status','2024-02-25 17:05:59.252065'),(187,'pettycash','0042_alter_travelclaim_end_date_and_more','2024-02-25 17:05:59.385801'),(188,'polls','0081_alter_checklistdetails_time_and_more','2024-02-25 17:05:59.400675'),(189,'polls','0082_alter_checklistdetails_time_and_more','2024-02-25 17:05:59.406738'),(190,'polls','0083_alter_checklistdetails_time_and_more','2024-02-25 17:05:59.417848'),(191,'polls','0084_alter_checklistdetails_time_and_more','2024-02-25 17:05:59.417848'),(192,'polls','0085_alter_checklistdetails_time_and_more','2024-02-25 17:05:59.434928'),(193,'polls','0086_alter_checklistdetails_time_and_more','2024-02-25 17:05:59.434928'),(194,'polls','0087_alter_checklistdetails_time_and_more','2024-02-25 17:05:59.450707'),(195,'polls','0088_alter_checklistdetails_time_and_more','2024-02-25 17:05:59.450707'),(196,'polls','0089_alter_checklistdetails_time_and_more','2024-02-25 17:05:59.467343'),(197,'polls','0090_alter_checklistdetails_time_and_more','2024-02-25 17:05:59.467343'),(198,'polls','0091_alter_checklistdetails_time_and_more','2024-02-25 17:05:59.483950'),(199,'polls','0092_alter_checklistdetails_time_and_more','2024-02-25 17:05:59.483950'),(200,'polls','0093_alter_checklistdetails_time_and_more','2024-02-25 17:05:59.501061'),(201,'polls','0094_alter_checklistdetails_time_and_more','2024-02-25 17:05:59.568850'),(202,'polls','0095_alter_checklistdetails_time_and_more','2024-02-25 17:05:59.730653'),(203,'polls','0096_alter_checklistdetails_equipment_and_more','2024-02-25 17:05:59.832323'),(204,'polls','0097_alter_checklistdetails_time_and_more','2024-02-25 17:05:59.899174'),(205,'polls','0098_alter_checklistdetails_time_and_more','2024-02-25 17:05:59.951372'),(206,'polls','0099_alter_checklistdetails_time_and_more','2024-02-25 17:05:59.965944'),(207,'polls','0100_alter_checklistdetails_time_and_more','2024-02-25 17:05:59.983859'),(208,'polls','0101_alter_checklistdetails_time_and_more','2024-02-25 17:06:00.049524'),(209,'polls','0102_alter_checklistdetails_time_and_more','2024-02-25 17:06:00.049524'),(210,'polls','0103_alter_checklistdetails_time_and_more','2024-02-25 17:06:00.067280'),(211,'polls','0104_alter_checklistdetails_time_and_more','2024-02-25 17:06:00.083022'),(212,'polls','0105_alter_checklistdetails_time_and_more','2024-02-25 17:06:00.084195'),(213,'polls','0106_alter_checklistdetails_time_and_more','2024-02-25 17:06:00.100722'),(214,'polls','0107_alter_checklistdetails_time_and_more','2024-02-25 17:06:00.100722'),(215,'polls','0108_alter_checklistdetails_time_and_more','2024-02-25 17:06:00.117270'),(216,'polls','0109_alter_checklistdetails_time_and_more','2024-02-25 17:06:00.132966'),(217,'polls','0110_alter_checklistdetails_time_and_more','2024-02-25 17:06:00.132966'),(218,'polls','0111_alter_checklistdetails_time_and_more','2024-02-25 17:06:00.150761'),(219,'polls','0112_natureofinjury_alter_checklistdetails_time_and_more','2024-02-25 17:06:00.267887'),(220,'polls','0113_alter_checklistdetails_time_and_more','2024-02-25 17:06:00.285158'),(221,'polls','0114_alter_checklistdetails_time_and_more','2024-02-25 17:06:00.285158'),(222,'polls','0115_alter_checklistdetails_time_and_more','2024-02-25 17:06:00.300646'),(223,'polls','0116_alter_checklistdetails_time_and_more','2024-02-25 17:06:00.317498'),(224,'polls','0117_alter_checklistdetails_time_and_more','2024-02-25 17:06:00.317498'),(225,'polls','0118_alter_checklistdetails_time_and_more','2024-02-25 17:06:00.334117'),(226,'polls','0119_alter_checklistdetails_time_and_more','2024-02-25 17:06:00.350033'),(227,'polls','0120_alter_checklistdetails_time_and_more','2024-02-25 17:06:00.350674'),(228,'polls','0121_alter_checklistdetails_time_and_more','2024-02-25 17:06:00.367694'),(229,'polls','0122_alter_checklistdetails_time_and_more','2024-02-25 17:06:00.382950'),(230,'polls','0123_alter_checklistdetails_time_and_more','2024-02-25 17:06:00.384210'),(231,'polls','0124_alter_checklistdetails_time_and_more','2024-02-25 17:06:00.449638'),(232,'polls','0125_alter_checklistdetails_time_and_more','2024-02-25 17:06:00.472387'),(233,'polls','0126_alter_checklistdetails_time_and_more','2024-02-25 17:06:00.482402'),(234,'polls','0127_alter_checklistdetails_time_and_more','2024-02-25 17:06:00.482402'),(235,'polls','0128_alter_checklistdetails_time_and_more','2024-02-25 17:06:00.499638'),(236,'polls','0129_alter_checklistdetails_time_and_more','2024-02-25 17:06:00.499638'),(237,'polls','0130_alter_checklistdetails_time_and_more','2024-02-25 17:06:00.517621'),(238,'polls','0131_alter_checklistdetails_time_and_more','2024-02-25 17:06:00.534186'),(239,'polls','0132_alter_checklistdetails_time_and_more','2024-02-25 17:06:00.534186'),(240,'polls','0133_alter_checklistdetails_time_and_more','2024-02-25 17:06:00.549431'),(241,'polls','0134_alter_checklistdetails_time_and_more','2024-02-25 17:06:00.566276'),(242,'polls','0135_alter_checklistdetails_time_and_more','2024-02-25 17:06:00.566276'),(243,'quality','0001_initial','2024-02-25 17:06:00.616447'),(244,'quality','0002_in_incidents','2024-02-25 17:06:00.827911'),(245,'quality','0003_employeesinvolved','2024-02-25 17:06:00.836937'),(246,'quality','0004_in_incidents_employees','2024-02-25 17:06:00.923116'),(247,'quality','0005_remove_in_incidents_employees','2024-02-25 17:06:00.933123'),(248,'quality','0006_in_incidents_employees','2024-02-25 17:06:01.032929'),(249,'quality','0007_driverinvolved_employeesinvolved_designation_and_more','2024-02-25 17:06:01.181281'),(250,'quality','0008_rename_employees_in_incidents_driver_name_and_more','2024-02-25 17:06:01.286959'),(251,'quality','0009_in_incidents_bodyparts_affected_and_more','2024-02-25 17:06:01.507139'),(252,'quality','0010_in_incidents_summary','2024-02-25 17:06:01.532174'),(253,'quality','0011_in_incidents_contributory_factors_and_more','2024-02-25 17:06:01.667693'),(254,'quality','0012_alter_in_incidents_summary_and_more','2024-02-25 17:06:01.694033'),(255,'quality','0013_in_incidents_created_date','2024-02-25 17:06:01.715564'),(256,'sessions','0001_initial','2024-02-25 17:06:01.731979'),(257,'user_management','0001_initial','2024-02-25 17:06:01.930628'),(258,'user_management','0002_delete_customuser','2024-02-25 17:06:01.962875'),(259,'polls','0136_alter_checklistdetails_time_and_more','2024-02-25 17:07:59.485914'),(260,'itassets','0034_alter_it_prodcuts_created_date','2024-02-26 17:37:20.088654'),(261,'polls','0137_alter_checklistdetails_time_and_more','2024-02-26 17:37:20.096470'),(262,'polls','0138_alter_checklistdetails_time_and_more','2024-02-26 17:37:20.114881'),(263,'accounts','0016_alter_customuser_employee_id','2024-02-27 08:59:51.812451'),(264,'itassets','0035_alter_it_prodcuts_created_date','2024-02-27 08:59:51.815523'),(265,'polls','0139_alter_checklistdetails_time_and_more','2024-02-27 08:59:51.832607'),(266,'itassets','0036_alter_it_prodcuts_created_date','2024-03-02 14:06:32.845346'),(267,'polls','0140_alter_checklistdetails_time_and_more','2024-03-02 14:06:32.859070'),(268,'polls','0141_workpermit_upload_iqama_alter_checklistdetails_time_and_more','2024-03-02 14:17:52.025201');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('4bdna14ppuev5fs6wev5d5zsluxumgyr','.eJxVjMsOwiAQRf-FtSE8BhCX7vsNhIFBqgaS0q6M_65NutDtPefcFwtxW2vYBi1hzuzCHDv9bhjTg9oO8j22W-ept3WZke8KP-jgU8_0vB7u30GNo35r4yxmjRYhKdJZU1HFiQjktVHFO8hWJQGSpHPCny2hFEZ4APRSFCrs_QHjpjd7:1rp1qm:bgLm1sLU1B-jrvA5Fp8qSnJJPBew8Vghpbwqe258k60','2024-04-09 11:08:04.998307'),('5k6qv0xmygy5yfav83cf3z8vv6t7hjzw','.eJxVjDsOwjAQRO_iGln-xNimpOcM1q53jQPIkeKkQtydREoBzRTz3sxbJFiXmtbOcxpJXMQgTr8dQn5y2wE9oN0nmae2zCPKXZEH7fI2Eb-uh_t3UKHXbR2y8qaQYybI1lhgDdltociVcwYLWkPRGFABcSQfLLrBW4pRBTQoPl8bZTkJ:1rermP:vb2du-UiJFdGZS4pkuP0K95B3sd1JHRgRCTAEwjN410','2024-03-12 10:21:33.080040'),('890eokdap6p9vk0guw8cyqdt6yo7dz5g','.eJxVjEEOwiAQRe8ya0NAYKgu3XsGMsxQqRpISrsy3l2bdKHb_977L4i0LiWuPc9xEjgDwuF3S8SPXDcgd6q3prjVZZ6S2hS1066uTfLzsrt_B4V6-daOCFmCdRgYjRUcfDh6JxI4M5NLgxZtGX0arSZNbkQ27E_ImawxBt4f7Zc4Hg:1rpRkv:nW3Jne0MjXg_xUuOS6-FKykL0R0SQHPkZ3zYuCL4ds4','2024-04-10 14:47:45.771146'),('anopmk3pkvjhew84pceobs1el7vnstzz','.eJxVjMsOgjAUBf-la9MU5Bbq0j3fQO6rFjVtQmFl_HclYaHbMzPnZSbc1jRtVZdpFnMxZ3P63Qj5oXkHcsd8K5ZLXpeZ7K7Yg1Y7FtHn9XD_DhLW9K1jHKjngN4JkIsNDYEUEAWQY8t9y0EbcSrQgYvcKYLXAEQhQvDkzfsDI0c5YA:1rffhV:jmkyCwtiilcpI-2J7XjG4DZ0kzkuYJpbqLRWcJu7iZ4','2024-03-14 15:39:49.731914'),('at636yluy18yluw1onz5wvvuhyw47zf7','.eJxVjDsOwjAQRO_iGln-xNimpOcM1q53jQPIkeKkQtydREoBzRTz3sxbJFiXmtbOcxpJXMQgTr8dQn5y2wE9oN0nmae2zCPKXZEH7fI2Eb-uh_t3UKHXbR2y8qaQYybI1lhgDdltociVcwYLWkPRGFABcSQfLLrBW4pRBTQoPl8bZTkJ:1rerPD:x-ptBMUiSDtHOhvwZM0vqgMSNJlVHy-Kn2IdsqoFJe4','2024-03-12 09:57:35.614926'),('ehd0jckv833aqcmo796y1oo1z74qozlv','.eJxVjMsOgjAUBf-la9MU5Bbq0j3fQO6rFjVtQmFl_HclYaHbMzPnZSbc1jRtVZdpFnMxZ3P63Qj5oXkHcsd8K5ZLXpeZ7K7Yg1Y7FtHn9XD_DhLW9K1jHKjngN4JkIsNDYEUEAWQY8t9y0EbcSrQgYvcKYLXAEQhQvDkzfsDI0c5YA:1rgmRE:hmCvaVxSu4S95lDYpXvGYvoRITL53whFEE-f-Xw-qc4','2024-03-17 17:03:36.486990'),('k1w7lzheto1ue0gp1gtm9zfczaoy6gkx','.eJxVjMsOgjAUBf-la9MU5Bbq0j3fQO6rFjVtQmFl_HclYaHbMzPnZSbc1jRtVZdpFnMxZ3P63Qj5oXkHcsd8K5ZLXpeZ7K7Yg1Y7FtHn9XD_DhLW9K1jHKjngN4JkIsNDYEUEAWQY8t9y0EbcSrQgYvcKYLXAEQhQvDkzfsDI0c5YA:1rjDlt:1VgEwuX9aRY6Df8R12h-_or9aLYjXpNqfcbSp94nSFA','2024-03-24 10:39:01.577810'),('kgbg8wvvbvxpse9e5oi9x02n3536hrd3','.eJxVjMsOgjAUBf-la9MU5Bbq0j3fQO6rFjVtQmFl_HclYaHbMzPnZSbc1jRtVZdpFnMxZ3P63Qj5oXkHcsd8K5ZLXpeZ7K7Yg1Y7FtHn9XD_DhLW9K1jHKjngN4JkIsNDYEUEAWQY8t9y0EbcSrQgYvcKYLXAEQhQvDkzfsDI0c5YA:1rfHqg:_AL1AFi_uB2fa7OJCMURCiXfQmh4oYSOQpgmf0QjBKE','2024-03-13 14:11:42.426665'),('njti5cmopk1931ao3moktxo92t3sy628','.eJxVjDsOwjAQRO_iGln-xNimpOcM1q53jQPIkeKkQtydREoBzRTz3sxbJFiXmtbOcxpJXMQgTr8dQn5y2wE9oN0nmae2zCPKXZEH7fI2Eb-uh_t3UKHXbR2y8qaQYybI1lhgDdltociVcwYLWkPRGFABcSQfLLrBW4pRBTQoPl8bZTkJ:1rfLLn:kWCxs2hxeXTxi4P3WTn9ESmwjAWJ8L8HueAdCZDpXfE','2024-03-13 17:56:03.014601'),('ofpu7olez4n8pl9hm0xjnvpybor9v4i1','.eJxVjMsOgjAUBf-la9MU5Bbq0j3fQO6rFjVtQmFl_HclYaHbMzPnZSbc1jRtVZdpFnMxZ3P63Qj5oXkHcsd8K5ZLXpeZ7K7Yg1Y7FtHn9XD_DhLW9K1jHKjngN4JkIsNDYEUEAWQY8t9y0EbcSrQgYvcKYLXAEQhQvDkzfsDI0c5YA:1rgkTD:iZwYQwe0dxzmy38D_B09RDfKTkYWLGI7BFTcuads6U4','2024-03-17 14:57:31.763162'),('qt9eoayfb9qvi65h1p9gdao94whqhvtp','.eJxVjMsOwiAQRf-FtSE8BhCX7vsNhIFBqgaS0q6M_65NutDtPefcFwtxW2vYBi1hzuzCHDv9bhjTg9oO8j22W-ept3WZke8KP-jgU8_0vB7u30GNo35r4yxmjRYhKdJZU1HFiQjktVHFO8hWJQGSpHPCny2hFEZ4APRSFCrs_QHjpjd7:1rmBfT:qOavnl9tIplp6F2JElu8wsm2VfuGHITWr1GMJmJkpEI','2024-04-01 15:00:39.708808'),('reocsofq6mg2hpuy73zlw2m4kiyse1lg','.eJxVjMsOgjAUBf-la9MU5Bbq0j3fQO6rFjVtQmFl_HclYaHbMzPnZSbc1jRtVZdpFnMxZ3P63Qj5oXkHcsd8K5ZLXpeZ7K7Yg1Y7FtHn9XD_DhLW9K1jHKjngN4JkIsNDYEUEAWQY8t9y0EbcSrQgYvcKYLXAEQhQvDkzfsDI0c5YA:1rgit5:kUJnKo6IXbDm4VN4L854j7GQbuonZ18Z9cHQac4HBxw','2024-03-17 13:16:07.107465'),('uwhwaklwd64ukovjmg4u1fwrxns591ql','.eJxVjMsOgjAUBf-la9MU5Bbq0j3fQO6rFjVtQmFl_HclYaHbMzPnZSbc1jRtVZdpFnMxZ3P63Qj5oXkHcsd8K5ZLXpeZ7K7Yg1Y7FtHn9XD_DhLW9K1jHKjngN4JkIsNDYEUEAWQY8t9y0EbcSrQgYvcKYLXAEQhQvDkzfsDI0c5YA:1rgNDy:pnSxy3X49e5qXlxcg9Xu6rrBNrMZbSSWIa_QRuNb09c','2024-03-16 14:08:14.879314'),('v9r1v3gz5nqz8cofq6ft9a8ppnu765mm','.eJxVjEEOwiAQRe8ya0NAYKgu3XsGMsxQqRpISrsy3l2bdKHb_977L4i0LiWuPc9xEjgDwuF3S8SPXDcgd6q3prjVZZ6S2hS1066uTfLzsrt_B4V6-daOCFmCdRgYjRUcfDh6JxI4M5NLgxZtGX0arSZNbkQ27E_ImawxBt4f7Zc4Hg:1rh4ed:ZTjAg9xGDmAoPxqIqHsUekFij12hESDbqByTtwCOqWU','2024-03-18 12:30:39.955310'),('wl0d8ubrfqrn1a9ihp7nzia17lwfvpgf','.eJxVjDsOwjAQRO_iGln-xNimpOcM1q53jQPIkeKkQtydREoBzRTz3sxbJFiXmtbOcxpJXMQgTr8dQn5y2wE9oN0nmae2zCPKXZEH7fI2Eb-uh_t3UKHXbR2y8qaQYybI1lhgDdltociVcwYLWkPRGFABcSQfLLrBW4pRBTQoPl8bZTkJ:1rfG4Q:qoOedDmZXFivceErfHmEzVCdWUVS7JPZ78uXKtqTDBo','2024-03-13 12:17:46.145461'),('wn2s5p5wanyekv1oyc5z658qps5t3v07','e30:1rey3f:ugp5SaO8Qab4mXCY3T3wEuWOMs_7pYhtoM8gWBJf1E8','2024-03-12 17:03:47.117299');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `itassets_allocation_status`
--

DROP TABLE IF EXISTS `itassets_allocation_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `itassets_allocation_status` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `status` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `itassets_allocation_status`
--

LOCK TABLES `itassets_allocation_status` WRITE;
/*!40000 ALTER TABLE `itassets_allocation_status` DISABLE KEYS */;
/*!40000 ALTER TABLE `itassets_allocation_status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `itassets_customhistory`
--

DROP TABLE IF EXISTS `itassets_customhistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `itassets_customhistory` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `timestamp` datetime(6) NOT NULL,
  `model_name` varchar(255) NOT NULL,
  `instance_id` int NOT NULL,
  `field_name` varchar(255) NOT NULL,
  `old_value` varchar(255) NOT NULL,
  `new_value` varchar(255) NOT NULL,
  `user_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `itassets_customhisto_user_id_6fcb7470_fk_accounts_` (`user_id`),
  CONSTRAINT `itassets_customhisto_user_id_6fcb7470_fk_accounts_` FOREIGN KEY (`user_id`) REFERENCES `accounts_customuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `itassets_customhistory`
--

LOCK TABLES `itassets_customhistory` WRITE;
/*!40000 ALTER TABLE `itassets_customhistory` DISABLE KEYS */;
/*!40000 ALTER TABLE `itassets_customhistory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `itassets_it_brand`
--

DROP TABLE IF EXISTS `itassets_it_brand`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `itassets_it_brand` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `brand` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `itassets_it_brand`
--

LOCK TABLES `itassets_it_brand` WRITE;
/*!40000 ALTER TABLE `itassets_it_brand` DISABLE KEYS */;
INSERT INTO `itassets_it_brand` VALUES (1,'HP'),(2,'Dell'),(3,'Lenovo'),(4,'Xerox');
/*!40000 ALTER TABLE `itassets_it_brand` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `itassets_it_category`
--

DROP TABLE IF EXISTS `itassets_it_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `itassets_it_category` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `category` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `itassets_it_category`
--

LOCK TABLES `itassets_it_category` WRITE;
/*!40000 ALTER TABLE `itassets_it_category` DISABLE KEYS */;
INSERT INTO `itassets_it_category` VALUES (1,'Computer'),(2,'Laptop'),(3,'Printer'),(4,'CCTV Cameras'),(5,'Monitor'),(6,'IP Phones');
/*!40000 ALTER TABLE `itassets_it_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `itassets_it_device_status`
--

DROP TABLE IF EXISTS `itassets_it_device_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `itassets_it_device_status` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `status` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `itassets_it_device_status`
--

LOCK TABLES `itassets_it_device_status` WRITE;
/*!40000 ALTER TABLE `itassets_it_device_status` DISABLE KEYS */;
INSERT INTO `itassets_it_device_status` VALUES (1,'Active'),(2,'Inactive'),(3,'Obsolute'),(4,'Damaged');
/*!40000 ALTER TABLE `itassets_it_device_status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `itassets_it_prodcuts`
--

DROP TABLE IF EXISTS `itassets_it_prodcuts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `itassets_it_prodcuts` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `model` varchar(100) DEFAULT NULL,
  `serial_number` varchar(100) NOT NULL,
  `supplier` varchar(100) DEFAULT NULL,
  `warranty_start_date` date DEFAULT NULL,
  `warranty_end_date` date DEFAULT NULL,
  `po_number` varchar(100) DEFAULT NULL,
  `processor` varchar(100) DEFAULT NULL,
  `ram` varchar(100) DEFAULT NULL,
  `harddisk` varchar(100) DEFAULT NULL,
  `operating_system` varchar(100) DEFAULT NULL,
  `brand_id` bigint NOT NULL,
  `category_id` bigint NOT NULL,
  `status_id` bigint NOT NULL,
  `Asset_tag` varchar(100) DEFAULT NULL,
  `allocation_status_id` bigint NOT NULL,
  `station_name_id` bigint NOT NULL,
  `created_date` date NOT NULL,
  `file` varchar(100) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  `current_allocation_id` bigint DEFAULT NULL,
  `asset_remarks` longtext,
  PRIMARY KEY (`id`),
  UNIQUE KEY `current_allocation_id` (`current_allocation_id`),
  KEY `itassets_it_prodcuts_brand_id_87703ad4_fk_itassets_it_brand_id` (`brand_id`),
  KEY `itassets_it_prodcuts_category_id_b553e99c_fk_itassets_` (`category_id`),
  KEY `itassets_it_prodcuts_status_id_b290f845_fk_itassets_` (`status_id`),
  KEY `itassets_it_prodcuts_allocation_status_id_396b196a_fk_itassets_` (`allocation_status_id`),
  KEY `itassets_it_prodcuts_station_name_id_1bedcf4c_fk_accounts_` (`station_name_id`),
  CONSTRAINT `itassets_it_prodcuts_allocation_status_id_396b196a_fk_itassets_` FOREIGN KEY (`allocation_status_id`) REFERENCES `itassets_allocation_status` (`id`),
  CONSTRAINT `itassets_it_prodcuts_brand_id_87703ad4_fk_itassets_it_brand_id` FOREIGN KEY (`brand_id`) REFERENCES `itassets_it_brand` (`id`),
  CONSTRAINT `itassets_it_prodcuts_category_id_b553e99c_fk_itassets_` FOREIGN KEY (`category_id`) REFERENCES `itassets_it_category` (`id`),
  CONSTRAINT `itassets_it_prodcuts_current_allocation_i_b8f1f88c_fk_itassets_` FOREIGN KEY (`current_allocation_id`) REFERENCES `itassets_itassetallocation` (`id`),
  CONSTRAINT `itassets_it_prodcuts_station_name_id_1bedcf4c_fk_accounts_` FOREIGN KEY (`station_name_id`) REFERENCES `accounts_station` (`id`),
  CONSTRAINT `itassets_it_prodcuts_status_id_b290f845_fk_itassets_` FOREIGN KEY (`status_id`) REFERENCES `itassets_it_device_status` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `itassets_it_prodcuts`
--

LOCK TABLES `itassets_it_prodcuts` WRITE;
/*!40000 ALTER TABLE `itassets_it_prodcuts` DISABLE KEYS */;
/*!40000 ALTER TABLE `itassets_it_prodcuts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `itassets_itassetallocation`
--

DROP TABLE IF EXISTS `itassets_itassetallocation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `itassets_itassetallocation` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `allocation_date` datetime(6) NOT NULL,
  `serial_number_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  `deallocation_date` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `itassets_itassetallo_serial_number_id_ab9b6664_fk_itassets_` (`serial_number_id`),
  KEY `itassets_itassetallo_user_id_5d75e46e_fk_accounts_` (`user_id`),
  CONSTRAINT `itassets_itassetallo_serial_number_id_ab9b6664_fk_itassets_` FOREIGN KEY (`serial_number_id`) REFERENCES `itassets_it_prodcuts` (`id`),
  CONSTRAINT `itassets_itassetallo_user_id_5d75e46e_fk_accounts_` FOREIGN KEY (`user_id`) REFERENCES `accounts_customuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `itassets_itassetallocation`
--

LOCK TABLES `itassets_itassetallocation` WRITE;
/*!40000 ALTER TABLE `itassets_itassetallocation` DISABLE KEYS */;
/*!40000 ALTER TABLE `itassets_itassetallocation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pettycash_expense`
--

DROP TABLE IF EXISTS `pettycash_expense`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pettycash_expense` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` datetime(6) NOT NULL,
  `description` longtext NOT NULL,
  `total_amount` decimal(10,2) NOT NULL,
  `employee_id` bigint NOT NULL,
  `claimant` varchar(100) NOT NULL,
  `station_name_id` bigint NOT NULL,
  `Approved_status` tinyint(1) DEFAULT NULL,
  `upload_bill` varchar(100) DEFAULT NULL,
  `approved_date` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `pettycash_expense_employee_id_b6174598_fk_accounts_customuser_id` (`employee_id`),
  KEY `pettycash_expense_station_name_id_296d7573_fk_accounts_` (`station_name_id`),
  CONSTRAINT `pettycash_expense_employee_id_b6174598_fk_accounts_customuser_id` FOREIGN KEY (`employee_id`) REFERENCES `accounts_customuser` (`id`),
  CONSTRAINT `pettycash_expense_station_name_id_296d7573_fk_accounts_` FOREIGN KEY (`station_name_id`) REFERENCES `accounts_station` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pettycash_expense`
--

LOCK TABLES `pettycash_expense` WRITE;
/*!40000 ALTER TABLE `pettycash_expense` DISABLE KEYS */;
INSERT INTO `pettycash_expense` VALUES (1,'2024-03-27 13:12:03.260362','Pest Killer for Toilet',17.00,6,'Mohammad Masud Ahmed',1,0,'PettycashInvoices/pest_killer.pdf',NULL);
/*!40000 ALTER TABLE `pettycash_expense` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pettycash_expenseitem`
--

DROP TABLE IF EXISTS `pettycash_expenseitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pettycash_expenseitem` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `item_name` varchar(150) NOT NULL,
  `quantity` int unsigned NOT NULL,
  `unit_price` decimal(10,2) NOT NULL,
  `amount` decimal(10,2) NOT NULL,
  `expense_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `pettycash_expenseite_expense_id_a3fe52ab_fk_pettycash` (`expense_id`),
  CONSTRAINT `pettycash_expenseite_expense_id_a3fe52ab_fk_pettycash` FOREIGN KEY (`expense_id`) REFERENCES `pettycash_expense` (`id`),
  CONSTRAINT `pettycash_expenseitem_chk_1` CHECK ((`quantity` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pettycash_expenseitem`
--

LOCK TABLES `pettycash_expenseitem` WRITE;
/*!40000 ALTER TABLE `pettycash_expenseitem` DISABLE KEYS */;
INSERT INTO `pettycash_expenseitem` VALUES (1,'pest killer',1,17.00,17.00,1);
/*!40000 ALTER TABLE `pettycash_expenseitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pettycash_travelclaim`
--

DROP TABLE IF EXISTS `pettycash_travelclaim`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pettycash_travelclaim` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `days` decimal(2,0) NOT NULL,
  `justification` varchar(255) NOT NULL,
  `accommodation` decimal(8,2) NOT NULL,
  `meals` decimal(8,2) NOT NULL,
  `transportation` decimal(8,2) NOT NULL,
  `miscellaneous` decimal(8,2) NOT NULL,
  `upload_bill` varchar(100) DEFAULT NULL,
  `user_id` bigint NOT NULL,
  `Total_Amount` decimal(8,2) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `created_date` datetime(6) NOT NULL,
  `end_date` date NOT NULL,
  `start_date` date NOT NULL,
  `approved_date` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `pettycash_travelclaim_user_id_febd24d1_fk_accounts_customuser_id` (`user_id`),
  CONSTRAINT `pettycash_travelclaim_user_id_febd24d1_fk_accounts_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_customuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pettycash_travelclaim`
--

LOCK TABLES `pettycash_travelclaim` WRITE;
/*!40000 ALTER TABLE `pettycash_travelclaim` DISABLE KEYS */;
INSERT INTO `pettycash_travelclaim` VALUES (1,3,'test',100.00,300.00,200.00,0.00,'travelclaimbills/report.pdf',4,600.00,0,'2024-02-27 10:14:03.617350','2024-02-29','2024-02-27',NULL),(2,3,'asdfdf',0.00,0.00,0.00,0.00,'',3,0.00,0,'2024-02-28 14:21:37.014599','2024-02-27','2024-02-25',NULL),(3,2,'sdfsf',0.00,0.00,0.00,0.00,'',3,0.00,0,'2024-02-28 14:24:49.540425','2024-02-26','2024-02-25',NULL);
/*!40000 ALTER TABLE `pettycash_travelclaim` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `polls_checklistdetails`
--

DROP TABLE IF EXISTS `polls_checklistdetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `polls_checklistdetails` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint DEFAULT NULL,
  `date` date NOT NULL,
  `equipment_id` bigint DEFAULT NULL,
  `time` time(6) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `polls_checklistdetails_user_id_2a99e2f6` (`user_id`),
  KEY `polls_checklistdetai_equipment_id_59544a16_fk_polls_equ` (`equipment_id`),
  CONSTRAINT `polls_checklistdetai_equipment_id_59544a16_fk_polls_equ` FOREIGN KEY (`equipment_id`) REFERENCES `polls_equipment` (`id`),
  CONSTRAINT `polls_checklistdetai_user_id_2a99e2f6_fk_accounts_` FOREIGN KEY (`user_id`) REFERENCES `accounts_customuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `polls_checklistdetails`
--

LOCK TABLES `polls_checklistdetails` WRITE;
/*!40000 ALTER TABLE `polls_checklistdetails` DISABLE KEYS */;
/*!40000 ALTER TABLE `polls_checklistdetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `polls_equipment`
--

DROP TABLE IF EXISTS `polls_equipment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `polls_equipment` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `Serial_Number` varchar(100) NOT NULL,
  `Capacity` varchar(100) NOT NULL,
  `Brand` varchar(100) NOT NULL,
  `Manufacture_Year` varchar(100) NOT NULL,
  `fueltype_id` bigint DEFAULT NULL,
  `station_name_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `polls_equipment_fueltype_id_e8986f2e_fk_polls_fuel_id` (`fueltype_id`),
  KEY `polls_equipment_station_name_id_fa569044_fk_accounts_station_id` (`station_name_id`),
  CONSTRAINT `polls_equipment_fueltype_id_e8986f2e_fk_polls_fuel_id` FOREIGN KEY (`fueltype_id`) REFERENCES `polls_fuel` (`id`),
  CONSTRAINT `polls_equipment_station_name_id_fa569044_fk_accounts_station_id` FOREIGN KEY (`station_name_id`) REFERENCES `accounts_station` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `polls_equipment`
--

LOCK TABLES `polls_equipment` WRITE;
/*!40000 ALTER TABLE `polls_equipment` DISABLE KEYS */;
/*!40000 ALTER TABLE `polls_equipment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `polls_equipmentspecificquestion`
--

DROP TABLE IF EXISTS `polls_equipmentspecificquestion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `polls_equipmentspecificquestion` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `text` longtext NOT NULL,
  `fueltype_id` bigint DEFAULT NULL,
  `subject_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `polls_equipmentspeci_fueltype_id_7f7ddf07_fk_polls_fue` (`fueltype_id`),
  KEY `polls_equipmentspeci_subject_id_70416f77_fk_polls_equ` (`subject_id`),
  CONSTRAINT `polls_equipmentspeci_fueltype_id_7f7ddf07_fk_polls_fue` FOREIGN KEY (`fueltype_id`) REFERENCES `polls_fuel` (`id`),
  CONSTRAINT `polls_equipmentspeci_subject_id_70416f77_fk_polls_equ` FOREIGN KEY (`subject_id`) REFERENCES `polls_equipment` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `polls_equipmentspecificquestion`
--

LOCK TABLES `polls_equipmentspecificquestion` WRITE;
/*!40000 ALTER TABLE `polls_equipmentspecificquestion` DISABLE KEYS */;
/*!40000 ALTER TABLE `polls_equipmentspecificquestion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `polls_excelfile`
--

DROP TABLE IF EXISTS `polls_excelfile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `polls_excelfile` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `file` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `polls_excelfile`
--

LOCK TABLES `polls_excelfile` WRITE;
/*!40000 ALTER TABLE `polls_excelfile` DISABLE KEYS */;
/*!40000 ALTER TABLE `polls_excelfile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `polls_fuel`
--

DROP TABLE IF EXISTS `polls_fuel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `polls_fuel` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fueltype` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `polls_fuel`
--

LOCK TABLES `polls_fuel` WRITE;
/*!40000 ALTER TABLE `polls_fuel` DISABLE KEYS */;
/*!40000 ALTER TABLE `polls_fuel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `polls_generalquestion`
--

DROP TABLE IF EXISTS `polls_generalquestion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `polls_generalquestion` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `text` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `polls_generalquestion`
--

LOCK TABLES `polls_generalquestion` WRITE;
/*!40000 ALTER TABLE `polls_generalquestion` DISABLE KEYS */;
/*!40000 ALTER TABLE `polls_generalquestion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `polls_genquestionresponse`
--

DROP TABLE IF EXISTS `polls_genquestionresponse`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `polls_genquestionresponse` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `response` varchar(100) NOT NULL,
  `checklistid_id` bigint DEFAULT NULL,
  `question_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `polls_genquestionres_checklistid_id_4602afd5_fk_polls_che` (`checklistid_id`),
  KEY `polls_genquestionres_question_id_cfcc7ea9_fk_polls_gen` (`question_id`),
  CONSTRAINT `polls_genquestionres_checklistid_id_4602afd5_fk_polls_che` FOREIGN KEY (`checklistid_id`) REFERENCES `polls_checklistdetails` (`id`),
  CONSTRAINT `polls_genquestionres_question_id_cfcc7ea9_fk_polls_gen` FOREIGN KEY (`question_id`) REFERENCES `polls_generalquestion` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `polls_genquestionresponse`
--

LOCK TABLES `polls_genquestionresponse` WRITE;
/*!40000 ALTER TABLE `polls_genquestionresponse` DISABLE KEYS */;
/*!40000 ALTER TABLE `polls_genquestionresponse` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `polls_incident`
--

DROP TABLE IF EXISTS `polls_incident`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `polls_incident` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_date` datetime(6) NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `polls_incident_user_id_6708fe71_fk_accounts_customuser_id` (`user_id`),
  CONSTRAINT `polls_incident_user_id_6708fe71_fk_accounts_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_customuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `polls_incident`
--

LOCK TABLES `polls_incident` WRITE;
/*!40000 ALTER TABLE `polls_incident` DISABLE KEYS */;
/*!40000 ALTER TABLE `polls_incident` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `polls_incident_nature_of_injury`
--

DROP TABLE IF EXISTS `polls_incident_nature_of_injury`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `polls_incident_nature_of_injury` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `incident_id` bigint NOT NULL,
  `natureofinjury_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `polls_incident_nature_of_incident_id_natureofinju_164af62a_uniq` (`incident_id`,`natureofinjury_id`),
  KEY `polls_incident_natur_natureofinjury_id_8afcd36c_fk_polls_nat` (`natureofinjury_id`),
  CONSTRAINT `polls_incident_natur_incident_id_8ff719d1_fk_polls_inc` FOREIGN KEY (`incident_id`) REFERENCES `polls_incident` (`id`),
  CONSTRAINT `polls_incident_natur_natureofinjury_id_8afcd36c_fk_polls_nat` FOREIGN KEY (`natureofinjury_id`) REFERENCES `polls_natureofinjury` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `polls_incident_nature_of_injury`
--

LOCK TABLES `polls_incident_nature_of_injury` WRITE;
/*!40000 ALTER TABLE `polls_incident_nature_of_injury` DISABLE KEYS */;
/*!40000 ALTER TABLE `polls_incident_nature_of_injury` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `polls_natureofinjury`
--

DROP TABLE IF EXISTS `polls_natureofinjury`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `polls_natureofinjury` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `polls_natureofinjury`
--

LOCK TABLES `polls_natureofinjury` WRITE;
/*!40000 ALTER TABLE `polls_natureofinjury` DISABLE KEYS */;
/*!40000 ALTER TABLE `polls_natureofinjury` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `polls_subquestionresponse`
--

DROP TABLE IF EXISTS `polls_subquestionresponse`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `polls_subquestionresponse` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `response` varchar(100) NOT NULL,
  `checklistid_id` bigint DEFAULT NULL,
  `question_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `polls_subquestionres_checklistid_id_f6a9295f_fk_polls_che` (`checklistid_id`),
  KEY `polls_subquestionres_question_id_a7ace797_fk_polls_equ` (`question_id`),
  CONSTRAINT `polls_subquestionres_checklistid_id_f6a9295f_fk_polls_che` FOREIGN KEY (`checklistid_id`) REFERENCES `polls_checklistdetails` (`id`),
  CONSTRAINT `polls_subquestionres_question_id_a7ace797_fk_polls_equ` FOREIGN KEY (`question_id`) REFERENCES `polls_equipmentspecificquestion` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `polls_subquestionresponse`
--

LOCK TABLES `polls_subquestionresponse` WRITE;
/*!40000 ALTER TABLE `polls_subquestionresponse` DISABLE KEYS */;
/*!40000 ALTER TABLE `polls_subquestionresponse` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `polls_workpermit`
--

DROP TABLE IF EXISTS `polls_workpermit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `polls_workpermit` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `created_date` date NOT NULL,
  `Created_time` time(6) NOT NULL,
  `Contractor_Name` varchar(100) NOT NULL,
  `Staff_in_charge` varchar(100) NOT NULL,
  `Phone_number` varchar(10) NOT NULL,
  `Iqama_number` varchar(10) NOT NULL,
  `Employee_Count` int NOT NULL,
  `Description` longtext NOT NULL,
  `Additional_notes` longtext NOT NULL,
  `Tools` longtext NOT NULL,
  `station_name_id` bigint DEFAULT NULL,
  `upload_Iqama` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `polls_workpermit_station_name_id_dc90a05a_fk_accounts_station_id` (`station_name_id`),
  CONSTRAINT `polls_workpermit_station_name_id_dc90a05a_fk_accounts_station_id` FOREIGN KEY (`station_name_id`) REFERENCES `accounts_station` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `polls_workpermit`
--

LOCK TABLES `polls_workpermit` WRITE;
/*!40000 ALTER TABLE `polls_workpermit` DISABLE KEYS */;
INSERT INTO `polls_workpermit` VALUES (1,'2024-02-27','2024-02-27','2024-02-27','09:56:13.000000','citynet','siraj','0580656544','2425924541',3,'sdfhjkh','hskdh','hhgjh',1,NULL),(2,'2024-02-27','2024-02-28','2024-02-27','17:00:16.000000','Single Point','Kumar','0580656544','2425924541',3,'to construct new security screening room between import and export for staff access','NA','Plier,cuttter,grinding machine, welding machine',1,NULL),(3,'2024-02-28','2024-03-05','2024-02-28','17:00:16.000000','Al shaik','Antony','0554388541','2328665944',3,'fire fighting and fire alarm system implementation for new security inspection room(between import and export).','NA','Threading machine, Speed cutter,Welding machine,Hand tools\r\nBattery drill, Holsaw machine, Bunche wise',1,NULL),(4,'2024-02-28','2024-02-28','2024-02-28','14:40:47.000000','NA','Athif','0560877591','2548989959',1,'to replace tow tractor tire','NA','Jacky,Spanner, Hand tools',1,NULL),(5,'2024-03-02','2024-03-02','2024-02-29','11:54:44.000000','ANFAAS AL AMAL GENERAL CONTRACTING COMPANY','Ganesh Pandian Rajendran','0565301513','2556864367',2,'replace old tire put new tow tractor','N/A','Hand tools',1,NULL),(6,'2024-03-02','2024-03-03','2024-03-02','14:42:29.000000','citynet','siraj','35335453','345345',4,'q5awa','arfd','asdfsdf',1,'WorkPermit_iqama/report_3.pdf'),(7,'2024-03-04','2024-03-06','2024-03-04','17:03:22.000000','Single point','Kumar','0543269172','2539828653',3,'Electrical and fire fighting work','N/A','Hand tools and crane',1,''),(8,'2024-03-06','2024-03-09','2024-03-06','16:09:52.000000','Anfaas al Amal general c0ntracting','Ganesh Pandian Rajendran','0565301513','2556864367',2,'PM Tow tractor and forklit','Prev work permit ref no :5','Hand tool blower other small tools',1,''),(9,'2024-11-03','2024-12-03','2024-03-11','17:15:16.000000','ANFAAS AL AMAL GENERAL CONTRACTING COMPANY','Bhuvanesh','0547349535','2563108063',2,'Forklift and tow tractor maintinance','N/A','Hand tools compressor blower',1,''),(10,'2024-03-13','2024-03-14','2024-03-11','14:39:45.000000','test','dfhj','9875799','79987524',2,'ssdf','asdfsdf','sdfds',1,'WorkPermit_iqama/example_report_50.pdf'),(11,'2024-03-21','2024-03-23','2024-03-21','14:47:05.000000','Al shaikh','Antony Joseph','0554388541','2328665944',3,'New new fire alarm and fire fighting work','N/A','Threding machine hand tools',1,'WorkPermit_iqama/DOC001_11_-_Copy.pdf'),(12,'2024-03-26','2024-03-28','2024-03-26','14:47:05.000000','ANFAAS AL AMAL GENERAL CONTRACTING COMPANY','Bhuvanesh','0564561751','2563108063',2,'tow tractor maintenance','N/A','Hand tools',1,'WorkPermit_iqama/DOC001_14.pdf'),(13,'2024-03-26','2024-03-27','2024-03-26','14:47:05.000000','Al sale','Muhammad Nuzam','0595871880','2486061225',2,'Weight scale maintenance','N/A','hand tools weight',1,'WorkPermit_iqama/DOC001_15.pdf');
/*!40000 ALTER TABLE `polls_workpermit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quality_driverinvolved`
--

DROP TABLE IF EXISTS `quality_driverinvolved`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quality_driverinvolved` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `iqama_id` decimal(10,0) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quality_driverinvolved`
--

LOCK TABLES `quality_driverinvolved` WRITE;
/*!40000 ALTER TABLE `quality_driverinvolved` DISABLE KEYS */;
/*!40000 ALTER TABLE `quality_driverinvolved` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quality_employeesinvolved`
--

DROP TABLE IF EXISTS `quality_employeesinvolved`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quality_employeesinvolved` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `department` varchar(100) DEFAULT NULL,
  `designation` varchar(100) DEFAULT NULL,
  `gaca_id` decimal(10,0) DEFAULT NULL,
  `iqama_id` decimal(10,0) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quality_employeesinvolved`
--

LOCK TABLES `quality_employeesinvolved` WRITE;
/*!40000 ALTER TABLE `quality_employeesinvolved` DISABLE KEYS */;
/*!40000 ALTER TABLE `quality_employeesinvolved` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quality_in_bodyparts`
--

DROP TABLE IF EXISTS `quality_in_bodyparts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quality_in_bodyparts` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `text` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quality_in_bodyparts`
--

LOCK TABLES `quality_in_bodyparts` WRITE;
/*!40000 ALTER TABLE `quality_in_bodyparts` DISABLE KEYS */;
/*!40000 ALTER TABLE `quality_in_bodyparts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quality_in_category`
--

DROP TABLE IF EXISTS `quality_in_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quality_in_category` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `text` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quality_in_category`
--

LOCK TABLES `quality_in_category` WRITE;
/*!40000 ALTER TABLE `quality_in_category` DISABLE KEYS */;
/*!40000 ALTER TABLE `quality_in_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quality_in_incidents`
--

DROP TABLE IF EXISTS `quality_in_incidents`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quality_in_incidents` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `Location` varchar(100) NOT NULL,
  `date_of_occurance` date NOT NULL,
  `time_of_occurance` time(6) NOT NULL,
  `category_id` bigint NOT NULL,
  `station_id` bigint NOT NULL,
  `surface_condition_id` bigint NOT NULL,
  `type_id` bigint NOT NULL,
  `visibility_id` bigint NOT NULL,
  `whether_condition_id` bigint NOT NULL,
  `Summary` varchar(256) NOT NULL,
  `contributory_factors` varchar(256) NOT NULL,
  `corrective_measurments` varchar(256) NOT NULL,
  `image1` varchar(100) DEFAULT NULL,
  `image2` varchar(100) DEFAULT NULL,
  `image3` varchar(100) DEFAULT NULL,
  `image4` varchar(100) DEFAULT NULL,
  `preventive_measures` varchar(256) NOT NULL,
  `created_date` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `quality_in_incidents_category_id_34bbac63_fk_quality_i` (`category_id`),
  KEY `quality_in_incidents_station_id_93bf6b88_fk_accounts_station_id` (`station_id`),
  KEY `quality_in_incidents_surface_condition_id_caf24c49_fk_quality_i` (`surface_condition_id`),
  KEY `quality_in_incidents_type_id_1362f034_fk_quality_i` (`type_id`),
  KEY `quality_in_incidents_visibility_id_a4687381_fk_quality_i` (`visibility_id`),
  KEY `quality_in_incidents_whether_condition_id_d5eb0476_fk_quality_w` (`whether_condition_id`),
  CONSTRAINT `quality_in_incidents_category_id_34bbac63_fk_quality_i` FOREIGN KEY (`category_id`) REFERENCES `quality_in_category` (`id`),
  CONSTRAINT `quality_in_incidents_station_id_93bf6b88_fk_accounts_station_id` FOREIGN KEY (`station_id`) REFERENCES `accounts_station` (`id`),
  CONSTRAINT `quality_in_incidents_surface_condition_id_caf24c49_fk_quality_i` FOREIGN KEY (`surface_condition_id`) REFERENCES `quality_in_surfacecondition` (`id`),
  CONSTRAINT `quality_in_incidents_type_id_1362f034_fk_quality_i` FOREIGN KEY (`type_id`) REFERENCES `quality_in_incidenttype` (`id`),
  CONSTRAINT `quality_in_incidents_visibility_id_a4687381_fk_quality_i` FOREIGN KEY (`visibility_id`) REFERENCES `quality_in_visibility` (`id`),
  CONSTRAINT `quality_in_incidents_whether_condition_id_d5eb0476_fk_quality_w` FOREIGN KEY (`whether_condition_id`) REFERENCES `quality_whethercondition` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quality_in_incidents`
--

LOCK TABLES `quality_in_incidents` WRITE;
/*!40000 ALTER TABLE `quality_in_incidents` DISABLE KEYS */;
/*!40000 ALTER TABLE `quality_in_incidents` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quality_in_incidents_bodyparts_affected`
--

DROP TABLE IF EXISTS `quality_in_incidents_bodyparts_affected`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quality_in_incidents_bodyparts_affected` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `in_incidents_id` bigint NOT NULL,
  `in_bodyparts_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `quality_in_incidents_bod_in_incidents_id_in_bodyp_01a489cd_uniq` (`in_incidents_id`,`in_bodyparts_id`),
  KEY `quality_in_incidents_in_bodyparts_id_1d3dd4ae_fk_quality_i` (`in_bodyparts_id`),
  CONSTRAINT `quality_in_incidents_in_bodyparts_id_1d3dd4ae_fk_quality_i` FOREIGN KEY (`in_bodyparts_id`) REFERENCES `quality_in_bodyparts` (`id`),
  CONSTRAINT `quality_in_incidents_in_incidents_id_7096effc_fk_quality_i` FOREIGN KEY (`in_incidents_id`) REFERENCES `quality_in_incidents` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quality_in_incidents_bodyparts_affected`
--

LOCK TABLES `quality_in_incidents_bodyparts_affected` WRITE;
/*!40000 ALTER TABLE `quality_in_incidents_bodyparts_affected` DISABLE KEYS */;
/*!40000 ALTER TABLE `quality_in_incidents_bodyparts_affected` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quality_in_incidents_driver_name`
--

DROP TABLE IF EXISTS `quality_in_incidents_driver_name`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quality_in_incidents_driver_name` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `in_incidents_id` bigint NOT NULL,
  `driverinvolved_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `quality_in_incidents_emp_in_incidents_id_employee_7fd41a31_uniq` (`in_incidents_id`,`driverinvolved_id`),
  KEY `quality_in_incidents_driverinvolved_id_8165f7f7_fk_quality_d` (`driverinvolved_id`),
  CONSTRAINT `quality_in_incidents_driverinvolved_id_8165f7f7_fk_quality_d` FOREIGN KEY (`driverinvolved_id`) REFERENCES `quality_driverinvolved` (`id`),
  CONSTRAINT `quality_in_incidents_in_incidents_id_90956d15_fk_quality_i` FOREIGN KEY (`in_incidents_id`) REFERENCES `quality_in_incidents` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quality_in_incidents_driver_name`
--

LOCK TABLES `quality_in_incidents_driver_name` WRITE;
/*!40000 ALTER TABLE `quality_in_incidents_driver_name` DISABLE KEYS */;
/*!40000 ALTER TABLE `quality_in_incidents_driver_name` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quality_in_incidents_employees_name`
--

DROP TABLE IF EXISTS `quality_in_incidents_employees_name`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quality_in_incidents_employees_name` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `in_incidents_id` bigint NOT NULL,
  `employeesinvolved_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `quality_in_incidents_emp_in_incidents_id_employee_336ca556_uniq` (`in_incidents_id`,`employeesinvolved_id`),
  KEY `quality_in_incidents_employeesinvolved_id_20b3f296_fk_quality_e` (`employeesinvolved_id`),
  CONSTRAINT `quality_in_incidents_employeesinvolved_id_20b3f296_fk_quality_e` FOREIGN KEY (`employeesinvolved_id`) REFERENCES `quality_employeesinvolved` (`id`),
  CONSTRAINT `quality_in_incidents_in_incidents_id_2ab59581_fk_quality_i` FOREIGN KEY (`in_incidents_id`) REFERENCES `quality_in_incidents` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quality_in_incidents_employees_name`
--

LOCK TABLES `quality_in_incidents_employees_name` WRITE;
/*!40000 ALTER TABLE `quality_in_incidents_employees_name` DISABLE KEYS */;
/*!40000 ALTER TABLE `quality_in_incidents_employees_name` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quality_in_incidents_nature_of_injury`
--

DROP TABLE IF EXISTS `quality_in_incidents_nature_of_injury`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quality_in_incidents_nature_of_injury` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `in_incidents_id` bigint NOT NULL,
  `in_natureofinjury_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `quality_in_incidents_nat_in_incidents_id_in_natur_b144ef8d_uniq` (`in_incidents_id`,`in_natureofinjury_id`),
  KEY `quality_in_incidents_in_natureofinjury_id_a912b6af_fk_quality_i` (`in_natureofinjury_id`),
  CONSTRAINT `quality_in_incidents_in_incidents_id_8eb4ff7b_fk_quality_i` FOREIGN KEY (`in_incidents_id`) REFERENCES `quality_in_incidents` (`id`),
  CONSTRAINT `quality_in_incidents_in_natureofinjury_id_a912b6af_fk_quality_i` FOREIGN KEY (`in_natureofinjury_id`) REFERENCES `quality_in_natureofinjury` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quality_in_incidents_nature_of_injury`
--

LOCK TABLES `quality_in_incidents_nature_of_injury` WRITE;
/*!40000 ALTER TABLE `quality_in_incidents_nature_of_injury` DISABLE KEYS */;
/*!40000 ALTER TABLE `quality_in_incidents_nature_of_injury` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quality_in_incidenttype`
--

DROP TABLE IF EXISTS `quality_in_incidenttype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quality_in_incidenttype` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `text` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quality_in_incidenttype`
--

LOCK TABLES `quality_in_incidenttype` WRITE;
/*!40000 ALTER TABLE `quality_in_incidenttype` DISABLE KEYS */;
/*!40000 ALTER TABLE `quality_in_incidenttype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quality_in_natureofinjury`
--

DROP TABLE IF EXISTS `quality_in_natureofinjury`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quality_in_natureofinjury` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `text` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quality_in_natureofinjury`
--

LOCK TABLES `quality_in_natureofinjury` WRITE;
/*!40000 ALTER TABLE `quality_in_natureofinjury` DISABLE KEYS */;
/*!40000 ALTER TABLE `quality_in_natureofinjury` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quality_in_surfacecondition`
--

DROP TABLE IF EXISTS `quality_in_surfacecondition`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quality_in_surfacecondition` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `text` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quality_in_surfacecondition`
--

LOCK TABLES `quality_in_surfacecondition` WRITE;
/*!40000 ALTER TABLE `quality_in_surfacecondition` DISABLE KEYS */;
/*!40000 ALTER TABLE `quality_in_surfacecondition` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quality_in_visibility`
--

DROP TABLE IF EXISTS `quality_in_visibility`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quality_in_visibility` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `text` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quality_in_visibility`
--

LOCK TABLES `quality_in_visibility` WRITE;
/*!40000 ALTER TABLE `quality_in_visibility` DISABLE KEYS */;
/*!40000 ALTER TABLE `quality_in_visibility` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quality_whethercondition`
--

DROP TABLE IF EXISTS `quality_whethercondition`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quality_whethercondition` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `text` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quality_whethercondition`
--

LOCK TABLES `quality_whethercondition` WRITE;
/*!40000 ALTER TABLE `quality_whethercondition` DISABLE KEYS */;
/*!40000 ALTER TABLE `quality_whethercondition` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-02 13:31:36
