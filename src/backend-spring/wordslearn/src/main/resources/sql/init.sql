CREATE DATABASE springmybatistest;

USE springmybatistest;

CREATE TABLE users (
  id int unsigned NOT NULL AUTO_INCREMENT COMMENT 'id',
  username char(25) NOT NULL COMMENT '用户名',
  password char(255) NOT NULL COMMENT '密码',
  is_admin tinyint(1) NOT NULL DEFAULT 0 COMMENT '是否管理员',
  PRIMARY KEY (id)
)CHARSET=utf8mb4;