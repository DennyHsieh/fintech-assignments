# 資料搜集與文字探勘共現性進行資料視覺化

蒐集洗錢相關的新聞資訊，用NER挑選出人名與事件，並繪製共現性圖

## Crawl the News
- Crwal the news with keywords of money laundering
- Code:

## NER
- 

## NER by CKIP
Crwal the NER result from CKIP system 
- Code:https://github.com/DennyHsieh/fintech-assignments/blob/master/hw2_NER/CKIP-NER.ipynb
### package
- os:處理文件與目錄
- requests:爬蟲工具
- csv:讀取新聞檔及匯出CKIP NER system分析的結果
### Flowchart
### 3種當別人使用你的程式最有可能會遇到的錯誤情況
- CKIP NER system的網址並不會根據輸入的內容改變，因此需透過requests.post來爬取
- 如果輸出的文字與類別對不上，且明顯是文字差一點的狀況，注意content的內容從文字開始，而不是“符號開始
- 輸入至CKIP NER的content必須把分行或空格去掉，因CKIP NER system 無法讀取過多分行的content


## 繪製共現圖
