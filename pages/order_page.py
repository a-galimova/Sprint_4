from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_page_locators import OrderPageLocators


class OrderPage:

    def __init__(self, driver):
        self.driver = driver

    def scroll_to_order_button(self, button_path):
        order_button = self.driver.find_element(By.XPATH, button_path)
        self.driver.execute_script("arguments[0].scrollIntoView();", order_button)

    def wait_for_order_button_is_clickable(self, button_path):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable((By.XPATH, button_path)))

    def click_button(self, button_path):
        self.driver.find_element(By.XPATH, button_path).click()

    def fill_metro(self, metro):
        self.driver.find_element(By.XPATH, OrderPageLocators.METRO_FIELD).send_keys(metro)

        first_autocomplete_option = self.driver.find_element(By.XPATH, OrderPageLocators.FIRST_AUTOCOMPLETE_OPTION)
        first_option = WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(first_autocomplete_option))
        first_option.click()

    def fill_date(self, date):
        self.driver.find_element(By.XPATH, OrderPageLocators.DATE_FIELD).send_keys(date)

        date_element = WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, OrderPageLocators.DATE_PICKER_DAY)))
        date_element.click()

    def fill_duration(self):
        duration_element = WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable((By.XPATH, OrderPageLocators.DURATION_FIELD)))
        duration_element.click()

        first_option = self.driver.find_element(By.XPATH, OrderPageLocators.FIRST_DURATION_OPTION)
        first_option = WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(first_option))
        first_option.click()

    def fill_order_form(self, name, surname, address, metro, phone):
        self.driver.find_element(By.XPATH, OrderPageLocators.NAME_FIELD).send_keys(name)
        self.driver.find_element(By.XPATH, OrderPageLocators.SURNAME_FIELD).send_keys(surname)
        self.driver.find_element(By.XPATH, OrderPageLocators.ADDRESS_FIELD).send_keys(address)

        self.fill_metro(metro)

        self.driver.find_element(By.XPATH, OrderPageLocators.PHONE_FIELD).send_keys(phone)
        self.driver.find_element(By.XPATH, OrderPageLocators.NEXT_BUTTON).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, OrderPageLocators.ABOUT_RENT_HEADER)))

    def fill_rent_form(self, date, color, comment):
        self.fill_date(date)
        self.fill_duration()
        self.driver.find_element(By.XPATH, OrderPageLocators.BLACK_COLOR_CHECKBOX).send_keys(color)
        self.driver.find_element(By.XPATH, OrderPageLocators.COMMENT_FIELD).send_keys(comment)
        self.driver.find_element(By.XPATH, OrderPageLocators.ORDER_BUTTON_IN_RENT_FORM).click()

    def order_scooter(self, button_path, name, surname, address, metro, phone, date, color, comment):
        self.scroll_to_order_button(button_path)
        self.wait_for_order_button_is_clickable(button_path)
        self.click_button(button_path)
        self.fill_order_form(name, surname, address, metro, phone)
        self.fill_rent_form(date, color, comment)

        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable((By.XPATH, OrderPageLocators.CONFIRM_BUTTON)))
        self.click_button(OrderPageLocators.CONFIRM_BUTTON)
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, OrderPageLocators.ORDER_COMPLETE_HEADER)))

    def check_order_is_successful(self):
        complete_order = self.driver.find_element(By.XPATH, OrderPageLocators.ORDER_COMPLETE_HEADER)
        return complete_order.text

    def go_to_main_page(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable((By.XPATH, OrderPageLocators.CHECK_STATUS_BUTTON)))
        self.click_button(OrderPageLocators.CHECK_STATUS_BUTTON)
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable((By.XPATH, OrderPageLocators.SCOOTER_LOGO)))
        self.click_button(OrderPageLocators.SCOOTER_LOGO)
        return self.driver.find_element(By.XPATH, OrderPageLocators.SCOOTER_MAIN_LOGO)

    def go_to_yandex_page(self):
        self.click_button(OrderPageLocators.YANDEX_LOGO)
        WebDriverWait(self.driver, 5).until(
            expected_conditions.url_changes(OrderPageLocators.YANDEX_URL))
