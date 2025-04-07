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
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-02 13:30:55
