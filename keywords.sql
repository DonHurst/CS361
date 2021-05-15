CREATE TABLE `keywordsRaw`(
	`id` int(11) NOT NULL,
	`title` varchar(255) NOT NULL,
	`jsonString` varchar(8001) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `keywordsList`(
	`id` int(11) NOT NULL,
	`title` varchar(255) NOT NULL,
	`jsonString` varchar(8001) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE `keywordsRaw`
  ADD PRIMARY KEY (`id`);

  ALTER TABLE `keywordsList`
  ADD PRIMARY KEY (`id`);