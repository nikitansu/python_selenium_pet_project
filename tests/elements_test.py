import random
import time

import allure

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage, \
    UploadAndDownloadPage, DynamicPropertiesPage


@allure.suite("Elements")
class TestElements():

    @allure.feature("TextBox")
    class TestTextBox():
        @allure.title("Check TextBox")
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver,'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_current_address, output_permanent_address = text_box_page.check_filled_form()
            assert full_name == output_name, "the full name does not match"
            assert email == output_email, "the email does not match"
            assert current_address == output_current_address, "the current address does not match"
            assert permanent_address == output_permanent_address, "the permanent address does not match"

    @allure.feature("CheckBox")
    class TestCheckBox():
        @allure.title("Check CheckBox")
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            print(input_checkbox)
            print(output_result)
            assert input_checkbox == output_result, "Selected checkboxes don't correspond with output list"

    @allure.feature("RadioButton")
    class TestRadioButton():

        @allure.title("Check RadioButton")
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button('yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('impressive')
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('no')
            output_no = radio_button_page.get_output_result()
            assert output_yes == "Yes", "'Yes' has not been selected"
            assert output_impressive == "Impressive", "'Impressive' has not been selected"
            assert output_no == "No", "'No' has not been selected"

    @allure.feature("WebTable")
    class TestWebTable():

        @allure.title("Check WebTableAddPerson")
        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            table_result = web_table_page.check_new_added_person()
            print(new_person)
            print(table_result)
            assert new_person in table_result

        @allure.title("Check WebTableSearchPerson")
        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            key_word = web_table_page.add_new_person()[0]
            web_table_page.search_some_person(key_word)
            table_result = web_table_page.check_search_person()
            print(key_word)
            print(table_result)
            assert key_word in table_result, "Person was not found in the table"

        @allure.title("Check WebTableUpdatePersonInfo")
        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            key_word = web_table_page.add_new_person()[0]
            web_table_page.search_some_person(key_word)
            age = web_table_page.update_person_info()
            row = web_table_page.check_search_person()
            assert age in row, "Person has not been updated"

        @allure.title("Check WebTableDeletePerson")
        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            key_word = web_table_page.add_new_person()[0]
            web_table_page.search_some_person(key_word)
            web_table_page.delete_person()
            text = web_table_page.check_deleted()
            assert text == 'No rows found'

        @allure.title("Check WebTableChangeCountRows")
        def test_web_table_change_count_rows(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            count = web_table_page.select_up_to_some_rows()
            assert count == [5, 10, 20, 25, 50, 100]

    @allure.feature("ButtonPage")
    class TestButtonsPage():

        @allure.title("Check DifferentClickOnTheButtons")
        def test_different_click_on_the_buttons(self, driver):
            button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            button_page.open()
            double = button_page.click_on_different_buttons("double")
            right = button_page.click_on_different_buttons("right")
            click = button_page.click_on_different_buttons("click")
            assert double == "You have done a double click", "Double click was not done"
            assert right == "You have done a right click", "Right click was not done"
            assert click == "You have done a dynamic click", "Click was not done"

    @allure.feature("LinksPage")
    class TestLinksPage():

        @allure.title("Check Link")
        def test_check_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href_link, current_url = links_page.check_new_tap_simple_link()
            print(href_link, current_url)
            assert href_link == current_url, "Broken link or incorrect URL"

        @allure.title("Check BrokenLink")
        def test_broken_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_broken_link('https://demoqa.com/bad-request')
            assert response_code == 400, "Link works or incorrect response status code"

    @allure.feature("UploadAndDownload")
    class TestUploadAndDownload():

        @allure.title("Check UploadFile")
        def test_upload_file(self, driver):
            upload_and_download_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_and_download_page.open()
            file_name, result = upload_and_download_page.upload_file()
            assert file_name == result, "the file has not been uploaded"

        @allure.title("Check DownloadFile")
        def test_download_file(self, driver):
            upload_and_download_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_and_download_page.open()
            check = upload_and_download_page.download_file()
            assert check is True, "the file has not been downloaded"

    @allure.feature("DynamicPropertiesPage")
    class TestDynamicPropertiesPage():

        @allure.title("Check ChangeColor")
        def test_change_color(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            color_before, color_after = dynamic_properties_page.check_changed_of_color()
            assert color_after != color_before, "Color has not been changed"

        @allure.title("Check AppearButton")
        def test_appear_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            appear = dynamic_properties_page.check_of_appear_button()
            assert appear is True, "The button has not appeared after 5 seconds"

        @allure.title("Check EnableButton")
        def test_enable_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            enable = dynamic_properties_page.check_of_appear_button()
            assert enable is True, "The button has not become clickable after 5 seconds"







