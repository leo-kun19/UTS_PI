import calendar
from datetime import datetime, timedelta
def print_future_date(days):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    day_of_week = calendar.day_name[future_date.weekday()]
    month_name = calendar.month_name[future_date.month]
    formatted_date = f"{day_of_week} on {future_date.day} {month_name} {future_date.year}"
    print(formatted_date)
current_date = datetime.now()
formatted_date = current_date.strftime("%d %B %Y")
print("tanggal sekarang:", formatted_date)

num_days = int(input("Masukkan berapa hari yang ingin dilihat dari tanggal sekarang: "))
print_future_date(num_days)
