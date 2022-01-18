import mysql.connector

def time_to_string(time_in_seconds):
    hours=int(time_in_seconds / 3600)
    time_without_hours=time_in_seconds-hours*3600
    minutes= int(time_without_hours / 60)
    seconds=time_without_hours-minutes*60
    time="Time used: " + str(hours) + "h " + str(minutes) + "min " + str(seconds) + "sec" 
    return time

def connect_to_sql():
    db = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",
    )    
    #create cursor
    mycursor = db.cursor()    
    #create database "timemanagement" if not exists    
    mycursor.execute("CREATE DATABASE IF NOT EXISTS timemanagement;")  
    mycursor.close()
    #connect to database timemanagement
    db = mysql.connector.connect(
      host="localhost",
      user="username",
      password="password",
      database="timemanagement",
    )    
    
    #create cursor
    mycursor = db.cursor()
    #create table if not exists
    mycursor.execute("CREATE TABLE IF NOT EXISTS Timemanagement_table (id INT AUTO_INCREMENT PRIMARY KEY,subject VARCHAR(255), start_time DATETIME NOT NULL, end_time DATETIME NOT NULL);")
    
    #return cursor
    return db, mycursor


def insert(subject,start_time,end_time):
    #connect to sql
    db, mycursor = connect_to_sql()
    
    #command for inserting
    insert_command = "INSERT INTO Timemanagement_table (subject ,start_time, end_time) VALUES (%s,%s,%s);"
    #values
    values = (subject,start_time,end_time)
    #execute command
    mycursor.execute(insert_command,values)
    db.commit()
    db.close()
      
      
def stats_of_the_day():
    #connect to sql
    db, mycursor = connect_to_sql()
    #complete query
    mycursor.execute("SELECT subject, SUM(time_to_sec(end_time)-time_to_sec(start_time)) FROM Timemanagement_table where end_time >= CURDATE() GROUP BY subject;")
    #get results
    myresult = mycursor.fetchall()
    if(len(myresult)==0):
        print("No results yet.")
        return
    #Print different results
    print("Studied today:")
    for result in myresult:
      name=result[0]
      time_in_seconds=result[1]
      print(name, time_to_string(time_in_seconds) )
    
    #total time used
    mycursor.execute("SELECT SUM(time_to_sec(end_time)-time_to_sec(start_time)) FROM Timemanagement_table where end_time >= CURDATE(); ")
    #get results
    myresult = mycursor.fetchall()
    print("TOTAL: ", time_to_string(myresult[0][0]))
    db.close()

#not work
def stats_of_the_spesific_time(starting,ending):
 
    
    #total time used
    db, mycursor = connect_to_sql()
    command="SELECT date(start_time), SUM(time_to_sec(end_time)-time_to_sec(start_time)) FROM Timemanagement_table where date(start_time) >= date(%s) and date(start_time) <= date(%s) GROUP BY date(start_time);"
    values=(starting,ending)
    mycursor.execute(command,values)
   #get results
    myresult = mycursor.fetchall()
    if(len(myresult)==0):
        print("No results yet.")
        return
    dates=[]
    hours=[]
    for result in myresult:
        date=result[0]
        hour=float(result[1]/3600)
        dates.append(date)
        hours.append(hour)
        print(""+str(result[0]) + " TOTAL: ", time_to_string(result[1]))
    
    db.close()
    return dates,hours
   
