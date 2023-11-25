from selenium.webdriver.common.by import By


class AccordianPageLocators():
    FIRST_SECTION_TITLE = (By.XPATH, '//div[@id="section1Heading"]')
    FIRST_SECTION_CONTENT = (By.XPATH, '//div[@id="section1Content"]//p')

    SECOND_SECTION_TITLE = (By.XPATH, '//div[@id="section2Heading"]')
    SECOND_SECTION_CONTENT = (By.XPATH, '//div[@id="section2Content"]//p')

    THIRD_SECTION_TITLE = (By.XPATH, '//div[@id="section3Heading"]')
    THIRD_SECTION_CONTENT = (By.XPATH, '//div[@id="section3Content"]//p')

class AutocompletePageLocators():
    MULTI_INPUT = (By.XPATH, '//input[@id="autoCompleteMultipleInput"]')
    MULTI_VALUE = (By.XPATH, '//div[@class="css-12jo7m5 auto-complete__multi-value__label"]')
    MULTI_VALUE_REMOVE = (By.XPATH, '//div[@class="css-xb97g8 auto-complete__multi-value__remove"]')
    SINGLE_VALUE = (By.XPATH, '//div[@class="auto-complete__single-value css-1uccc91-singleValue"]')
    SINGLE_INPUT = (By.XPATH, '//input[@id="autoCompleteSingleInput"]')

class DatePickerPageLocators():
    DATE_INPUT = (By.XPATH, '//input[@id="datePickerMonthYearInput"]')
    DATE_SELECT_MONTH = (By.XPATH, '//select[@class="react-datepicker__month-select"]')
    DATE_SELECT_YEAR = (By.XPATH, '//select[@class="react-datepicker__year-select"]')
    DATE_SELECT_DAY_LIST = (By.XPATH, '//div[contains(@class, "react-datepicker__day react-datepicker")]')

    DATE_AND_TIME_INPUT = (By.XPATH, '//input[@id="dateAndTimePickerInput"]')
    DATE_AND_TIME_MONTH = (By.XPATH, '//div[@class="react-datepicker__month-read-view"]')
    DATE_AND_TIME_YEAR = (By.XPATH, '//div[@class="react-datepicker__year-read-view"]')
    DATE_AND_TIME_TIME_LIST = (By.XPATH, '//li[@class="react-datepicker__time-list-item "]')
    DATE_AND_TIME_MONTH_LIST = (By.XPATH, '//div[@class="react-datepicker__month-option"]')
    DATE_AND_TIME_YEAR_LIST = (By.XPATH, '//div[@class="react-datepicker__year-option"]')


class SliderPageLocators():
    INPUT_SLIDER = (By.XPATH, '//input[@class="range-slider range-slider--primary"]')
    SLIDER_VALUE = (By.XPATH, '//input[@id="sliderValue"]')

class ProgressBarPageLocators():
    PROGRESS_BAR_BUTTON = (By.XPATH, '//button[@id="startStopButton"]')
    PROGRESS_BAR_VALUE = (By.XPATH, '//div[@class="progress-bar bg-info"]')


class TabsPageLocators():
    TAB_WHAT = (By.XPATH, '//a[@id="demo-tab-what"]')
    TAB_WHAT_CONTENT = (By.XPATH, '//div[@id="demo-tabpane-what"]')

    TAB_ORIGIN = (By.XPATH, '//a[@id="demo-tab-origin"]')
    TAB_ORIGIN_CONTENT = (By.XPATH, '//div[@id="demo-tabpane-origin"]')

    TAB_USE = (By.XPATH, '//a[@id="demo-tab-use"]')
    TAB_USE_CONTENT = (By.XPATH, '//div[@id="demo-tabpane-use"]')

    TAB_MORE = (By.XPATH, '//a[@id="demo-tab-more"]')
    TAB_MORE_CONTENT = (By.XPATH, '//div[@id="demo-tabpane-more"]')

class ToolTipsPageLocators():
    BUTTON = (By.XPATH, '//button[@id="toolTipButton"]')
    TOOL_TIP_BUTTON = (By.XPATH, '//button[@aria-describedby="buttonToolTip"]')

    FIELD = (By.XPATH, '//input[@id="toolTipTextField"]')
    TOOL_TIP_FIELD = (By.XPATH, '//input[@aria-describedby="textFieldToolTip"]')


    CONTRARY_LINK = (By.XPATH, '//a[text()="Contrary"]')
    TOOL_TIP_CONTRARY_LINK = (By.XPATH, '//a[@aria-describedby="contraryTexToolTip"]')


    SECTION_LINK = (By.XPATH, '//a[text()="1.10.32"]')
    TOOL_TIP_SECTION_LINK = (By.XPATH, '//a[@aria-describedby="sectionToolTip"]')

    TOOL_TIPS_INNERS = (By.XPATH, '//div[@class="tooltip-inner"]')

class MenuPageLocators():
    MENU_ITEM = (By.XPATH, '//li//a[@href="#"]')


