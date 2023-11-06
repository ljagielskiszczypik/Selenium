import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriver
import test_hotel_search
import test_hotel_results
from selenium.webdriver.chrome.service import Service
service = Service()
options = webdriver.ChromeOptions()


class Test_hotele:
   @pytest.fixture()
   def test_Setup(self):
       self.driver = webdriver.Chrome(service=service,options=options)
       self.driver.implicitly_wait(10)
       self.driver.get('http://www.kurs-selenium.pl/demo/')
       self.driver.maximize_window()
       yield
       self.driver.quit()

   def test_continue(self, test_Setup):
       test = test_hotel_search.test_search_hotel(self.driver)
       test.search_hotel_city()
       test.search_hotel_date('11/09/2023', '30/09/2023')
       test.search_hotel_travellers('4')
       test.search_hotel_submit()
       results_hotel = test_hotel_results.Test_results(self.driver)
       hotele_nazwy = results_hotel.search_results_hotel_names()
       cena_hotel = results_hotel.search_results_hotel_prices()

       assert hotele_nazwy[0] == 'Jumeirah Beach Hotel'
       assert hotele_nazwy[1] == 'Oasis Beach Tower'
       assert hotele_nazwy[2] == 'Rose Rayhaan Rotana'
       assert hotele_nazwy[3] == 'Hyatt Regency Perth'

       assert cena_hotel[0] == '$22'
       assert cena_hotel[1] == '$50'
       assert cena_hotel[2] == '$80'
       assert cena_hotel[3] == '$150'