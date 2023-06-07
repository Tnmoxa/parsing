# from selenium.webdriver.common.by import By
# import undetected_chromedriver as uc
# import pandas as pd
# import time
#
# dates = []
# total_area = []
# addresses = []
# main_prices = []
# sq_prices = []
# descriptions = []
#
# start_time = time.time()
# driver = uc.Chrome()
# i = 200
# links1 = ['link1', 'link2']
# print(len(links1))
# for link in links1:
#     try:
#         driver.get(link)
#
#         dates.append(driver.find_element(By.CLASS_NAME,
#                                          "a10a3f92e9--color_gray40_100--ppbi0.a10a3f92e9--lineHeight_5u--cJ35s"
#                                          ".a10a3f92e9--fontWeight_normal--P9Ylg.a10a3f92e9--fontSize_14px--TCfeJ"
#                                          ".a10a3f92e9--display_block--pDAEx.a10a3f92e9--text--g9xAG.a10a3f92e9"
#                                          "--text_letterSpacing__0--mdnqq").text)
#
#         data1 = driver.find_elements(By.XPATH, ".//div[@data-name='ObjectFactoidsItem']")
#
#         total_area.append(data1[0].text.split('\n')[1])
#
#         addresses.append(driver.find_element(By.CLASS_NAME, "a10a3f92e9--address-line--GRDTb").text[:-8])
#         main_prices.append(driver.find_element(By.XPATH, ".//div[@data-name='PriceInfo']").text)
#         data2 = driver.find_elements(By.CLASS_NAME,
#                                      "a10a3f92e9--color_black_100--kPHhJ.a10a3f92e9--lineHeight_20px--tUURJ"
#                                      ".a10a3f92e9--fontWeight_normal--P9Ylg.a10a3f92e9--fontSize_14px--TCfeJ"
#                                      ".a10a3f92e9--display_block--pDAEx.a10a3f92e9--text--g9xAG.a10a3f92e9"
#                                      "--text_letterSpacing__normal--xbqP6")
#         sq_prices.append(data2[1].text)
#         descriptions.append(driver.find_element(By.CLASS_NAME,
#                                                 "a10a3f92e9--color_black_100--kPHhJ.a10a3f92e9--lineHeight_6u--A1GMI"
#                                                 ".a10a3f92e9--fontWeight_normal--P9Ylg.a10a3f92e9--fontSize_16px"
#                                                 "--RB9YW.a10a3f92e9--display_block--pDAEx.a10a3f92e9--text--g9xAG"
#                                                 ".a10a3f92e9--text_letterSpacing__0--mdnqq.a10a3f92e9"
#                                                 "--text_whiteSpace__pre-wrap--scZwb").text)
#     except Exception as e:
#         print()
#         print(e)
#         print(link)
#     i -= 1
#     if i == 0:
#         break
#     if i % 10 == 0:
#         print(i)
# driver.quit()
#
# print(len(dates))
# data = {
#     # 'latitude': latitude,
#     # 'longitude': longitude,
#     'dates': dates,
#     'total_area': total_area,
#     'addresses': addresses,
#     'main_prices': main_prices,
#     'sq_prices': sq_prices,
#     'descriptions': descriptions,
# }
# driver.quit()
# end_time = time.time()
# execution_time = end_time - start_time
# print(f"{len(dates)} объявлений обработаны за {execution_time} секунд.")
# df = pd.DataFrame(data)
# df

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

dates = []
total_area = []
addresses = []
main_prices = []
sq_prices = []
descriptions = []

start_time = time.time()

links = ['link1', 'link2']  # Replace with your list of links

for link in links:
    try:
        response = requests.get(link)
        soup = BeautifulSoup(response.content, 'html.parser')

        dates.append(soup.find('div', class_='a10a3f92e9--color_gray40_100--ppbi0.a10a3f92e9--lineHeight_5u--cJ35s'
                                             '.a10a3f92e9--fontWeight_normal--P9Ylg.a10a3f92e9--fontSize_14px--TCfeJ'
                                             '.a10a3f92e9--display_block--pDAEx.a10a3f92e9--text--g9xAG.a10a3f92e9'
                                             '--text_letterSpacing__0--mdnqq').text)

        data1 = soup.find_all('div', {'data-name': 'ObjectFactoidsItem'})
        total_area.append(data1[0].find_all('span')[1].text)

        addresses.append(soup.find('div', class_='a10a3f92e9--address-line--GRDTb').text[:-8])
        main_prices.append(soup.find('div', {'data-name': 'PriceInfo'}).text)

        data2 = soup.find_all('span', class_='a10a3f92e9--color_black_100--kPHhJ a10a3f92e9--lineHeight_20px--tUURJ '
                                             'a10a3f92e9--fontWeight_normal--P9Ylg a10a3f92e9--fontSize_14px--TCfeJ '
                                             'a10a3f92e9--display_block--pDAEx a10a3f92e9--text--g9xAG '
                                             'a10a3f92e9--text_letterSpacing__normal--xbqP6')
        sq_prices.append(data2[1].text)

        descriptions.append(soup.find('span', class_='a10a3f92e9--color_black_100--kPHhJ '
                                                     'a10a3f92e9--lineHeight_6u--A1GMI '
                                                     'a10a3f92e9--fontWeight_normal--P9Ylg '
                                                     'a10a3f92e9--fontSize_16px--RB9YW '
                                                     'a10a3f92e9--display_block--pDAEx a10a3f92e9--text--g9xAG '
                                                     'a10a3f92e9--text_letterSpacing__0--mdnqq '
                                                     'a10a3f92e9--text_whiteSpace__pre-wrap--scZwb').text)
    except Exception as e:
        print()
        print(e)
        print(link)

data = {
    'dates': dates,
    'total_area': total_area,
    'addresses': addresses,
    'main_prices': main_prices,
    'sq_prices': sq_prices,
    'descriptions': descriptions,
}

end_time = time.time()
execution_time = end_time - start_time
print(f"{len(dates)} объявлений обработаны за {execution_time} секунд.")

df = pd.DataFrame(data)
print(df)
