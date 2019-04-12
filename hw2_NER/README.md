# HW2_資料搜集與文字探勘共現性進行資料視覺化

According to our final project topic(防洗錢之風險性人物評估), we decided to finish hw2 by divided to 3 parts. (Shown as below)
- 蒐集洗錢相關的新聞資訊
- 用NER挑選出人名與事件
- 並繪製共現性圖

### Overview and Procedure
- 由於防洗錢題目非常注重判別人名是否為高風險洗錢之人物，而我們已經有風險性關鍵字(於ref資料夾有風險性關鍵字分類)，並建立資料庫
- 因此經過課堂討論後決定，以搜尋關鍵字和新聞內文為資料，
- 再將擷取內文丟到NER得到人名
- 最後做在其中一種風險屬性（最高,高,中,低風險）下的人名之共現性圖與熱點圖

### Package Install
```
pip install google-search-api
pip install googletrans
pip install tensorflow
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
- Code and result: https://github.com/DennyHsieh/fintech-assignments/blob/master/hw2_NER/Co-occurrence_Diagram.ipynb

### 分工
- 可參考git log
- DennyHsieh: Crawl the News, readme correction final organization all codes
- judy4831: NER by zh-NER-TF, TDM, Co-occurrence_Diagram and Heatmap
- BentonWu: NER by CKIP, first readme