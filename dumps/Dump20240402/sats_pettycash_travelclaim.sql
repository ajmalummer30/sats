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
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-02 13:30:53
