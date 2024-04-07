-- ctlrmix_imoj.campaigns definition

CREATE TABLE `campaigns` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `company_id` int(11) NOT NULL,
  `type` tinyint(4) NOT NULL,
  `status` tinyint(4) NOT NULL,
  `advert_id` int(10) unsigned NOT NULL,
  `change_time` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `advert_id_company_id` (`advert_id`,`company_id`),
  KEY `company_id` (`company_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


-- ctlrmix_imoj.campaign_stats definition

CREATE TABLE `campaign_stats` (
  `advert_id` int(10) unsigned NOT NULL,
  `stat_date` date NOT NULL,
  `app_type` tinyint(3) unsigned NOT NULL,
  `card_nmID` bigint(20) unsigned NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `card_id` bigint(20) unsigned DEFAULT NULL,
  `views` int(10) unsigned NOT NULL,
  `clicks` int(10) unsigned NOT NULL,
  `ctr` decimal(6,2) NOT NULL,
  `cpc` decimal(8,2) NOT NULL,
  `sum` decimal(8,2) NOT NULL,
  `atbs` int(10) unsigned NOT NULL,
  `orders` int(10) unsigned NOT NULL,
  `cr` int(10) unsigned NOT NULL,
  `shks` int(10) unsigned NOT NULL,
  `sum_price` decimal(10,2) NOT NULL,
  PRIMARY KEY (`advert_id`,`stat_date`,`app_type`,`card_nmID`),
  KEY `card_id` (`card_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;