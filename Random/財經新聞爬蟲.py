import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import jieba
import jieba.analyse
from collections import Counter

response = requests.get("https://tw.stock.yahoo.com/news/")
soup = BeautifulSoup(response.text, "html.parser")
result = soup.find_all("a", class_="C($c-primary-text)")

title = ["《台北股市》", "《國際產業》", "《各報要聞》", "《公告》", "《國際金融》", "【盤前焦點】", "《基金》", "《研究報告》"]

LINE = ""
for line in result:
    for i in range(len(title)):
        real_line = line.text
        if title[i] in line.text:
            real_line = line.text.replace(title[i], "")
            LINE += real_line
            break
    if line.text == real_line:
        LINE += line.text

dictfile = "C:/Users/user/Desktop/繁中字典檔.txt"  # 字典檔
stopfile = "C:/Users/user/Desktop/stopwords.txt"  # stopwords
fontpath = "C:/Users/user/Desktop/msjh.ttc"  # 字型檔

jieba.set_dictionary(dictfile)
jieba.analyse.set_stop_words(stopfile)

tags = jieba.analyse.extract_tags(LINE, topK=25)

seg_list = jieba.lcut(LINE, cut_all=False)
dictionary = Counter(seg_list)

freq = {}
for ele in dictionary:
    if ele in tags:
        freq[ele] = dictionary[ele]
# print(freq) # 計算出現的次數

wordcloud = WordCloud(font_path= fontpath).generate_from_frequencies(freq)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()