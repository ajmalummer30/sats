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
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-02 13:30:55
