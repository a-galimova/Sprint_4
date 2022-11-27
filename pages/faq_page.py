from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class FaqPage:

    def __init__(self, driver):
        self.driver = driver

    def scroll_to_faq(self, header_id):
        faq_question = self.driver.find_element(By.ID, header_id)
        self.driver.execute_script("arguments[0].scrollIntoView();", faq_question)

    def wait_for_question_is_clickable(self, header_id):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable((By.ID, header_id)))

    def wait_for_answer_is_visible(self, panel_id):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.ID, panel_id)))

    def click_question_button(self, header_id):
        self.driver.find_element(By.ID, header_id).click()

    def get_question_text(self, header_id):
        return self.driver.find_element(By.ID, header_id).text

    def get_answer_text(self, panel_id):
        return self.driver.find_element(By.ID, panel_id).text

    def get_answer(self, header_id, panel_id):
        self.scroll_to_faq(header_id)
        self.wait_for_question_is_clickable(header_id)
        self.click_question_button(header_id)
        self.wait_for_answer_is_visible(panel_id)
        return self.get_answer_text(panel_id)
