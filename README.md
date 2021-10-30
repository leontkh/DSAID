# DSAID
## Section: 1
Please find the output in /output and the corresponding DAG file in /dag

## Section: 2
The database will be constructed with the tables (and respective column names) as below:

Salespeople
* salesperson_id [Unique Key]
* salesperson_name

Cars
* car_serial_no [Unique Key]
* manufacturer
* model_name
* weight
* price
* is_sold

Sales
* sale_id [Unique Key]
* date
* time
* salesperson_id
* car_serial_no [Unique]
* customer_id

Customers
* customer_id [Unique Key]
* customer_name
* customer_phone

## Section: 3
Please find the image in /system_design

<img src="system_design/DSAID.png"
     alt="System Design for Image Processing"
     style="float: left; margin-right: 10px;" />

## Section: 4
Please find the associated code and image in /sg_covid_cases

<img src="sg_covid_cases/sg_covid_cases.png"
     alt="System Design for Image Processing"
     style="float: left; margin-right: 10px;" />

## Section: 5
Please find the associated model pickle file and prediction in /classifier_model

<img src="classifier_model/prediction.png"
     alt="System Design for Image Processing"
     style="float: left; margin-right: 10px;" />