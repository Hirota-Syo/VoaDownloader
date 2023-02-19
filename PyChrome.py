#import
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import chromedriver_binary
import time
import os
import sys
import glob
import shutil
import time
import json
from pyhtml2pdf import converter

#変数

class CChrome(object):

    ###########################################
    # 機能	：コンストラクタ
    ###########################################
    def __init__(self, ):
        self.value = "Class2Init"
        self.driver = None

    ###########################################
    # 機能	：WebDriverを起動する
    ###########################################
    def StartDriver(self, ):
        self.driver = webdriver.Chrome()

    ###########################################
    # 機能	：WebDriverを閉じる
    ###########################################
    def QuitDriver(self, ):
        self.driver.quit()

    ###########################################
    # 機能	：ウィンドウを閉じる
    ###########################################
    def CloseDriver(self,):
        self.driver.close()

    ###########################################
    # 機能	：WebDriverを起動する（すでに開いているChromeを取得）
    ###########################################
    def StartDriverOpened(self,):

        # 起動時にオプションをつける。（ポート指定により、起動済みのブラウザのドライバーを取得）
        options = webdriver.ChromeOptions()
        options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        self.driver = webdriver.Chrome(options=options)
        
    ###########################################
    # 機能	：Windowをすべて閉じる（ウィンドウ内のすべてのタブ）
    ###########################################
    def QuitDriverOpened(self,):

        #開いているタブをすべて閉じる
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            self.driver.close()

        self.QuitDriver()
        return 

    ###########################################
    # 機能	：ChromeであるURLのWebサイトを開く
    # 引数	：strurl    URL
    ###########################################
    def OpenUrl(self,strurl):
        self.driver.get(strurl)

    ###########################################
    # 機能	：ラジオボタン押下
    ###########################################
    def PushRadio(self,):
        self.ClickXpath('//label[@for="saigaiJykyKndCd001"]')
        self.ClickXpath('//label[@for="saigaiJykyKndCd101"]')
        self.ClickXpath('//label[@for="saigaiJykyKndCd201"]')
        self.ClickXpath('//button[@id="btn-exec"]')
        self.ClickXpath('//button[@data-remodal-action="confirm"]')

    ###########################################
    # 機能	：ページのタイトルを表示する
    ###########################################
    def DisplayTitle(self,):
        print(self.driver.title)
        print("========== source ========== ")
        print(self.driver.page_source)

    ###########################################
    # 機能	：URLを取得する（ウィンドウ内のすべてのタブ）
    ###########################################
    def GetUrlsInWndw(self,):
        strUrl_list = list()
        
        #開いているタブのURLを取得
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            strUrl_list.append(self.driver.current_url)
        
        return strUrl_list

    ###########################################
    # 機能	：ハイパーリンクのURLを取得する
    ###########################################
    def GetHref(self,strxpath):
        element = self.driver.find_element_by_xpath(strxpath)
        url = element.get_attribute('href')
        return url

    
    ###########################################
    # 機能	：現在のURLを取得する
    ###########################################
    def GetCurUrl(self,):
        cur_url = self.driver.current_url
        return cur_url
    
    ###########################################
    # 機能	：タイトルを取得する
    ###########################################
    def strGetContent(self,strxpath):
        element = self.driver.find_element_by_xpath(strxpath)
        return element.text

    ###########################################
    # 機能	：クリックする
    ###########################################
    def ClickXpath(self,strxpath):
        element = self.driver.find_element_by_xpath(strxpath)
        element.click()
        time.sleep(1)
        
    ###########################################
    # 機能	：入力する
    ###########################################
    def TypeXpath(self,strxpath,strString):
        element = self.driver.find_element_by_xpath(strxpath)
        element.send_keys(strString)
        time.sleep(1)
        
    ###########################################
    # 機能	：ダウンロードする（完了まで待機）
    # 引用	：引用3
    ###########################################
    def download_file(self, url, file_path):
        from requests import get
        reply = get(url, stream=True,verify=False)
        with open(file_path, 'wb') as file:
            for chunk in reply.iter_content(chunk_size=1024): 
                if chunk:
                    file.write(chunk)

            
    ###########################################
    # 機能	：要素を取得するまで待機する
    ###########################################
    def WaitImplcty(self,iwait):
        self.driver.implicitly_wait(iwait)

###########################################
#引用1
#@mimuro_syunya, "PythonのSeleniumを使って、起動済みのブラウザを操作する。", qiita, https://qiita.com/mimuro_syunya/items/2464cd2404b67ea5da56 (閲覧：2022年01月09日)
#引用2
#Octopus Data Inc., "XPathとは？基本概念や書き方をわかりやすく解説！", octoparse, https://www.octoparse.jp/blog/xpath-introduction/#%EF%BD%82 (閲覧：2022年01月09日)
#引用3
#spatel4140, "Wait for Download to finish in selenium webdriver JAVA", Stack Exchange Inc, https://stackoverflow.com/questions/22714112/wait-for-download-to-finish-in-selenium-webdriver-java (閲覧：2022年01月09日)
###########################################