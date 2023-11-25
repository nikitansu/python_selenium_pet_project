import time

import allure

from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage, FramesPage, NestedFramesPage, \
    ModalDialogsPage


@allure.suite("AlertsFrameWindow")
class TestAlertsFrameWindow():
    @allure.feature("BrowserWindow")
    class TestBrowserWindows():

        @allure.title("Check NewTab")
        def test_new_tab(self, driver):
            new_tab_and_window_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            new_tab_and_window_page.open()
            text_result = new_tab_and_window_page.check_opened_new_tab()
            assert text_result == 'This is a sample page', "New tap has not been opened"

        @allure.title("Check NewWindow")
        def test_new_window(self, driver):
            new_tab_and_window_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            new_tab_and_window_page.open()
            text_result = new_tab_and_window_page.check_opened_new_window()
            assert text_result == 'This is a sample page', "New tap has not been opened"

    @allure.feature("AlertsPage")
    class TestAlertsPage():

        @allure.title("Check SeeAlert")
        def test_see_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_see_alert()
            assert alert_text == "You clicked a button", "ALert was not shown"

        @allure.title("Check Alert Appears After Five Sec")
        def test_alert_appears_after_five_sec(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_alert_appears_after_five_sec()
            assert alert_text == "This alert appeared after 5 seconds", "ALert was not shown"

        @allure.title("Check Confirm Alert")
        def test_confirm_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_confirm_alert()
            assert alert_text == "You selected Ok", "ALert was not shown"

        @allure.title("Check Prompt Alert")
        def test_prompt_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            text, alert_text = alert_page.check_prompt_alert()
            assert text in alert_text, "ALert was not shown"

    @allure.feature("FramesPage")
    class TestFramesPage():
        @allure.title("Check Frames")
        def test_frames(self, driver):
            frame_page = FramesPage(driver, 'https://demoqa.com/frames')
            frame_page.open()
            result_frame1 = frame_page.check_frame("frame1")
            result_frame2 = frame_page.check_frame("frame2")
            assert result_frame1 == ['This is a sample page', '500px', '350px'], "The frame doesn't exist"
            assert result_frame2 == ['This is a sample page', '100px', '100px'], "The frame doesn't exist"

    @allure.feature("NestedFramesPage")
    class TestNestedFramesPage():

        @allure.title("Check Nested Frames")
        def test_nested_frames(self, driver):
            nested_frame_page = NestedFramesPage(driver, 'https://demoqa.com/nestedframes')
            nested_frame_page.open()
            parent_text, child_text = nested_frame_page.check_nested_frame()
            assert parent_text == "Parent frame", "Parent frame doesn't exist"
            assert child_text == "Child Iframe", "Child frame doesn't exist"

    @allure.feature("NestedModalDialogsPage")
    class TestModalDialogsPage():

        @allure.title("Check Modal Dialogs")
        def test_modal_dialogs(self, driver):
            modal_dialogs_page = ModalDialogsPage(driver, 'https://demoqa.com/modal-dialogs')
            modal_dialogs_page.open()
            small, large = modal_dialogs_page.check_modal_dialogs()
            assert small[1] < large[1], "Text from the small dialog >= text from the large dialog"
            assert small[0] == 'Small Modal', "Wrong title for small modal dialog"
            assert large[0] == 'Large Modal', "Wrong title for large modal dialog"


