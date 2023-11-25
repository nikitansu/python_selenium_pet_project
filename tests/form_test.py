import allure

from pages.form_page import FormPage


@allure.suite("Form")
class TestForm:
    @allure.feature("FormPage")
    class TestFormPage:
        @allure.title("Check Test Form Page")
        def test_page(self, driver):
            form_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
            form_page.open()
            person_info = form_page.fill_form_fields()
            result = form_page.form_result()

            assert[person_info.first_name + " " + person_info.last_name, person_info.email] == [result[0], result[1]], "the form has not been filled"