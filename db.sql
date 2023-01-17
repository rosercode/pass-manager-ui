CREATE DATABASE `account_db`;
use `account_db`

CREATE TABLE `account` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'id 主键',
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '密码字段更新时间',
  `info` varchar(255)  DEFAULT NULL COMMENT '简介',
  `nickname` varchar(100)  DEFAULT NULL COMMENT '昵称',
  `account` varchar(255)  DEFAULT NULL COMMENT '账号',
  `password` varchar(255)  DEFAULT NULL COMMENT '密码',
  `website` varchar(255)  DEFAULT NULL COMMENT '网址',
  `bind_email` varchar(255)  DEFAULT NULL COMMENT '绑定邮箱',
  `bind_phone` varchar(255)  DEFAULT NULL COMMENT '绑定手机号码',
  `comment` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) COMMENT='密码表';