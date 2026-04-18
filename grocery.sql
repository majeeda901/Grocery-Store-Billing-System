-- MySQL dump 10.13  Distrib 8.0.44, for Win64 (x86_64)
--
-- Host: localhost    Database: grocery
-- ------------------------------------------------------
-- Server version	8.0.44

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bill_items`
--

DROP TABLE IF EXISTS `bill_items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bill_items` (
  `id` int NOT NULL AUTO_INCREMENT,
  `bill_id` int DEFAULT NULL,
  `prd_id` int DEFAULT NULL,
  `qty` float DEFAULT NULL,
  `prd_price` int DEFAULT NULL,
  `total` float DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `bill_id` (`bill_id`),
  KEY `prd_id` (`prd_id`),
  CONSTRAINT `bill_items_ibfk_1` FOREIGN KEY (`bill_id`) REFERENCES `bills` (`bill_id`) ON DELETE CASCADE,
  CONSTRAINT `bill_items_ibfk_2` FOREIGN KEY (`prd_id`) REFERENCES `product_info` (`prd_id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bill_items`
--

LOCK TABLES `bill_items` WRITE;
/*!40000 ALTER TABLE `bill_items` DISABLE KEYS */;
INSERT INTO `bill_items` VALUES (1,1,45,2,93,186),(2,1,46,1,452,452),(3,1,50,1,65,65),(4,1,43,1,135,135),(5,1,44,2,255,510),(6,2,17,2,25,50),(7,2,31,1,160,160),(8,2,40,1,23,23),(9,2,26,2,52,104),(10,3,1,1,65,65),(11,3,3,1,185,185),(12,3,35,1,55,55),(13,3,36,1,42,42),(14,3,38,2,25,50),(15,4,8,1,295,295),(16,4,10,2,125,250),(17,4,11,1,185,185),(18,4,41,2,45,90),(19,5,23,3,40,120),(20,5,40,1,23,23),(21,5,39,1,30,30),(22,5,13,2,72,144),(23,5,4,1,23,23);
/*!40000 ALTER TABLE `bill_items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bills`
--

DROP TABLE IF EXISTS `bills`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bills` (
  `bill_id` int NOT NULL AUTO_INCREMENT,
  `cusmr_id` int DEFAULT NULL,
  `total_amount` float DEFAULT NULL,
  `date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`bill_id`),
  KEY `cusmr_id` (`cusmr_id`),
  CONSTRAINT `bills_ibfk_1` FOREIGN KEY (`cusmr_id`) REFERENCES `customer_info` (`cusmr_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bills`
--

LOCK TABLES `bills` WRITE;
/*!40000 ALTER TABLE `bills` DISABLE KEYS */;
INSERT INTO `bills` VALUES (1,1,1348,'2026-04-18 19:29:20'),(2,2,337,'2026-04-18 19:30:15'),(3,3,397,'2026-04-18 19:31:09'),(4,4,820,'2026-04-18 19:31:56'),(5,5,340,'2026-04-18 19:32:48');
/*!40000 ALTER TABLE `bills` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer_info`
--

DROP TABLE IF EXISTS `customer_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer_info` (
  `cusmr_id` int NOT NULL AUTO_INCREMENT,
  `cusmr_name` varchar(40) DEFAULT NULL,
  `mobile` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`cusmr_id`),
  UNIQUE KEY `mobile` (`mobile`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer_info`
--

LOCK TABLES `customer_info` WRITE;
/*!40000 ALTER TABLE `customer_info` DISABLE KEYS */;
INSERT INTO `customer_info` VALUES (1,'majeeda','8192018374'),(2,'sameera','9080706050'),(3,'saida','8090504030'),(4,'rasoolbee','7060403010'),(5,'hannu','9020301060');
/*!40000 ALTER TABLE `customer_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_info`
--

DROP TABLE IF EXISTS `product_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_info` (
  `prd_id` int NOT NULL,
  `prd_name` varchar(50) DEFAULT NULL,
  `prd_qty` float DEFAULT NULL,
  `prd_in_stock` int DEFAULT NULL,
  `org_prd_price` int DEFAULT NULL,
  `sell_prd_price` int DEFAULT NULL,
  PRIMARY KEY (`prd_id`),
  UNIQUE KEY `prd_name` (`prd_name`),
  CONSTRAINT `product_info_chk_1` CHECK ((`prd_in_stock` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_info`
--

LOCK TABLES `product_info` WRITE;
/*!40000 ALTER TABLE `product_info` DISABLE KEYS */;
INSERT INTO `product_info` VALUES (1,'Rice(kg)',1,39,55,65),(2,'Wheat(kg)',1,30,45,55),(3,'Oil(ltr)',1,69,160,185),(4,'Salt(kg)',1,59,20,23),(5,'Chilli powder(grms)',250,40,60,65),(6,'Turmeric(grms)',100,50,20,25),(7,'Peanut(grms)',250,40,40,46),(8,'Parachute Hair Oil(ml)',250,39,280,295),(9,'Mysore Sandel Soap(unit)',1,50,40,43),(10,'Vaseline Moisture(ml)',150,48,110,125),(11,'Loreal Shampoo(ml)',175,39,170,185),(12,'Upma Rava(grms)',250,40,15,22),(13,'Oats(grms)',100,58,60,72),(14,'Flour-Atta(kg)',1,50,45,52),(15,'Milk(ml)',500,30,35,40),(16,'Curd(ml)',500,30,30,34),(17,'Biscuits(grms)',200,48,22,25),(18,'Chips(grms)',150,60,15,20),(19,'Noodles(grms)',200,45,40,45),(20,'Sugar(grms)',250,50,40,46),(21,'Tea(grms)',100,45,30,42),(22,'Coffee(grms)',50,60,20,24),(23,'Eggs(box)',6,97,36,40),(24,'Detergent(grms)',250,60,30,38),(25,'Dish Wash Liquid(ml)',100,30,60,67),(26,'Juice(ml)',100,38,43,52),(28,'Bread(grms)',300,55,34,40),(29,'Floor Cleanser(ml)',150,45,43,49),(30,'Garam Masala(grms)',30,20,24,30),(31,'Apples(box)',4,149,140,160),(32,'Oranges(box)',3,120,110,132),(33,'Mango(box)',2,140,150,172),(34,'Banana(box)',3,100,40,45),(35,'Onion(grms)',200,59,42,55),(36,'Tomato(grms)',250,49,30,42),(37,'Coriander(grms)',100,40,20,24),(38,'Chilli(grms)',150,58,20,25),(39,'Potato(grms)',250,59,25,30),(40,'Carrot(grms)',250,68,20,23),(41,'Sanitory (Pack)',1,48,42,45),(42,'Toilet Clenser(ml)',200,65,72,85),(43,'Bucket(unit)',1,29,120,135),(44,'Baby Soap(unit)',1,18,240,255),(45,'Baby Oil(ml)',200,38,80,93),(46,'Baby Shampoo(ml)',250,49,300,452),(47,'Baby Powder(grms)',160,30,200,230),(48,'Slippers(pair)',1,20,200,320),(49,'Yellow Gram(grms)',200,45,80,100),(50,'Washroom Mug(unit)',1,39,50,65);
/*!40000 ALTER TABLE `product_info` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-04-19  1:15:06
