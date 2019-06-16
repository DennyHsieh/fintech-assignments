# Analysis of the Final Project

## Setup
- Download StanfordNLP from [Google Drive](https://drive.google.com/file/d/1z-YgKRQMXh7pwIGyYGnSvddzhdFk46eT/view?usp=sharing)
- Install Python packages below on Python 3.6

```bash
$ pip install nltk
$ pip install opencc
$ pip install jieba
```

## Find Suspect
- Target
    - Step 1: 從文章中所有出現過的人名找出真正的犯罪嫌疑人
         - 定義與犯罪有關的字詞，與人名前後的字詞進行比對
         - 找出和犯罪罪名距離最近的的人名

    - Step 2: 找出犯罪嫌疑人的個人資訊
         - 以文法樹結構找出人物身分或職稱
         - 從人名前後查找年齡資訊

- Code: AML_Final_Demo.ipynb
- Output Data: /final_demo/AML_data_all.csv
