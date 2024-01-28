-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: 02 ديسمبر 2023 الساعة 10:38
-- إصدار الخادم: 10.4.22-MariaDB
-- PHP Version: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `CrimeAnalysis`
--

-- --------------------------------------------------------

--
-- بنية الجدول `crime_data_analysis`
--

CREATE TABLE `crime_data_analysis` (
  `CrimeType` varchar(255) DEFAULT NULL,
  `Location` varchar(255) DEFAULT NULL,
  `Date`  Timestamp DEFAULT NULL,
  `CrimeCount` int(11) DEFAULT NULL
 
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------
--
-- بنية الجدول `victim_analysis`
--
CREATE TABLE `victim_analysis` (
    `VictimAge` int(11) DEFAULT NULL,
    `VictimGender` varchar(255) DEFAULT NULL,
  `InjuryType` varchar(255) DEFAULT NULL,  
  `TotalCrimes` int(11) DEFAULT NULL,
  `AvgPoliceResponseTime` FLOAT DEFAULT NULL

) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

 
-- --------------------------------------------------------

--
-- بنية الجدول `demographic_data_analysis`
--

CREATE TABLE `demographic_data_analysis` (
  `Name` varchar(255) DEFAULT NULL,
  `VictimName` varchar(255) DEFAULT NULL,
  `ArrestLocation` varchar(255) DEFAULT NULL,
  `InjuryType` varchar(255) DEFAULT NULL,  
  `CrimeCount` int(11) DEFAULT NULL,

 
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------
-- --------------------------------------------------------
--
-- بنية الجدول `Police_response_time_analysis`
--
CREATE TABLE `Police_response_time_analysis` (
  `WeatherConditions` varchar(255) DEFAULT NULL,
  `InjuryType` varchar(255) DEFAULT NULL,  
  `AvgPoliceResponseTime` FLOAT DEFAULT NULL

) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
-- --------------------------------------------------------

-- --------------------------------------------------------
--
-- بنية الجدول `Arrested_data_analysis`
--
CREATE TABLE `Arrested_data_analysis` (
  `Charges` varchar(255) DEFAULT NULL,
  `Gender` varchar(255) DEFAULT NULL,  
  `Addres` varchar(255) DEFAULT NULL,
  `Age` Int(11) DEFAULT NULL,
  'TotalCharges' Int(11) DEFAULT NULL,
  `AvgAgeArrested` FLOAT DEFAULT NULL

) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
-- --------------------------------------------------------

--
-- بنية الجدول `witness_evidence_analysis`
-- 

CREATE TABLE `witness_evidence_analysis` (
  `Witnesses` Boolean DEFAULT NULL,
  `EvidenceCollected` Boolean DEFAULT NULL,
  `Location` varchar(255) DEFAULT NULL,  
  `TotalCrimes` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;