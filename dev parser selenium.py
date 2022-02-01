from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import csv


HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
            'accept': '*/*', 'x-client-data':
            'VGo9iQEIorbJAQjEtskBCKmdygEI9tDKAQiMnssBCKKgywEI3PLLAQjv8ssBCM72ywEIs/jLAQie+csBCPv5ywEIvv8KBU=='}

driver = webdriver.Chrome()

driver.get('https://id.dev.by/@/hello')
sleep(3)
login = driver.find_element(By.XPATH, '//input[@name="email"]')
password = driver.find_element(By.XPATH, '//input[@name="password"]')
login.send_keys('onelifeitsme@gmail.com')
password.send_keys('OneLife30')
driver.find_element(By.XPATH, '//span[@class="button__content"]').click()

sleep(2)

driver.get('https://companies.dev.by/')

sleep(2)
companies = []
info = []
names = driver.find_elements(By.XPATH, '//tr[@class="odd" or @class="even"]/td[1]/a[1]')

companies = [{'name': n.text, 'url': n.get_attribute('href')} for n in names]
sleep(3)


print(f'Получено {len(companies)} компаний')
for i in info:
    print(i)


def parse():
    count = 0
    for i in range(len(companies)):
        driver.get(companies[count]['url'])
        sleep(3)
        try:
            email = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//li[contains(text(),"почта")]/child::span'))).text

            companies[i]['email'] = email
            print('email получен')
            print(email)
        except NoSuchElementException:
            print('email не получен')
        count += 1
        print('осталось', len(companies)-count)


parse()


with open("devby.csv", "w", encoding='UTF-8') as temp:
    polya = ['name', 'url', 'email']
    out = csv.DictWriter(temp, fieldnames=polya)
    out.writeheader()
    for i in companies:
        out.writerow(i)
