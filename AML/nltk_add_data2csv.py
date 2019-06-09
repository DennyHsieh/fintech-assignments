import os
import re
import jieba
import pandas as pd
from opencc import OpenCC
from nltk.parse.stanford import StanfordParser
from nltk.tokenize import StanfordSegmenter
from nltk.tag import StanfordNERTagger
from nltk import Tree
from nltk.draw.util import CanvasFrame
from nltk.draw import TreeWidget


class Table:
    def __init__(self, keyword, cnt):
        self.no = 1
        self.profile_id = 1
        self.name = None
        self.names = []
        self.age = None
        self.title = None
        self.cnt = cnt
        self.keyword = keyword
        self.res = None

    def add_data(self):
        if self.set_data():
            datas = []
            file = os.path.join('mysql_data', 'final_demo_result.csv')
            column = ['id', 'profile_id', 'name', 'age', 'title', 'cnt', 'keyword']
            if not os.path.exists(file):
                for n in self.names:
                    # self.name = n
                    datas.append([self.no, self.profile_id, n, self.age, self.title, self.cnt, self.keyword])
                    self.no += 1
                    self.profile_id += 1
                df = pd.DataFrame(datas, columns=column)
                df.to_csv(file, encoding='utf-8', index=False)
            else:
                df = pd.read_csv(file)
                self.no = df['id'].max() + 1
                self.profile_id = df['profile_id'].max() + 1
                # self.no = df['id'].iloc[-1] + 1
                # self.profile_id = df['profile_id'].iloc[-1] + 1
                for n in self.names:
                    df_name_repeat = df.loc[df['name'] == n]
                    # print(df_name_repeat)
                    # self.name = n
                    # 重複人名，profile_id用原本的，ID+1
                    if not df_name_repeat.empty:
                        print('repeat!')
                        old_profile_id = df_name_repeat['profile_id'].iloc[0]
                        datas.append([self.no, old_profile_id, n, self.age, self.title, self.cnt, self.keyword])
                        self.no += 1
                    else:
                        datas.append([self.no, self.profile_id, n, self.age, self.title, self.cnt, self.keyword])
                        self.no += 1
                        self.profile_id += 1
                df2 = pd.DataFrame(datas, columns=column)
                df_concat = pd.concat([df, df2], ignore_index=True)
                # print(df_concat)
                df_concat.to_csv(file, encoding='utf-8', index=False)
                # print(self.no, self.profile_id)

            # print('Add data No.', self.no, 'to database. Keyword is', self.keyword)
            # print(self.no, self.profile_id, self.names, self.age, self.title, self.cnt, self.keyword)
        pass

    def seperate_sentence(self):
        sentences = []
        content = self.cnt
        for key in re.finditer(self.keyword, content):
            end_list = ['。', '：', '；', '！', '!', '？', '?']
            sentence_start = 0
            sentence_end = len(content) - 1
            for end in end_list:
                dis_to_keystart = content[:key.start()][::-1].find(end)
                if dis_to_keystart != -1: sentence_start = max(sentence_start, key.start() - dis_to_keystart)
                dis_to_keyend = content[key.end():].find(end)
                if dis_to_keyend != -1: sentence_end = min(sentence_end, key.end() + dis_to_keyend)

            sentences.append(content[sentence_start: sentence_end + 1])
        return sentences

    def standford_nlp(self, sentence_tran=None):
        os.environ["CLASSPATH"] = "./StanfordNLP/stanford-parser-2018-10-17"
        os.environ["STANFORD_MODELS"] = "./StanfordNLP/models"
        cc = OpenCC('t2s')
        sentence_simp = cc.convert(sentence_tran)

        self.res = list(jieba.cut(sentence_simp, cut_all=False))
        ch_parser = StanfordParser(model_path='./StanfordNLP/models/chinesePCFG.ser.gz')

        return ch_parser.parse(self.res)

    def draw_tree(self):
        sentences_prase = self.standford_nlp(self.cnt)
        for line in sentences_prase:
            # print(line, len(line))
            # line.draw()
            for sentence_prase in line:
                return sentence_prase

    def set_data(self):
        result_stanfordnlp = self.draw_tree()
        s2t_cc = OpenCC('s2t')
        # 正面表列句型，如果在條件內存檔，否則下一筆(目前尚未正面表列)
        if result_stanfordnlp is not None:  # 修成條件
            # Run zh-NER-TF
            # sys.stdout('python main.py --mode=demo --demo_model=1521112368')
            chi_tagger = StanfordNERTagger('./StanfordNLP/models/chinese.misc.distsim.crf.ser.gz',
                                           './StanfordNLP/jars/stanford-ner.jar')
            for word, tag in chi_tagger.tag(self.res):
                if tag == "PERSON":
                    # print(word, tag)
                    if word not in self.names:
                        word_s2t = s2t_cc.convert(word)
                        self.names.append(word_s2t)
            return True
        else:
            return False


if __name__ == "__main__":
    # Test data
    kw = '殺人'
    # content = '僱員工要睜大眼！35歲水電工黃元鴻，利用安裝監視器電源插座機會，強盜殺害莊姓老婦人，一審判無期徒刑後，民事賠償部分，台北地院認為黃是利用裝修水電職務上機會殺人劫財，是民法188條第1項所稱執行職務範圍內，昨判決黃要和水電行林姓雇主，連帶賠償莊婦兒女共462萬1220元。全案可上訴。八里雙屍命案，媽媽嘴咖啡的老闆因員工謝依涵殺人被判須連帶賠償，被稱為「史上最衰的老闆」，並引發討論，甚至出現判決結果不同的情況。記者昨到黃原本工作的水電行，等了許久都沒有看到任何人，水電行似乎已沒有營業，不知道雇主、也是黃元鴻姨丈對被連帶判賠的看法。下跪道歉 一審判無期73歲莊姓老婦人2016年11月被發現陳屍家中廚房，檢警循線逮捕老婦家裝潢的水電工黃元鴻涉有重嫌。黃原否認犯案，經警方突破心防，才坦承強盜殺人，遭檢方起訴。本案刑責部分，一審以黃當庭向被害人家屬下跪，顯有悔意，犯行未達罪無可逭，也非兩公約所稱最嚴重之罪，去年11月依強盜殺人罪判黃無期徒刑；而黃和林姓雇主遭連帶求償562萬多元附帶民事案移送民庭。被求償 雇主認不應該北院法官審理時，黃沒有意見，只是認為求償金額太高。林姓雇主則認為不該負起雇用人的責任，連帶賠償。法官認為，黃元鴻是利用到莊婦家安裝電源插座機會殺人，確實與他執行水電技工的職務有時間、處所密切關連，是民法188條第1項所稱的執行職務範圍內，不是林不能預見或無相當因果關係。此外，林對黃的行為，也無法證明他已盡選任或監督盡相當的注意義務，因此要與黃負連帶賠償責任，判決2人連帶給付精神慰撫金和殯葬費共462萬多元。'
    # content = "黃元鴻是利用到莊婦家安裝電源插座機會殺人"
    content = "媽媽嘴咖啡的老闆因員工謝依涵與員工黃豪坪兩人因殺人被判須連帶賠償，謝依涵很傷心"
    # Table(keyword=kw).draw_tree()#.draw()
    Table(keyword=kw, cnt=content).add_data()
