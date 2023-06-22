# CTA-Bus-Data-Visualisation


This is a python project. It takes Chicago Transit Authority bus data CSV file as input and converts it into SQL database. It further performs task using the database and prints a graph to visualise the operated database.


## Functions in this code
convert(filename, dbname): Converting CSV file to SQL database

route_data():
  1. The function connects to the bus_data.db database.
  2. It then uses a SQL query to get the average daily ridership for the input route.
  3. It then prints out the average daily ridership for the input route.
  4. It then uses another SQL query to get the number of days where the input route had more than 1200 riders.
  5. It then appends the number of days where the input route had more than 1200 riders to a list called heavy_use.
  6. It then uses another SQL query to get the number of riders for the input route on each day.
  7. It then appends the number of riders for the input route on each day to a list called daily_use.
  8. It then calculates the percentage of days when the input route had more than 1200 riders, and prints it out.
  9. It then closes the connection to the database.

yr_sum(*args):

my_func():
  1. The function opens a connection to the database.
  2. The function then executes a query to get the rides column from the bus_data table where the date is like %/%/2018.
  3. The function then fetches all the data from the query and stores it in a list.
  4. The function then executes another query to get the rides column from the bus_data table where the date is like %/%/2020.
  5. The function then fetches all the data from the query and stores it in another list.
  6. The function then plots both lists on a line graph and shows it to the user.
  7. The function then saves the line graph as an image file.

bus_data_backup(filename, dbname): Creating a backup data base file

update(): Making changes in the database, decreasing every rides value by 10% where daytype is A


## Modules used
pandas 

sqlite3

matplotlib.pyplot

from matplotlib import style

