import os
import requests
from bs4 import BeautifulSoup
from google import google
from googletrans import Translator

# Google search api
num_page = 10

# Set the keywords and medias(蘋果、自由、中時)
websites = [" site:appledaily.com.tw", " site:ltn.com.tw", " site:chinatimes.com"]
contents = ["ndArticle_margin", "text", "article-body"]
low_risk_keywords = ["人口販運", "性剝削、兒童", "偽造貨幣", "殺人、重傷害", "搶奪", "勒贖", "海盜", "恐怖主義、資恐"]
medium_risk_keywords = ["非法販賣武器", "贓物", "竊盜", "綁架、拘禁等妨害自由", "環保犯罪", "偽造文書"]
high_risk_keywords = ["仿冒、盜版、侵害營業秘密"]
exhigh_risk_keywords = ["毒品販運", "詐欺", "走私", "稅務犯罪", "組織犯罪", "證券犯罪", "貪汙賄賂", "第三方洗錢"]
all_keywords = list(low_risk_keywords + medium_risk_keywords + high_risk_keywords + exhigh_risk_keywords)

# Google translator
trans = Translator()

for keyword in all_keywords:
    for cnt in range(len(websites)):
        search_results = google.search(keyword + websites[cnt], num_page)
        for result in search_results:
            # Check the validity of link
            if result.link is None:
                continue

            try:
                res = requests.get(result.link, timeout=10).text
            except:
                # print('error page')
                continue

            soup = BeautifulSoup(res, 'html.parser')

            # TODO: get the contents, and put the name result to zh-NER-TF model
