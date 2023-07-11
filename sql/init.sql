
CREATE DATABASE wordslearn;

USE wordslearn;

CREATE TABLE `user` (
  `id` int unsigned NOT NULL AUTO_INCREMENT COMMENT 'id',
  `username` char(32) NOT NULL COMMENT '用户名',
  `password` varchar(256) NOT NULL COMMENT '密码-可以使用SHA256',
  `salt` char(32) NOT NULL COMMENT '密码加盐',
  `isadmin` tinyint(1) NOT NULL DEFAULT '0' COMMENT '是否管理员',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB CHARSET=utf8mb4;