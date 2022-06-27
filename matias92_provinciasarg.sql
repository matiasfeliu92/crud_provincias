-- phpMyAdmin SQL Dump
-- version 5.1.4
-- https://www.phpmyadmin.net/
--
-- Host: mysql-matias92.alwaysdata.net
-- Generation Time: Jun 27, 2022 at 11:04 PM
-- Server version: 10.6.7-MariaDB
-- PHP Version: 7.4.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `matias92_provinciasarg`
--

-- --------------------------------------------------------

--
-- Table structure for table `ciudades`
--

CREATE TABLE `ciudades` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `poblacion_hab` int(11) NOT NULL,
  `superficie_km2` int(11) NOT NULL,
  `ref_ciudad` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `ciudades`
--

INSERT INTO `ciudades` (`id`, `nombre`, `poblacion_hab`, `superficie_km2`, `ref_ciudad`) VALUES
(1, 'La Plata', 193144, 27, 9),
(2, 'Rio Gallegos', 107000, 61, 3),
(3, 'Olavarria', 290723, 56, 9);

-- --------------------------------------------------------

--
-- Stand-in structure for view `gfdhfdh`
-- (See below for the actual view)
--
CREATE TABLE `gfdhfdh` (
);

-- --------------------------------------------------------

--
-- Table structure for table `provincias`
--

CREATE TABLE `provincias` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `superficie_km2` int(11) NOT NULL,
  `region` varchar(50) NOT NULL,
  `densidad (hab)` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `provincias`
--

INSERT INTO `provincias` (`id`, `nombre`, `superficie_km2`, `region`, `densidad (hab)`) VALUES
(1, 'Catamarca', 102602, 'Noroeste', 396895),
(2, 'San Luis', 76748, 'Cuyo', 502003),
(3, 'Santa Cruz', 243943, 'Patagonia ', 273964),
(4, 'Chaco', 99633, 'Noreste', 1192616),
(5, 'Cordoba', 165310, 'Sierras', 3798261),
(7, 'Entre Rios', 78781, 'Litoral', 1405890),
(9, 'Buenos Aires', 4543654, 'Centro', 543546),
(10, 'Corrientes', 4543654, 'Noreste', 543546);

-- --------------------------------------------------------

--
-- Structure for view `gfdhfdh`
--
DROP TABLE IF EXISTS `gfdhfdh`;

CREATE ALGORITHM=UNDEFINED DEFINER=`matias92`@`%` SQL SECURITY DEFINER VIEW `gfdhfdh`  AS SELECT `provincias`.`id` AS `id`, `provincias`.`nombre` AS `nombre`, `provincias`.`superficie (km2)` AS `superficie (km2)`, `provincias`.`region` AS `region`, `provincias`.`densidad (hab)` AS `densidad (hab)` FROM `provincias``provincias`  ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `ciudades`
--
ALTER TABLE `ciudades`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`),
  ADD KEY `nombre_2` (`nombre`),
  ADD KEY `FKciudad` (`ref_ciudad`);

--
-- Indexes for table `provincias`
--
ALTER TABLE `provincias`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`),
  ADD KEY `nombre_2` (`nombre`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `ciudades`
--
ALTER TABLE `ciudades`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `provincias`
--
ALTER TABLE `provincias`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `ciudades`
--
ALTER TABLE `ciudades`
  ADD CONSTRAINT `FKciudad` FOREIGN KEY (`ref_ciudad`) REFERENCES `provincias` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
