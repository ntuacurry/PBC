string = input(str())
str = string.split()
#print(str)
i = (len(str))
str1 = ''

for n in range(0, i):
 str1 = str1 + '+' + str[n]
list_str1 = list(str1)
list_str1.pop(0)
str2 = ''.join(list_str1)

GS = 'https' + '://' + 'scholar.google.com.tw/scholar?hl=zh-TW&as_sdt=0%2C5&q=' + str2 + '&btnG='

import webbrowser
webbrowser.open(GS, new = 0, autoraise = True)
#print(GS)
