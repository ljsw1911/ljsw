/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50717
Source Host           : localhost:3306
Source Database       : ljsw

Target Server Type    : MYSQL
Target Server Version : 50717
File Encoding         : 65001

Date: 2020-05-18 10:09:13
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for activity
-- ----------------------------
DROP TABLE IF EXISTS `activity`;
CREATE TABLE `activity` (
  `activity_id` int(10) NOT NULL AUTO_INCREMENT,
  `activity_name` varchar(255) DEFAULT NULL,
  `activity_type` varchar(255) NOT NULL,
  `discount` float(20,3) DEFAULT NULL,
  `enough_price` float(20,2) DEFAULT NULL,
  `points` float(255,3) DEFAULT NULL,
  `ending_time` datetime NOT NULL,
  PRIMARY KEY (`activity_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of activity
-- ----------------------------
INSERT INTO `activity` VALUES ('1', '打7折活动', '打折', '0.700', '0.00', null, '2020-07-15 09:55:00');
INSERT INTO `activity` VALUES ('2', '满200减20', '打折', '0.800', '200.00', null, '2020-08-15 08:56:56');
INSERT INTO `activity` VALUES ('3', '返积分', '返积分', null, '0.00', '0.100', '2020-09-15 08:58:28');
INSERT INTO `activity` VALUES ('4', '打9折活动', '打折', '0.900', '0.00', null, '2020-08-15 09:55:00');
INSERT INTO `activity` VALUES ('5', '满500减250', '打折', '0.500', '500.00', null, '2020-08-15 08:56:56');
INSERT INTO `activity` VALUES ('6', '返积分', '返积分', null, '0.00', '0.200', '2020-09-15 08:58:28');

-- ----------------------------
-- Table structure for addres
-- ----------------------------
DROP TABLE IF EXISTS `addres`;
CREATE TABLE `addres` (
  `address_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `estate` varchar(255) DEFAULT NULL,
  `building` varchar(255) DEFAULT NULL,
  `identity` int(11) DEFAULT '0',
  `room` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`address_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of addres
-- ----------------------------
INSERT INTO `addres` VALUES ('1', '13', '瓦罗兰大陆', '德玛西亚', '1', '101');
INSERT INTO `addres` VALUES ('2', '13', '艾欧尼亚大陆', '艾欧尼亚', '0', '110');
INSERT INTO `addres` VALUES ('3', '13', '瓦罗兰大陆', '诺克萨斯', '1', '101');

-- ----------------------------
-- Table structure for article_pub
-- ----------------------------
DROP TABLE IF EXISTS `article_pub`;
CREATE TABLE `article_pub` (
  `article_id` int(11) NOT NULL AUTO_INCREMENT,
  `article_title` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `article_main` longtext COLLATE utf8_bin,
  `article_datatime` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `author_id` int(11) DEFAULT NULL COMMENT '和uer_id表进行俩表查询',
  `category_id` int(11) DEFAULT NULL,
  `article_pic` longtext COLLATE utf8_bin,
  PRIMARY KEY (`article_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of article_pub
-- ----------------------------
INSERT INTO `article_pub` VALUES ('1', '这是什么', 0xE8BF99E4B8AAE4B89CE8A5BFE5BE88E5A5BDE79C8BEFBC8CE4B88DE5A4A7E4B88DE59C86E6ADA3E6ADA3E5A5BD, '2020-05-15 15:46:43', '2', '0', null);
INSERT INTO `article_pub` VALUES ('3', '还行吧', 0xE595A6E595A6E595A6E595A6E5958A, '2020-05-15 15:46:47', '0', '1', null);
INSERT INTO `article_pub` VALUES ('4', '垃圾怎么分类', 0xE8BF99E4B8AAE69687E7ABA0E8AFA5E58699E595A5E5B0B1E58699E595A5E590A7, '2020-05-15 15:46:48', '4', '1', null);
INSERT INTO `article_pub` VALUES ('5', '这咋整', 0xE8BF99E6A0B7E698AFE4B88DE698AFE58FAFE4BBA5E58699E8BF9BE58EBBE591A2EFBC9FEFBC9FEFBC9F, '2020-05-15 15:46:49', '4', '1', null);
INSERT INTO `article_pub` VALUES ('6', '呼啦啦啦呼啦啦', 0xE5868DE58699E4B880E7AF87E69687E7ABA0E590A7EFBC8CE5B0B1E58699E8BF99E4B988E5A49AE590A7, '2020-05-17 16:18:12', '4', '2', 0x687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F466C58375F355F646C544245536861654A6D704A74316A696D4F5F4D2C687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F4676374773457359596D47496C37677468485242795335735F4745472C687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F46753833736A74334B4531316C476F304A684B6A466E5233504A3975);
INSERT INTO `article_pub` VALUES ('7', '苏喂苏喂苏苏为', 0xE8BF98E695A2E5868DE58699E782B9E588ABE79A84E4B88D, '2020-05-17 16:20:10', '4', '2', 0x687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F466C58375F355F646C544245536861654A6D704A74316A696D4F5F4D2C687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F4676374773457359596D47496C37677468485242795335735F4745472C687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F46753833736A74334B4531316C476F304A684B6A466E5233504A39752C687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F466B723470514E5953593073674270326C345667356F4F4D623244432C687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F466C58375F355F646C544245536861654A6D704A74316A696D4F5F4D2C687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F4676374773457359596D47496C37677468485242795335735F474547);
INSERT INTO `article_pub` VALUES ('8', '文章8', 0xE58685E5AEB938, '2020-05-15 15:49:34', '8', '3', null);
INSERT INTO `article_pub` VALUES ('9', '文章9', 0xE58685E5AEB939, '2020-05-15 15:49:36', '2', '4', null);
INSERT INTO `article_pub` VALUES ('10', '文章10', 0xE58685E5AEB93130, '2020-05-15 15:49:38', '5', '4', null);
INSERT INTO `article_pub` VALUES ('11', '文章11', 0xE58685E5AEB93131, '2020-05-15 15:49:45', '5', '4', null);
INSERT INTO `article_pub` VALUES ('12', '文章12', 0xE58685E5AEB93132, '2020-05-15 15:49:46', '6', '4', null);
INSERT INTO `article_pub` VALUES ('13', '垃圾分类怎么回收', 0xE4BDA0E8AFB4E5928BE59B9EE694B6E5B0B1E5928BE59B9EE694B6EFBC8CE997AEE997AEE7B1BBE8819AE8AF86E789A9E5B0B1E5A5BDE595A6, '2020-05-17 16:17:58', '8', '2', 0x687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F466C58375F355F646C544245536861654A6D704A74316A696D4F5F4D2C687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F4676374773457359596D47496C37677468485242795335735F4745472C687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F46753833736A74334B4531316C476F304A684B6A466E5233504A39752C687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F466B723470514E5953593073674270326C345667356F4F4D62324443);
INSERT INTO `article_pub` VALUES ('14', '大树各自挺高', 0xE69C89E6A091E58FB6EFBC8CE69C89E6A091E5B9B2EFBC8CE69C89E5B08FE88D89E79A84E999AAE4BCB4, '2020-05-17 16:08:38', '8', '2', 0x687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F466C58375F355F646C544245536861654A6D704A74316A696D4F5F4D2C687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F4676374773457359596D47496C37677468485242795335735F4745472C687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F46753833736A74334B4531316C476F304A684B6A466E5233504A39752C687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F466B723470514E5953593073674270326C345667356F4F4D62324443);
INSERT INTO `article_pub` VALUES ('15', '今天天气不错', 0xE59388E59388E59388EFBC8CE79C9FE79A84E4B88DE99499E5958A, '2020-05-15 15:46:40', '1', '0', null);

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`) USING BTREE,
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`) USING BTREE,
  CONSTRAINT `auth_group_permissions_ibfk_1` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_ibfk_2` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`) USING BTREE,
  CONSTRAINT `auth_permission_ibfk_1` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can view log entry', '1', 'view_logentry');
INSERT INTO `auth_permission` VALUES ('5', 'Can add permission', '2', 'add_permission');
INSERT INTO `auth_permission` VALUES ('6', 'Can change permission', '2', 'change_permission');
INSERT INTO `auth_permission` VALUES ('7', 'Can delete permission', '2', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('8', 'Can view permission', '2', 'view_permission');
INSERT INTO `auth_permission` VALUES ('9', 'Can add group', '3', 'add_group');
INSERT INTO `auth_permission` VALUES ('10', 'Can change group', '3', 'change_group');
INSERT INTO `auth_permission` VALUES ('11', 'Can delete group', '3', 'delete_group');
INSERT INTO `auth_permission` VALUES ('12', 'Can view group', '3', 'view_group');
INSERT INTO `auth_permission` VALUES ('13', 'Can add user', '4', 'add_user');
INSERT INTO `auth_permission` VALUES ('14', 'Can change user', '4', 'change_user');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete user', '4', 'delete_user');
INSERT INTO `auth_permission` VALUES ('16', 'Can view user', '4', 'view_user');
INSERT INTO `auth_permission` VALUES ('17', 'Can add content type', '5', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('18', 'Can change content type', '5', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('19', 'Can delete content type', '5', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('20', 'Can view content type', '5', 'view_contenttype');
INSERT INTO `auth_permission` VALUES ('21', 'Can add session', '6', 'add_session');
INSERT INTO `auth_permission` VALUES ('22', 'Can change session', '6', 'change_session');
INSERT INTO `auth_permission` VALUES ('23', 'Can delete session', '6', 'delete_session');
INSERT INTO `auth_permission` VALUES ('24', 'Can view session', '6', 'view_session');
INSERT INTO `auth_permission` VALUES ('25', 'Can add addres', '7', 'add_addres');
INSERT INTO `auth_permission` VALUES ('26', 'Can change addres', '7', 'change_addres');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete addres', '7', 'delete_addres');
INSERT INTO `auth_permission` VALUES ('28', 'Can view addres', '7', 'view_addres');
INSERT INTO `auth_permission` VALUES ('29', 'Can add detailed points', '8', 'add_detailedpoints');
INSERT INTO `auth_permission` VALUES ('30', 'Can change detailed points', '8', 'change_detailedpoints');
INSERT INTO `auth_permission` VALUES ('31', 'Can delete detailed points', '8', 'delete_detailedpoints');
INSERT INTO `auth_permission` VALUES ('32', 'Can view detailed points', '8', 'view_detailedpoints');
INSERT INTO `auth_permission` VALUES ('33', 'Can add user', '9', 'add_user');
INSERT INTO `auth_permission` VALUES ('34', 'Can change user', '9', 'change_user');
INSERT INTO `auth_permission` VALUES ('35', 'Can delete user', '9', 'delete_user');
INSERT INTO `auth_permission` VALUES ('36', 'Can view user', '9', 'view_user');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`) USING BTREE,
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`) USING BTREE,
  CONSTRAINT `auth_user_groups_ibfk_1` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`) USING BTREE,
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`) USING BTREE,
  CONSTRAINT `auth_user_user_permissions_ibfk_1` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for category
-- ----------------------------
DROP TABLE IF EXISTS `category`;
CREATE TABLE `category` (
  `category_id` int(11) NOT NULL,
  `category_name` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of category
-- ----------------------------
INSERT INTO `category` VALUES ('0', '关注');
INSERT INTO `category` VALUES ('1', '推荐');
INSERT INTO `category` VALUES ('2', '社区');
INSERT INTO `category` VALUES ('3', '新闻');
INSERT INTO `category` VALUES ('4', '视频');

-- ----------------------------
-- Table structure for collection
-- ----------------------------
DROP TABLE IF EXISTS `collection`;
CREATE TABLE `collection` (
  `coll_id` int(11) NOT NULL AUTO_INCREMENT,
  `article_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`coll_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of collection
-- ----------------------------
INSERT INTO `collection` VALUES ('1', '1', '1');
INSERT INTO `collection` VALUES ('2', '1', '3');
INSERT INTO `collection` VALUES ('3', '1', '4');
INSERT INTO `collection` VALUES ('4', '0', '2');
INSERT INTO `collection` VALUES ('5', '1', '5');
INSERT INTO `collection` VALUES ('6', '1', '8');
INSERT INTO `collection` VALUES ('7', '0', '10');
INSERT INTO `collection` VALUES ('8', '0', '0');

-- ----------------------------
-- Table structure for comments
-- ----------------------------
DROP TABLE IF EXISTS `comments`;
CREATE TABLE `comments` (
  `comm_id` int(11) NOT NULL AUTO_INCREMENT,
  `comment` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `article_id` int(11) DEFAULT NULL COMMENT '文章id',
  `comment_user_id` int(11) DEFAULT NULL COMMENT '评论人的id',
  PRIMARY KEY (`comm_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of comments
-- ----------------------------
INSERT INTO `comments` VALUES ('1', '写的真好', '0', '3');
INSERT INTO `comments` VALUES ('2', '不错不错', '1', '5');
INSERT INTO `comments` VALUES ('3', '还可以哟', '0', '2');
INSERT INTO `comments` VALUES ('4', '哎哟哟', '1', '6');
INSERT INTO `comments` VALUES ('5', '丢丢丢', '3', '4');
INSERT INTO `comments` VALUES ('6', 'come on', '3', '6');
INSERT INTO `comments` VALUES ('7', '加油', '3', '2');
INSERT INTO `comments` VALUES ('8', '还行吧', '3', '3');

-- ----------------------------
-- Table structure for detailed_points
-- ----------------------------
DROP TABLE IF EXISTS `detailed_points`;
CREATE TABLE `detailed_points` (
  `data_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `point_type` varchar(255) DEFAULT NULL,
  `points_time` datetime DEFAULT NULL,
  `points_num` int(11) DEFAULT NULL,
  PRIMARY KEY (`data_id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of detailed_points
-- ----------------------------
INSERT INTO `detailed_points` VALUES ('1', '13', '手机注册', '2020-05-15 00:09:56', '200');
INSERT INTO `detailed_points` VALUES ('2', '13', '每日首次登陆', '2020-05-15 14:11:32', '50');
INSERT INTO `detailed_points` VALUES ('5', '13', '每日首次登陆', '2020-05-15 14:23:47', '50');
INSERT INTO `detailed_points` VALUES ('6', '13', '兑换1积分', '2020-05-15 16:03:34', '1');
INSERT INTO `detailed_points` VALUES ('7', '13', '每日首次登陆', '2020-05-15 16:04:21', '50');
INSERT INTO `detailed_points` VALUES ('8', '13', '兑换99积分', '2020-05-15 16:04:30', '99');
INSERT INTO `detailed_points` VALUES ('9', '13', '兑换0积分', '2020-05-15 16:04:43', '0');
INSERT INTO `detailed_points` VALUES ('10', '13', '兑换100积分', '2020-05-15 16:06:46', '100');
INSERT INTO `detailed_points` VALUES ('11', '13', '兑换0积分', '2020-05-15 16:06:58', '0');
INSERT INTO `detailed_points` VALUES ('12', '13', '兑换0积分', '2020-05-15 16:07:10', '0');
INSERT INTO `detailed_points` VALUES ('13', '13', '兑换0积分', '2020-05-15 16:07:13', '0');
INSERT INTO `detailed_points` VALUES ('14', '13', '兑换0积分', '2020-05-15 16:14:21', '0');
INSERT INTO `detailed_points` VALUES ('15', '13', '兑换0积分', '2020-05-15 16:14:59', '0');
INSERT INTO `detailed_points` VALUES ('16', '13', '兑换0积分', '2020-05-15 16:44:17', '0');
INSERT INTO `detailed_points` VALUES ('17', '13', '兑换0积分', '2020-05-15 16:48:23', '0');
INSERT INTO `detailed_points` VALUES ('18', '13', '兑换0积分', '2020-05-15 16:48:59', '0');
INSERT INTO `detailed_points` VALUES ('19', '13', '兑换0积分', '2020-05-15 16:49:00', '0');
INSERT INTO `detailed_points` VALUES ('20', '13', '兑换0积分', '2020-05-15 16:49:01', '0');
INSERT INTO `detailed_points` VALUES ('21', '13', '兑换0积分', '2020-05-15 16:49:33', '0');

-- ----------------------------
-- Table structure for discount
-- ----------------------------
DROP TABLE IF EXISTS `discount`;
CREATE TABLE `discount` (
  `discount_id` int(10) NOT NULL AUTO_INCREMENT,
  `goods_id` int(10) NOT NULL,
  `activity_id` int(10) NOT NULL,
  PRIMARY KEY (`discount_id`,`goods_id`,`activity_id`) USING BTREE,
  KEY `goods_id` (`goods_id`),
  KEY `activity_id` (`activity_id`),
  CONSTRAINT `discount_ibfk_1` FOREIGN KEY (`goods_id`) REFERENCES `goods` (`goods_id`) ON DELETE CASCADE,
  CONSTRAINT `discount_ibfk_2` FOREIGN KEY (`activity_id`) REFERENCES `activity` (`activity_id`) ON DELETE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of discount
-- ----------------------------
INSERT INTO `discount` VALUES ('1', '1', '1');
INSERT INTO `discount` VALUES ('2', '1', '3');
INSERT INTO `discount` VALUES ('13', '1', '4');
INSERT INTO `discount` VALUES ('3', '2', '1');
INSERT INTO `discount` VALUES ('9', '2', '2');
INSERT INTO `discount` VALUES ('14', '2', '3');
INSERT INTO `discount` VALUES ('4', '3', '1');
INSERT INTO `discount` VALUES ('8', '3', '3');
INSERT INTO `discount` VALUES ('10', '3', '2');
INSERT INTO `discount` VALUES ('15', '3', '3');
INSERT INTO `discount` VALUES ('5', '4', '1');
INSERT INTO `discount` VALUES ('11', '4', '2');
INSERT INTO `discount` VALUES ('6', '5', '1');
INSERT INTO `discount` VALUES ('7', '6', '2');
INSERT INTO `discount` VALUES ('12', '7', '2');

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`) USING BTREE,
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`) USING BTREE,
  CONSTRAINT `django_admin_log_ibfk_1` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('4', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('5', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('6', 'sessions', 'session');
INSERT INTO `django_content_type` VALUES ('7', 'user', 'addres');
INSERT INTO `django_content_type` VALUES ('8', 'user', 'detailedpoints');
INSERT INTO `django_content_type` VALUES ('9', 'user', 'user');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2020-05-12 22:40:14.889114');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2020-05-12 22:40:15.024248');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0001_initial', '2020-05-12 22:40:15.411129');
INSERT INTO `django_migrations` VALUES ('4', 'admin', '0002_logentry_remove_auto_add', '2020-05-12 22:40:15.494287');
INSERT INTO `django_migrations` VALUES ('5', 'admin', '0003_logentry_add_action_flag_choices', '2020-05-12 22:40:15.504310');
INSERT INTO `django_migrations` VALUES ('6', 'contenttypes', '0002_remove_content_type_name', '2020-05-12 22:40:15.578995');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0002_alter_permission_name_max_length', '2020-05-12 22:40:15.626398');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0003_alter_user_email_max_length', '2020-05-12 22:40:15.679644');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0004_alter_user_username_opts', '2020-05-12 22:40:15.690435');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0005_alter_user_last_login_null', '2020-05-12 22:40:15.733930');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0006_require_contenttypes_0002', '2020-05-12 22:40:15.738646');
INSERT INTO `django_migrations` VALUES ('12', 'auth', '0007_alter_validators_add_error_messages', '2020-05-12 22:40:15.750626');
INSERT INTO `django_migrations` VALUES ('13', 'auth', '0008_alter_user_username_max_length', '2020-05-12 22:40:15.800168');
INSERT INTO `django_migrations` VALUES ('14', 'auth', '0009_alter_user_last_name_max_length', '2020-05-12 22:40:15.846048');
INSERT INTO `django_migrations` VALUES ('15', 'auth', '0010_alter_group_name_max_length', '2020-05-12 22:40:15.890900');
INSERT INTO `django_migrations` VALUES ('16', 'auth', '0011_update_proxy_permissions', '2020-05-12 22:40:15.902476');
INSERT INTO `django_migrations` VALUES ('17', 'sessions', '0001_initial', '2020-05-12 22:40:15.922974');
INSERT INTO `django_migrations` VALUES ('18', 'user', '0001_initial', '2020-05-12 22:40:15.944567');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------

-- ----------------------------
-- Table structure for focus
-- ----------------------------
DROP TABLE IF EXISTS `focus`;
CREATE TABLE `focus` (
  `focus_id` int(11) NOT NULL AUTO_INCREMENT,
  `author_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`focus_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of focus
-- ----------------------------
INSERT INTO `focus` VALUES ('1', '1', '2');
INSERT INTO `focus` VALUES ('2', '1', '6');
INSERT INTO `focus` VALUES ('3', '2', '7');
INSERT INTO `focus` VALUES ('4', '2', '3');
INSERT INTO `focus` VALUES ('5', '3', '2');
INSERT INTO `focus` VALUES ('6', '0', '1');

-- ----------------------------
-- Table structure for garbage
-- ----------------------------
DROP TABLE IF EXISTS `garbage`;
CREATE TABLE `garbage` (
  `gar_id` int(11) NOT NULL AUTO_INCREMENT,
  `gar_img` varchar(200) DEFAULT NULL,
  `gar_name` varchar(200) NOT NULL,
  `gar_type` int(11) NOT NULL,
  `gar_introduce` varchar(1000) DEFAULT NULL,
  `gar_define` varchar(1000) DEFAULT NULL,
  `gar_guide` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`gar_id`),
  KEY `gar_type_id` (`gar_type`) USING BTREE,
  CONSTRAINT `garbage_ibfk_1` FOREIGN KEY (`gar_type`) REFERENCES `garbage_type` (`gar_type_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of garbage
-- ----------------------------
INSERT INTO `garbage` VALUES ('1', '', '茶叶', '1', '湿垃圾（厨房、易腐餐厨垃圾）', null, null);

-- ----------------------------
-- Table structure for garbage_type
-- ----------------------------
DROP TABLE IF EXISTS `garbage_type`;
CREATE TABLE `garbage_type` (
  `gar_type_id` int(11) NOT NULL AUTO_INCREMENT,
  `gar_type_name` varchar(100) NOT NULL,
  PRIMARY KEY (`gar_type_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of garbage_type
-- ----------------------------
INSERT INTO `garbage_type` VALUES ('1', '湿垃圾（厨房、易腐餐厨垃圾');
INSERT INTO `garbage_type` VALUES ('2', '可回收垃圾');
INSERT INTO `garbage_type` VALUES ('3', '干垃圾');
INSERT INTO `garbage_type` VALUES ('4', '有害垃圾');

-- ----------------------------
-- Table structure for goods
-- ----------------------------
DROP TABLE IF EXISTS `goods`;
CREATE TABLE `goods` (
  `goods_id` int(11) NOT NULL AUTO_INCREMENT,
  `goods_name` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '产品名称',
  `goods_pic` longtext COLLATE utf8_bin COMMENT '产品图片',
  `goods_introduce` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '产品介绍',
  `goods_freight` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '产品运费',
  `goods_price` float(10,2) DEFAULT NULL COMMENT '产品价格',
  `goods_num` int(11) DEFAULT NULL COMMENT '产品数量',
  `goods_sales` int(11) DEFAULT NULL COMMENT '产品已出售',
  `goods_category` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '产品分类',
  `goods_para` varchar(255) COLLATE utf8_bin DEFAULT NULL COMMENT '产品参数',
  PRIMARY KEY (`goods_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of goods
-- ----------------------------
INSERT INTO `goods` VALUES ('1', '电饭煲', 0x687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F466C58375F355F646C544245536861654A6D704A74316A696D4F5F4D2C687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F4676374773457359596D47496C37677468485242795335735F4745472C687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F46753833736A74334B4531316C476F304A684B6A466E5233504A39752C687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F466B723470514E5953593073674270326C345667356F4F4D62324443, '高效、节能', '10', '200.00', '283', '10', '家用电器', '\'产地：煜婷\', \'包装方式：可馨\', \'产品规格：月婵\'');
INSERT INTO `goods` VALUES ('2', '水杯', 0x687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F466C58375F355F646C544245536861654A6D704A74316A696D4F5F4D2C687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F4676374773457359596D47496C37677468485242795335735F4745472C687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F46753833736A74334B4531316C476F304A684B6A466E5233504A39752C687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F466B723470514E5953593073674270326C345667356F4F4D62324443, '晶莹剔透', '8', '15.00', '300', '20', '生活用品', '\'产地：煜婷\', \'包装方式：灵芸\', \'产品规格：明美\'');
INSERT INTO `goods` VALUES ('3', '耳机', 0x687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F466C58375F355F646C544245536861654A6D704A74316A696D4F5F4D2C687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F4676374773457359596D47496C37677468485242795335735F4745472C687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F46753833736A74334B4531316C476F304A684B6A466E5233504A39752C687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F466B723470514E5953593073674270326C345667356F4F4D62324443, '无燥', '7', '220.00', '280', '40', '手机销售', '\'产地：正梅\', \'包装方式：优璇\', \'产品规格：月婵\'');
INSERT INTO `goods` VALUES ('4', '充电线', 0x687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F466C58375F355F646C544245536861654A6D704A74316A696D4F5F4D2C687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F4676374773457359596D47496C37677468485242795335735F4745472C687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F46753833736A74334B4531316C476F304A684B6A466E5233504A39752C687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F466B723470514E5953593073674270326C345667356F4F4D62324443, '原装', '6', '19.00', '400', '25', '手机销售', '\'产地：香怡\', \'包装方式：正梅\', \'产品规格：明美\'');
INSERT INTO `goods` VALUES ('5', '移动硬盘', 0x687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F466C58375F355F646C544245536861654A6D704A74316A696D4F5F4D2C687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F4676374773457359596D47496C37677468485242795335735F4745472C687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F46753833736A74334B4531316C476F304A684B6A466E5233504A39752C687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F466B723470514E5953593073674270326C345667356F4F4D62324443, '2T', '10', '176.00', '362', '18', '家用电器', '\'产地：漫妮\', \'包装方式：月婵\', \'产品规格：明美\'');
INSERT INTO `goods` VALUES ('6', '字帖', 0x687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F466C58375F355F646C544245536861654A6D704A74316A696D4F5F4D2C687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F4676374773457359596D47496C37677468485242795335735F4745472C687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F46753833736A74334B4531316C476F304A684B6A466E5233504A39752C687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F466B723470514E5953593073674270326C345667356F4F4D62324443, '30天速成', '0', '6.00', '1362', '27', '生活用品', '\'产地：明美\', \'包装方式：煜婷\', \'产品规格：雅静\'');
INSERT INTO `goods` VALUES ('7', '护手霜', 0x687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F466C58375F355F646C544245536861654A6D704A74316A696D4F5F4D2C687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F4676374773457359596D47496C37677468485242795335735F4745472C687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F46753833736A74334B4531316C476F304A684B6A466E5233504A39752C687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F466B723470514E5953593073674270326C345667356F4F4D62324443, '值得拥有', '0', '12.00', '273', '37', '生活用品', '\'产地：惠茜\', \'包装方式：月婵\', \'产品规格：优璇\'');
INSERT INTO `goods` VALUES ('8', '电动牙刷', 0x687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F466C58375F355F646C544245536861654A6D704A74316A696D4F5F4D2C687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F4676374773457359596D47496C37677468485242795335735F4745472C687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F46753833736A74334B4531316C476F304A684B6A466E5233504A39752C687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F466B723470514E5953593073674270326C345667356F4F4D62324443, '让牙齿洁白', '12', '140.00', '692', '35', '生活用品', '\'产地：优璇\', \'包装方式：香怡\', \'产品规格：可馨\'');
INSERT INTO `goods` VALUES ('9', '保温壶', 0x687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F466C58375F355F646C544245536861654A6D704A74316A696D4F5F4D2C687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F4676374773457359596D47496C37677468485242795335735F4745472C687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F46753833736A74334B4531316C476F304A684B6A466E5233504A39752C687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F466B723470514E5953593073674270326C345667356F4F4D62324443, '36小时超长保温', '15', '306.00', '160', '25', '生活用品', '\'产地：灵芸\', \'包装方式：香怡\', \'产品规格：明美\'');
INSERT INTO `goods` VALUES ('10', '晾衣架', 0x687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F466C58375F355F646C544245536861654A6D704A74316A696D4F5F4D2C687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F4676374773457359596D47496C37677468485242795335735F4745472C687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F46753833736A74334B4531316C476F304A684B6A466E5233504A39752C687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F466B723470514E5953593073674270326C345667356F4F4D62324443, '充分利用空间', '27', '120.00', '260', '15', '家具用品', '\'产地：漫妮\', \'包装方式：正梅\', \'产品规格：香怡\'');
INSERT INTO `goods` VALUES ('11', '拖把', 0x687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F466C58375F355F646C544245536861654A6D704A74316A696D4F5F4D2C687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F4676374773457359596D47496C37677468485242795335735F4745472C687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F46753833736A74334B4531316C476F304A684B6A466E5233504A39752C687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F466B723470514E5953593073674270326C345667356F4F4D62324443, '好用', '10', '27.00', '380', '40', '清洁用品', '\'产地：漫妮\', \'包装方式：雅静\', \'产品规格：惠茜\'');
INSERT INTO `goods` VALUES ('12', '衬衣', 0x687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F466C58375F355F646C544245536861654A6D704A74316A696D4F5F4D2C687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F4676374773457359596D47496C37677468485242795335735F4745472C687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F46753833736A74334B4531316C476F304A684B6A466E5233504A39752C687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F466B723470514E5953593073674270326C345667356F4F4D62324443, '纯棉制作', '8', '99.00', '270', '29', '服装采购', '\'产地：漫妮\', \'包装方式：雅静\', \'产品规格：月婵\'');
INSERT INTO `goods` VALUES ('13', '羊肉卷', 0x687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F466C58375F355F646C544245536861654A6D704A74316A696D4F5F4D2C687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F4676374773457359596D47496C37677468485242795335735F4745472C687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F46753833736A74334B4531316C476F304A684B6A466E5233504A39752C687474703A2F2F71616577686E35706F2E626B742E636C6F7564646E2E636F6D2F466B723470514E5953593073674270326C345667356F4F4D62324443, '鲜嫩可口', '5', '20.00', '1000', '3', '餐饮食物', '\'产地：香怡\', \'包装方式：月婵\', \'产品规格：煜婷\'');

-- ----------------------------
-- Table structure for ljsw_cache_table
-- ----------------------------
DROP TABLE IF EXISTS `ljsw_cache_table`;
CREATE TABLE `ljsw_cache_table` (
  `cache_key` varchar(255) NOT NULL,
  `value` longtext NOT NULL,
  `expires` datetime(6) NOT NULL,
  PRIMARY KEY (`cache_key`),
  KEY `ljsw_cache_table_expires` (`expires`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ljsw_cache_table
-- ----------------------------
INSERT INTO `ljsw_cache_table` VALUES (':1:0020db4412f89ff710c60c04985c9ad71708fb5367c6d5cbb3d06dacaaa9ff96', 'gASVAwAAAAAAAABLDC4=', '2020-05-20 22:41:40.000000');
INSERT INTO `ljsw_cache_table` VALUES (':1:029376a2e08c26b2d6cd511a9e4ef917407befb195de4fecc4b572df64799d32', 'gASVAwAAAAAAAABLDS4=', '2020-05-20 22:44:32.000000');
INSERT INTO `ljsw_cache_table` VALUES (':1:155d5fa439f9dec3ca081f668273dc8168658a90f9b6187aac3fd9c7479253e4', 'gASVAwAAAAAAAABLCy4=', '2020-05-20 17:06:19.000000');
INSERT INTO `ljsw_cache_table` VALUES (':1:342d38daffc3425dc660aeaeb3e17d19e7e3350eff4c350021f11c1218f2d77b', 'gASVAwAAAAAAAABLDS4=', '2020-05-20 22:44:22.000000');
INSERT INTO `ljsw_cache_table` VALUES (':1:3c0165d858e2c0a2c766592205d57d55f8acd68565bf5961fa9e6f79bfdf09c1', 'gASVAwAAAAAAAABLCy4=', '2020-05-20 16:35:49.000000');
INSERT INTO `ljsw_cache_table` VALUES (':1:3debef2f7dffb92f0cdc81cb6a3dda78f0a55e1574634b2b91d350d4f746c7d2', 'gASVAwAAAAAAAABLDC4=', '2020-05-20 17:42:38.000000');
INSERT INTO `ljsw_cache_table` VALUES (':1:62cf6fc1e2a1426cdafb38016dec8f9178f3b21b25deafc7581abdf924e8dc38', 'gASVAwAAAAAAAABLCy4=', '2020-05-20 17:03:43.000000');
INSERT INTO `ljsw_cache_table` VALUES (':1:62dd39bb155abb6f7f23d890481073dd91417842fa08a04e8639d0330b50633a', 'gASVAwAAAAAAAABLCy4=', '2020-05-20 17:06:31.000000');
INSERT INTO `ljsw_cache_table` VALUES (':1:73758393906eb501d3a55def68d41b5c595744793524868bb339c0bc8064de31', 'gASVAwAAAAAAAABLCy4=', '2020-05-20 17:03:42.000000');
INSERT INTO `ljsw_cache_table` VALUES (':1:8b0730a0c59a9b88dc5b3d1f8fb57a4a9d7a81cb15107ba3ac73cf0b6d661187', 'gASVAwAAAAAAAABLCy4=', '2020-05-20 16:53:47.000000');
INSERT INTO `ljsw_cache_table` VALUES (':1:a7d83c2c8884f8b4cf3a60adf5ad3027aea15e9b4659430d2e1ac39a9bfb4513', 'gASVAwAAAAAAAABLCy4=', '2020-05-20 17:03:44.000000');
INSERT INTO `ljsw_cache_table` VALUES (':1:aa5f11a09bbe03f9e3b8a7a1eaf7f687b6a785b8f2c430ff589fcd38ce8e1046', 'gASVAwAAAAAAAABLDC4=', '2020-05-20 22:43:47.000000');
INSERT INTO `ljsw_cache_table` VALUES (':1:dffb267a4363220c7e74a20a9af0a84e6a29d3543068b230cf3e9e450fc2e5b4', 'gASVAwAAAAAAAABLCy4=', '2020-05-20 17:03:21.000000');
INSERT INTO `ljsw_cache_table` VALUES (':1:VCODE-17645109827', 'gASVBgAAAAAAAABKoB8MAC4=', '2020-05-14 17:42:19.000000');

-- ----------------------------
-- Table structure for order
-- ----------------------------
DROP TABLE IF EXISTS `order`;
CREATE TABLE `order` (
  `order_id` int(11) NOT NULL AUTO_INCREMENT,
  `goods_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `or_name` varchar(255) DEFAULT NULL,
  `or_address` varchar(255) DEFAULT NULL,
  `or_phone` varchar(255) DEFAULT NULL,
  `or_num` int(11) DEFAULT NULL,
  `or_price` decimal(65,2) NOT NULL,
  `or_freight` decimal(65,2) DEFAULT NULL,
  `or_time` datetime DEFAULT NULL,
  `or_status` tinyint(4) DEFAULT '0',
  `or_note` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`order_id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of order
-- ----------------------------
INSERT INTO `order` VALUES ('1', '11', '4', '可乐', '安徽省', '13212312312', null, '127.93', '12.00', '2020-05-16 11:02:37', '0', '请尽快发货');
INSERT INTO `order` VALUES ('2', '7', '2', '可乐', '安徽省', '13212312312', null, '87.20', '8.00', '2020-05-16 12:02:37', null, '请尽快发货');
INSERT INTO `order` VALUES ('3', '7', '2', '可乐', '安徽省', '13212312312', null, '87.20', '8.00', '2020-05-16 12:02:37', null, '请尽快发货');
INSERT INTO `order` VALUES ('4', '7', '2', '可乐', '安徽省', '13212312312', null, '87.20', '8.00', '2020-05-16 12:02:37', null, '请尽快发货');
INSERT INTO `order` VALUES ('5', '7', '2', '可乐', '安徽省', '13212312312', null, '87.20', '8.00', '2020-05-16 12:02:37', '0', '请尽快发货');
INSERT INTO `order` VALUES ('6', '1', '2', '可乐', '安徽省', '13212312312', null, '87.20', '8.00', '2020-05-16 12:02:37', '0', '请尽快发货');
INSERT INTO `order` VALUES ('7', '1', '2', '可乐', '安徽省', '13212312312', null, '87.20', '8.00', '2020-05-16 12:02:37', '0', '请尽快发货');
INSERT INTO `order` VALUES ('8', '1', '2', '可乐', '安徽省', '13212312312', '10', '87.20', '8.00', '2020-05-16 12:02:37', '0', '请尽快发货');
INSERT INTO `order` VALUES ('9', '1', '2', '可乐', '安徽省', '13212312312', '10', '87.20', '8.00', '2020-05-16 12:02:37', '0', '请尽快发货');
INSERT INTO `order` VALUES ('10', '1', '2', '可乐', '安徽省', '13212312312', '10', '87.20', '8.00', '2020-05-16 12:02:37', '0', '请尽快发货');
INSERT INTO `order` VALUES ('11', '1', '2', '可乐', '安徽省', '13212312312', '10', '87.20', '8.00', '2020-05-16 12:02:37', '0', '请尽快发货');
INSERT INTO `order` VALUES ('12', '1', '2', '可乐', '安徽省', '13212312312', '10', '87.20', '8.00', '2020-05-16 12:02:37', '0', '请尽快发货');
INSERT INTO `order` VALUES ('13', '1', '2', '可乐', '安徽省', '13212312312', '5', '87.20', '8.00', '2020-05-16 20:58:25', '0', '请尽快发货');
INSERT INTO `order` VALUES ('14', '1', '3', '雪碧', '安徽省', '13212312312', '5', '87.20', '8.00', '2020-05-16 21:01:46', '0', '请尽快发货');
INSERT INTO `order` VALUES ('15', '1', '3', '雪碧', '安徽省', '13212312312', '5', '87.20', '8.00', '2020-05-16 21:04:16', '0', '请尽快发货');
INSERT INTO `order` VALUES ('16', '1', '3', '芬达', '安徽省', '13212312312', '4', '66.78', '8.00', '2020-05-16 21:05:12', '0', '请尽快发货');
INSERT INTO `order` VALUES ('17', '1', '3', '茶兀', '安徽省', '13212312312', '4', '66.78', '8.00', '2020-05-16 21:05:42', '0', '请尽快发货');

-- ----------------------------
-- Table structure for picture
-- ----------------------------
DROP TABLE IF EXISTS `picture`;
CREATE TABLE `picture` (
  `picture_id` int(11) NOT NULL AUTO_INCREMENT,
  `picture_path` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `picture_type` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `article_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`picture_id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of picture
-- ----------------------------
INSERT INTO `picture` VALUES ('1', '/aaa/1', 'picture', '0');
INSERT INTO `picture` VALUES ('2', '/aaa/2', 'picture', '0');
INSERT INTO `picture` VALUES ('3', '/aaa/3', 'picture', '0');
INSERT INTO `picture` VALUES ('4', '/aaa/4', 'picture', '1');
INSERT INTO `picture` VALUES ('5', '/aaa/5', 'picture', '1');
INSERT INTO `picture` VALUES ('6', '/aaa/6', 'picture', '1');
INSERT INTO `picture` VALUES ('7', '/aaa/7', 'picture', '1');
INSERT INTO `picture` VALUES ('8', '/aaa/8', 'picture', '1');
INSERT INTO `picture` VALUES ('9', '/aaa/9', 'video', '2');
INSERT INTO `picture` VALUES ('10', '/aaa/10', 'video', '3');
INSERT INTO `picture` VALUES ('11', '/aaa/11', 'picture', '4');
INSERT INTO `picture` VALUES ('12', '/aaa/12', 'picture', '4');
INSERT INTO `picture` VALUES ('13', '/aaa/13', 'picture', '4');
INSERT INTO `picture` VALUES ('14', '/aaa/14', 'picture', '4');
INSERT INTO `picture` VALUES ('15', '/aaa/15', 'picture', '4');
INSERT INTO `picture` VALUES ('16', '/aaa/16', 'picture', '5');
INSERT INTO `picture` VALUES ('17', '/aaa/17', 'picture', '6');
INSERT INTO `picture` VALUES ('18', '/aaa/18', 'picture', '6');

-- ----------------------------
-- Table structure for praise
-- ----------------------------
DROP TABLE IF EXISTS `praise`;
CREATE TABLE `praise` (
  `praise_id` int(11) NOT NULL AUTO_INCREMENT,
  `article_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`praise_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of praise
-- ----------------------------
INSERT INTO `praise` VALUES ('1', '1', '1');
INSERT INTO `praise` VALUES ('2', '1', '5');
INSERT INTO `praise` VALUES ('4', '0', '4');
INSERT INTO `praise` VALUES ('5', '0', '2');
INSERT INTO `praise` VALUES ('6', '1', '3');
INSERT INTO `praise` VALUES ('7', '1', '7');
INSERT INTO `praise` VALUES ('8', '0', '0');

-- ----------------------------
-- Table structure for recycling
-- ----------------------------
DROP TABLE IF EXISTS `recycling`;
CREATE TABLE `recycling` (
  `recycling_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `recycling_time` datetime DEFAULT NULL,
  `current_time` datetime DEFAULT NULL,
  `recycle_msg` varchar(255) DEFAULT NULL,
  `recycle_state` int(11) unsigned DEFAULT '0',
  `addres_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`recycling_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of recycling
-- ----------------------------
INSERT INTO `recycling` VALUES ('1', '13', '2020-05-15 21:07:21', '2020-05-15 21:07:25', 'dad', '2', '1');
INSERT INTO `recycling` VALUES ('2', '13', '2020-05-15 21:07:45', '2020-05-15 21:07:48', 'iiii', '0', '2');
INSERT INTO `recycling` VALUES ('3', '13', '2020-05-15 22:51:48', '2020-05-15 22:51:50', '7979', '1', '1');
INSERT INTO `recycling` VALUES ('4', '13', '2020-05-29 22:52:01', '2020-05-15 22:52:08', '787', '2', '2');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_phone` varchar(32) NOT NULL,
  `avatar` varchar(255) DEFAULT NULL,
  `gender` int(11) DEFAULT '0',
  `nickname` varchar(16) NOT NULL,
  `birthday` date DEFAULT NULL,
  `signature` varchar(120) DEFAULT NULL,
  `position` int(11) DEFAULT '0',
  `now_integral` int(11) DEFAULT '0',
  `add_integral` int(11) DEFAULT '0',
  `recycle_num` int(11) DEFAULT '0',
  `qq` varchar(32) DEFAULT NULL,
  `vx` varchar(64) DEFAULT NULL,
  `zfb` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `user_phone` (`user_phone`) USING BTREE,
  UNIQUE KEY `nickname` (`nickname`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('13', '12345678912', 'avatars/th1_o6uMeex.jpg', '0', 'dog', '2020-05-23', 'a single dog', '0', '20', '120', '0', null, null, null);
INSERT INTO `user` VALUES ('14', '12256468787', 'avatars/9c16fdfaaf51f3de216575e1db76441a382979fa.jpg', '0', '', null, null, '0', '0', '0', '0', null, null, null);
