# tbl_user table ###########################
CREATE TABLE `BucketList`.`tbl_user` (
  `user_id` BIGINT UNIQUE AUTO_INCREMENT,
  `user_name` VARCHAR(255) NULL,
  `user_email` VARCHAR(255) NULL,
  `user_password` VARCHAR(255) NULL,
  PRIMARY KEY (`user_id`));



# store proc create user ###################

USE `BucketList`;
DROP procedure IF EXISTS `sp_createUser`;

DELIMITER $$
USE `BucketList`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createUser`(
    IN p_name VARCHAR(255),
    IN p_email VARCHAR(255),
    IN p_password VARCHAR(255)
)
BEGIN
    if ( select exists (select 1 from tbl_user where user_email = p_email) ) THEN
     
        select 'Email Address Exists !!';
     
    ELSE
     
        insert into tbl_user
        (
            user_name,
            user_email,
            user_password
        )
        values
        (
            p_name,
            p_email,
            p_password
        );
     
    END IF;
END$$

DELIMITER ;



# store proc #1 ###########################
USE `BucketList`;
DROP procedure IF EXISTS `sp_AuthenticateUser`;

DELIMITER $$
USE `BucketList`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_AuthenticateUser`(
IN p_email VARCHAR(255)
)
BEGIN

     select * from tbl_user where user_email = p_email;

END$$

DELIMITER ;



# create tbl_item table  ###########################
CREATE TABLE `BucketList`.`tbl_item` (
  `item_id` BIGINT UNIQUE AUTO_INCREMENT,
  `user_email` VARCHAR(255) NULL,
  `item_name` VARCHAR(255) NULL,
  PRIMARY KEY (`item_id`));


# store proc #2 ###########################
DELIMITER $$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_AddItems`(
in p_email varchar(255),
in p_item_name varchar(255)
)
BEGIN
    insert into tbl_item(
        user_email,
        item_name
    )
    values(
        p_email,
        p_item_name
    );
END

# store proc #3 ###########################

USE `Diane`;
DROP procedure IF EXISTS `sp_GetPotentialAttacks`;

DELIMITER $$
USE `Diane`$$
CREATE PROCEDURE `sp_GetPotentialAttacks` (
in p_priority INT(2)
)
BEGIN
    select log_host, log_function from wp_itsec_log where log_priority = p_priority; 
END$$

DELIMITER ;