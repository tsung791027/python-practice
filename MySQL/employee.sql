Create TABLE IF NOT EXISTS employee(
    ID INT AUTO_INCREMENT,
    Birth_date DATE NOT NULL,
    Fist_name VARCHAR(20) NOT NULL,
    Last_name VARCHAR(20) NOT NULL,
    Gender ENUM('M', 'F') NOT NULL,
    Hired_date DATE NOT NULL DEFAULT "2020-01-01",
    PRIMARY KEY(ID)
);