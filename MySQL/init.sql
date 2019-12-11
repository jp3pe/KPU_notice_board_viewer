-- DB 생성
CREATE SCHEMA `kpu` DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;
-- Table 생성=
CREATE TABLE `kpu`.`bulletin_board` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(100) CHARACTER SET 'utf8' COLLATE 'utf8_unicode_ci' NOT NULL,
  `content` MEDIUMTEXT CHARACTER SET 'utf8' COLLATE 'utf8_unicode_ci' NOT NULL,
  PRIMARY KEY (`id`)
);