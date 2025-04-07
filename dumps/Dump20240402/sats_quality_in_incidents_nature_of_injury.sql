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
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-02 13:30:55
