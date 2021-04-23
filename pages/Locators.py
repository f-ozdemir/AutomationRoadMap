from selenium.webdriver.common.by import By


class Site_Locators:
    # --- Home Page Locators ---
    website = "https://www.amazon.com"
    MAIN_PAGE = (By.CSS_SELECTOR, ".nav-logo-sprites")
    IS_ON_MAIN_PAGE = (By.CSS_SELECTOR, ".nav-logo-sprites")

    # --- Signing Page Locators ---
    SIGN_IN = (By.CSS_SELECTOR, ".nav-action-inner")
    # SIGN_IN = (By.XPATH, "//a[@class,'nav-action-inner']//a[text() = 'Sign in']")
    USER_EMAIL_OR_MOBIL_NO_TEXTBOX = (By.CSS_SELECTOR, ".ap_email")
    EMAIL_CONTINUE = (By.CSS_SELECTOR, '.a-button-input')
    PASSWORD_TEXTBOX = (By.CSS_SELECTOR, ".ap_password")
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, ".#signInSubmit")

    # --- Search Results Page Locators ---
    SEARCH_TEXTBOX = (By.CSS_SELECTOR, "#twotabsearchtextbox")
    SEARCH_SUBMIT_BUTTON = (By.XPATH, "//div[contains(@class,'nav-search-submit')]/input")
    SEARCH_TEXT = "Samsung"

    # --- Search Results Page Locators ---
    SEARCH_RESULT_LINK = (By.CSS_SELECTOR, "#search")
    SECOND_PAGE_BUTTON = (By.XPATH, "//li[@class = 'a-normal']//a[text() = '2']")
    PRODUCT_PAGE = (By.CSS_SELECTOR, ".a-size-medium.a-text-normal")[2]

    # --- Product Details Page Locators ---
    ADD_TO_LIST_BUTTON = (By.CSS_SELECTOR, "#add-to-wishlist-button-submit")
    VIEW_LIST = (By.XPATH, "//a[contains(text() ,'Wish List')]")
    DELETE_BUTTON = (By.CSS_SELECTOR, '#delete-button-I3977YOBYJCJO5')
