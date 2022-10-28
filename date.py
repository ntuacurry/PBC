def date(sheet):
    for i in range(5):
        week = 7 * i
        date_lst = []
        for j in range(1, 8):
            if (week + j) <= 31:
                date_lst.append(week + j)
        sheet.insert("", i, values=date_lst)
    return sheet