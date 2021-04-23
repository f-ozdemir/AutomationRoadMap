from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BaseClass(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, selector):
        """
        Wait for element to present
        :param selector: locator of the element to find

        """
        return WebDriverWait(self.driver, 25).until(ec.element_to_be_clickable(selector))

    def wait_till_element_disappears(self, selector):
        """
        Wait for element to disappears
        :param selector: locator of the element to find

        """
        return WebDriverWait(self.driver, 25).until(ec.invisibility_of_element_located(selector))

    def hover(self, selector):
        """
        Hover over the selected element
        :param selector: locator of the element to find

        """
        hover_element = self.wait_for_element(selector)
        hover = ActionChains(self.driver).move_to_element(hover_element)
        hover.perform()

    def element_exists(self, selector):
        """
        Return true if element present and false if element absent
        :param selector: locator of the element to find

        """
        try:
            return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(selector))
        except TimeoutException:
            return False
