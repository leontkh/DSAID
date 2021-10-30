# DSAID

This GitHub repository is my submission for the DSAID Data Engineering Technical Test from GovTech. If you have questions or doubts, you can direct them to my email at tkokhow@gmail.com.

## Contents Section
* [Section 1: Data Pipelines](https://github.com/leontkh/DSAID#section-1-data-pipelines)
* [Section 2: Databases](https://github.com/leontkh/DSAID#section-2-databases)
* [Section 3: System Design](https://github.com/leontkh/DSAID#section-3-system-design)
* [Section 4: Charts and APIs](https://github.com/leontkh/DSAID#section-4-charts-and-apis)
* [Section 5: Machine Learning](https://github.com/leontkh/DSAID#section-5-machine-learning)

## Section 1: Data Pipelines
### _Key files_

Please find
* The processed datasets in [/output](https://github.com/leontkh/DSAID/tree/master/output) 
* The airflow DAG file that processed the datasets in [/dags](https://github.com/leontkh/DSAID/tree/master/dags).

### _Steps to get started_

This solution leverages on Apache Airflow. To begin, set environment variables by opening a terminal. 
1. Set `CSV_INPUT_PATH` as the input location for dropping .csv files to be processed
e.g. `CSV_INPUT_PATH=/file/path/to/the/input/folder/`
2. Set `CSV_OUTPUT_PATH` as the output location for the processed .csv files to be saved.
3. After setting these two environment variables, set up and initiate Airflow.

After setting up Airflow, Airflow's scheduler should recognise the cron statement in the DAG's `schedule_interval` parameter, running the DAG every 1:01am. When activated, the DAG iterates through each .csv file at the CSV_INPUT_PATH location and processes each of them. 

### _What the DAG does_

For each .csv file, the DAG runs the following processes on the .csv's data:

* Deleting any rows which do not have a `name`
* Removing titles from the `name` field e.g. Mr., Dr.
* Separates the remaining name by spaces
* Picks out the first two parts and puts them into `first_name` and `last_name` respectively
* Discards the rest of the name to drop titles at the end of names e.g. MD
* Remove any zeros prepended to the `price` field by changing data type to float
* Create a new field named `above_100`, which is true if the `price` is strictly greater than 100

## Section 2: Databases
### _Database set-up_

To begin setting up the database for the car dealership, run 
> docker-compose up

To initiate the Postgres docker container
The DDL statements are included in `docker-compose.yml`

To connect to the postgres_db container, open a new terminal and use
> POSTGRES_CID=\`docker container ls| grep postgres_db| awk '{ print $1 }'\` && docker exec -it $POSTGRES_CID bash

Then to connect into Postgres use
> psql -d postgres_db -U postgres_user

Here you can run the following SQL statements after inserting in the data.

### _Database entity-relations_

The database will be constructed with the tables as per the ER diagram below, found under the folder of [/database_diagram](https://github.com/leontkh/DSAID/tree/master/database_diagram):

<img src="database_diagram/ER_diagram.png"
     alt="ER diagram for database"
     style="float: left; margin-right: 10px;" />

### _SQL statements_
SQL statements for the query task given:

1:
>SELECT 
     result.customer_name, result.customer_id, SUM(c2.price)
FROM(
     SELECT 
          c.customer_name, c.customer_id,  s.car_serial_no 
     FROM 
          customers as c 
     LEFT JOIN 
          sales as s 
     ON 
          c.customer_id = s.customer_id
     ) as result 
LEFT JOIN 
     Cars as c2 
ON 
     result.car_serial_no = c2.car_serial_no
GROUP BY 
     result.customer_id, result.customer_name;

2:
>SELECT 
     c.manufacturer, COUNT(\*) 
FROM 
     sales as s 
LEFT JOIN 
     cars as c 
ON 
     s.car_serial_no = c.car_serial_no 
WHERE 
     EXTRACT(MONTH FROM s.sale_date) = EXTRACT(MONTH FROM CURRENT_DATE) AND EXTRACT(YEAR FROM s.sale_date) = EXTRACT(YEAR FROM CURRENT_DATE) 
GROUP BY 
     c.manufacturer 
ORDER BY 
     COUNT(\*) 
DESC LIMIT 3;

## Section 3: System Design
### _Key files_

Please find the image in the folder /system_design

<img src="system_design/system_design.png"
     alt="System Design for Image Processing"
     style="float: left; margin-right: 10px;" />

*Text explaining logic behind diagram*

## Section 4: Charts and APIs
### Question

Your team decided to design a dashboard to display the statistic of COVID19 cases. You are tasked to display one of the components of the dashboard which is to display a visualisation representation of number of COVID19 cases in Singapore over time.

Your team decided to use the public data from https://documenter.getpostman.com/view/10808728/SzS8rjbc#b07f97ba-24f4-4ebe-ad71-97fa35f3b683.

Display a graph to show the number cases in Singapore over time using the APIs from https://covid19api.com/.

### Solution

Please find the associated code and image in /sg_covid_cases

<img src="sg_covid_cases/sg_covid_cases.png"
     alt="Graph of cases over time in Singapore"
     style="float: left; margin-right: 10px;" />

*Text explaining logic behind diagram, especially where data is NA*

## Section 5: Machine Learning
### Question

Using the dataset from https://archive.ics.uci.edu/ml/datasets/Car+Evaluation, create a machine learning model to predict the buying price given the following parameters:

Maintenance = High Number of doors = 4 Lug Boot Size = Big Safety = High Class Value = Good

### Solution

Please find the the model pickle file (trained_model.pkl) and prediction image (prediction.png) in the folder /classifier_model. The encoder pickle file (encoder.pkl) will be necessary in processing the inputs to the model. The .ipynb file shows the steps used to train the model.

<img src="classifier_model/prediction.png"
     alt="Classifer prediction"
     style="float: left; margin-right: 10px;" />

*Text explaining logic behind diagram*

*How to use the pickle files*