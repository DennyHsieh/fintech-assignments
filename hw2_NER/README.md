# 資料搜集與文字探勘共現性進行資料視覺化

According to our final project topic(防洗錢之風險性人物評估), we decided to finish hw2 by divided to 3 parts. (Shown as below)
- 蒐集洗錢相關的新聞資訊
- 用NER挑選出人名與事件
- 並繪製共現性圖

### Package Install
```
pip install google-search-api
pip3 install googletrans
pip3 install tensorflow
git clone https://github.com/Determined22/zh-NER-TF.git
```

- google-search-api: Google搜尋套件
- googletrans: Google翻譯套件
- tensorflow: NER用到之機器學習套件

## Crawl the News

- Crawl the news with keywords of money laundering
- News:
    - appledaily(蘋果)
    - ltn(自由)
    - chinatime(中時)
- Code: https://github.com/DennyHsieh/fintech-assignments/blob/master/hw2_NER/news_crawler.py
- Output Data: 
    - csv file: https://github.com/DennyHsieh/fintech-assignments/tree/master/hw2_NER/crawl_data_csv
    - numpy file(google search result): https://github.com/DennyHsieh/fintech-assignments/tree/master/hw2_NER/search_results_npy

## NER
- Seperate NER data By 2 ways
    - NER by zh-NER-TF
        - Analysis the NER result by sample code
        - Code: https://github.com/DennyHsieh/fintech-assignments/blob/master/hw2_NER/PER.ipynb
        - NER training log: https://github.com/DennyHsieh/fintech-assignments/blob/master/hw2_NER/NER_training_log.md
    - NER by CKIP
        - Analysis the NER result from CKIP system 
        - Code and result: https://github.com/DennyHsieh/fintech-assignments/blob/master/hw2_NER/CKIP-NER.ipynb
    - Final NER result (include the result of zh-NER-TF and CKIP)
        - Data(csv with PER): https://github.com/DennyHsieh/fintech-assignments/tree/master/hw2_NER/PER

## TDM, Co-occurrence_Diagram and Heatmap
- Target:
    - 將文件中分類過的詞進行 term to matrix(TDM)
    - 將TDM轉成Co-occurrence Matrix
    - 繪製出各類別之間的共現圖
Code and result: https://github.com/DennyHsieh/fintech-assignments/blob/master/hw2_NER/Co-occurrence_Diagram.ipynb
