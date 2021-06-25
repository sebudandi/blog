CREATE TABLE IF NOT EXISTS `blogtable` 
(
    `id` INT NOT NULL AUTO_INCREMENT,
    `author` TEXT NOT NULL,
    `title` TEXT NOT NULL,
    `article` TEXT DEFAULT NULL,
    `postdate` DATE DEFAULT NULL,
    
    PRIMARY KEY (`id`)
)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;



