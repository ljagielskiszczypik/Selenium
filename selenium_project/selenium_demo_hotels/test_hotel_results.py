from selenium import webdriver
from selenium.webdriver.common.by import By
from Hotel_locators import Search_hotel_results_locators
class Test_results:
   def __init__(self,driver):
       self.driver=driver
   def search_results_hotel_names(self):
       hotele = self.driver.find_elements(By.XPATH,Search_hotel_results_locators.find_elements_by_xpath_hotel_names)
       return [hotel.get_attribute('textContent') for hotel in hotele]
   def search_results_hotel_prices(self):
       cennik = self.driver.find_elements(By.XPATH,Search_hotel_results_locators.find_elements_by_xpath_hotel_prices)
       return [cena.get_attribute('textContent') for cena in cennik]
