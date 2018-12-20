CREATE TABLE `settings` (
  `device_id` VARCHAR(30),
  `status` VARCHAR(30),
  `room_width` FLOAT,
  `room_height` FLOAT
);

CREATE TABLE `tables` (
  `id` INT,
  `x_pos` DECIMAL,
  `y_pos` DECIMAL,
  `width` FLOAT,
  `height` FLOAT,
  `channel` INT,
  `address` INT
);

INSERT INTO `settings` VALUES (0, "available", 1000, 800);