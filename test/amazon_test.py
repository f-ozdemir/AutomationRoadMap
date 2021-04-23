import unittest

from selenium import webdriver

from base.base_page import BaseClass
from pages.login_page import LoginPage
from pages.main_page import AMAZON
from pages.product_page import ProductPage
from pages.search_page import SearchPage


class Amazon(unittest.TestCase):
    """
    Test case is:
    1.  http://www.amazon.com sitesine gidecek ve anasayfanın açıldığını assertion ile onaylayacak,
    2. Login ekranını açıp, bir kullanıcı ile login olunacak ( daha önce siteye üyeliği varsa o olabilir )
    3. Ekranin ustundeki Search alanına 'samsung' yazıp ara butonuna tıklanacak,
    4. Gelen sayfada samsung icin sonuc bulunduğunu onaylayacak,
    5. Arama sonuçlarından 2. sayfaya tıklayacak ve açılan sayfada 2. sayfanin şu an gösterimde oldugunu onaylayacak,
    6. Üstten 3. urunun içindeki 'Add to List' butonuna tıklayacak,
    7. Ekranin en üstündeki 'List' linkine tiklayacak içerisinden Wish listi seçecek,
    8. Acilan sayfada bir onceki sayfada izlemeye alinmis urunun bulundugunu onaylayacak,
    9. Favorilere alinan bu urunun yanindaki 'Delete' butonuna basarak, favorilerimden cikaracak,
    10. Sayfada bu urunun artik favorilere alinmadigini onaylayacak.

    """

    def setUp(self):
        """Selenium initializing requirements are met in here."""

        self.driver = webdriver.Chrome("C:/Users/fadime.ozdemir/Documents/chromedriver_win32/chromedriver.exe")
        self.driver.maximize_window()
        self.methods = BaseClass(self.driver)
        self.main = AMAZON(self.driver, self.methods)
        self.login = LoginPage(self.driver, self.methods)
        self.search = SearchPage(self.driver, self.methods)
        self.product = ProductPage(self.driver, self.methods)

    def test_amazon(self):
        self.main.navigate_to_home_page()
        self.login.navigate_to_login_page()
        self.login.login_info_filling()
        self.login.login()
        self.search.enterSearchText()
        self.search.clickSearch()
        self.search.clickSecondPage()
        self.search.productClick()
        self.product.addToList()
        self.product.viewList()
        self.product.deleteItem()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
