import os 
from datetime import datetime 


# Events with their names and dates
events = {
    "summer_break": datetime(2023, 6, 9, 15, 0),
    "lia_start": datetime(2023, 9, 25, 8, 0),
    "christmas": datetime(2023, 12, 24),
    "bellas_birthday": datetime(2023, 12, 7),
    "new_year": datetime(2024, 1, 1),
    "graduation_party": datetime(2024, 6, 9, 16, 30)
}

#construct the log directory path
log_dir = os.path.join(os.path.dirname(__file__), "logs")

# Create the log directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)


# Create the log file path
log_path = os.path.join(log_dir, "countdown.log")

current_time = datetime.now()

with open(log_path, "w") as file:
    file.write(f"-------------------------------------------------\nCountdown from {datetime.now().replace(microsecond=0)}\n-------------------------------------------------\n\n")
    file.write(f"| {'Event':<20} | {'Years':<10} | {'Months':<10} | {'Days':<10} | {'Hours':<10} | {'Minutes':<10} | {'Seconds':<10} |\n")
    file.write(f"|{'-' * 22}|{'-' * 12}|{'-' * 12}|{'-' * 12}|{'-' * 12}|{'-' * 12}|{'-' * 12}|\n")

    print(f"-------------------------------------------------\n Countdown from {datetime.now().replace(microsecond=0)}\n-------------------------------------------------\n\n")

    print(f"| {'Event':<20} | {'Years':<10} | {'Months':<10} | {'Days':<10} | {'Hours':<10} | {'Minutes':<10} | {'Seconds':<10} |")
    print(f"|{'-' * 22}|{'-' * 12}|{'-' * 12}|{'-' * 12}|{'-' * 12}|{'-' * 12}|{'-' * 12}|")



    for event, date in events.items():
        time_remaining = date - current_time

        # Calculate the breakdown of time remaining
        years = time_remaining.days // 365
        months = (time_remaining.days % 365) // 30
        days = (time_remaining.days % 365) % 30
        hours = time_remaining.seconds // 3600
        minutes = (time_remaining.seconds % 3600) // 60
        seconds = (time_remaining.seconds % 3600) % 60

        file.write(f"| {event:<20} | {years:<10} | {months:<10} | {days:<10} | {hours:<10} | {minutes:<10} | {seconds:<10} |\n")
        print(f"| {event:<20} | {years:<10} | {months:<10} | {days:<10} | {hours:<10} | {minutes:<10} | {seconds:<10} |")

    