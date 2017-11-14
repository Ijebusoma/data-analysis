This is a project based on the Udacity Fullstack nanodegree. 
We are required to create an SQL log report based on analysis of data from a large database.
The report should pull data from the database through Python code and answer the following question:

* 1. What are the most popular three articles of all time? Which articles have been accessed the most? 
* 2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views?
* 3. On which days did more than 1% of requests lead to errors? This involves analysis the status code returned by each request and determining which requests led to errors.




### MAIN PREREQUISUITES
* You need to have Python installed on your PC
* Postgresql is also required

### STEPS TO RUN THIS PROJECT
* Install Postgresql by following this [guide](https://www.postgresql.org/docs/9.2/static/installation.html).

  On Linux terminal, you can simply use this command instead: ```sudo apt-get -qqy install make zip unzip postgresql```
  * Create a user for Postgresql with the command: ```sudo postgres -c 'createuser -dRS <username>'```
* Clone the sample [data](https://github.com/udacity/fullstack-nanodegree-vm)
* Create the news database locally with the command: ```psql -c 'createdb news ```
* Populate the database just created with the sample data by running ```psql news -f newsdata.sql```
* Create the views used in this project with the commands below
* Change directory to the location where you cloned the project
* Run ```python newsdata.py```
  
##### POSTGRESQL SHORTCUTS
* Connect to the database : ```psql news```
* See more about a table: ```\d <tablename>```
* Delete a view: ```drop view --viewname```

#### SQL Command To Create the Views Used in this Project

##### 1. total_request

```
CREATE VIEW total_request AS
SELECT count(*) AS COUNT,
       date(TIME) AS date
FROM log
GROUP BY date
ORDER BY COUNT DESC; 
```

##### 2. error_request
```
CREATE VIEW error_request AS
SELECT count(*) AS COUNT,
       date(TIME) AS date
FROM log
WHERE status like '%404%'
GROUP BY date
ORDER BY COUNT DESC;
```
##### 3. error_rate
```
CREATE VIEW error_rate AS
SELECT total_request.date,
       round((100.0*error_request.count)/total_request.count,2) AS err_perc
FROM error_request,total_request
WHERE error_request.date=total_request.date;
```
![alt text](https://github.com/Ijebusoma/data-analysis/blob/master/logresult.png)
