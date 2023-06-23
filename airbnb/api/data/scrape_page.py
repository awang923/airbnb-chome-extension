from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import time
import pandas as pd

chrome_options = Options()
chrome_options.headless = True
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.airbnb.com/rooms/685214106425613938?adults=4&check_in=2023-07-17&check_out=2023-07-19&source_impression_id=p3_1686857170_HrAks4Fs1%2Fadmm%2FY&previous_page_section_name=1000&federated_search_id=b917768d-845b-4946-b374-f86f17de8d02')
# print(driver.title)
time.sleep(3)
src = driver.page_source

# url = 'https://www.airbnb.com/rooms/685214106425613938?adults=4&check_in=2023-07-17&check_out=2023-07-19&source_impression_id=p3_1686857170_HrAks4Fs1%2Fadmm%2FY&previous_page_section_name=1000&federated_search_id=b917768d-845b-4946-b374-f86f17de8d02'
# r = driver.get(url)
# print(r)

soup = BeautifulSoup(src, 'html.parser')

name = soup.find('h1', class_ = 'hpipapi i1pmzyw7 dir dir-ltr')


price = soup.find('span', class_ = '_1qs94rc')
    
dates = soup.find_all('div', class_ = '_1e8a8lh')
checkIn = dates[0].text
checkOut = dates[1].text

# checkouts = soup.find_all('div', class_ = '_1e8a8lh')
# for i in checkouts:
#     item = i.text
#     CheckOuts.append(item)

# print(len(Names), len(Prices), len(CheckIns), len(CheckOuts))
# print(Prices)
# print(CheckIns)

df = pd.DataFrame({"Name": name.text, "Price": price.text, "Check In": checkIn, "Check Out": checkOut})
print(df)
driver.close()