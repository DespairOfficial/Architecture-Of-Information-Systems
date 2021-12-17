import json
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome import options
from fake_useragent import UserAgent
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

useragent = UserAgent()
EXE_PATH = r"C:\Users\Despair\Desktop\chromedriver_win32\chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36")
# options.add_argument(f"user-agent={useragent.data_randomize}")
#options.add_argument("--proxy-server=")

browser = webdriver.Chrome(executable_path=EXE_PATH, options = options)

url = "http://unro.minjust.ru/NKOReports.aspx?request_type=nko"


# def append_to_json(_dict,path):
#     with open(path, 'ab+') as f:
#         f.seek(0,2)
#         if(f.tell()==0):
#             f.write(json.dumps([_dict]).encode())
#         else:
#             f.seek(-1,2)
#             f.truncate()
#             f.write(' , '.encode(encoding='utf-8'))
#             f.write(json.dumps(_dict).encode(encoding='utf-8'))
#             f.write(']'.encode(encoding='utf-8'))


counterTrs = 0
try:
    browser.get(url=url)
    browser.find_element('id','b_refresh').click()
    btn_pdg_count = browser.find_elements('class name','pdg_count')
    for i in btn_pdg_count:
        if(i.text=='500'):
            i.click()

    SOFUCKINGBIGARRAY = []       
    for j in range(0,2):
        
        print(f'Parsing page {j}')
        table = browser.find_element('id','pdg')
        trs = table.find_elements('tag name','tr')
        for i in range(0,10):
            trs.pop(0)
        del trs[-3:]

        
        for tr in trs:
            if tr:          
                tds = tr.find_elements('tag name','td')
                tdsList = []
                for td in tds:
                    tdsList.append(td.text)
                tdsList = list(filter(None, tdsList))
                if tdsList:
                    newData = {
                        "Наименование НКО": tdsList[0],
                        "Учетный номер": tdsList[1],
                        "ОГРН": tdsList[2],
                        "Форма": tdsList[3],
                        "Вид отчета": tdsList[4],
                        "Период": tdsList[5]
                    }
                    SOFUCKINGBIGARRAY.append(newData)

    with open("data.json", "w", encoding = 'utf-8') as file:
        json.dump(SOFUCKINGBIGARRAY, file,indent=4, ensure_ascii=False, sort_keys=False)

        


        nextPageButton = WebDriverWait(browser,30).until(lambda b: b.find_element('id','pdg_next'))
        action = ActionChains(browser)
        action.move_to_element(nextPageButton).click().perform()
except Exception as ex:
    print(ex)
finally:
    browser.close()
    browser.quit()

