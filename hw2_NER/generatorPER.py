import os
import requests
import csv


def ckipner(content):
    data = {"text": content, "type": "ws"}  # 要輸入CKIP網站的內容，content為新聞內容
    url = "http://ckip.iis.sinica.edu.tw/service/ner/ner"
    headers = {
        'Content-Type': 'application/json'
    }
    result = requests.post(url, json=data, headers=headers).text
    # result
    stringlist = result.split('[')
    stringlist = stringlist[3:]
    length = len(stringlist)

    ner_result = {}
    for i in range(length):
        a = stringlist[i]
        iwantstring = a[0:a.find('}')]
        tagstring = a[a.find(': "'):a.find('"}')]
        front = iwantstring[0:iwantstring.find(',')]
        letter1 = iwantstring[iwantstring.find(', '):iwantstring.find(']')]
        letter2 = letter1[letter1.find(' '):]
        intfront = int(front)
        intlater = int(letter2)
        # print(content[intfront:intlater], tagstring, '"')

        # 將結果輸出成字典
        if tagstring[3:] not in ner_result.keys():
            ner_result[tagstring[3:]] = [content[intfront:intlater]]
        else:
            ner_result[tagstring[3:]].append(content[intfront:intlater])
    return ner_result


# Read and write csv
crawl_data_folder = 'crawl_data_csv'
with open(os.path.join(crawl_data_folder, 'news_data.csv'), newline='', mode='r') as csvinput, \
        open(os.path.join(crawl_data_folder, 'news_data_ckipner.csv'), newline='', mode='w') as csvoutput:
    rows = csv.DictReader(csvinput)
    fieldnames = rows.fieldnames + ['NER_ckip'] + ['PER_ckip']  # add column name to beginning
    csvwriter = csv.DictWriter(csvoutput, fieldnames)
    csvwriter.writeheader()

    for row in rows:
        # keyword = row['keywords']
        msg = row['content']
        try:
            ckipner_all = ckipner(msg)
            ckipner_PER = ckipner_all['PERSON']
            # print(ckipner_PER)
        except:
            ckipner_all = None
            ckipner_PER = None
        csvwriter.writerow(dict(row, NER_ckip=ckipner_all, PER_ckip=ckipner_PER))
        print('Finish adding NER:' + row['title'])
