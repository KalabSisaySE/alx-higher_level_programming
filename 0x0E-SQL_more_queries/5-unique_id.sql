-- creates the table `unique_id`
-- unique id and default value 1

CREATE TABLE IF NOT EXISTS `unique_id` (
    `id` INT UNIQUE DEFAULT 1,
    `name` VARCHAR(256)
);
