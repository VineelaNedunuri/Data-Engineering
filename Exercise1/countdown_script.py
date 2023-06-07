import os 
import datetime

# Events with their names and dates
events = {
    "summer_break": datetime.datetime(2023, 6, 9, 15, 0),
    "lia_start": datetime.datetime(2023, 9, 25, 8, 0),
    "christmas": datetime.datetime(2023, 12, 24),
    "bellas_birthday": datetime.datetime(2023, 12, 7),
    "new_year": datetime.datetime(2024, 1, 1),
    "graduation_party": datetime.datetime(2024, 6, 9, 16, 30)
}

#construct the log directory path
log_dir = os.path.join(os.path.dirname(__file__), "logs")

# Create the log directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)


# Create the log file path
log_path = os.path.join(log_dir, "countdown.log")

current_time = datetime.datetime.now()

for event, date in events.items():
    time_remaining = date - current_time

    # Calculate the breakdown of time remaining
    years = time_remaining.days // 365
    months = (time_remaining.days % 365) // 30
    days = (time_remaining.days % 365) % 30
    hours, remainder = divmod(time_remaining.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    countdown = f"{event}\t{years} {months} {days} {hours} {minutes} {seconds}"   

    print(countdown)
