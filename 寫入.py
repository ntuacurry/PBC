# 寫入Excel
import xlwings as xw
workbook = xw.Book("record.xlsx")
sheet = workbook.sheets["記帳"]
for i in range(2:):
    cell = "A" + str(i)
    if sheet.range(cell).value = ""
        sheet.range("A" + str(i)).value = time.strftime("%Y.%m.%d", time.localtime())
        sheet.range("B" + str(i)).value = category.get()
        sheet.range("C" + str(i)).value = amount.get()
        sheet.range("D" + str(i)).value = purpose.get()

