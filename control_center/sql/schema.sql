CREATE TABLE `settings` (
  `device_id` VARCHAR(30),
  `status` VARCHAR(30)
);

CREATE TABLE `tables` (
  `id` int,
  `x_pos` DECIMAL,
  `y_pos` DECIMAL,
  `height` FLOAT,
  `width` FLOAT
);

INSERT INTO `settings` VALUES (0, "available");