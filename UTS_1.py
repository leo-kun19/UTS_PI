import calendar

def main():
    number = int(input("Masukkan Angka: "))
    current_year = int(calendar.datetime.datetime.now().year)
    days_this_year = 366 if calendar.isleap(current_year) else 365
    result = number / days_this_year
    print("{:.11f}".format(result))

if __name__ == "__main__":
    main()
