def is_year_leap(year):
    ##Datetime whether a year is a leap year

   if year % 4 == 0:
    print("The year", year, "is a year leap")
    return true

   if year % 100 == 0:
    print("The year", year, "is a year leap")
    return false

   if year % 400 == 0:
    print("The year", year, "is a year leap")
    return true

else:

