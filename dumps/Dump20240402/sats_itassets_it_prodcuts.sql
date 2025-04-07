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
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-02 13:30:55
