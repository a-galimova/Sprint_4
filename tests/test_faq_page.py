import allure
from selenium import webdriver
from pages.faq_page import FaqPage
from locators.faq_page_locators import FaqPageLocators


class TestFaqPage:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()

    @allure.title('Check the first FAQ question and answer')
    @allure.description('Click on the first question button and validate question and answer text')
    def test_faq_page_click_first_question_success(self):
        self.driver.get(FaqPageLocators.FAQ_PAGE_URL)

        faq_page = FaqPage(self.driver)

        question_text = faq_page.get_question_text(FaqPageLocators.FIRST_QUESTION_HEADER_ID)
        answer_text = faq_page.get_answer(FaqPageLocators.FIRST_QUESTION_HEADER_ID,
                                          FaqPageLocators.FIRST_ANSWER_PANEL_ID)

        assert question_text == 'Сколько это стоит? И как оплатить?'
        assert answer_text == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    @allure.title('Check the second FAQ question and answer')
    @allure.description('Click on the second question button and validate question and answer text')
    def test_faq_page_click_second_question_success(self):
        self.driver.get(FaqPageLocators.FAQ_PAGE_URL)

        faq_page = FaqPage(self.driver)

        question_text = faq_page.get_question_text(FaqPageLocators.SECOND_QUESTION_HEADER_ID)
        answer_text = faq_page.get_answer(FaqPageLocators.SECOND_QUESTION_HEADER_ID,
                                          FaqPageLocators.SECOND_ANSWER_PANEL_ID)

        assert question_text == 'Хочу сразу несколько самокатов! Так можно?'
        assert answer_text == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

    @allure.title('Check the third FAQ question and answer')
    @allure.description('Click on the third question button and validate question and answer text')
    def test_faq_page_click_third_question_success(self):
        self.driver.get(FaqPageLocators.FAQ_PAGE_URL)

        faq_page = FaqPage(self.driver)

        question_text = faq_page.get_question_text(FaqPageLocators.THIRD_QUESTION_HEADER_ID)
        answer_text = faq_page.get_answer(FaqPageLocators.THIRD_QUESTION_HEADER_ID,
                                          FaqPageLocators.THIRD_ANSWER_PANEL_ID)

        assert question_text == 'Как рассчитывается время аренды?'
        assert answer_text == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'

    @allure.title('Check the fourth FAQ question and answer')
    @allure.description('Click on the fourth question button and validate question and answer text')
    def test_faq_page_click_fourth_question_success(self):
        self.driver.get(FaqPageLocators.FAQ_PAGE_URL)

        faq_page = FaqPage(self.driver)

        question_text = faq_page.get_question_text(FaqPageLocators.FOURTH_QUESTION_HEADER_ID)
        answer_text = faq_page.get_answer(FaqPageLocators.FOURTH_QUESTION_HEADER_ID,
                                          FaqPageLocators.FOURTH_ANSWER_PANEL_ID)

        assert question_text == 'Можно ли заказать самокат прямо на сегодня?'
        assert answer_text == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    @allure.title('Check the fifth FAQ question and answer')
    @allure.description('Click on the fifth question button and validate question and answer text')
    def test_faq_page_click_fifth_question_success(self):
        self.driver.get(FaqPageLocators.FAQ_PAGE_URL)

        faq_page = FaqPage(self.driver)

        question_text = faq_page.get_question_text(FaqPageLocators.FIFTH_QUESTION_HEADER_ID)
        answer_text = faq_page.get_answer(FaqPageLocators.FIFTH_QUESTION_HEADER_ID,
                                          FaqPageLocators.FIFTH_ANSWER_PANEL_ID)

        assert question_text == 'Можно ли продлить заказ или вернуть самокат раньше?'
        assert answer_text == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

    @allure.title('Check the sixth FAQ question and answer')
    @allure.description('Click on the sixth question button and validate question and answer text')
    def test_faq_page_click_sixth_question_success(self):
        self.driver.get(FaqPageLocators.FAQ_PAGE_URL)

        faq_page = FaqPage(self.driver)

        question_text = faq_page.get_question_text(FaqPageLocators.SIXTH_QUESTION_HEADER_ID)
        answer_text = faq_page.get_answer(FaqPageLocators.SIXTH_QUESTION_HEADER_ID,
                                          FaqPageLocators.SIXTH_ANSWER_PANEL_ID)

        assert question_text == 'Вы привозите зарядку вместе с самокатом?'
        assert answer_text == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'

    @allure.title('Check the seventh FAQ question and answer')
    @allure.description('Click on the seventh question button and validate question and answer text')
    def test_faq_page_click_seventh_question_success(self):
        self.driver.get(FaqPageLocators.FAQ_PAGE_URL)

        faq_page = FaqPage(self.driver)

        question_text = faq_page.get_question_text(FaqPageLocators.SEVENTH_QUESTION_HEADER_ID)
        answer_text = faq_page.get_answer(FaqPageLocators.SEVENTH_QUESTION_HEADER_ID,
                                          FaqPageLocators.SEVENTH_ANSWER_PANEL_ID)

        assert question_text == 'Можно ли отменить заказ?'
        assert answer_text == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

    @allure.title('Check the eighth FAQ question and answer')
    @allure.description('Click on the eighth question button and validate question and answer text')
    def test_faq_page_click_eighth_question_success(self):
        self.driver.get(FaqPageLocators.FAQ_PAGE_URL)

        faq_page = FaqPage(self.driver)

        question_text = faq_page.get_question_text(FaqPageLocators.EIGHTH_QUESTION_HEADER_ID)
        answer_text = faq_page.get_answer(FaqPageLocators.EIGHTH_QUESTION_HEADER_ID,
                                          FaqPageLocators.EIGHTH_ANSWER_PANEL_ID)

        assert question_text == 'Я живу за МКАДом, привезёте?'
        assert answer_text == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
