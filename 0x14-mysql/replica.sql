-- Create user to check DB status 
-- Run on the master server

CREATE USER IF NOT EXISTS 'replica_user'@'%'
IDENTIFIED BY 'replica01';
GRANT REPLICATION SLAVE, REPLICATION CLIENT ON *.*
TO 'replica_user'@'%';
FLUSH PRIVILEGES;

-- Grant holberton privileges
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
