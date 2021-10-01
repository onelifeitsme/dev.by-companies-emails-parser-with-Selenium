from selenium import webdriver
from time import sleep
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36', 'accept': '*/*', 'x-client-data': 'VGo9iQEIorbJAQjEtskBCKmdygEI9tDKAQiMnssBCKKgywEI3PLLAQjv8ssBCM72ywEIs/jLAQie+csBCPv5ywEIvv8KBU=='}

driver = webdriver.Chrome()

driver.get('https://id.dev.by/@/hello')
sleep(3)
login = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div/form/ul/li[1]/input')
password = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div/form/ul/li[2]/div/input')
login.send_keys('onelifeitsme@gmail.com')
password.send_keys('OneLife30')
driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div/form/button/span').click()

sleep(2)

driver.get('https://companies.dev.by/')

sleep(2)
companies = []
info = []
names = driver.find_elements_by_xpath('//tr/td[1]/a[1]')
for i in names:
    info.append({
        'name': i.text,
        'url': i.get_attribute('href')
    })
info = info[1:]
sleep(3)


def parse():
    count = 0
    for i in range(len(info)):
        driver.get(info[count]['url'])
        sleep(3)
        try:
            email = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#page-branding-container > div > div > div.dev-center.companies > div.colums-table > div.dev-right.col2 > div.widget-block > div.sidebar-for-companies > div.sidebar-views-contacts.h-card.vcard > ul > li:nth-child(1) > span'))).text

            info[i]['email'] = email
            print('есть пробитие')
        except:
            pass
        count +=1
        print('осталось', len(info)-count)




parse()

for i in info:
    print(i)

with open("devby.csv", "w", encoding='UTF-8') as temp:
    polya = ['name', 'url', 'email']
    out = csv.DictWriter(temp, fieldnames=polya)
    out.writeheader()
    for i in info:
        out.writerow(i)


# email = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="page-branding-container"]/div/div/div[1]/div[3]/div[2]/div[1]/div/div[1]/ul/li[1]/span'))).text
# print(email)


