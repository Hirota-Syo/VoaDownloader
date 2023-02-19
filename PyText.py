#import
import pandas as pd
import csv
import pprint
import unicodedata
import re

#変数

class CText(object):

    ###########################################
    # 機能	：コンストラクタ
    ###########################################
    def __init__(self, ):
        self.value = "Class2Init"

    ############################################
    ## 機能	：CSVをlistのlistで返す
    ############################################
    def OpenCsv(self, strDirAndFile):
        with open(strDirAndFile,'r') as f:
            reader = csv.reader(f)
            list_of_rows = list(reader)
        return list_of_rows

    ############################################
    ## 機能	：CSVに書き込む
    ############################################
    def WriteCsv(self, strDirAndFile, str_list):
        with open(strDirAndFile, 'w',newline="") as f:
            writer = csv.writer(f)
            writer.writerow(str_list)

    ############################################
    ## 機能	：ファイル名への使用不可文字を変換する
    ############################################
    def Rename(self, strname):
        import re
        return re.sub(r'[\\|/|:|?|.|"|<|>|\|]', '-', strname)
        #return re.sub(r'[:|?|.|<|>|\]', '-', strname)

        

###########################################
#引用1
#@ikura1, "PythonのCSV出力時に空行が入る現象の回避", qiita, https://qiita.com/ikura1/items/17e6dd19f98145afc2eb (閲覧：2022年01月12日)
#引用2
#© 2017 nkmk.me, "XPathとは？基本概念や書き方をわかりやすく解説！", note.nkmk.me, https://note.nkmk.me/python-csv-reader-writer/ (閲覧：2022年01月12日)
###########################################
