import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriver
#import test_search_hotel1
#import test_search_results1
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