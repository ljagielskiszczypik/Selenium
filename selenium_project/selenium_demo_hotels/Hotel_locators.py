class Search_hotel_locators:
   find_element_classname_hotel = 'select2-chosen'
   find_element_xpath_hotel_send_key = '//*[@id="select2-drop"]/div/input'
   find_element_by_xpath_span = '//span[text()="Dubai"]'
   find_element_by_class_name_start = 'dpd1'
   find_element_by_class_name_end = 'dpd2'
   find_element_id_travellers_input = 'travellersInput'
   find_element_id_adultInput_input = 'adultInput'
   find_element_xpath_submit = '//button[@type="submit"]'


class Search_hotel_results_locators:
   find_elements_by_xpath_hotel_names = '//h4[contains(@class,"list_title")]//b'
   find_elements_by_xpath_hotel_prices = '//div[contains(@class,"fs26")]//b'