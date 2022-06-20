/*
    ESTRUCTURA DE DB
*/
USE `strtg_autoservice`;

CREATE TABLE Clients (
  clientID int(11) NOT NULL AUTO_INCREMENT,
  username varchar(100) DEFAULT NULL,
  password varchar(100) DEFAULT NULL,
  isEnabled int(1) DEFAULT '0',
  createdAt date DEFAULT NULL,
  PRIMARY KEY (`clientID`)
);
INSERT INTO clients (username, password, isEnabled, createdAt) VALUES ('softys', 'sAuto123', 1, CURDATE());

CREATE TABLE ProcessGroups (
	groupID int(11) NOT NULL AUTO_INCREMENT,
    groupName varchar(100) NOT NULL,
    clientID int(11) NOT NULL,
    isEnabled int(1) DEFAULT 0,
    PRIMARY KEY (`groupID`),
    FOREIGN KEY (clientID) REFERENCES clients(clientID)
);
INSERT INTO ProcessGroups ( groupName, clientID, isEnabled) VALUES ('GroupTestName', 1, 1);
INSERT INTO ProcessGroups ( groupName, clientID, isEnabled) VALUES ('Validacion Archivos Institucional', 1, 1);

CREATE TABLE processTypes (
	processTypeID int(11) NOT NULL AUTO_INCREMENT,
    processTypeName varchar(100) NOT NULL,
    processURL varchar(100) NOT NULL,
    PRIMARY KEY (`processTypeID`)
);
INSERT INTO processTypes (processTypeName, processURL) VALUES ('Validacion','/api/protected/dataVal/validateData');
INSERT INTO processTypes (processTypeName, processURL) VALUES ('Maestros','/api/protected/dataVal/validateData');


CREATE TABLE Processes (
	processID int(11) NOT NULL AUTO_INCREMENT,
    processTypeID int(11) NOT NULL,
    groupID int(11) NOT NULL,
    processName varchar(100) NOT NULL,
    targetTable varchar(100) NOT NULL,
    customProcedure varchar(200) NOT NULL,
    isEnabled int(1) DEFAULT 0,
    PRIMARY KEY (`processID`),
    FOREIGN KEY (groupID) REFERENCES ProcessGroups(groupID),
    FOREIGN KEY (processTypeID) references processTypes(processTypeID)
);
INSERT INTO Processes (processTypeID, groupID, processName, targetTable, customProcedure, isEnabled) VALUES (1, 1, 'Data Institucional', '', '', 1);
INSERT INTO Processes (processTypeID, groupID, processName, targetTable, customProcedure, isEnabled) VALUES (1, 1, 'Data Masivos', '', '', 1);
INSERT INTO Processes (processTypeID, groupID, processName, targetTable, customProcedure, isEnabled) VALUES (2, 2, 'Maestro test', '', '', 1);
INSERT INTO Processes (processTypeID, groupID, processName, targetTable, customProcedure, isEnabled) VALUES (2, 2, 'MaestroDTS', '', '', 1);

CREATE TABLE ValidationStructure (
	validationStructureID int(11) NOT NULL AUTO_INCREMENT,
    processID int(11) NOT NULL,
    columnName varchar(300) NOT NULL,
    columnNumber int NOT NULL,
    columnType varchar(200) NOT NULL,
    optional int(1) DEFAULT 0,
    checkValue int(1) DEFAULT 0,
    customValidation int(1) DEFAULT 0,
    customValidationQuery varchar(500) DEFAULT '',
    errorMessage varchar(100) DEFAULT '',
    PRIMARY KEY (`validationStructureID`),
    FOREIGN KEY (processID) REFERENCES Processes(processID)
);
INSERT INTO ValidationStructure (processID, columnName, columnNumber, columnType, optional, checkValue, customValidation, customValidationQuery, errorMessage) VALUES 
(1, 'codigoDistribuidor', 1,  'string', 0, 0, 0, '', ''),
(1, 'nombreDistribuidor', 2,  'string', 0, 0, 0, '', ''),
(1, 'region', 3,  'string', 1, 0, 0, '', ''),
(1, 'oficina', 4,  'string', 1, 0, 0, '', ''),
(1, 'checkVentas', 5,  'int', 0, 0, 1, 'checkVentas in (0,1)', 'CheckVentas debe ser solo 0 o 1'),
(1, 'soles', 6, 'float', 0, 1, 1, 'soles > 0', 'soles debe ser mayor a 0'),
(3, 'codigoDistribuidor', 1,'string', 0, 0, 0, '', ''),
(3, 'nombreDistribuidor', 2,'string', 0, 0, 0, '', ''),
(2, 'codigoDistribuidor', 1,'string', 0, 0, 0, '', ''),
(2, 'nroDistribuidor', 2, 'int', 0, 0, 0, '', ''),
(2, 'Fecha', 3,  'date', 0, 0, 0, '', ''),
(2, "Soles", 4,  'float', 0, 0, 0, '', '');

INSERT INTO ValidationStructure (processID, columnName, columnNumber, columnType, optional, checkValue, customValidation, customValidationQuery, errorMessage) VALUES 
(4,'CodigoDistribuidor', 1, 'string', 0, 0, 0, '', ''),
(4,'Fecha', 2, 'date', 0, 0, 0, '', ''),
(4,'NroFactura', 3, 'string', 0, 0, 0, '', ''),
(4,'CodigoCliente', 4, 'string', 0, 0, 0, '', ''),
(4,'RUC', 5, 'string', 0, 0, 0, '', ''),
(4,'RazonSocial', 6, 'string', 0, 0, 0, '', ''),
(4,'Mercado/Categoria/Tipo', 7, 'string', 0 , 0,0, '', ''),
(4,'CodigoVendedorDistribuidor', 8, 'string', 0 , 0,0, '', ''),
(4,'DNIVendedorDistribuidor', 9, 'string', 0 , 0,0, '', ''),
(4,'NombreVendedorDistribuidor', 10, 'string', 0 , 0,0, '', ''),
(4,'CodigoProducto', 11, 'string', 0 , 0,0, '', ''),
(4,'DescripcionProducto', 12, 'string', 0 , 0,0, '', ''),
(4,'Cantidad', 13, 'int', 0 , 1, 0, '', ''),
(4,'UnidadDeMedida', 14, 'string', 0, 0, 0, '', ''),
(4,'PrecioUnitario', 15, 'int', 0, 0, 0, '', ''),
(4,'PrecioTotalSinIGV', 16, 'int', 0, 1, 0, '', '');


/*
    CHECK QUERIES
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
CREATE PROCEDURE SP_verifyProcessID (IN procID int(11))
BEGIN
	SELECT processID
    FROM processes
    WHERE processID = procID
    AND isEnabled = 1;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE SP_checkRoles (IN roleNameInput int(11))
BEGIN
	SELECT *
    FROM roles
    WHERE roleName = roleNameInput;
END //
DELIMITER ;

/*
    GET QUERIES
*/
DELIMITER //
CREATE PROCEDURE SP_getProcessStructure (IN procID int(11))
BEGIN
	DECLARE json TEXT DEFAULT '';
    
	SELECT JSON_OBJECT(
    'processName', P.processName,
    'validationData',
	( SELECT JSON_ARRAYAGG(JSON_OBJECT(
		'validationStructureID', VS.validationStructureID,
        'processID', VS.processID,
        'columnName', VS.columnName,
        'columnNumber', VS.columnNumber,
        'columnType', vs.columnType,
        'optional', vs.optional,
        'checkValue', vs.checkValue,
        'customValidation', vs.customValidation,
        'customValidationQuery', vs.customValidationQuery,
        'errorMessage', vs.errorMessage
	)))) INTO json
    FROM processes P
    INNER JOIN validationStructure VS
		ON P.processID = VS.processID
    WHERE P.processID = procID
    AND P.isEnabled = 1;
    
    select json;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE SP_getGroups (IN cliID int(11))
BEGIN
	DECLARE json TEXT DEFAULT '';
	SELECT DISTINCT JSON_ARRAYAGG(JSON_OBJECT(
        'groupID', PG.groupID,
        'groupName', groupName, 
        'isEnabled', PG.isEnabled
	)) INTO json
	FROM ProcessGroups PG
    WHERE clientID = cliID; 
    SELECT json;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE SP_getProcesses (IN grpID int(11))
BEGIN
	DECLARE json TEXT DEFAULT '';
	SELECT DISTINCT JSON_ARRAYAGG(JSON_OBJECT(
		'processID', P.processID,
        'processType', TP.processTypeName,
        'processName', processName,
        'targetTable', targetTable,
        'customProcedure', customProcedure,
        'isEnabled', P.isEnabled
	)) into json
	FROM Processes P
    INNER JOIN processTypes TP
		ON TP.processTypeID = P.processTypeID
    WHERE P.GroupID = grpID;
    SELECT json;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE SP_getValidation (IN processID int(11))
BEGIN
	DECLARE json TEXT DEFAULT '';
	SELECT DISTINCT JSON_ARRAYAGG(JSON_OBJECT(
		'validationStructureId', VS.validationStructureId, 
        'columnName', columnName, 
        'columnNumber', columnNumber, 
        'columnType', columnType,
		'optional', optional, 
        'checkValue', checkValue,
        'customValidation', customValidation, 
        'customValidationQuery', customValidationQuery, 
        'errorMessage', errorMessage
	)) into json
	FROM validationStructure VS
    WHERE VS.processID = processID;
    SELECT json;
END //
DELIMITER ;

/*
    GetInfo
*/
DELIMITER //
CREATE PROCEDURE SP_getProcessInfo (processID int(11))
BEGIN
	DECLARE json TEXT DEFAULT '';
    
	SELECT DISTINCT JSON_OBJECT(
		'processID', P.processID,
        'processType', TP.processTypeName,
        'processType', PG.groupName,
        'processName', processName,
        'targetTable', targetTable,
        'customProcedure', customProcedure,
        'isEnabled', P.isEnabled
	) into json
	FROM Processes P
    INNER JOIN processTypes TP
		ON TP.processTypeID = P.processTypeID
	INNER JOIN processgroups PG
		ON PG.groupID = P.groupID
    WHERE P.GroupID = grpID;
    
    SELECT json;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE SP_getGroupInfo ( IN grpID int(11) )
BEGIN
	DECLARE json TEXT DEFAULT '';
	SELECT DISTINCT JSON_OBJECT(
		'groupID', PG.groupID,
        'groupName', PG.groupName,
        'isEnabled', PG.isEnabled
	) into json
	FROM processgroups PG
	WHERE PG.groupID = grpID;
    SELECT json;
END //
DELIMITER ;

/*
    UPSERT ITEM
*/
DELIMITER //
CREATE PROCEDURE SP_upsertGroup ( grpID int(11), grpName varchar(100), cliID int(11), isEnbld int(1) )
BEGIN
	IF EXISTS ( SELECT * FROM processgroups WHERE groupID = grpID LIMIT 1 ) THEN
		BEGIN
			UPDATE processGroups SET
				groupName = grpName,
				isEnabled = isEnbld
			WHERE groupID = grpID;
			SELECT grpID;
		END;
		ELSE
		BEGIN
			INSERT INTO processgroups (groupName, clientID, isEnabled) VALUES ( grpName, cliID, isEnbld );
			SELECT LAST_INSERT_ID();
		END;
	END IF;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE SP_upsertProcess ( procID int(11), procTypeID int(11), grpID int(11), procName varchar(100), target varchar(100), customProc varchar(200), isEnbld int(1) )
BEGIN
	IF EXISTS ( SELECT * FROM Processes WHERE ProcessID = procID LIMIT 1 ) THEN
		BEGIN
			UPDATE processes SET
				processTypeID = procTypeID,
                groupID = grpID,
                processName = procName,
                targetTable = target,
                customProcedure = customProc,
                isEnabled = isEnbld
			WHERE processID = procID;
            SELECT procID;
        END;
	ELSE
		BEGIN
			INSERT INTO Processes ( procTypeID, groupID, processName, targetTable, customProcedure, isEnabled ) VALUES 
                ( procTypeID, grpID, procName, target, customProc, isEnbld );
             SELECT LAST_INSERT_ID();
        END;
	END IF;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE SP_upsertValidation ( valID int(11),  procID int(11), clName varchar(100), clNumber int(11), clType varchar(100), opt int(1), val int(1), customVal int(1), customValQuery varchar(500), errMsg varchar(100) )
BEGIN
	IF EXISTS ( SELECT * FROM validationstructure WHERE validationStructureID = valID LIMIT 1 ) THEN
		BEGIN
		UPDATE validationStructure SET	
			processID = procID,
            columnName = clName,
            columnNumber = clNumber,
            columnType = clType,
            optional = opt,
            checkValue = val,
            customValidation = customVal,
            customValidationQuery = customValQuery,
            errorMessage = errMsg
		WHERE validationStructureID = valID;
        SELECT valID;
		END;
    ELSE
		BEGIN
		INSERT INTO validationstructure ( processID, columnName, columnNumber, columnType, optional, checkValue,  customValidation, customValidationQuery, errorMessage ) 
		VALUES ( procID, clName, clNumber, clType, opt, val,  customVal, customValQuery, errMsg );
		SELECT LAST_INSERT_ID();
		END;
    END IF;
END //
DELIMITER ;

/*
    DELETE ITEM
*/
DELIMITER //
CREATE PROCEDURE SP_deleteGroup ( IN grpID INT(11) )
BEGIN
	DELETE FROM ProcessGroups WHERE groupID = grpID;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE SP_deleteProcess ( IN procID INT(11) )
BEGIN
	DELETE FROM Processes WHERE processID = procID;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE SP_deleteValidations ( IN procID INT(11) )
BEGIN
	DELETE FROM validationStructure WHERE processID = procID;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE SP_getCheckValues (IN procID int(11) )
BEGIN
	SELECT JSON_ARRAYAGG(
		JSON_OBJECT(
			'columnName', columnName
	))
    FROM validationStructure
    WHERE processID = procID 
    AND checkValue = 1
    AND columnType IN ('int','float');
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE SP_getCheckCustomProcedure (IN procID int(11) )
BEGIN
	SELECT customProcedure
    FROM processes
    WHERE processID = procID AND isEnabled = 1;
END //
DELIMITER ;

SELECT * FROM validationstructure where processID = 4