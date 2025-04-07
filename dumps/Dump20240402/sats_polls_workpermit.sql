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
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-02 13:30:55
