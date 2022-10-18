from calendar import weekday

if __name__ == "__main__":
    month, day, year = list(map(int, input().split(" ")))
    days_dict = {
                0: "monday",
                1: "tuesday",
                2: "wednesday",
                3: "thursday",
                4: "friday",
                5: "saturday",
                6: "sunday"}
    print(days_dict[weekday(
                year = year,
                month = month,
                day = day )].upper()
          )