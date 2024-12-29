CREATE DATABASE  IF NOT EXISTS `myntra` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `myntra`;
-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: myntra
-- ------------------------------------------------------
-- Server version	8.0.40

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
-- Table structure for table `cust`
--

DROP TABLE IF EXISTS `cust`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cust` (
  `custid` int NOT NULL AUTO_INCREMENT,
  `custname` varchar(50) NOT NULL,
  `password` varchar(45) NOT NULL,
  `contactno` varchar(10) NOT NULL,
  `address` varchar(100) NOT NULL,
  `added_on` date NOT NULL,
  PRIMARY KEY (`custid`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cust`
--

LOCK TABLES `cust` WRITE;
/*!40000 ALTER TABLE `cust` DISABLE KEYS */;
INSERT INTO `cust` VALUES (1,'Nisha','00000000','9874563214','vasai','2024-12-01'),(2,'krishna','11111111','9874563214','vasai','2024-12-15'),(3,'Nisha Singh','12345678','9874563214','vasai','2024-12-19'),(4,'Pankaj Singh','00000000','9860225061','vasai east','2024-12-23'),(5,'Ishaan Sharma','11111111','9876543210','Borivali east','2024-12-23'),(6,'rachna','abc123@t','8944525165','vasai','2024-12-24'),(7,'Pankaj Singh','12345678','9876543210','vasai','2024-12-24');
/*!40000 ALTER TABLE `cust` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cust_prod`
--

DROP TABLE IF EXISTS `cust_prod`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cust_prod` (
  `cpid` int NOT NULL AUTO_INCREMENT,
  `custid` int NOT NULL,
  `prodid` int NOT NULL,
  `quantity` int NOT NULL,
  `Amount` int NOT NULL,
  `ordered_on` date NOT NULL,
  PRIMARY KEY (`cpid`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cust_prod`
--

LOCK TABLES `cust_prod` WRITE;
/*!40000 ALTER TABLE `cust_prod` DISABLE KEYS */;
INSERT INTO `cust_prod` VALUES (1,5,26,2,5098,'2024-12-23'),(2,5,25,1,2849,'2024-12-23'),(3,5,20,1,1100,'2024-12-23'),(4,5,50,2,2200,'2024-12-24'),(5,5,51,2,2400,'2024-12-24'),(6,6,50,1,1100,'2024-12-24'),(7,5,21,2,2000,'2024-12-24'),(8,5,22,1,950,'2024-12-24'),(9,7,23,2,2100,'2024-12-24'),(10,7,26,1,2549,'2024-12-24');
/*!40000 ALTER TABLE `cust_prod` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `prodid` int NOT NULL AUTO_INCREMENT,
  `brand` varchar(100) NOT NULL,
  `pcategory` varchar(100) NOT NULL,
  `pname` varchar(100) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `size` varchar(10) NOT NULL,
  `added_on` date NOT NULL,
  `price` int NOT NULL,
  `QUANTITY` int DEFAULT '3',
  PRIMARY KEY (`prodid`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (1,'KALINI','CLOTH','Bandhani Kurta With Trouser & Dupatta','F','XL','2024-12-16',1000,3),(2,'KALINI','CLOTH','Bandhani Kurta With Trouser & Dupatta','F','L','2024-12-16',800,3),(3,'KALINI','CLOTH','Bandhani Kurta With Trouser & Dupatta','F','M','2024-12-16',750,3),(4,'Roadster','CLOTH','Blue T-shirt','M','L','2024-12-17',450,3),(5,'Roadster','CLOTH','Blue T-shirt','M','XXL','2024-12-17',550,3),(6,'Allen Solly','CLOTH','Brand Logo Printed Sweatshirt','M','XXL','2024-12-17',550,3),(7,'Allen Solly','CLOTH','Brand Logo Printed Sweatshirt','M','XL','2024-12-17',500,3),(8,'THE BEAR HOUSE','CLOTH','Men Maroon & Navy Blue Slim Fit Checked Shirt','M','XL','2024-12-17',600,3),(9,'THE BEAR HOUSE','CLOTH','Men Maroon & Navy Blue Slim Fit Checked Shirt','M','XXL','2024-12-17',700,3),(10,'Roadster','CLOTH','Men Black & Grey Striped Cardigan','M','XXL','2024-12-17',700,3),(11,'Roadster','CLOTH','Men Black & Grey Striped Cardigan','M','XL','2024-12-17',650,3),(12,'Roadster','CLOTH','Men Black & Grey Striped Cardigan','M','L','2024-12-17',600,3),(13,'WROGN','CLOTH','Men Black Slim Fit Clean Look Mid Rise Stretchable Jeans','M','34','2024-12-17',1199,3),(14,'WROGN','CLOTH','Men Black Slim Fit Clean Look Mid Rise Stretchable Jeans','M','32','2024-12-17',1100,3),(15,'WROGN','CLOTH','Men Black Slim Fit Clean Look Mid Rise Stretchable Jeans','M','36','2024-12-17',1200,3),(16,'Levis','CLOTH','Men 511 Slim Fit Light Fade Stretchable Jeans','M','32','2024-12-17',800,3),(17,'Levis','CLOTH','Men 511 Slim Fit Light Fade Stretchable Jeans','M','34','2024-12-17',850,3),(18,'Levis','CLOTH','Men 511 Slim Fit Light Fade Stretchable Jeans','M','36','2024-12-17',1000,3),(19,'Pepe Jeans','CLOTH','Men Holborne Straight Fit Mid Rise Clean Look Stretchable Jeans','M','36','2024-12-17',1300,3),(20,'Pepe Jeans','CLOTH','Men Holborne Straight Fit Mid Rise Clean Look Stretchable Jeans','M','34','2024-12-17',1100,2),(21,'Pepe Jeans','CLOTH','Men Holborne Straight Fit Mid Rise Clean Look Stretchable Jeans','M','32','2024-12-17',1000,1),(22,'Pepe Jeans','CLOTH','Men Straight Fit Light Fade Stretchable Jeans','M','32','2024-12-17',950,2),(23,'Pepe Jeans','CLOTH','Men Straight Fit Light Fade Stretchable Jeans','M','34','2024-12-17',1050,1),(24,'Pepe Jeans','CLOTH','Men Straight Fit Light Fade Stretchable Jeans','M','36','2024-12-17',1150,3),(25,'Pepe Jeans','CLOTH','Men Slim Fit Low-Rise Light Fade Stretchable Jeans','M','36','2024-12-17',2849,2),(26,'Pepe Jeans','CLOTH','Men Slim Fit Low-Rise Light Fade Stretchable Jeans','M','34','2024-12-17',2549,0),(27,'H&M','CLOTH','Boys Printed T-shirt','K','11-12','2024-12-17',399,3),(28,'H&M','CLOTH','Boys Printed T-shirt','K','12-13','2024-12-17',499,3),(29,'BE AWARA','CLOTH','Kids Typography Printed Cotton T-Shirt','K','8-9','2024-12-17',299,3),(30,'BE AWARA','CLOTH','Kids Typography Printed Cotton T-Shirt','K','9-10','2024-12-17',399,3),(31,'BE AWARA','CLOTH','Kids Typography Printed Cotton T-Shirt','K','10-11','2024-12-17',499,3),(32,'YK X Minute Mirth','CLOTH','Boys Batman Printed Pure Cotton T-shirt','K','10-11','2024-12-17',499,3),(33,'YK X Minute Mirth','CLOTH','Boys Batman Printed Pure Cotton T-shirt','K','11-12','2024-12-17',550,3),(34,'YK X Minute Mirth','CLOTH','Boys Batman Printed Pure Cotton T-shirt','K','9-10','2024-12-17',350,3),(35,'YK Disney','CLOTH','Girls Pack Of 3 Minnie Mouse Printed Extended Sleeves T-shirt','K','5-6','2024-12-17',269,3),(36,'YK Disney','CLOTH','Girls Pack Of 3 Minnie Mouse Printed Extended Sleeves T-shirt','K','7-8','2024-12-17',369,3),(37,'YK Disney','CLOTH','Girls Pack Of 3 Minnie Mouse Printed Extended Sleeves T-shirt','K','9-10','2024-12-17',469,3),(38,'H&M','CLOTH','Girls Clothing Tops T-Shirts','K','9-10','2024-12-17',469,3),(39,'H&M','CLOTH','Girls Clothing Tops T-Shirts','K','11-12','2024-12-17',480,3),(40,'H&M','CLOTH','Flared Low Jeans','F','34','2024-12-17',800,3),(41,'H&M','CLOTH','Flared Low Jeans','F','36','2024-12-17',800,3),(42,'The Souled Store','CLOTH','Pink Panther Printed Drop-Shoulder Sleeves Cotton Oversized T-shirt','F','L','2024-12-17',500,3),(43,'The Souled Store','CLOTH','Pink Panther Printed Drop-Shoulder Sleeves Cotton Oversized T-shirt','F','XL','2024-12-17',550,3),(44,'The Souled Store','CLOTH','Pink Panther Printed Drop-Shoulder Sleeves Cotton Oversized T-shirt','F','XXL','2024-12-17',650,3),(45,'DILLINGER','CLOTH','Graphic Printed Oversized Pure Cotton T-Shirt','F','L','2024-12-17',391,3),(46,'DILLINGER','CLOTH','Graphic Printed Oversized Pure Cotton T-Shirt','F','XXL','2024-12-17',550,3),(47,'Basics By Tokyo Talkies','CLOTH','Women Flared Clean Look Stretchable Jeans','F','32','2024-12-17',800,3),(48,'Basics By Tokyo Talkies','CLOTH','Women Flared Clean Look Stretchable Jeans','F','34','2024-12-17',900,3),(49,'Basics By Tokyo Talkies','CLOTH','Women Flared Clean Look Stretchable Jeans','F','36','2024-12-17',1100,3),(50,'Harvard','CLOTH','Women Blue Wide Leg High-Rise Low Distress Light Fade Jeans','F','34','2024-12-17',1100,0),(51,'Harvard','CLOTH','Women Blue Wide Leg High-Rise Low Distress Light Fade Jeans','F','36','2024-12-17',1200,1);
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-29 18:28:51
