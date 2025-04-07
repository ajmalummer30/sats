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
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-02 13:30:54
