import time
import datetime
import MySQL_control as sql
import Plot_results as plot

def main():
    boolean = True
    while(boolean):
        print("What do you want to do? (Start study = 1, Todays stats=2, stats in the time interval=3, quit=q)")
        answer=input("Answer: ")
        print(answer)
        if(answer=="1"):
                
            #make new timestamp
            timestamp = time.time()
            start_time = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
            subject=input("Subject (QM,GR,StatMec,ELSE): ")
            print("You are studying now.")
            input("Press Enter, when you have studied enough.")
            timestamp = time.time()
            end_time = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')  
            
            
            #Insert timestamp to the sql
            sql.insert(subject,start_time,end_time)
        
        if(answer=="2"):
            #make timestamp of today
            sql.stats_of_the_day()
        
        if(answer=="3"):
            print("Give starting date (in format: 1808-02-18): ")
            starting = input("date: ")
            print("Give ending date (in format: 1808-02-18): ")
            ending = input("date: ")
            dates,hours=sql.stats_of_the_spesific_time(starting, ending)
            #plot results
            plot.plot_results(dates,hours)
        if(answer=="q"):
            boolean=False
if(__name__=="__main__"):
    main()
    
