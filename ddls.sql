-- ctlrmix_imoj.campaigns definition
CREATE TABLE `campaigns` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `company_id` int(11) NOT NULL,
  `type` int(10) unsigned NOT NULL,
  `status` int(11) NOT NULL,
  `advert_id` int(10) unsigned NOT NULL,
  `change_time` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `advert_id_company_id` (`advert_id`,`company_id`),
  KEY `company_id` (`company_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;