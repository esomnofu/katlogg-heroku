-- phpMyAdmin SQL Dump
-- version 4.7.9
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 03, 2018 at 09:49 AM
-- Server version: 10.1.31-MariaDB
-- PHP Version: 7.2.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `catalogue`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add product', 1, 'add_product'),
(2, 'Can change product', 1, 'change_product'),
(3, 'Can delete product', 1, 'delete_product'),
(4, 'Can add news', 2, 'add_news'),
(5, 'Can change news', 2, 'change_news'),
(6, 'Can delete news', 2, 'delete_news'),
(7, 'Can add Rating', 3, 'add_ratings'),
(8, 'Can change Rating', 3, 'change_ratings'),
(9, 'Can delete Rating', 3, 'delete_ratings'),
(10, 'Can add xpath list', 4, 'add_xpathlist'),
(11, 'Can change xpath list', 4, 'change_xpathlist'),
(12, 'Can delete xpath list', 4, 'delete_xpathlist'),
(13, 'Can add log entry', 5, 'add_logentry'),
(14, 'Can change log entry', 5, 'change_logentry'),
(15, 'Can delete log entry', 5, 'delete_logentry'),
(16, 'Can add permission', 6, 'add_permission'),
(17, 'Can change permission', 6, 'change_permission'),
(18, 'Can delete permission', 6, 'delete_permission'),
(19, 'Can add group', 7, 'add_group'),
(20, 'Can change group', 7, 'change_group'),
(21, 'Can delete group', 7, 'delete_group'),
(22, 'Can add user', 8, 'add_user'),
(23, 'Can change user', 8, 'change_user'),
(24, 'Can delete user', 8, 'delete_user'),
(25, 'Can add content type', 9, 'add_contenttype'),
(26, 'Can change content type', 9, 'change_contenttype'),
(27, 'Can delete content type', 9, 'delete_contenttype'),
(28, 'Can add session', 10, 'add_session'),
(29, 'Can change session', 10, 'change_session'),
(30, 'Can delete session', 10, 'delete_session');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$100000$FIqjdJFYv5K7$OL4Cnae17CfAL4OxOoXHBHPq7/irfmTnZ+oXiPfV+qA=', '2018-05-08 15:27:40.340515', 1, 'admin', '', '', 'vincent@diamondscripts.ng', 1, 1, '2018-05-08 15:20:57.355801');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(5, 'admin', 'logentry'),
(7, 'auth', 'group'),
(6, 'auth', 'permission'),
(8, 'auth', 'user'),
(9, 'contenttypes', 'contenttype'),
(2, 'products', 'news'),
(1, 'products', 'product'),
(3, 'products', 'ratings'),
(10, 'sessions', 'session'),
(4, 'xpaths', 'xpathlist');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2018-05-08 14:48:46.233433'),
(2, 'auth', '0001_initial', '2018-05-08 14:48:56.753077'),
(3, 'admin', '0001_initial', '2018-05-08 14:48:59.859434'),
(4, 'admin', '0002_logentry_remove_auto_add', '2018-05-08 14:48:59.933273'),
(5, 'contenttypes', '0002_remove_content_type_name', '2018-05-08 14:49:01.038982'),
(6, 'auth', '0002_alter_permission_name_max_length', '2018-05-08 14:49:02.185212'),
(7, 'auth', '0003_alter_user_email_max_length', '2018-05-08 14:49:03.658817'),
(8, 'auth', '0004_alter_user_username_opts', '2018-05-08 14:49:03.721144'),
(9, 'auth', '0005_alter_user_last_login_null', '2018-05-08 14:49:04.287175'),
(10, 'auth', '0006_require_contenttypes_0002', '2018-05-08 14:49:04.349856'),
(11, 'auth', '0007_alter_validators_add_error_messages', '2018-05-08 14:49:04.427865'),
(12, 'auth', '0008_alter_user_username_max_length', '2018-05-08 14:49:06.127355'),
(13, 'auth', '0009_alter_user_last_name_max_length', '2018-05-08 14:49:06.954257'),
(14, 'products', '0001_initial', '2018-05-08 14:49:07.543217'),
(15, 'products', '0002_news', '2018-05-08 14:49:07.996391'),
(16, 'products', '0003_auto_20180319_1553', '2018-05-08 14:49:09.424644'),
(17, 'products', '0004_auto_20180323_1232', '2018-05-08 14:49:10.622501'),
(18, 'products', '0005_auto_20180323_1544', '2018-05-08 14:49:11.814687'),
(19, 'products', '0006_auto_20180404_1747', '2018-05-08 14:49:12.859496'),
(20, 'products', '0007_auto_20180404_1748', '2018-05-08 14:49:13.808312'),
(21, 'products', '0008_auto_20180410_0900', '2018-05-08 14:49:14.796553'),
(22, 'products', '0009_ratings', '2018-05-08 14:49:16.156046'),
(23, 'products', '0010_auto_20180419_1604', '2018-05-08 14:49:16.500003'),
(24, 'products', '0011_auto_20180419_1622', '2018-05-08 14:49:16.710825'),
(25, 'sessions', '0001_initial', '2018-05-08 14:49:17.382644'),
(26, 'xpaths', '0001_initial', '2018-05-08 14:49:17.813420'),
(27, 'xpaths', '0002_auto_20180424_1139', '2018-05-08 14:49:18.164552'),
(28, 'xpaths', '0003_xpathlist_product_url', '2018-05-08 14:49:18.762871'),
(29, 'xpaths', '0004_auto_20180425_1139', '2018-05-08 14:49:18.825374');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('3jew8ywbleackeezj7efzljqfv0ounmx', 'YzZjMzA1ZDA2NDlhNTgwMjcxOTlkODIyNzhhZGU1NjIwMTMwMjdmMjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhYTNkNTJjYTg4MDI0OWJkZmU0ZmRiOWQzYjkzYWJhMmZiOGJlYjk0In0=', '2018-05-22 15:27:40.519283');

-- --------------------------------------------------------

--
-- Table structure for table `products_news`
--

CREATE TABLE `products_news` (
  `id` int(11) NOT NULL,
  `product_name` varchar(1000) NOT NULL,
  `product_seller` varchar(250) NOT NULL,
  `product_old_price` varchar(250) NOT NULL,
  `product_current_price` varchar(250) NOT NULL,
  `product_url` varchar(1500) NOT NULL,
  `product_categories` varchar(1500) NOT NULL,
  `product_valid_sizes` varchar(500) NOT NULL,
  `product_off` varchar(100) NOT NULL,
  `product_valid_images` varchar(1500) NOT NULL,
  `product_news` longtext NOT NULL,
  `date` datetime(6) NOT NULL,
  `product_price_change_type` varchar(100) NOT NULL,
  `product_color` varchar(500) NOT NULL,
  `product_color_change` varchar(100) NOT NULL,
  `product_size_change` varchar(100) NOT NULL,
  `product_description` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `products_product`
--

CREATE TABLE `products_product` (
  `id` int(11) NOT NULL,
  `store_name` varchar(100) NOT NULL,
  `product_name` varchar(1000) NOT NULL,
  `product_seller` varchar(250) NOT NULL,
  `product_old_price` varchar(250) NOT NULL,
  `product_current_price` varchar(250) NOT NULL,
  `product_url` varchar(1500) NOT NULL,
  `product_categories` varchar(1500) NOT NULL,
  `product_old_sizes` varchar(500) NOT NULL,
  `product_valid_sizes` varchar(500) NOT NULL,
  `product_off` varchar(100) NOT NULL,
  `product_valid_images` varchar(1500) NOT NULL,
  `date` datetime(6) NOT NULL,
  `product_old_color` varchar(500) NOT NULL,
  `product_color` varchar(500) NOT NULL,
  `product_description` longtext NOT NULL,
  `sub_sub_category` int(11) NOT NULL,
  `interest_id` int(11) NOT NULL,
  `age_range` varchar(10) NOT NULL,
  `sex` char(2) NOT NULL,
  `comments` int(11) NOT NULL,
  `likes` int(11) NOT NULL,
  `dislikes` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `products_ratings`
--

CREATE TABLE `products_ratings` (
  `id` int(11) NOT NULL,
  `item_name` varchar(1000) NOT NULL,
  `item_rating` varchar(100) NOT NULL,
  `date` datetime(6) NOT NULL,
  `rater_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `xpaths_xpathlist`
--

CREATE TABLE `xpaths_xpathlist` (
  `id` int(11) NOT NULL,
  `website_name` varchar(1000) NOT NULL,
  `major_url` varchar(1000) NOT NULL,
  `relay_links` varchar(1000) NOT NULL,
  `start_page_number` varchar(1000) NOT NULL,
  `end_page_number` varchar(1000) NOT NULL,
  `pagination_index` varchar(1000) NOT NULL,
  `product_name` varchar(1000) NOT NULL,
  `product_seller` varchar(1000) NOT NULL,
  `product_color` varchar(1000) NOT NULL,
  `product_current_price` varchar(1000) NOT NULL,
  `product_old_price` varchar(1000) NOT NULL,
  `product_categories` varchar(1000) NOT NULL,
  `product_sizes` varchar(1000) NOT NULL,
  `product_percentage_off` varchar(1000) NOT NULL,
  `product_images` varchar(1000) NOT NULL,
  `product_description` varchar(1000) NOT NULL,
  `product_url` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `products_news`
--
ALTER TABLE `products_news`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `products_product`
--
ALTER TABLE `products_product`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `products_ratings`
--
ALTER TABLE `products_ratings`
  ADD PRIMARY KEY (`id`),
  ADD KEY `products_ratings_rater_id_b5c29103_fk_auth_user_id` (`rater_id`);

--
-- Indexes for table `xpaths_xpathlist`
--
ALTER TABLE `xpaths_xpathlist`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT for table `products_news`
--
ALTER TABLE `products_news`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `products_product`
--
ALTER TABLE `products_product`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `products_ratings`
--
ALTER TABLE `products_ratings`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `xpaths_xpathlist`
--
ALTER TABLE `xpaths_xpathlist`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `products_ratings`
--
ALTER TABLE `products_ratings`
  ADD CONSTRAINT `products_ratings_rater_id_b5c29103_fk_auth_user_id` FOREIGN KEY (`rater_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
