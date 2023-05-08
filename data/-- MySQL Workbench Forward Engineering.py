-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema proyecto_etl
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema proyecto_etl
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `proyecto_etl` DEFAULT CHARACTER SET utf8mb3 ;
USE `proyecto_etl` ;

-- -----------------------------------------------------
-- Table `proyecto_etl`.`actor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proyecto_etl`.`actor` (
  `Actor_id` INT NOT NULL,
  `Name` VARCHAR(200) NULL DEFAULT NULL,
  PRIMARY KEY (`Actor_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `proyecto_etl`.`film`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proyecto_etl`.`film` (
  `Film_id` INT NOT NULL,
  `Title` VARCHAR(200) NULL DEFAULT NULL,
  `Premiere` VARCHAR(200) NULL DEFAULT NULL,
  `Runtime` VARCHAR(200) NULL DEFAULT NULL,
  `Genres` VARCHAR(200) NULL DEFAULT NULL,
  `Language` VARCHAR(200) NULL DEFAULT NULL,
  `Type` VARCHAR(45) NULL DEFAULT NULL,
  `Description` VARCHAR(500) NULL DEFAULT NULL,
  `Age_certification` VARCHAR(50) NULL DEFAULT NULL,
  `IMDB_id` VARCHAR(45) NULL DEFAULT NULL,
  `IMDB_score` VARCHAR(45) NULL DEFAULT NULL,
  `IMDB_votes` VARCHAR(45) NULL DEFAULT NULL,
  `TMDB_score` VARCHAR(45) NULL DEFAULT NULL,
  `TMDB_votes` VARCHAR(45) NULL DEFAULT NULL,
  `comentarios` LONGTEXT NULL DEFAULT NULL,
  PRIMARY KEY (`Film_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `proyecto_etl`.`reparto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proyecto_etl`.`reparto` (
  `Reparto_id` INT NOT NULL,
  `Film_id` INT NULL DEFAULT NULL,
  `Actor_id` INT NULL DEFAULT NULL,
  `Character` VARCHAR(200) NULL DEFAULT NULL,
  `Role` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`Reparto_id`),
  INDEX `fk_pelicula` (`Film_id` ASC) VISIBLE,
  INDEX `fk_actor` (`Actor_id` ASC) VISIBLE,
  CONSTRAINT `fk_actor`
    FOREIGN KEY (`Actor_id`)
    REFERENCES `proyecto_etl`.`actor` (`Actor_id`),
  CONSTRAINT `fk_pelicula`
    FOREIGN KEY (`Film_id`)
    REFERENCES `proyecto_etl`.`film` (`Film_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
