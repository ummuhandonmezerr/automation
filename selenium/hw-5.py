from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class LCW:
    CATEGORY_PAGE = (By.CSS_SELECTOR, ".sf-with-ul.outlet")  # [0]
    PRODUCT_PAGE = (By.CSS_SELECTOR, ".product-card")  # [0]
    CHOOSE_SIZE = (By.XPATH, "//a[contains(text(),'S')]")  # [107]
    ADD_TO_CART = (By.CSS_SELECTOR, ".col-xl-12")  # [0]
    CART_PAGE = (By.CSS_SELECTOR, ".header-cart")  # [0]
    MAIN_PAGE = (By.CSS_SELECTOR, ".img-logo")  # [0]
    website = "https://www.lcwaikiki.com/tr-TR/TR"
    driver = "C:/Users/ummuhan.donmezer/Downloads/chromedriver_win32/chromedriver.exe"
    cart_button = (By.CSS_SELECTOR, ".row") # [21]
    category_button= (By.CSS_SELECTOR, ".dropdown-button") #[0]
    main_page= (By.CSS_SELECTOR, ".fast-delivery") #[0]


    def __init__(self):

        self.driver = webdriver.Chrome(self.driver)
        self.driver.maximize_window()
        self.driver.get(self.website)
        self.wait = WebDriverWait(self.driver, 15)

    def test_navigate(self):

        self.wait.until(ec.presence_of_all_elements_located(self.CATEGORY_PAGE))[0].click()
        assert self.wait.until(ec.presence_of_all_elements_located(self.category_button))[0].is_displayed(), "You are not on the category page"
        self.wait.until(ec.presence_of_all_elements_located(self.PRODUCT_PAGE))[0].click()
        assert self.wait.until(ec.element_to_be_clickable(self.ADD_TO_CART)).is_displayed(), "You are not on the product page"
        self.wait.until(ec.presence_of_all_elements_located(self.CHOOSE_SIZE))[107].click()
        self.wait.until(ec.presence_of_all_elements_located(self.ADD_TO_CART))[0].click()
        self.wait.until(ec.presence_of_all_elements_located(self.CART_PAGE))[0].click()
        assert self.wait.until(ec.presence_of_all_elements_located(self.cart_button))[21].is_displayed(), "You are not on the cart page"
        self.wait.until(ec.presence_of_all_elements_located(self.MAIN_PAGE))[0].click()
        assert self.wait.until(ec.presence_of_all_elements_located(self.main_page))[0].is_displayed(), "You are not on the home page"

LCW().test_navigate()





