from datetime import datetime 
import datetime

# Function to print current time in YYYY MM DD HH MM SS
def display_current_datetime():
    current_date = datetime.datetime.now()
    # to remove the microseconds
    dt = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {dt} ")


display_current_datetime()


# function to calculate a future date
def calculate_future_date():
    days = int(input("Enter the number of days to add to the current date: "))
    dt = datetime.datetime.now()
    future = datetime.timedelta(days)
    future_date = dt + future
    future_date = future_date.strftime("%Y-%m-%d %H:%M:%S")   
    print(f"Future date: {future_date}")


calculate_future_date()
