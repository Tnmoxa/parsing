import csv

from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


# Функция для парсинга объявлений на Авито с использованием Selenium
def parse_avito():
    url = "https://m.avito.ru/moskva/kvartiry/prodam-ASgBAgICAUSSA8YQ?context=H4sIAAAAAAAA_0q0MrSqLraysFJKK8rPDUhMT1WyLrYyNLNSKk5NLErOcMsvyg3PTElPLVGyrgUEAAD__xf8iH4tAAAA"  # Замените "your_region" на ваш регион или город
    webdriver_path = './chromedriver'

    # Создаем экземпляр сервиса ChromeDriver
    service = Service(webdriver_path)

    # Настройки ChromeDriver
    options = Options()
    options.headless = True  # Запуск в безголовом режиме (без открытия окна браузера)

    # Запускаем браузер
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(url)
    time.sleep(2)  # Добавьте паузу для загрузки страницы

    # Имитация прокрутки страницы для динамической загрузки данных
    body = driver.find_element(By.TAG_NAME, "body")
    print(body)
    num_scrolls = 1  # Установите желаемое количество прокруток страницы
    while num_scrolls > 0:
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)  # Пауза между прокрутками
        num_scrolls -= 1

    # Извлечение данных объявлений
    ads = driver.find_elements(By.CLASS_NAME, "items-items-kAJAg")
    print(ads)


    for ad in ads:
        title = ad.find_elements(By.CLASS_NAME, "iva-item-title-py3i_")
        for titl in title:
            taga = titl.find_elements(By.TAG_NAME, "a")
            print(taga)
            link = taga[0].get_attribute('href')
        # title = ad.find_element_by_tag_name("h3").text.strip()
        # price = ad.find_element_by_class_name("price").text.strip()
        # area = ad.find_element_by_class_name("param.area").text.strip()
        # price_per_sqm = ad.find_element_by_class_name("about").text.strip()
        # location = ad.find_element_by_class_name("data").text.strip()
        # address = ad.find_element_by_class_name("address").text.strip()
        # date = ad.find_element_by_class_name("date").text.strip()

        # Сохраняем данные в CSV-файл
        with open("авито_недвижимость.csv", "a", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([title])
            # writer.writerow([title, price, area, price_per_sqm, location, address, date])

    # Закрываем браузер
    driver.quit()


# Вызываем функцию для парсинга объявлений на Авито
parse_avito()

# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
#
# def parse_avito():
#     url = "https://m.avito.ru/moskva/kvartiry/prodam-ASgBAgICAUSSA8YQ?context=H4sIAAAAAAAA_0q0MrSqLraysFJKK8rPDUhMT1WyLrYyNLNSKk5NLErOcMsvyg3PTElPLVGyrgUEAAD__xf8iH4tAAAA"
#     webdriver_path = './chromedriver'
#
#     # Создаем экземпляр сервиса ChromeDriver
#     service = Service(webdriver_path)
#
#     # Настройки ChromeDriver
#     options = Options()
#     options.headless = True
#
#     # Запускаем браузер
#     driver = webdriver.Chrome(service=service, options=options)
#
#     driver.get(url)
#     time.sleep(2)
#
#     # Имитация прокрутки страницы для динамической загрузки данных
#     body = driver.find_element(By.TAG_NAME, "body")
#     num_scrolls = 5
#
#     while num_scrolls > 0:
#         body.send_keys(Keys.PAGE_DOWN)
#         time.sleep(1)
#         num_scrolls -= 1
#
#     # Извлечение данных объявлений
#     ads = driver.find_elements(By.CLASS_NAME, "iva-item-content-m2FiN")
#
#     for ad in ads[:20]:
#         title = ad.find_element(By.CLASS_NAME, "iva-item-titleStep-_CxvN").text
#         price = ad.find_element(By.CLASS_NAME, "iva-item-priceStep-_0Rze").text
#         print('Title:', title)
#         print('Price:', price)
#         print('---')
#
#     driver.quit()
#
# parse_avito()