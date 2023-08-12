
CREATE DATABASE wordslearn;

USE wordslearn;

CREATE TABLE `users` (
  `id` int unsigned NOT NULL AUTO_INCREMENT COMMENT 'id',
  `username` char(16) NOT NULL COMMENT '用户名',
  `password` char(64) NOT NULL COMMENT '密码-可以使用SHA256',
  `salt` char(8) NOT NULL COMMENT '密码加盐',
  `isadmin` tinyint(1) NOT NULL DEFAULT '0' COMMENT '是否管理员',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB CHARSET=utf8mb4;

CREATE TABLE `words` (
  `id` int unsigned NOT NULL AUTO_INCREMENT COMMENT 'id',
  `word` char(64) NOT NULL COMMENT '单词',
  `pronounce` char(64) COMMENT '音标',
  `chinese` char(128) COMMENT '中文',
  `note` char(255) COMMENT '备注',
  `type` tinyint(1) NOT NULL COMMENT '单词类型 1-单词 0-词组',
  `sound_id` int COMMENT '音频id',
  `sound_start` float COMMENT '音频开始时间',
  `sound_end` float COMMENT '音频结束时间',
  `groupid` int NOT NULL COMMENT '所属组id',
  `bookid` int NOT NULL COMMENT '所属书id',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB CHARSET=utf8mb4;

CREATE TABLE `groups` (
  `id` int unsigned NOT NULL AUTO_INCREMENT COMMENT 'id',
  `name` char(32) NOT NULL COMMENT '组名称',
  `bookid` int NOT NULL COMMENT '所属书id',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB CHARSET=utf8mb4;

CREATE TABLE `books` (
  `id` int unsigned NOT NULL AUTO_INCREMENT COMMENT 'id',
  `name` char(32) NOT NULL COMMENT '书名称',
  `description` char(255) COMMENT '书描述',
  `cover` varchar(2048) COMMENT '书封面 url',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB CHARSET=utf8mb4;

CREATE TABLE `sounds` (
  `id` int unsigned NOT NULL AUTO_INCREMENT COMMENT 'id',
  `url` varchar(2048) NOT NULL COMMENT '音频url',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB CHARSET=utf8mb4;

