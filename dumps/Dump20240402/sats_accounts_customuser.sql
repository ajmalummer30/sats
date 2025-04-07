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
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-02 13:30:54
