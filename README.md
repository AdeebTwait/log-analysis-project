# Log Analysis Project 


Part of the udacity [Full Stack Web Developer Nanodegree.](https://udacity.com/course/full-stack-web-developer-nanodegree--nd004)


## Introduction
 Python application that summarizes data from a large database using sql queries.
The database in this project is a newspaper company database where it has three tables: `articles`,  `authors` and `log`.


 - The `articles` table includes information about the authors of articles.
- The `authors` table includes the articles themselves.
- The `log` table includes one entry for each time a user has accessed the site.

And here are the questions the application should answer:
- What are the most popular three articles of all time?
- Who are the most popular article authors of all time?
- On which days did more than 1% of requests lead to errors?

Each one of these questions should be answered with a single database query.

## Required Libraries and Dependencies
- Python 3
- Postgresql
- Vagrant
- VirtualBox
- Psycopg2 (python module)

## How to run the application
Download the project zip file to your computer and unzip the file. Or clone this repository to your desktop.

Open the text-based interface for your operating system (e.g. the terminal window in Linux, the command prompt in Windows) and navigate to the project directory.

### Bringing the VM up

Bring up the VM with the following command:
``` sh
vagrant up 
```
The first time you run this command, it will take awhile, as Vagrant needs to download the VM image.

You can then log into the VM with the following command:
```sh
vagrant ssh
```

More detailed instructions for installing the Vagrant VM can be found here.

### Make sure you're in the right place
Once inside the VM, navigate to the tournament directory with this command:
```sh
cd /vagrant
```

### Load the logs into the database
First, unzip the zip file with the command:

```sh
unzip newsdata.zip
```

Then run the following command to load the logs into the database:
```sh
psql -d news -f newsdata.sql
```

### Create the views
``` sql
CREATE VIEW total_req as
            SELECT count(*)::numeric AS num, TO_CHAR(time, 'Month DD,YYYY') AS day
            FROM log
            GROUP BY day;
```

```sql
CREATE VIEW total_err as
            SELECT count(*)::numeric AS num, TO_CHAR(time, 'Month DD,YYYY') AS day
            FROM log
            WHERE status != '200 OK'
            GROUP BY day;
```
### Run the reporting tool
The logs reporting tool is executed with the following command:
```
python log-project.py
```

The answers to the three questions should now be displayed.

