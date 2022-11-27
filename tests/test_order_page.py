import allure
from selenium import webdriver
from pages.order_page import OrderPage
from locators.order_page_locators import OrderPageLocators


class TestOrderPage:

    @allure.title('Check the order flow with the header button and first data set')
    @allure.description('Click on the order button in the header, fill forms with the first data set, and verify that the order is created')
    def test_order_page_header_button_first_data_set_success(self):
        driver = webdriver.Firefox()
        driver.get(OrderPageLocators.ORDER_PAGE_URL)

        order_page = OrderPage(driver)

        order_page.order_scooter(button_path=OrderPageLocators.HEADER_ORDER_BUTTON,
                                 name='Иван',
                                 surname='Иванов',
                                 address='Улица 1',
                                 metro='Черкизовская',
                                 phone='89111111111',
                                 date='01.12.2022',
                                 color='чёрный жемчуг',
                                 comment='Комментарий')
        order_header = order_page.check_order_is_successful()
        assert 'Заказ оформлен' in order_header

        scooter_main_logo = order_page.go_to_main_page()
        assert scooter_main_logo is not None

        order_page.go_to_yandex_page()

        driver.quit()

    @allure.title('Check the order flow with the finish order button and first data set')
    @allure.description('Click on the fisnish order button in the header, fill forms with the first data set, and verify that the order is created')
    def test_order_page_finis_button_first_data_set_success(self):
        driver = webdriver.Firefox()
        driver.get(OrderPageLocators.ORDER_PAGE_URL)

        order_page = OrderPage(driver)

        order_page.order_scooter(button_path=OrderPageLocators.FINISH_ORDER_BUTTON,
                                 name='Иван',
                                 surname='Иванов',
                                 address='Улица 1',
                                 metro='Черкизовская',
                                 phone='89111111111',
                                 date='01.12.2022',
                                 color='чёрный жемчуг',
                                 comment='Комментарий')
        order_header = order_page.check_order_is_successful()
        assert 'Заказ оформлен' in order_header

        scooter_main_logo = order_page.go_to_main_page()
        assert scooter_main_logo is not None

        order_page.go_to_yandex_page()

        driver.quit()

    @allure.title('Check the order flow with the header button and second data set')
    @allure.description('Click on the order button in the header, fill forms with the second data set, and verify that the order is created')
    def test_order_page_header_button_second_data_set_success(self):
        driver = webdriver.Firefox()
        driver.get(OrderPageLocators.ORDER_PAGE_URL)

        order_page = OrderPage(driver)

        order_page.order_scooter(button_path=OrderPageLocators.HEADER_ORDER_BUTTON,
                                 name='Петр',
                                 surname='Петров',
                                 address='Улица 2',
                                 metro='Черкизовская',
                                 phone='89222222222',
                                 date='02.12.2022',
                                 color='чёрный жемчуг',
                                 comment='')
        order_header = order_page.check_order_is_successful()
        assert 'Заказ оформлен' in order_header

        scooter_main_logo = order_page.go_to_main_page()
        assert scooter_main_logo is not None

        order_page.go_to_yandex_page()

        driver.quit()

    @allure.title('Check the finish order flow with the header button and second data set')
    @allure.description('Click on the finish order button in the header, fill forms with the second data set, and verify that the order is created')
    def test_order_page_finish_button_second_data_set_success(self):
        driver = webdriver.Firefox()
        driver.get(OrderPageLocators.ORDER_PAGE_URL)

        order_page = OrderPage(driver)

        order_page.order_scooter(button_path=OrderPageLocators.FINISH_ORDER_BUTTON,
                                 name='Петр',
                                 surname='Петров',
                                 address='Улица 2',
                                 metro='Черкизовская',
                                 phone='89222222222',
                                 date='02.12.2022',
                                 color='чёрный жемчуг',
                                 comment='')
        order_header = order_page.check_order_is_successful()
        assert 'Заказ оформлен' in order_header

        scooter_main_logo = order_page.go_to_main_page()
        assert scooter_main_logo is not None

        order_page.go_to_yandex_page()

        driver.quit()
