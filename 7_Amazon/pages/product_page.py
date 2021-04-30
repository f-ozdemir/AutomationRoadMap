import time

from selenium.webdriver.common.by import By


class ProductPage:
    """Product page go to 2.second page's which is third one product and add to wishlist"""

    ADD_TO_LIST_BUTTON = (By.ID, "add-to-wishlist-button-submit")
    VIEW_LIST = (By.CLASS_NAME, "w-button-text")
    DELETE_BUTTON = (By.XPATH, "(//input[@name= 'submit.deleteItem'])[1]")

    def __init__(self, driver, methods):
        self.driver = driver
        self.methods = methods

    def addToList(self):
        """
        Add product to Wish list

        """
        time.sleep(1)
        self.methods.wait_for_element(self.ADD_TO_LIST_BUTTON).click()

    def viewList(self):
        """
        View the Wish list

        """
        self.methods.wait_for_element(self.VIEW_LIST).click()

    def deleteItem(self):
        """
        Deleted product from the Wish list

        """
        self.methods.wait_for_element(self.DELETE_BUTTON).click()
        successfully_deleted = self.methods.element_exists(self.DELETE_BUTTON)
        assert successfully_deleted, True
