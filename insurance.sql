CREATE DATABASE Insurance;
USE Insurance;

CREATE TABLE User (
    userId INT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    role VARCHAR(50) NOT NULL
);
CREATE TABLE Client (
    clientId INT PRIMARY KEY,
    clientName VARCHAR(50) NOT NULL,
    contactInfo VARCHAR(10) NOT NULL,
    policy varchar(50)
) ;
CREATE TABLE Claim (
    claimId INT PRIMARY KEY,
    claimNumber INT,
    dateFiled DATE NOT NULL,
    claimAmount DECIMAL(10, 2) NOT NULL,
    status VARCHAR(255) NOT NULL,
    policy varchar(50),
    client varchar(50)
);
CREATE TABLE Payment (
    paymentId INT PRIMARY KEY,
    paymentDate DATE NOT NULL,
    paymentAmount DECIMAL(10, 2) NOT NULL,
    client varchar(50)
);

CREATE TABLE Policy (
  
INSERT INTO user(userId,username,password,role) VALUES 
(1,'lebron','james','investor'),
(2,'stephen','curry','developer');

INSERT INTO Client(clientId,clientName,ContactInfo,Policy) VALUES
(1,'Newman','8765432112','Health'),
(2,'Hilton','9852316782','LongTerm');

INSERT INTO Claim(claimId,claimNumber,dateFiled,claimAmount,status,policy,client) VALUES 
(1,'345','2019-7-23','50000','OPEN','Health','Lebron'),
(2,'678','2019-3-19','20000','CLOSED','LongTerm','Stephen');

INSERT INTO Payment(PaymentId,PaymentDate,PaymentAmount,Client) VALUES 
(1,'2019-4-04','10000','Stephen'),
(2,'2019-12-22','43000','Lebron');

SELECT * FROM student;

SELECT * FROM claim;