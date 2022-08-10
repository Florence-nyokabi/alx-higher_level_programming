# 0x0E-SQL_more_queries


## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
  * How to create a new MySQL user
  * How to manage privileges for a user to a database or table
  * What’s a `PRIMARY KEY`
  * What’s a `FOREIGN KEY`
  * How to use `NOT NULL` and `UNIQUE` constraints
  * How to retrieve datas from multiple tables in one request
  * What are subqueries
  * What are `JOIN` and `UNION`


### Requirements
#### General
  * Allowed editors: `vi`, `vim`, `emacs`
  * All your files will be executed on Ubuntu 20.04 LTS using `MySQL 8.0` (version 8.0.25)
  * All your files should end with a new line
  * All your SQL queries should have a comment just before (i.e. syntax above)
  * All your files should start by a comment describing the task
  * All SQL keywords should be in uppercase (`SELECT`, `WHERE…`)
  * A `README.md` file, at the root of the folder of the project, is mandatory
  * The length of your files will be tested using `wc`
  
  
# More Info
## Comments for your SQL file:

```
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```

## Install MySQL 8.0 on Ubuntu 20.04 LTS

```
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
```

## Connect to your MySQL server:

```
$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$
```

## Use “container-on-demand” to run MySQL

**In the container, credentials are `root/root`**

  * Ask for container `Ubuntu 20.04`
  * Connect via SSH
  * OR connect via the Web terminal
  * In the container, you should start MySQL before playing with it:

```
$ service mysql start                                                   
 * Starting MySQL database server mysqld 
$
$ cat 0-list_databases.sql | mysql -uroot -p                               
Database                                                                                   
information_schema                                                                         
mysql                                                                                      
performance_schema                                                                         
sys                      
$
```
**In the container, credentials are `root/root`**

## How to import a SQL dump

```
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
```

![image](https://user-images.githubusercontent.com/99530400/183885718-1bae3255-23c8-4b74-b391-9647f677f76f.png)


# Tasks
## 0. My privileges!

Write a script that lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on your server (in localhost).

```
guillaume@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password: 
ERROR 1141 (42000) at line 3: There is no such grant defined for user 'user_0d_1' on host 'localhost'
guillaume@ubuntu:~/$ 
guillaume@ubuntu:~/$ echo "CREATE USER 'user_0d_1'@'localhost';" |  mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ echo "GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';" |  mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password: 
Grants for user_0d_1@localhost                                                                                                
GRANT SELECT, INSERT, UPDA..., DROP ROLE ON *.* TO `user_0d_1`@`localhost`                                                                                                                             
GRANT APPLICATION_PASSWORD_ADMIN,AUDIT...,XA_RECOVER_ADMIN ON *.* TO `user_0d_1`@`localhost`                                        
ERROR 1141 (42000) at line 4: There is no such grant defined for user 'user_0d_2' on host 'localhost'              
guillaume@ubuntu:~/$ 
```

**Repo:**

  * GitHub repository: `alx-higher_level_programming`
  * Directory: `0x0E-SQL_more_queries`
  * File: `0-privileges.sql`
   
# 1. Root user

Write a script that creates the MySQL server user `user_0d_1`.

  * `user_0d_1` should have all privileges on your MySQL server
  * The `user_0d_1` password should be set to user `_0d_1_pwd`
  * If the user `user_0d_1` already exists, your script should not fail

```
guillaume@ubuntu:~/$ cat 1-create_user.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password: 
Grants for user_0d_1@localhost                                                                                                
GRANT SELECT, INSERT..., DROP ROLE ON *.* TO `user_0d_1`@`localhost`                                                                                                                             
GRANT APPLICATION_PASSWORD_ADMIN,...,XA_RECOVER_ADMIN ON *.* TO `user_0d_1`@`localhost`                                        
ERROR 1141 (42000) at line 4: There is no such grant defined for user 'user_0d_2' on host 'localhost'
guillaume@ubuntu:~/$ 
```

**Repo:**

  * GitHub repository: `alx-higher_level_programming`
  * Directory: `0x0E-SQL_more_queries`
  * File: `1-create_user.sql`
