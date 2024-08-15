/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - ornamental_fishes
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`ornamental_fishes` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `ornamental_fishes`;

/*Table structure for table `age_group` */

DROP TABLE IF EXISTS `age_group`;

CREATE TABLE `age_group` (
  `group_id` int(11) NOT NULL AUTO_INCREMENT,
  `group_name` varchar(111) DEFAULT NULL,
  PRIMARY KEY (`group_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `age_group` */

insert  into `age_group`(`group_id`,`group_name`) values 
(2,'0-2'),
(3,'2-4');

/*Table structure for table `assistance` */

DROP TABLE IF EXISTS `assistance`;

CREATE TABLE `assistance` (
  `assistance_id` int(11) NOT NULL AUTO_INCREMENT,
  `buyer_id` int(11) DEFAULT NULL,
  `seller_id` int(11) DEFAULT NULL,
  `description` varchar(2222) DEFAULT NULL,
  `reply` varchar(1111) DEFAULT NULL,
  `date` varchar(1111) DEFAULT NULL,
  PRIMARY KEY (`assistance_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `assistance` */

insert  into `assistance`(`assistance_id`,`buyer_id`,`seller_id`,`description`,`reply`,`date`) values 
(1,1,1,'hello i want pet food ?','ok','2024-02-12'),
(2,1,1,'what hapeen','pending','2024-02-12');

/*Table structure for table `buyer` */

DROP TABLE IF EXISTS `buyer`;

CREATE TABLE `buyer` (
  `buyer_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `first_name` varchar(111) DEFAULT NULL,
  `last_name` varchar(111) DEFAULT NULL,
  `email` varchar(111) DEFAULT NULL,
  `contact` varchar(111) DEFAULT NULL,
  `Address` varchar(1111) DEFAULT NULL,
  PRIMARY KEY (`buyer_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `buyer` */

insert  into `buyer`(`buyer_id`,`login_id`,`first_name`,`last_name`,`email`,`contact`,`Address`) values 
(1,3,'buyer','buyer','buyer@gmail.cvom','1234567890','palakkad'),
(2,4,'sivaganga','KJ','sivaganga@gmail.com','9976542011','kollam'),
(3,5,'anu','r','buy4@gmail.cvom','9283293823','fdfgkjesgfikkfkgk ');

/*Table structure for table `complaints` */

DROP TABLE IF EXISTS `complaints`;

CREATE TABLE `complaints` (
  `complaints_id` int(11) NOT NULL AUTO_INCREMENT,
  `sender_id` int(11) DEFAULT NULL,
  `complaint` varchar(111) DEFAULT NULL,
  `date` varchar(111) DEFAULT NULL,
  `reply` varchar(111) DEFAULT NULL,
  PRIMARY KEY (`complaints_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `complaints` */

insert  into `complaints`(`complaints_id`,`sender_id`,`complaint`,`date`,`reply`) values 
(1,1,'check1','2024-02-12','pending');

/*Table structure for table `count` */

DROP TABLE IF EXISTS `count`;

CREATE TABLE `count` (
  `count_id` int(11) NOT NULL AUTO_INCREMENT,
  `fish_id` int(11) DEFAULT NULL,
  `count` varchar(111) DEFAULT NULL,
  `date` varchar(111) DEFAULT NULL,
  PRIMARY KEY (`count_id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `count` */

insert  into `count`(`count_id`,`fish_id`,`count`,`date`) values 
(1,1,'43','2024-02-12'),
(2,2,'35','2024-02-12'),
(3,3,'96','2024-02-12'),
(12,12,'88','2024-02-12'),
(11,11,'66','2024-02-12');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `buyer_id` int(11) DEFAULT NULL,
  `seller_id` int(11) DEFAULT NULL,
  `date` varchar(111) DEFAULT NULL,
  `feedback` varchar(2222) DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`feedback_id`,`buyer_id`,`seller_id`,`date`,`feedback`) values 
(1,1,1,'2024-02-12','damm good'),
(2,1,1,'2024-02-12','ok');

/*Table structure for table `fish_category` */

DROP TABLE IF EXISTS `fish_category`;

CREATE TABLE `fish_category` (
  `category_id` int(11) NOT NULL AUTO_INCREMENT,
  `category_name` varchar(111) DEFAULT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `fish_category` */

insert  into `fish_category`(`category_id`,`category_name`) values 
(2,'top swimmer');

/*Table structure for table `fishes` */

DROP TABLE IF EXISTS `fishes`;

CREATE TABLE `fishes` (
  `fish_id` int(11) NOT NULL AUTO_INCREMENT,
  `category_id` int(11) DEFAULT NULL,
  `group_id` int(11) DEFAULT NULL,
  `fish_name` varchar(111) DEFAULT NULL,
  `image` varchar(3333) DEFAULT NULL,
  `description` varchar(2222) DEFAULT NULL,
  `date` varchar(111) DEFAULT NULL,
  `amount` varchar(111) DEFAULT NULL,
  `seller_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`fish_id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `fishes` */

insert  into `fishes`(`fish_id`,`category_id`,`group_id`,`fish_name`,`image`,`description`,`date`,`amount`,`seller_id`) values 
(1,2,2,'gold','static/bae10cb2-0ef6-467c-bb31-fa26541d1182837fac2a-1402-4712-a723-d6755a15e62ejump.png','The goldfish is a freshwater fish in the family Cyprinidae of order Cypriniformes. It is commonly kept as a pet in indoor aquariums, and is one of the most popular aquarium fish.','2024-02-12','50',1),
(2,2,2,'arowna','static/947114b3-4464-4187-8d5c-4556aeb4cb9801513f19-41bb-4415-bf11-fa263341ec0bfish (8).png','Arowanas are freshwater fish known for their unique appearance and considered as ornamental species in the aquarium trade','2024-02-12','1000',1),
(3,2,2,'fighter1','static/bc6e19e6-f559-4a22-8be0-24ddd3bc14f38f708167-f6d9-40d1-a420-5ee5b04d0cadfish (5).png','Consequently, Siamese fighting fish are highly adaptable and durable, able to tolerate a variety of harsh or toxic environments; this accounts for their popularity as pets, as well as their ability to successfully colonize bodies of water all over the world.','2024-02-12','150',1),
(11,2,3,'discus','static/d3c330a4-cc62-4b34-848e-1857a2b7a148page4_pic2.jpg','Discus Fishes are common and very sensitive fishes in our aquariums, we are delivering quality discus fishes that are imported from Thailand, Malaysia, ..','2024-02-12','100',1),
(12,2,3,'disucs new','static/b1a1f7a7-bfd8-4b3e-b736-309973f03bbbfish (10).png','It is true, Discus Fish are noted as some of the most tranquil tropical fish in the market. ','2024-02-12','200',1);

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(111) DEFAULT NULL,
  `password` varchar(111) DEFAULT NULL,
  `usertype` varchar(111) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values 
(1,'admin','admin','admin'),
(2,'seller','seller123','seller'),
(3,'buyer','buyer1234','buyer'),
(4,'ganga','ganga123','buyer'),
(5,'buyer12345','buyer1345','buyer');

/*Table structure for table `order_detail` */

DROP TABLE IF EXISTS `order_detail`;

CREATE TABLE `order_detail` (
  `order_detail_id` int(11) NOT NULL AUTO_INCREMENT,
  `order_master_id` int(11) DEFAULT NULL,
  `fish_id` int(11) DEFAULT NULL,
  `count` varchar(111) DEFAULT NULL,
  `amount` varchar(111) DEFAULT NULL,
  PRIMARY KEY (`order_detail_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `order_detail` */

insert  into `order_detail`(`order_detail_id`,`order_master_id`,`fish_id`,`count`,`amount`) values 
(1,1,3,'2','150'),
(2,2,3,'2','150'),
(3,2,1,'2','50'),
(4,3,11,'2','100'),
(5,4,2,'2','1000');

/*Table structure for table `order_master` */

DROP TABLE IF EXISTS `order_master`;

CREATE TABLE `order_master` (
  `order_master_id` int(11) NOT NULL AUTO_INCREMENT,
  `seller_id` int(11) DEFAULT NULL,
  `buyer_id` int(11) DEFAULT NULL,
  `total_amount` varchar(111) DEFAULT NULL,
  `date` varchar(111) DEFAULT NULL,
  `status` varchar(111) DEFAULT NULL,
  PRIMARY KEY (`order_master_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `order_master` */

insert  into `order_master`(`order_master_id`,`seller_id`,`buyer_id`,`total_amount`,`date`,`status`) values 
(1,1,1,'300.00','2024-02-12','paid'),
(2,1,1,'400','2024-02-12','paid'),
(3,1,1,'200.00','2024-02-14','paid'),
(4,1,2,'2000.00','2024-02-21','pending');

/*Table structure for table `payments` */

DROP TABLE IF EXISTS `payments`;

CREATE TABLE `payments` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `seller_id` int(11) DEFAULT NULL,
  `order_master_id` int(11) DEFAULT NULL,
  `buyer_id` int(11) DEFAULT NULL,
  `amount` varchar(111) DEFAULT NULL,
  `date` varchar(111) DEFAULT NULL,
  `status` varchar(111) DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `payments` */

insert  into `payments`(`payment_id`,`seller_id`,`order_master_id`,`buyer_id`,`amount`,`date`,`status`) values 
(1,1,1,1,'300.00','2024-02-12','paid'),
(2,1,2,1,'400','2024-02-12','paid'),
(3,1,3,1,'200.00','2024-02-14','paid'),
(4,1,4,2,'2000.00','2024-02-21','pending');

/*Table structure for table `seller` */

DROP TABLE IF EXISTS `seller`;

CREATE TABLE `seller` (
  `seller_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `first_name` varchar(111) DEFAULT NULL,
  `last_name` varchar(111) DEFAULT NULL,
  `email` varchar(111) DEFAULT NULL,
  `contact` varchar(111) DEFAULT NULL,
  `address` varchar(111) DEFAULT NULL,
  PRIMARY KEY (`seller_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `seller` */

insert  into `seller`(`seller_id`,`login_id`,`first_name`,`last_name`,`email`,`contact`,`address`) values 
(1,2,'seller','seller','seller@gmail.com','1234567891','sellershop');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
