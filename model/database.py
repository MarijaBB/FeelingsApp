import mysql.connector
#easier and faster way through MySQL Workbench :)

mydb = mysql.connector.connect(
  host="localhost",
  user="",     # not showing publicly
  password="", # not showing publicly
  database = "feelDB"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE FeelDB")

mycursor.execute("CREATE TABLE Feelings (FeelingId SMALLINT AUTO_INCREMENT PRIMARY KEY,"
"                                        Title VARCHAR(50) NOT NULL,"
"                                        Image VARCHAR(100) NOT NULL)")

mycursor.execute("CREATE TABLE Messages (MessageId BIGINT AUTO_INCREMENT PRIMARY KEY, "
"                 Message VARCHAR(500) NOT NULL, "
"                 FeelingId SMALLINT, "
"                 ColorCode VARCHAR(25), "
"                 FOREIGN KEY (FeelingId) REFERENCES Feelings(FeelingId) ON DELETE CASCADE)")


mycursor.execute("CREATE TABLE Users (UserId BIGINT AUTO_INCREMENT PRIMARY KEY, "
"                                       UserName VARCHAR(30) NOT NULL, "
"                                       Email VARCHAR(100) NOT NULL UNIQUE, "
"                                       PasswordHash VARCHAR(255) NOT NULL, "
"                                       CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP)"  ) 

mycursor.execute("CREATE TABLE History (UserId BIGINT AUTO_INCREMENT PRIMARY KEY,"
"                                        FeelingId SMALLINT NOT NULL,"
"                                        Time DATETIME DEFAULT CURRENT_TIMESTAMP,"
"                                        FOREIGN KEY (UserId) REFERENCES Users(UserId) ON DELETE CASCADE,"
"                                        FOREIGN KEY (FeelingId) REFERENCES Feelings(FeelingId) ON DELETE CASCADE)") 

mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x)