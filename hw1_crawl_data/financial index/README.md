# Financial Index - History Data of US Weekly Initial claims
利用爬蟲方法整理1967至今美國每週初領失業救濟金（經季節性調整）的資料

## Package
- os: 處理文件與目錄
- pandas: 讀取csv檔與資料處理，並製作Dataframe
- selenium: 爬蟲套件
- datetime: 日期格式化

## Flowchart
![]("Flow chart.png")

## 5種當別人使用你的程式最有可能會遇到的錯誤情況
- 關閉瀏覽器以前需確認檔案已下載完成
- 因為有修改檔名，更新資料時會遇到已有同名檔案存在的問題，需要先把原先檔案刪除
- 要確認檔案下載下來的格式，此例中雖然副檔名為xls但實際上是html格式
- 使用相對路徑時要注意目前所在的路徑
- 資料轉成data frame時格式可能會跑掉，如標題錯位，需要印出來確認後再整理
