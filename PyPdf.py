from pyhtml2pdf import converter

class CPdf(object):


    ###########################################
    # 機能	：コンストラクタ
    ###########################################
    def __init__(self, ):
        pass
        
    ############################################
    # 機能 	：WebサイトをPDF保存する
    # 引数 	：strhtml     印刷したいWebページのURL
    #      	：strfileName 保存するPDF名
    ############################################
    def SaveHtmlAsPdf(self, strhtml, strfileName):
        converter.convert(strhtml, strfileName)
        return

###########################################
#引用1
#Kumara Fernando, "Simple python wrapper to convert HTML to PDF with headless Chrome via selenium.", pypi.org, https://pypi.org/project/pyhtml2pdf/ (閲覧：2023年02月18日)
###########################################
