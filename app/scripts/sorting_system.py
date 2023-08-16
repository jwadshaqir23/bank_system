from datetime import datetime

date1 = "01-10-2020"
date2 = "30-04-2021"
date3 = "25-07-2024"

def convert_to_datetime(date_str):
    try:
        return datetime.strptime(date_str, "%d-%m-%Y")
    except ValueError:
        return None

date_list = [date1, date2, date3]

# Filter out invalid dates and convert the remaining date strings to datetime objects
valid_dates = [date for date in map(convert_to_datetime, date_list) if date is not None]

# Sort the valid dates in descending order (latest to oldest)
sorted_dates = sorted(valid_dates, reverse=True)

# Print the sorted dates from the latest to the oldest
for date_obj in sorted_dates:
    print(date_obj.strftime("%d-%m-%Y"))
# make sort and get the number of row and get the data and make the ouput
