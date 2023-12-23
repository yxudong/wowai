CREATE TABLE `user_info` (
  `id` bigint(20) unsigned NOT NULL COMMENT 'id',
  `user_id` bigint(20) NOT NULL DEFAULT '0' COMMENT 'user_id',
  `name` varchar(500) NOT NULL DEFAULT '' COMMENT 'name',
  `email` varchar(500) NOT NULL DEFAULT '' COMMENT 'email',
  `password` varchar(500) NOT NULL DEFAULT '' COMMENT 'password',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uniq_user_id` (`user_id`),
  UNIQUE KEY `uniq_email` (`email`),
  KEY `idx_name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `user_verify_code` (
  `id` bigint(20) unsigned NOT NULL COMMENT 'id',
  `user_id` bigint(20) NOT NULL DEFAULT '0' COMMENT 'user_id',
  `email` varchar(500) NOT NULL DEFAULT '' COMMENT 'email',
  `verify_code` varchar(500) NOT NULL DEFAULT '' COMMENT 'verify_code',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uniq_user_id` (`user_id`),
  UNIQUE KEY `uniq_email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;













CREATE TABLE `user_task_config` (
  `task_config_id` bigint(20) unsigned NOT NULL COMMENT 'task_config_id',
  `user_id` bigint(20) NOT NULL DEFAULT '0' COMMENT 'user_id',
  `task_config_name` varchar(500) NOT NULL DEFAULT '' COMMENT 'task_config_name',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`task_config_id`),
  KEY `idx_user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `document_category_config` (
  `category_id` bigint(20) unsigned NOT NULL COMMENT 'category_id',
  `task_config_id` bigint(20) NOT NULL DEFAULT '0' COMMENT 'task_config_id',
  `category_name` varchar(500) NOT NULL DEFAULT '' COMMENT 'category_name',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`category_id`),
  KEY `idx_task_config_id` (`task_config_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `document_field_config` (
  `field_id` bigint(20) unsigned NOT NULL COMMENT 'field_id',
  `category_id` bigint(20) NOT NULL DEFAULT '0' COMMENT 'category_id',
  `field_name` varchar(500) NOT NULL DEFAULT '' COMMENT 'field_name',
  `field_type` int(4) NOT NULL DEFAULT '0' COMMENT 'field_type',
  `hide_status` int(4) NOT NULL DEFAULT '0' COMMENT 'hide_status',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`field_id`),
  KEY `idx_category_id` (`category_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;









CREATE TABLE `user_task_queue` (
  `queue_id` bigint(20) unsigned NOT NULL COMMENT 'queue_id',
  `user_id` bigint(20) NOT NULL DEFAULT '0' COMMENT 'user_id',
  `queue_name` varchar(500) NOT NULL DEFAULT '' COMMENT 'queue_name',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`queue_id`),
  KEY `idx_user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `queue_upload_detail` (
  `file_id` bigint(20) unsigned NOT NULL COMMENT 'file_id',
  `queue_id` bigint(20) NOT NULL DEFAULT '0' COMMENT 'queue_id',
  `origin_file_name` varchar(500) NOT NULL DEFAULT '' COMMENT 'origin_file_name',
  `file_name` varchar(500) NOT NULL DEFAULT '' COMMENT 'file_name',
  `upload_status` int(4) NOT NULL DEFAULT '0' COMMENT 'upload_status',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`file_id`),
  UNIQUE KEY `uniq_queue_id_file_name` (`queue_id`,`file_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `queue_classify_detail` (
  `detail_file_id` bigint(20) unsigned NOT NULL COMMENT 'detail_file_id',
  `queue_id` bigint(20) NOT NULL DEFAULT '0' COMMENT 'queue_id',
  `parent_file_id` bigint(20) unsigned NOT NULL COMMENT 'parent_file_id',
  `file_name` varchar(500) NOT NULL DEFAULT '' COMMENT 'file_name',
  `catagory` varchar(500) NOT NULL DEFAULT '' COMMENT 'catagory',
  `catagory_status` int(4) NOT NULL DEFAULT '0' COMMENT 'catagory_status',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`detail_file_id`),
  UNIQUE KEY `uniq_queue_id_file_name` (`queue_id`,`file_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `queue_recognize_detail` (
  `detail_file_id` bigint(20) unsigned NOT NULL COMMENT 'detail_file_id',
  `queue_id` bigint(20) NOT NULL DEFAULT '0' COMMENT 'queue_id',
  `file_name` varchar(500) NOT NULL DEFAULT '' COMMENT 'file_name',
  `catagory` varchar(500) NOT NULL DEFAULT '' COMMENT 'catagory',
  `recognize_status` int(4) NOT NULL DEFAULT '0' COMMENT 'recognize_status',
  `export_status` int(4) NOT NULL DEFAULT '0' COMMENT 'export_status',
  `recognize_result` LONGTEXT NOT NULL DEFAULT '' COMMENT 'recognize_result',
  `field_result` LONGTEXT NOT NULL DEFAULT '' COMMENT 'field_result',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`detail_file_id`),
  UNIQUE KEY `uniq_queue_id_file_name` (`queue_id`,`file_name`),
  KEY `idx_file_name` (`file_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;




