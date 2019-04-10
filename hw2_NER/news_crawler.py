import os
import requests
import numpy as np
import csv
from bs4 import BeautifulSoup
from google import google
from googletrans import Translator

# Google search api
num_page = 10

# Set the keywords and news(蘋果、自由、中時)
news = ["appledaily", "ltn", "chinatimes"]
websites = [" site:appledaily.com.tw", " site:ltn.com.tw", " site:chinatimes.com"]
contents = ["ndArticle_margin", "text", "article-body"]
low_risk_keywords = ["人口販運", "性剝削", "兒童", "偽造貨幣", "殺人", "重傷害", "搶奪", "勒贖", "海盜", "恐怖主義", "資恐"]
medium_risk_keywords = ["非法販賣武器", "贓物", "竊盜", "綁架", "拘禁", "妨害自由", "環保犯罪", "偽造文書"]
high_risk_keywords = ["仿冒", "盜版", "侵害營業秘密"]
exhigh_risk_keywords = ["毒品販運", "詐欺", "走私", "稅務犯罪", "組織犯罪", "證券犯罪", "貪汙賄賂", "第三方洗錢"]
all_keywords = list(low_risk_keywords + medium_risk_keywords + high_risk_keywords + exhigh_risk_keywords)

# Google translator
trans = Translator()

# If you want to change keywords, replace all_keywords to xxx_risk_keywords
for keyword in all_keywords:
    for cnt in range(len(websites)):
        search_results = google.search(keyword + websites[cnt], num_page)

        # Save google-api searching results to numpy array
        search_results_folder = 'search_results_npy'
        if not os.path.exists(search_results_folder):
            os.mkdir(search_results_folder)
        fname_search = keyword + '_' + news[cnt] + '.npy'
        fpath_search = os.path.join(search_results_folder, fname_search)
        np.save(fpath_search, search_results)

        links = []
        for result in search_results:
            # Check the validity of link
            link = result.link
            if link is None:
                continue

            try:
                req = requests.get(link, timeout=10)
                soup = BeautifulSoup(req.text, 'html.parser')
            except:
                # print('error page')
                continue

            title = result.name

            # Get the news content from website
            cnts_p_tags = ''
            find_cnts = soup.findAll('div', attrs={'class': contents[cnt]})
            if find_cnts is None:
                continue

            for find_cnt in find_cnts:
                if news[cnt] == 'appledaily':
                    title = title.split("www")[0]
                    find_p_tags = find_cnt.find('p')
                    apple_text = find_p_tags.text

                    # Remove ad
                    ads = ['推薦新聞', '跟上國際脈動', '看了這則', '即時論壇徵稿']
                    for ad in ads:
                        try:
                            apple_text = apple_text.split(ad)[0]
                        except:
                            continue
                    cnts_p_tags += apple_text
                else:
                    title = title.split("http")[0]
                    find_p_tags = find_cnt.findAll('p', attrs={'class': None})
                    for find_p_tag in find_p_tags:
                        if find_p_tag.string is None:
                            continue
                        cnts_p_tags += find_p_tag.text

            # Translate to simplified Chinese
            try:
                cnts_p_tags_cn = trans.translate(cnts_p_tags, dest="zh-CN").text
            except:
                cnts_p_tags_cn = None
                continue

            print('Finish crawling ', keyword, link)
            # print(news[cnt], title, link, cnts_p_tags, cnts_p_tags_cn)

            # Save the result ('news', 'title', 'link', 'content', 'content_cn') to csv
            crawl_data_folder = 'crawl_data_csv'
            if not os.path.exists(crawl_data_folder):
                os.mkdir(crawl_data_folder)

            with open(os.path.join(crawl_data_folder, 'news_data.csv'), mode='a+', newline='') as csvfile:
                fieldnames = ['news', 'keywords', 'title', 'link', 'content', 'content_cn']
                news_writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=',', quotechar='"')
                news_writer.writerow({'news': news[cnt], 'keywords': keyword, 'title': title, 'link': link,
                                      'content': cnts_p_tags, 'content_cn': cnts_p_tags_cn})

                # news_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                # news_writer.writerow([news[cnt], title, link, cnts_p_tags, cnts_p_tags_cn])
