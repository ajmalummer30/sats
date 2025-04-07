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
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-02 13:30:54
