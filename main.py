from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

sonuc_dict = dict()

driver = webdriver.Safari()
driver.set_window_size(1920,1080)
driver.get('https://www.google.com')

# siteleri çek
with open('sites.txt', mode='r', encoding='utf-8', errors="ignore") as sites:
    for url in sites:
        url = url.strip()
        with open('keywords.txt', mode='r', encoding='utf-8', errors="ignore") as keywords:  # keywords dosyasını her url için tekrar açıyoruz
            for kw in keywords:
                # Google'da arama kutusunu bul - Arama kutusu
                search_box = driver.find_element(By.NAME, 'q')
                search_box.clear()

                # arama kutusuna query at
                search_box.send_keys(f'intitle:"{kw.strip()}" site:{url}')  # kw'nin sonundaki boşlukları da kaldırdık.
                search_box.submit()
                time.sleep(5)

                results = driver.find_element(By.XPATH, '//div[@id="result-stats"]').text.rstrip(' sonuç bulundu')
                results = results.lstrip('Yaklaşık ')
                results = int(results)
                sonuc_dict[(url, kw.strip())] = results  # kw'nin sonundaki boşlukları kaldırdık.

driver.close()
print(sonuc_dict)
