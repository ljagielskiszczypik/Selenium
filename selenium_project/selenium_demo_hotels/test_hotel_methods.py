from selenium.webdriver.common.by import By
from Hotel_locators import Search_hotel_locators
class test_search_hotel:
   def __init__(self,driver):
       self.driver = driver
   def search_hotel_city(self):
       self.driver.find_element(By.CLASS_NAME, Search_hotel_locators.find_element_classname_hotel).click()
       self.driver.find_element(By.XPATH, Search_hotel_locators.find_element_xpath_hotel_send_key).send_keys('Dubai')
       self.driver.find_element(By.XPATH, Search_hotel_locators.find_element_by_xpath_span).click()
   def search_hotel_date(self, start, end):
       self.driver.find_element(By.CLASS_NAME, Search_hotel_locators.find_element_by_class_name_start).send_keys(start)
       self.driver.find_element(By.CLASS_NAME, Search_hotel_locators.find_element_by_class_name_end).send_keys(end)
   def search_hotel_travellers(self, howmany: str):
       self.driver.find_element(By.ID, Search_hotel_locators.find_element_id_travellers_input).click()
       self.driver.find_element(By.ID, Search_hotel_locators.find_element_id_adultInput_input).clear()
       self.driver.find_element(By.ID, Search_hotel_locators.find_element_id_adultInput_input).send_keys(howmany)
   def search_hotel_submit(self):
       self.driver.find_element(By.XPATH, Search_hotel_locators.find_element_xpath_submit).click()