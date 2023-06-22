# Ankit Anand
# aanand35@uic.edu
# I hereby attest that I have adhered to the rules for quizzes and projects as well as UIC’s Academic Integrity standards. Signed: Ankit Anand

import pandas  # importing pandas
import sqlite3  # importing sql
import matplotlib.pyplot as plt  # importing matplotlib
from matplotlib import style  # importing matplotlib styles


def convert(filename, dbname):
  """Converting CSV file to SQL database"""
  data = pandas.read_csv(
    "bus_data.csv"
  )  # Using pandas to read a csv file and store it in a dataframe.
  conn = sqlite3.connect(dbname)
  cur = conn.cursor()
  cur.execute(
    "DROP table IF EXISTS bus_data"
  )  # Using the execute function to drop the table "bus_data" if it exists.

  cur.execute(
    "CREATE TABLE bus_data (route text, date text, daytype text, rides float)"
  )  # Creating a table called bus_data with four columns: route, date, daytype and rides.

  for i in range(len(data)):
    a = data['route'][i]
    a = "'" + a + "'"
    b = data['date'][i]
    b = "'" + b + "'"
    c = data['daytype'][i]
    c = "'" + c + "'"
    d = data['rides'][i]

    cur.execute("INSERT INTO bus_data VALUES (%s, %s, %s, %f)" % (a, b, c, d))

  conn.commit()
  conn.close()


convert("bus_data.csv", "bus_data.db")

daily_use = []  # Empty list to store daily use data
heavy_use = []  # Empty list to heavy use data (1200 > rides)

input_route = input(
  "Enter route: ")  # Stores the route in the input_route variable.


def route_data():
  """1. The function connects to the bus_data.db database.
2. It then uses a SQL query to get the average daily ridership for the input route.
3. It then prints out the average daily ridership for the input route.
4. It then uses another SQL query to get the number of days where the input route had more than 1200 riders.
5. It then appends the number of days where the input route had more than 1200 riders to a list called heavy_use.
6. It then uses another SQL query to get the number of riders for the input route on each day.
7. It then appends the number of riders for the input route on each day to a list called daily_use.
8. It then calculates the percentage of days when the input route had more than 1200 riders, and prints it out.
9. It then closes the connection to the database."""

  conn = sqlite3.connect("bus_data.db")
  cur = conn.cursor()
  output = cur.execute(
    "SELECT AVG(rides) FROM bus_data WHERE route LIKE '{}'".format(
      input_route))

  data = output.fetchall()

  for i in data:
    print("Average daily ridership for route", input_route, "is", round(i[0]))
  heavy_data = cur.execute(
    "SELECT rides FROM bus_data WHERE rides > 1200 AND route LIKE '{}'".format(
      input_route))
  heavy_data_output = heavy_data.fetchall()
  for i in heavy_data_output:
    heavy_use.append(i[0])

  daily_data = cur.execute(
    "SELECT rides FROM bus_data WHERE route LIKE '{}'".format(input_route))
  daily_data_output = daily_data.fetchall()
  for i in daily_data_output:
    daily_use.append(i[0])

  len_heavy_use = len(heavy_use)
  len_daily_use = len(daily_use)

  percentage = (len_heavy_use / len_daily_use) * 100
  print("Percentage of days for which that route is in heavy use", round(percentage),
        "%")
  conn.close()


route_data()

year_input = input("Enter year: ")
year_split = year_input.split()  # Spliting input
sum_store = []  # Empty list to store sum of all the input years


def yr_sum(*args):
  conn = sqlite3.connect("bus_data.db")
  cur = conn.cursor()
  for i in args:
    output = cur.execute(
      "SELECT SUM(rides) FROM bus_data WHERE date LIKE '%/%/{}'".format(i)
    )  # The SQL query selects the sum of the rides column from the bus_data table where the date column contains the value of i
    data = output.fetchall(
    )  # The code uses a for loop to iterate through the data. Then, it appends the sum of each year to the sum_store list. Then, it uses another for loop to iterate through the sum_store list. Then, it adds the sum of each year to the count variable. Then, it prints out the sum of all rides in the input years
    for j in data:
      sums = j[0]
      sum_store.append(sums)
      count = 0
      for number in sum_store:
        count += number
  print("Sum of all rides of input years:", count)

  conn.close()


yr_sum(*year_split)

lst1 = []  # Empty list to store data for 2018
lst2 = []  # Empty list to store data for 2020


def my_func():
  """1. The function opens a connection to the database.
2. The function then executes a query to get the rides column from the bus_data table where the date is like %/%/2018.
3. The function then fetches all the data from the query and stores it in a list.
4. The function then executes another query to get the rides column from the bus_data table where the date is like %/%/2020.
5. The function then fetches all the data from the query and stores it in another list.
6. The function then plots both lists on a line graph and shows it to the user.
7. The function then saves the line graph as an image file."""

  conn = sqlite3.connect("bus_data.db")
  cur = conn.cursor()
  output = cur.execute("SELECT rides FROM bus_data WHERE date LIKE '%/%/2018'")
  data = output.fetchall()
  for i in data:
    lst1.append(i[0])
  output2 = cur.execute(
    "SELECT rides FROM bus_data WHERE date LIKE '%/%/2020'")
  data2 = output2.fetchall()
  for j in data2:
    lst2.append(j[0])
  style.use("ggplot")
  plt.plot(lst1, label="2018 Ridership")
  plt.plot(lst2, label="2020 Ridership")
  plt.legend()
  plt.show()
  plt.savefig("my_fig.png")
  conn.close()


my_func()


def bus_data_backup(filename, dbname):
  """Creating a backup data base file"""
  data = pandas.read_csv("bus_data.csv")
  conn = sqlite3.connect(dbname)
  cur = conn.cursor()
  cur.execute("DROP table IF EXISTS bus_data_backup")

  cur.execute(
    "CREATE TABLE bus_data_backup (route text, date text, daytype text, rides float)"
  )

  for i in range(len(data)):
    a = data['route'][i]
    a = "'" + a + "'"
    b = data['date'][i]
    b = "'" + b + "'"
    c = data['daytype'][i]
    c = "'" + c + "'"
    d = data['rides'][i]

    cur.execute("INSERT INTO bus_data_backup VALUES (%s, %s, %s, %f)" %
                (a, b, c, d))

  conn.commit()
  conn.close()


bus_data_backup("bus_data.csv", "bus_data_backup.db")


def update():
  """Making changes in the database, decreasing every rides value by 10% where daytype is A"""
  conn = sqlite3.connect("bus_data.db")
  cur = conn.cursor()
  sql_comm = "UPDATE bus_data SET rides = rides - rides*0.1 WHERE daytype LIKE 'A'"
  sql_floor = "UPDATE FLOOR(rides) AS FLOOR_rides FROM bus_data WHERE daytype LIKE 'A'"
  cur.execute(sql_comm)
  cur.execute(sql_floor)
  conn.commit()
  conn.close()


update()
