from bs4 import BeautifulSoup
from ..models import Listing
import requests
import pandas as pd

Names =[]
Prices = []
Reviews = []
Listing = []

# url = 'https://www.airbnb.com/s/Honolulu--Oahu--Hawaii--United-States/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2023-07-01&monthly_length=3&price_filter_input_type=0&price_filter_num_nights=5&channel=EXPLORE&query=Honolulu%2C%20Oahu%2C%20Hawaii&place_id=ChIJTUbDjDsYAHwRbJen81_1KEs&date_picker_type=calendar&checkin=2023-07-17&checkout=2023-07-19&adults=4&source=structured_search_input_header&search_type=autocomplete_click'
r = requests.get('https://www.airbnb.com/')
url = r.url

soup = BeautifulSoup(url.content, 'html.parser')

names = soup.find_all('div', class_ = 't1jojoys dir dir-ltr')
for i in names:
    item = i.text
    Names.append(item)

prices = soup.find_all('div', class_ = '_tt122m')
for i in prices:
    item = i.text
    Prices.append(item)
    
reviews = soup.find_all('span', class_ = 'r1dxllyb dir dir-ltr')
for i in reviews:
    item = i.text
    Reviews.append(item)

# listings = soup.find_all('div', class_='c1l1h97y dir dir-ltr')
# for i in listings:
#     Listing.append(i)
# print(Listing[0])
# print(len(Names), len(Prices), len(Reviews))
# print(type(Prices[0]))

for name, price, review in zip(Names, Prices, Reviews):
    listing = Listing(name = name, price = price, reviews = review)
    listing.save()

df = pd.DataFrame({"Name": Names, "Price": Prices, "Review": Reviews})
print(df)

