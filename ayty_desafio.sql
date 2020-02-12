CREATE DATABASE  IF NOT EXISTS `ayty_desafio` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `ayty_desafio`;
-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: ayty_desafio
-- ------------------------------------------------------
-- Server version	8.0.19

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
-- Table structure for table `call`
--

DROP TABLE IF EXISTS `call`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `call` (
  `id_call` bigint unsigned NOT NULL AUTO_INCREMENT,
  `extension` varchar(255) DEFAULT NULL,
  `nu_ddd` varchar(6) DEFAULT NULL,
  `nu_phone` varchar(12) DEFAULT NULL,
  `dt_start` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `dt_answer` datetime DEFAULT NULL,
  `dt_finish` datetime DEFAULT NULL,
  PRIMARY KEY (`id_call`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `call`
--

LOCK TABLES `call` WRITE;
/*!40000 ALTER TABLE `call` DISABLE KEYS */;
INSERT INTO `call` VALUES (6,'1111','48','9984486613','2020-02-11 22:57:55','2020-02-11 20:01:56','2020-02-11 20:03:30'),(7,'2222','48','9984486612','2020-02-11 22:58:53','2020-02-11 20:02:25','2020-02-11 20:03:23'),(8,'3333','48','9984486611','2020-02-11 22:59:01','2020-02-12 11:33:20','2020-02-12 11:33:53'),(9,'5555','48','9984486615','2020-02-11 22:59:11',NULL,NULL),(10,'9999','48','984480000','2020-02-12 14:28:22',NULL,NULL);
/*!40000 ALTER TABLE `call` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `exten_event`
--

DROP TABLE IF EXISTS `exten_event`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `exten_event` (
  `id_exten_event` bigint unsigned NOT NULL AUTO_INCREMENT,
  `extension` varchar(255) DEFAULT NULL,
  `status` varchar(80) DEFAULT NULL,
  `dt_event` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_exten_event`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exten_event`
--

LOCK TABLES `exten_event` WRITE;
/*!40000 ALTER TABLE `exten_event` DISABLE KEYS */;
INSERT INTO `exten_event` VALUES (1,'1111','ring','2020-02-11 23:08:50'),(2,'2222','in_call','2020-02-11 23:09:17'),(3,'3333','available','2020-02-11 23:09:30'),(4,'8888','ring','2020-02-12 14:36:00');
/*!40000 ALTER TABLE `exten_event` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `extension`
--

DROP TABLE IF EXISTS `extension`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `extension` (
  `id_extension` bigint unsigned NOT NULL AUTO_INCREMENT,
  `extension` varchar(255) DEFAULT NULL,
  `nm_extension` varchar(255) DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL DEFAULT '1',
  `must_record` tinyint(1) DEFAULT NULL,
  `number_transfer` varchar(255) DEFAULT NULL,
  `was_exported` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id_extension`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `extension`
--

LOCK TABLES `extension` WRITE;
/*!40000 ALTER TABLE `extension` DISABLE KEYS */;
INSERT INTO `extension` VALUES (1,'9999','9999',0,1,NULL,0),(4,'5555','5555',1,1,NULL,0);
/*!40000 ALTER TABLE `extension` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'ayty_desafio'
--

--
-- Dumping routines for database 'ayty_desafio'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-02-12 11:44:02
