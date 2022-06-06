CREATE SCHEMA `strtg_autoservice`;
USE `strtg_autoservice`;

CREATE TABLE Clients (
  clientID int(11) NOT NULL AUTO_INCREMENT,
  username varchar(100) DEFAULT NULL,
  password varchar(100) DEFAULT NULL,
  isEnabled int(1) DEFAULT '0',
  createdAt date DEFAULT NULL,
  PRIMARY KEY (`clientID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
INSERT INTO clients (username, password, isEnabled, createdAt) VALUES ('softys', 'sAuto123', 1, CURDATE());

CREATE TABLE roles (
	roleID int(11) NOT NULL AUTO_INCREMENT,
    roleName varchar(50) NOT NULL,
    isEnabled int(1) DEFAULT 0,
    ProcessGroupAccess INT (1) DEFAULT 0,
    ProcessAccess INT (1) DEFAULT 0,
    ProcessStructureAccess INT (1) DEFAULT 0,
    createdAt date DEFAULT NULL,
    PRIMARY KEY (`roleID`)
);

INSERT INTO roles (roleName, isEnabled, ProcessGroupAccess, ProcessAccess, ProcessStructureAccess, createdAt) VALUES ('ADMIN', 1, 1, 1, 1, CURDATE());
INSERT INTO roles (roleName, isEnabled, ProcessGroupAccess, ProcessAccess, ProcessStructureAccess, createdAt) VALUES ('SUPERVISOR', 1, 1, 1, 1, curdate());
INSERT INTO roles (roleName, isEnabled, ProcessGroupAccess, ProcessAccess, ProcessStructureAccess, createdAt) VALUES ('NORMAL',1 , 1, 1, 0, curdate());

CREATE TABLE ProcessGroups (
	groupID int(11) NOT NULL AUTO_INCREMENT,
    groupURL varchar(100) NOT NULL,
    groupName varchar(100) NOT NULL,
    clientID int(11) NOT NULL,
    isEnabled int(1) DEFAULT 0,
    PRIMARY KEY (`groupID`),
    FOREIGN KEY (clientID) REFERENCES clients(clientID)
);
INSERT INTO ProcessGroups (groupURL, groupName, clientID, isEnabled) VALUES ('https://strategio.cloud/api/','Validacion Archivos', 2, 1);

CREATE TABLE Processes (
	processID int(11) NOT NULL AUTO_INCREMENT,
    groupID int(11) NOT NULL,
    processURL varchar(100) NOT NULL,
    processName varchar(100) NOT NULL,
    isEnabled int(1) DEFAULT 0,
    isRemoved int(1) DEFAULT 0,
    PRIMARY KEY (`processID`),
    FOREIGN KEY (groupID) REFERENCES processgroups(groupID)
);
INSERT INTO Processes (groupID, processURL, processName, isEnabled, isRemoved) VALUES ( 2, '/validateData','Maestro test', 1, 0);

CREATE TABLE ValidationStructure (
	validationStructureID int(11) NOT NULL AUTO_INCREMENT,
    processID int(11) NOT NULL,
    columnName varchar(300) NOT NULL,
    columnNumber int NOT NULL,
    columnType varchar(200) NOT NULL,
    optional int(1) DEFAULT 0,
    customValidation int(1) DEFAULT 0,
    customValidationQuery varchar(500) DEFAULT '',
    errorMessage varchar(100) DEFAULT '',
    PRIMARY KEY (`validationStructureID`),
    FOREIGN KEY (processID) references processes(processID)
);
INSERT INTO ValidationStructure (processID, columnName, columnNumber, columnType, optional, customValidation, customValidationQuery, errorMessage) VALUES 
(1, 'codigoDistribuidor', 1,  'string', 0, 0, '', ''),
(1, 'nombreDistribuidor', 2,  'string', 0, 0, '', ''),
(1, 'region', 3,  'string', 1, 0, '', ''),
(1, 'oficina', 4,  'string', 1, 0, '', ''),
(1, 'checkVentas', 5,  'int', 0, 1, 'checkVentas in (0,1)', 'CheckVentas debe ser solo 0 o 1'),
(1, 'soles', 6, 'float', 0, 1, 'soles > 0', 'soles debe ser mayor a 0');

/*
DELIMITER //
CREATE PROCEDURE [] ()
BEGIN
	
END
DELIMITER //
DELIMITER ;
*/

DELIMITER //
CREATE PROCEDURE SP_UserCheck ( IN usr varchar(100), pwd varchar(100) )
BEGIN
	SELECT C.clientID
    FROM Clients AS C
    WHERE LOWER(C.username) = LOWER(usr) AND C.password = pwd
    AND C.isEnabled = 1;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE SP_getStructureProcess (IN procID int(11))
BEGIN
	SELECT
        vs.*      
    FROM processes p
    INNER JOIN validationStructure vs
		ON p.processID = vs.processID
	WHERE p.processID = 1;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE SP_verifyProcessID (IN procID int(11))
BEGIN
	SELECT processID
    FROM processes
    WHERE processID = procID
    AND isEnabled = 1
    AND isRemoved = 0;
END //
DELIMITER ;



