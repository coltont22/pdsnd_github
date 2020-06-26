import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    print("Please type in the city you'd like to view. (Chicago, New York City, or Washington)")
    city_name = 0
    while city_name < 1:
        city = input().lower()
        if city not in ('chicago', 'new york city', 'washington'):
            print("Please input one of the following cities: Chicago, New York City, or Washington")
        else:
            city_name +=1

    # TO DO: get user input for month (all, january, february, ... , june)
    print("Please type in the month you'd like to view. (All, January, February, March, April, May, or June")
    month_start = 0
    while month_start < 1:
        month = input().lower()
        if month not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
            print("Please input one of the following months: All, January, February, March, April, May, or June")
        else:
            month_start += 1

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print("Please type in the day of the week you'd like to view. (All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday)")
    day_name = 0
    while day_name < 1:
        day = input().lower()
        if day not in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            print("Please input one of the following days: All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday")
        else:
            day_name += 1

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month: ",df['month'].mode())

    # TO DO: display the most common day of week
    print("The most common day of the week is: ",df['day_of_week'].mode())

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("The most common Hour of the day is: ", df['hour'].mode())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].value_counts()
    start = start_station.idxmax()
    print("The most popular starting point is: ",start)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].value_counts()
    end = end_station.idxmax()
    print("The most popular ending point is: ", end)

    # TO DO: display most frequent combination of start station and end station trip
    # got help from : https://stackoverflow.com/questions/53037698/how-can-i-find-the-most-frequent-two-column-combination-in-a-dataframe-in-python
    comb_station = df.groupby(['Start Station','End Station']).size()
    comb = comb_station.idxmax()
    print("The most popular combination of stations is, starting at: ",comb[0]," and ending at: ",comb[1])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("The total is: ",df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print("The average is: ",df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()


    # TO DO: Display counts of user types
    user= df['User Type'].value_counts()
    print(user)

    # TO DO: Display counts of gender
    if 'Gender' not in df:
        print("Filtered selection doesn't have data on gender.")
    else:
        gender= df['Gender'].value_counts()
        print(gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in df:
        print("Filtered selection doesn't have data on Birth Year.")
    else:
        print("The earlest birth year was: ", df['Birth Year'].min().astype(int))
        print("The most recent birth year was: ", df['Birth Year'].nlargest(1).astype(int))
        print("The most common birth year was: ", df['Birth Year'].mean().astype(int))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    print("Would you like to see the raw data?")

    data = 0
    while data < 1:
        raw = input().lower()
        if raw not in ('yes','no'):
            print("Please input yes or no")
        else:
            data +=1
    data_1=0
    starting = 0
    ending = 5
    while data_1 < 1:
        if raw == 'yes':
            print(df.iloc[starting:ending])
            starting += 5
            ending += 5
