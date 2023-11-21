👋 Hi,

Here i have stored my Selenium projects created with python language. For now i created 2 simple test automation projects😃.

* The first one located in "/selenium_project/selenium_demo/" sings up in demo site ('http://seleniumdemo.com/') for selenium practice and then simply changes billing information for the temporary account. The __init__ method of this test uses random module so everytime test runs a new email and password is being used. The result of the test is verified with assert method which is chcecking if 'Address changed successfully' string is visible after changing billing information.
  
* The second test located in "/selenium_project/selenium_demo_hotels" is also using demo test site for selenium('http://www.kurs-selenium.pl/demo/'). In this scenario, test is inserting filter values(such as city, travellers,date) for searching available hotels. After submiting filters test is gathering all visible results in form of a list and then asserts the price and name of every gathered hotel.
