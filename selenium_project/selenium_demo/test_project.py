import pytest
from selenium_project.selenium_demo.Test_methods import test_change_billing
from selenium_project.selenium_demo.conftest import Test_Base
@pytest.mark.usefixtures('test_setup')
class Test_projekt(Test_Base):
   def test_continue(self,test_setup):
       Billing=test_change_billing(self.driver)
       Billing.sing_up()
       Billing.changing_billing()
