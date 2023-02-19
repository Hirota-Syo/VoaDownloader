import PyChrome
import PyPdf
import PyText

import os
import shutil
from datetime import datetime

URL_VOA = "https://learningenglish.voanews.com/"
XPATH_BTN_ARTICLE = "/html/body/div[2]/div/div[4]/div[3]/div/div[1]/div/h2/a"
XPATH_BTN_NO1 = "/html/body/div[2]/div/div[3]/div[2]/div/div/div[2]/div/ul/li[1]/div/div/a/h4"
XPATH_BTN_NO2 = "/html/body/div[2]/div/div[3]/div[2]/div/div/div[2]/div/ul/li[2]/div/div/a/h4"
XPATH_TITLE = "/html/body/div[2]/div/div[3]/div/div[1]/div/div[2]/h1"
DIR_ONEDRIVE = "C:/Users/hirot/OneDrive/global/English/"
STR_XPATH_BTN_DWNLAD = "/html/body/div[2]/div/div[3]/div/div[2]/div/div/div/div[1]/div/div[1]/div[1]/div/div[2]/div/div/ul/li[1]/a"

###########################################
# 機能 ：main
###########################################
def main():
    Chrome = PyChrome.CChrome()
    Pdf = PyPdf.CPdf()
    Text = PyText.CText()
    
    #Chromeを開始する
    Chrome.StartDriver()    

    #learning Engllishまで移動する
    Chrome.OpenUrl(URL_VOA)
    Chrome.ClickXpath(XPATH_BTN_ARTICLE)
    Chrome.ClickXpath(XPATH_BTN_NO1)
    
    #コンテンツのタイトルを取得する
    strTitl = Chrome.strGetContent(XPATH_TITLE)
    strTitl = Text.Rename(strTitl)

    #PDFを保存する
    strUrl = Chrome.GetCurUrl()
    Pdf.SaveHtmlAsPdf(strUrl,strTitl+".pdf")
    
    #mp3を保存する
    strHref = Chrome.GetHref(STR_XPATH_BTN_DWNLAD)
    Chrome.download_file(strHref,os.getcwd()+"/"+strTitl+".mp3")
    
    #Ondriveにフォルダを作る
    strYymmdd = datetime.today().strftime('%y%m%d')
    strNewDir = DIR_ONEDRIVE+strYymmdd
    os.makedirs(strNewDir, exist_ok=True)
    
    try:
        new_path = shutil.move(strTitl+".pdf", strNewDir)
    except Exception as e:
        print("error:shutil.move")
        pass
    try:
        new_path = shutil.move(strTitl+".mp3", strNewDir)
    except Exception as e:
        print("error:shutil.move")
        pass


    Chrome.QuitDriverOpened()

if __name__ == "__main__":
    main()