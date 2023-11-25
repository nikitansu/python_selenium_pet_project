import time

import allure

from pages.widgets_page import AccordianPage, AutocompletePage, DatePickerPage, SliderPage, ProgressBarPage, TabsPage, \
    ToolTipsPage, MenuPage


@allure.suite("Widgets")
class TestWidgets:
    @allure.feature("AccordianPage")
    class TestAccordianPage():

        @allure.title("Check Accordian")
        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            first_title, first_content = accordian_page.check_accordian('first')
            second_title, second_content = accordian_page.check_accordian('second')
            third_title, third_content = accordian_page.check_accordian('third')
            assert first_title == 'What is Lorem Ipsum?' and first_content > 0, "Incorrect title or missing text"
            assert second_title == 'Where does it come from?' and second_content > 0, "Incorrect title or missing text"
            assert third_title == 'Why do we use it?' and third_content > 0, "Incorrect title or missing text"

    @allure.feature("AutocompletePage")
    class TestAutocompletePage():

        @allure.title("Fill Multi Autocomplete")
        def test_fill_multi_autocomplete(self, driver):
            autocomplete_page = AutocompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            colors = autocomplete_page.fill_multi_input()
            colors_result = autocomplete_page.check_color_in_multi()
            assert colors == colors_result, "The added colors are missed in the input"

        @allure.title("Remove Value From Multi")
        def test_remove_value_from_multi(self, driver):
            autocomplete_page = AutocompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            autocomplete_page.fill_multi_input()
            count_value_before, count_value_after = autocomplete_page.remove_value_from_multi()
            assert count_value_before > count_value_after, "The value was not deleted"

        @allure.title("Fill Single Autocomplete")
        def test_fill_single_autocomplete(self, driver):
            autocomplete_page = AutocompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            color = autocomplete_page.fill_single_input()
            color_result = autocomplete_page.check_color_in_single()
            assert color == color_result, "The added color is missed in the input"

    @allure.feature("DatePickerPage")
    class TestDatePickerPage():

        @allure.title("Change Date")
        def test_change_date(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_date()
            assert value_date_before != value_date_after, "date has not been changed"

        @allure.title("Change Date And Time")
        def test_change_date_and_time(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_date_and_time()
            assert value_date_before != value_date_after, "date and time have not been changed"

    @allure.feature("SliderPage")
    class TestSliderPage():

        @allure.title("Slider")
        def test_slider(self, driver):
            slider_page = SliderPage(driver, 'https://demoqa.com/slider')
            slider_page.open()
            before, after = slider_page.change_slider_value()
            assert before != after, "the slider value has not been changed"

    @allure.feature("ProgressBarPage")
    class TestProgressBarPage():

        @allure.title("ProgressBar")
        def test_progress_bar(self, driver):
            progress_bar_page = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
            progress_bar_page.open()
            before, after = progress_bar_page.change_progress_bar_value()
            assert before != after, "the progress bar value has not been changed"

    @allure.feature("TabsPage")
    class TestTabsPage():

        @allure.title("Tabs")
        def test_tabs(self, driver):
            tabs_page = TabsPage(driver, 'https://demoqa.com/tabs')
            tabs_page.open()
            what_tab, what_content = tabs_page.check_tabs('what')
            origin_tab, origin_content = tabs_page.check_tabs('origin')
            use_tab, use_content = tabs_page.check_tabs('use')
            more_tab, more_content = tabs_page.check_tabs('more')
            assert what_tab == 'What' and what_content != 0, "The tab 'What' was not pressed or text missed"
            assert origin_tab == 'Origin' and origin_content != 0, "The tab 'Origin' was not pressed or text missed"
            assert use_tab == 'Use' and use_content != 0, "The tab 'Use' was not pressed or text missed"
            assert more_tab == 'More' and more_content != 0, "The tab 'More' was not pressed or text missed"

    @allure.feature("ToolTips")
    class TestToolTips():

        @allure.title("ToolTips")
        def test_tool_tips(self, driver):
            tool_tips_page = ToolTipsPage(driver, 'https://demoqa.com/tool-tips')
            tool_tips_page.open()
            button_text, field_text, contrary_text, section_text = tool_tips_page.check_tool_tip()
            assert button_text == 'You hovered over the Button', "Hover hasn't appeared or message incorrect"
            assert field_text == 'You hovered over the text field', "Hover hasn't appeared or message incorrect"
            assert contrary_text == 'You hovered over the Contrary', "Hover hasn't appeared or message incorrect"
            assert section_text == 'You hovered over the 1.10.32', "Hover hasn't appeared or message incorrect"

    @allure.feature("ToolTips")
    class TestMenuPage():

        @allure.title("MenuItems")
        def test_menu_items(self, driver):
            menu_page = MenuPage(driver, 'https://demoqa.com/menu#')
            menu_page.open()
            data = menu_page.check_menu()
            assert data == ['Main Item 1', 'Main Item 2', 'Sub Item', 'Sub Item', 'SUB SUB LIST »', 'Sub Sub Item 1', 'Sub Sub Item 2', 'Main Item 3'], "Items are missed in menu"











