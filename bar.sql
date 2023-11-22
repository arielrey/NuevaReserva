-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema bar
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema bar
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `bar` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `bar` ;

-- -----------------------------------------------------
-- Table `bar`.`cliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bar`.`cliente` (
  `id_cliente` INT NOT NULL auto_increment,
  `nombre` VARCHAR(45) NOT NULL,
  `apellido` VARCHAR(45) NOT NULL,
  `dni` varchar(45) not null,
  `telefono` INT NOT NULL,
  PRIMARY KEY (`id_cliente`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `bar`.`mesa`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bar`.`mesa` (
  `id_mesa` INT NOT NULL,
  `descripcion` VARCHAR(20),
  PRIMARY KEY (`id_mesa`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `bar`.`reserva`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bar`.`reserva` (
  `id_reserva` INT NOT NULL auto_increment,
  `id_mesa` INT NOT NULL,
  `id_cliente` INT NOT NULL,
  `fecha` date  NOT NULL,
  `hora` time  NOT NULL,
  PRIMARY KEY (`id_reserva`),
  INDEX `id_mesa_idx` (`id_mesa` ASC) VISIBLE,
  INDEX `id_cliente_idx` (`id_cliente` ASC) VISIBLE,
  CONSTRAINT `id_cliente`
    FOREIGN KEY (`id_cliente`)
    REFERENCES `bar`.`cliente` (`id_cliente`),
  CONSTRAINT `id_mesa`
    FOREIGN KEY (`id_mesa`)
    REFERENCES `bar`.`mesa` (`id_mesa`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;


-- INSERTS NECESARIOS --
INSERT INTO mesa (id_mesa, descripcion) VALUES (1,"familiar"),(2,"una persona"),(3,"pareja");


-- -----------------------------------------
-- SEGUNDO DB RESP. --
-- -----------------------------------------

-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema bar
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema bar
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `bar` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `bar` ;

-- -----------------------------------------------------
-- Table `bar`.`cliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bar`.`cliente` (
  `id_cliente` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `apellido` VARCHAR(45) NOT NULL,
  `dni` VARCHAR(45) NOT NULL,
  `telefono` INT NOT NULL,
  PRIMARY KEY (`id_cliente`))
ENGINE = InnoDB
AUTO_INCREMENT = 17
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `bar`.`mesa`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bar`.`mesa` (
  `id_mesa` INT NOT NULL,
  `descripcion` VARCHAR(20) NULL DEFAULT NULL,
  PRIMARY KEY (`id_mesa`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `bar`.`reserva`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bar`.`reserva` (
  `id_reserva` INT NOT NULL AUTO_INCREMENT,
  `id_mesa` INT NOT NULL,
  `id_cliente` INT NOT NULL,
  `fecha` DATE NOT NULL,
  `hora` TIME NOT NULL,
  PRIMARY KEY (`id_reserva`),
  INDEX `id_mesa_idx` (`id_mesa` ASC) VISIBLE,
  INDEX `id_cliente_idx` (`id_cliente` ASC) VISIBLE,
  CONSTRAINT `id_cliente`
    FOREIGN KEY (`id_cliente`)
    REFERENCES `bar`.`cliente` (`id_cliente`),
  CONSTRAINT `id_mesa`
    FOREIGN KEY (`id_mesa`)
    REFERENCES `bar`.`mesa` (`id_mesa`))
ENGINE = InnoDB
AUTO_INCREMENT = 14
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
