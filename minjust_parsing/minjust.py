import json
from selenium import webdriver
from selenium.webdriver.chrome import options
from fake_useragent import UserAgent

useragent = UserAgent()
EXE_PATH = r"C:\Users\Despair\Desktop\chromedriver_win32\chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={useragent.data_randomize}")
#options.add_argument("--proxy-server=suka")

browser = webdriver.Chrome(executable_path=EXE_PATH, options = options)

url = "http://unro.minjust.ru/NKOReports.aspx?request_type=nko"


try:
    browser.get(url=url)
    button = browser.find_element('id','b_refresh')
    button.click()
    table = browser.find_element('id','pdg')
    trs = table.find_elements('tag name','tr')
    for i in range(0,3):
        trs.pop(0)
    for i in range(0,6):
            trs.pop(1)
    del trs[-3:]

    data = {}
    counterTrs = 0
    for tr in trs:
        if tr:          
            tds = tr.find_elements('tag name','td')
            tdsList = []
            for td in tds:
                tdsList.append(td.text)
            tdsList = list(filter(None, tdsList))
            if tdsList:
                data[counterTrs]={
                    "Наименование НКО": tdsList[0],
                    "Учетный номер": tdsList[1],
                    "ОГРН": tdsList[2],
                    "Форма": tdsList[3],
                    "Вид отчета": tdsList[4],
                    "Период": tdsList[5]
                }
                counterTrs +=1

    with open("data.json", "w", encoding = 'utf-8') as file:
        json.dump(data, file,indent=4, ensure_ascii=False, sort_keys=False)

except Exception as ex:
    print(ex)
finally:
    browser.close()
    browser.quit()

