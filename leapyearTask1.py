def leap_year(year):
    """ Функция, определяющая является год высокоснымили нет """
    g=year
    if g%4==0 and g%100!=0 or g%400==0:
        print('високосный')
    else:
        print('невисокосный')
    return g


leap_year(2100)