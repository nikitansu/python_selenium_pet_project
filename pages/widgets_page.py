import random
import time

import allure
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from generator.generator import generated_color, generated_date
from locators.widgets_page_locators import AccordianPageLocators, AutocompletePageLocators, DatePickerPageLocators, \
    SliderPageLocators, ProgressBarPageLocators, TabsPageLocators, ToolTipsPageLocators, MenuPageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    @allure.step("Check Accordian")
    def check_accordian(self, accordian_number):
        accordian = {
                            'first': {'title': self.locators.FIRST_SECTION_TITLE,
                                      'content': self.locators.FIRST_SECTION_CONTENT},

                            'second': {'title': self.locators.SECOND_SECTION_TITLE,
                                       'content': self.locators.SECOND_SECTION_CONTENT},

                            'third': {'title': self.locators.THIRD_SECTION_TITLE,
                                      'content': self.locators.THIRD_SECTION_CONTENT}
                            }

        section_title = self.element_is_visible(accordian[accordian_number]['title'])
        section_title.click()
        try:
            section_content = self.element_is_visible(accordian[accordian_number]['content']).text
        except TimeoutException:
            section_title.click()
            section_content = self.element_is_visible(accordian[accordian_number]['content']).text
        return [section_title.text, len(section_content)]

class AutocompletePage(BasePage):
    locators = AutocompletePageLocators()

    @allure.step("Fill Multi Input")
    def fill_multi_input(self):
        colors = random.sample(next(generated_color()).color_name, k=random.randint(2, 5))
        for color in colors:
            input_multi = self.element_is_clickable(self.locators.MULTI_INPUT)
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.RETURN)
        return colors

    @allure.step("Remove Value From Multi")
    def remove_value_from_multi(self):
        count_value_before = len(self.elements_are_present(self.locators.MULTI_VALUE))
        remove_button_list = self.elements_are_present(self.locators.MULTI_VALUE_REMOVE)
        for value in remove_button_list:
            value.click()
            break
        count_value_after = len(self.elements_are_present(self.locators.MULTI_VALUE))
        return count_value_before, count_value_after

    @allure.step("Check Color In Multi")
    def check_color_in_multi(self):
        color_list = self.elements_are_present(self.locators.MULTI_VALUE)
        colors = []
        for color in color_list:
            colors.append(color.text)
        return

    @allure.step("Fill Single Input")
    def fill_single_input(self):
        color = random.sample(next(generated_color()).color_name, k=1)
        input_single = self.element_is_clickable(self.locators.SINGLE_INPUT)
        input_single.send_keys(color)
        input_single.send_keys(Keys.RETURN)
        return color[0]

    @allure.step("Check Color In Single")
    def check_color_in_single(self):
        color = self.element_is_visible(self.locators.SINGLE_VALUE)
        return color.text

class DatePickerPage(BasePage):
    locators = DatePickerPageLocators()

    @allure.step("Select Date")
    def select_date(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.set_date_by_text(self.locators.DATE_SELECT_MONTH, date.month)
        self.set_date_by_text(self.locators.DATE_SELECT_YEAR, date.year)
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        value_date_after = input_date.get_attribute('value')
        return value_date_before, value_date_after

    @allure.step("Select Date And Time")
    def select_date_and_time(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.element_is_visible(self.locators.DATE_AND_TIME_MONTH).click()
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_MONTH_LIST, date.month)
        self.element_is_visible(self.locators.DATE_AND_TIME_YEAR).click()
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_YEAR_LIST, '2020')
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_TIME_LIST, date.time)
        input_date_after = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
        value_date_after = input_date_after.get_attribute('value')
        return value_date_before, value_date_after

    @allure.step("Set Date By Text")
    def set_date_by_text(self, element, value):
        select = Select(self.element_is_present(element))
        select.select_by_visible_text(value)

    @allure.step("Set Date Item From List")
    def set_date_item_from_list(self, elements, value):
        item_list = self.elements_are_present(elements)
        for item in item_list:
            if item.text == value:
                item.click()
                break

class SliderPage(BasePage):
    locators = SliderPageLocators()

    @allure.step("Change Slider Value")
    def change_slider_value(self):
        value_before = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        slider_input = self.element_is_visible(self.locators.INPUT_SLIDER)
        self.action_drag_and_drop_by_offset(slider_input, random.randint(1, 100), 0)
        value_after = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        return value_before, value_after




class ProgressBarPage(BasePage):
    locators = ProgressBarPageLocators()

    @allure.step("Change Progress Bar Value")
    def change_progress_bar_value(self):
        value_before = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
        progress_bar_button = self.element_is_clickable(self.locators.PROGRESS_BAR_BUTTON)
        progress_bar_button.click()
        time.sleep(random.randint(2, 5))
        progress_bar_button.click()
        value_after = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
        return value_before, value_after

class TabsPage(BasePage):
    locators = TabsPageLocators()

    @allure.step("Check Tabs")
    def check_tabs(self, name_tab):
        tabs = {
            'what': {'title': self.locators.TAB_WHAT,
                      'content': self.locators.TAB_WHAT_CONTENT},

            'origin': {'title': self.locators.TAB_ORIGIN,
                       'content': self.locators.TAB_ORIGIN_CONTENT},

            'use': {'title': self.locators.TAB_USE,
                      'content': self.locators.TAB_USE_CONTENT},

            'more': {'title': self.locators.TAB_MORE,
                      'content': self.locators.TAB_MORE_CONTENT}
        }

        tab = self.element_is_visible(tabs[name_tab]['title'])
        tab.click()
        tab_content = self.element_is_visible(tabs[name_tab]['content']).text
        return tab.text, len(tab_content)

class ToolTipsPage(BasePage):
    locators = ToolTipsPageLocators()

    @allure.step("Get Text From Tool Tip")
    def get_text_from_tool_tip(self, hover_element, wait_element):
        element = self.element_is_present(hover_element)
        time.sleep(0.5)
        self.action_move_to_element(element)
        self.element_is_visible(wait_element)
        tool_tip_text = self.element_is_visible(self.locators.TOOL_TIPS_INNERS)
        text = tool_tip_text.text
        return text

    @allure.step("Check Tool Tip")
    def check_tool_tip(self):
        tool_tip_text_button = self.get_text_from_tool_tip(self.locators.BUTTON, self.locators.TOOL_TIP_BUTTON)
        tool_tip_text_field = self.get_text_from_tool_tip(self.locators.FIELD, self.locators.TOOL_TIP_FIELD)
        tool_tip_text_contrary_link = self.get_text_from_tool_tip(self.locators.CONTRARY_LINK, self.locators.TOOL_TIP_CONTRARY_LINK)
        tool_tip_text_section_link = self.get_text_from_tool_tip(self.locators.SECTION_LINK, self.locators.TOOL_TIP_SECTION_LINK)
        return tool_tip_text_button, tool_tip_text_field, tool_tip_text_contrary_link, tool_tip_text_section_link

class MenuPage(BasePage):
    locators = MenuPageLocators()

    @allure.step("Check Menu")
    def check_menu(self):
        menu_item_list = self.elements_are_present(self.locators.MENU_ITEM)
        data = []
        for item in menu_item_list:
            self.action_move_to_element(item)
            data.append(item.text)
        return data














