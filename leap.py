def leap_year(year):
    if(year % 4 == 0):
        if(year % 100 != 0):
            leap_year = year
            return True
        elif(year % 400 == 0):
             leap_year = year
             return True


    return False
