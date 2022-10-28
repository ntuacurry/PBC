def CALENDAR(year, mon):
    import calendar as cd
    import time

    month = cd.Calendar()

    # 設定每周的第一天為周日
    month.setfirstweekday(6)
    month_lst = month.monthdayscalendar(year, mon)
    for i in range(len(month_lst)):
        for j in range(7):
            if month_lst[i][j] == 0:
                month_lst[i][j] = ""
    return month_lst