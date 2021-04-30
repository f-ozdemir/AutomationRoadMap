from selenium.webdriver.common.by import By


class LoginPage:
    """Website login page to user logged in"""

    SIGN_IN = (By.ID, "nav-link-accountList")
    USER_EMAIL_OR_MOBIL_NO_TEXTBOX = (By.ID, "ap_email")
    EMAIL_SUBMIT = (By.ID, 'continue')
    PASSWORD_TEXTBOX = (By.ID, "ap_password")
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, "#signInSubmit")
    email = 'fadimetesting@gmail.com'
    password = '%?>^2:wJERH.GDyk'

    def __init__(self, driver, methods):
        self.driver = driver
        self.methods = methods

    def navigate_to_login_page(self):
        """
        Navigates to the login page

        """
        self.methods.wait_for_element(self.SIGN_IN).click()

    def login_info_filling(self):
        """
        Fills login information

        """
        self.methods.wait_for_element(self.USER_EMAIL_OR_MOBIL_NO_TEXTBOX).send_keys(self.email)
        self.methods.wait_for_element(self.EMAIL_SUBMIT).click()
        self.methods.wait_for_element(self.PASSWORD_TEXTBOX).send_keys(self.password)

    def login(self):
        """
        Completed login information

        """
        self.methods.wait_for_element(self.SIGN_IN_BUTTON).click()
