import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class DEFACTO(unittest.TestCase):
    """ Test Case is:
    https://www.defacto.com.tr/ adresine gidin.
    Herhangi bir kategori sayfasına gidin.
    Herhangi bir ürün sayfasına gidin.
    Ürünü sepete ekleyin.
    Sepet sayfasına gidin.
    Anasayfaya geri dönün.

    Chrome driver kullanılacak.
    Python ile yazılacak.
    POM kullanılmadan tek python dosyası içerisinde yazılacak.
    Locator’lar sayfanın üst bölümünde tanımlanacak.
    Test bittikten sonra driver kapatılacak.
    Sayfaların doğruluğunun kontrolü için her adımda assertion kullanılacak.
    """

    CATEGORY_PAGE = (By.CSS_SELECTOR, ".mainmenu-item")  # 1
    PRODUCT_PAGE = (By.CSS_SELECTOR, ".product-items")  # 0
    CHOOSE_SIZE = (By.CSS_SELECTOR, "div[id='productDetailSizeButtons'] > button")  # 0
    ADD_TO_CART = (By.CSS_SELECTOR, ".product-info-action-add-to-cart")
    CART_PAGE = (By.XPATH, "//a[contains(text(),'SEPETE GİT')]")
    MAIN_PAGE = (By.CSS_SELECTOR, ".header-logo")
    website = "https://www.defacto.com.tr/"

    IS_ON_CATEGORY_PAGE = (By.CSS_SELECTOR, ".mainmenu-item")
    IS_ON_PRODUCT_PAGE = (By.CSS_SELECTOR, ".product-details")
    SIZE = (By.ID, "productDetailSizeButtons")
    IS_ON_CART_PAGE = (By.CSS_SELECTOR, ".shopping-order-summary-complete-address")
    IS_ON_MAIN_PAGE = (By.CSS_SELECTOR, ".header-logo")

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.driver = webdriver.Chrome("C:/Users/fadime.ozdemir/Desktop/chromedriver_win32 (1)/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get(self.website)
        self.wait = WebDriverWait(self.driver, 15)

    def test_navigate(self):
        assert "DeFacto ile Kadın ve Erkek Giyimde Akdeniz Modası" in self.driver.title

        self.wait.until(ec.presence_of_all_elements_located(self.CATEGORY_PAGE))[1].click()
        is_on_category = self.wait.until(ec.presence_of_all_elements_located(self.IS_ON_CATEGORY_PAGE))[1].text
        assert is_on_category == "KADIN"

        self.wait.until(ec.presence_of_all_elements_located(self.PRODUCT_PAGE))[0].click()
        assert self.wait.until(
            ec.presence_of_element_located(self.IS_ON_PRODUCT_PAGE)).is_displayed(), 'It is not loaded size'

        assert self.wait.until(ec.presence_of_element_located(self.SIZE)).is_displayed(), 'It is not loaded size'
        self.wait.until(ec.presence_of_all_elements_located(self.CHOOSE_SIZE))[0].click()

        self.wait.until(ec.element_to_be_clickable(self.ADD_TO_CART)).click()

        self.wait.until(ec.element_to_be_clickable(self.CART_PAGE)).click()
        assert self.wait.until(ec.presence_of_element_located(self.IS_ON_CART_PAGE)).is_displayed(), 'It not cart page'

        self.wait.until(ec.element_to_be_clickable(self.MAIN_PAGE)).click()
        assert self.wait.until(ec.presence_of_element_located(self.IS_ON_MAIN_PAGE)).is_displayed(), 'It not main page'

        def tearDown(self):
            self.driver.quit()

    if __name__ == '__main__':
        unittest.main()
