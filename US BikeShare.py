import pandas as pd
import numpy as np


CITY_DATA = {'chicago':'chicago.csv',
              'new york city': 'new_york_city.csv',
               'washington': 'washington.csv'}

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']
WEEKDAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

LINE_LEN =90
print_line = lambda char: print(char[0]*LINE_LEN)


def get_filter_city():
    #Take city from user
    #Return city name
    
    # Built and display the list of cities for which we have datasets
    city_list = []
    num_cities = 0
    
    for a_city in CITY_DATA:
        city_list.append(a_city)
        num_cities += 1
        print('     {0:20}. {1}'.format(num_cities, a_city.title()))
        
    #ask input a number for city from list
    while True:
        try:
            city_num = int(input("\n  Enter a no. of city(1-{}): ".format(len(city_list))))
        except:
            continue
        
        if city_num in range(1, len(city_list)+1):
            break
        
        #get city's name given by user
        city = city_list[city_num -1]
        return city


    
def get_filter_month():
    
    #Ask user for specific month or all
    
    while True:
        try:
            month = input('  Enter month number:  ')
        except:
                     print("      Only input 1 to 6 or a for all")
                     continue
                    
        if month == 'a':
                     month = 'all'
                     break
        
        elif month in {'1','2','3','4','5','6'}:
                     #reassign month
                     month = MONTHS[int(month)-1]
                     break
        else:
                     continue
    return month
    
                     
                     
                     
def get_filter_day():
    #ask for specific day or all
                     
    while True:
        try:
            day = input('  Enter month number "a" for all:  ')
        except:
            print("      Only input 1 to 6 or a for all")
            continue
            
            
        if day == 'a':
            day = 'all'
            break
        elif day in {'1','2','3','4','5','6'}:
            #reassign day
            # -1 for correct index
            day = WEEKDAYS[int(day) -1]
            break
        else:
            continue
    return day

def get_filter():
    
    #Ask user to specify city,month and day to analyze
    #Returns 3 items: city,month,day in str
    #city : name of the city
    #month : specific month or all
    #day :specific day or all
    
    print_line('=')
    print('\n Hello! Lets explore some US bikeshare data\n')
    
    #get the user input city
    city = get_filter_city()
    
    #get user input for month
    month = get_filter_month()
    
    #get user input for day
    day = get_filter_day()
    
                    
    return city,month,day
    
def user_stats(df):
    #user stats function display stats on bikeshare users
    
    print('  USer Stats.... ')
    start_time = time.time()
    
    #display counts of user type
    user_type = df['User']

    
def station_stats(df):
    #Display Stats on most popular station and trips
    print('  Most Popular Stations and Trip...')
    start_time = time.time()
    
    filtered_rides = len(df)
    
    #display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    start_station_trips = df['Start Station'].value_counts()[start_station]
    
    print('   Start Sation:    ',start_station)
    print('{0:30}{1}/{2} trips'.format(' ',start_station_trips,filtered_rides))
    
    #display most commmonly used end station
    end_station = df['End Station'].mode()[0]
    end_station_trips = df['End Station'].value_counts()[end_station]
    
    print('   End Station:    ',end_station)
    print('{0:30}{1}/{2} trips'.format(' ',end_station,end_station_trips))
    
    #display most frequent combination of start station and end station
    #group the results by start station adn end station
    df_start_end_combination_gd = df.group(['Start Station'],['End Station'])
    most_freq_trip_count = df_start _end_combination_gd['Trip Duration'].count().max()
    most_freq_trip = df_start_end_combination_gd['']
    
    
    
def hour_12_srt(hour):
    #converts an int hour time to string format
    
    if hour == 0:
        str_hour = '12 AM'
    elif hour == 12:
        str_hour = '12 PM'
    else:
        str_hour = '{} AM'.format(hour) if hour <12 else '{} PM'.format(hour - 12)
    return str_hour
        

    
def time_stats(df):
    #Display stats on most frequest times of travel
    
    print('   Most frequent Time of Travel...')
    start_time = time.time()
    
    #display the most common month
    month = MONTHS[df['month'].mode()[0] -1].title()
    print('  Month:   ',month)
    
    #dispay the most commonday of week
    common_day = df['day_of_week'].mode()[0]
    common_day = WEEKDAYS[common_day].title()
    print('    Day of the week:  ',common_day)
    
    #display the most common start hour
    #convert to 12-hour string
    hour = hour_12_str(df['hour'].mode[0])
    print('    Start Hour:  ',hour)
    
    print_proccesing_time(start_time)
    
    

    
def filter_summary(city,month,day,init_total_rides,df):
    #display selected city,chosen filter and simple stats on datasets
    
    start_time = time.time()
    
    filtered_rides = len(df)
    num_station_start = len(df['Start Station'].unique())
    num_staion_end = len(df['End Station'].unique())
    
    print('  Gatering Stats for:   ',city)
    print('  Filters(month,day):  ',month,' ',day)
    print('  Total rides in datasets:  ',init_total_rides)
    print('  Rides in filtered datasets:  ',filtered_rides)
    print('  Number of start station:  ',num_station_start)
    print('  Number if end staion:  ',num_station_end)
    
    print_proccesing_time(start_time)
    
    
    
    
def load_data(city,month,day):
    #loads data city,month,day
    start_time = time.time()
    
    #load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    #convert the start time column into date time
    df['Start Time'] = pd.to_datetime(df['Start Time '])
    
    #extract month,day of week and hour from start time to create new columns
    df['month'] = df['Start Time'].dt.month          #range(1-12)
    df['day_of_week'] = df['Start Time'].dt.month    #range(0-6)
    df['hour'] = df[Start Time].dt.hour              #range(0-23)
    
    init_total_rides = len(df)
    filtered_rides = init_total_rides     #actual
    
    #filter by month if applicable
    if month != 'all':
        #use the index of the MONTHS list to get the corresponding int
        month_i = MONTHS.index(month) + 1     #index() return 0-based, so +1
        
        
        #filter by month to create the new datadrame
        df = df[df.month == month_i]
        month = month.title()
        
        
    #filter by day of week
    if day != 'all':
        # use the index of WEEKDAYS list to get the corresponding int
        day_i = WEEKDAYS.index(day)     #index() returns 0-based, maches df
        
        #filter by day of week to create the new dataframe
        df = df[df.day_of_week == day_i]
        day = day.title()
        
    
    print_processing_time(start_time)
    
    filter_summary(city.title(),month,day,init_total_rides,df)
    
    return df
    
    
    
    
    
    

def main():
    while True:
        city,month,date = get_filter() #it fliter out and takes the result from th user
                                       #like which city data you want to check
        df = load_data(city,month,day) #prints the basic details about data
        
        time_stats(df)
        station_stats(df)

if __name__ == "__main__":
    main()







































