import openyxl
def export(aelf, stocks):
 wb = openyxl.workbook()
 sheet = wb.create_sheet("健身房人數", 0)
 
 
 response = requests.get(
	    "https://dasc.cyc.org.tw/api")
    soup = BeautifulSoup(response.text, "lxml")
 
 
    for stock in stocks:
	sheet.append(stock)
 
    wb.save("健身房人數.xlsx")