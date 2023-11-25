from selenium.webdriver.common.by import By


class TextBoxPageLocators():

    # form fields
    FULL_NAME = (By.XPATH, '//input[@id="userName"]')
    EMAIL = (By.XPATH, '//input[@id="userEmail"]')
    CURRENT_ADDRESS = (By.XPATH, '//textarea[@id="currentAddress"]')
    PERMANENT_ADDRESS = (By.XPATH, '//textarea[@id="permanentAddress"]')
    SUBMIT = (By.XPATH, '//button[@id="submit"]')


    # created fields
    CREATED_FULL_NAME = (By.XPATH, '//p[@id="name"]')
    CREATED_EMAIL = (By.XPATH, '//p[@id="email"]')
    CREATED_CURRENT_ADDRESS = (By.XPATH, '//p[@id="currentAddress"]')
    CREATED_PERMANENT_ADDRESS = (By.XPATH, '//p[@id="permanentAddress"]')

class CheckBoxPageLocators():

    EXPAND_ALL_BUTTON = (By.XPATH, '//button[@title="Expand all"]')
    ITEM_LIST = (By.XPATH, '//span[@class="rct-title"]')
    CHECKED_ITEMS = (By.XPATH, '//*[name()="svg" and @class="rct-icon rct-icon-check"]')
    TITLE_ITEM = 'ancestor::span//span[@class="rct-title"]'
    OUTPUT_RESULT = (By.XPATH, '//span[@class="text-success"]')


class RadioButtonPageLocators():
    YES_RADIOBUTTON = (By.XPATH, '//label[@for="yesRadio"]')
    IMPRESSIVE_RADIOBUTTON = (By.XPATH, '//label[@for="impressiveRadio"]')
    NO_RADIOBUTTON = (By.XPATH, '//label[@for="noRadio"]')
    OUTPUT_RESULT = (By.XPATH, '//span[@class="text-success"]')

class WebTablePageLocators():

    #person form
    ADD_BUTTON = (By.XPATH, '//button[@id="addNewRecordButton"]')
    FIRSTNAME_INPUT = (By.XPATH, '//input[@id="firstName"]')
    LASTNAME_INPUT = (By.XPATH, '//input[@id="lastName"]')
    EMAIL_INPUT = (By.XPATH, '//input[@id="userEmail"]')
    AGE_INPUT = (By.XPATH, '//input[@id="age"]')
    SALARY_INPUT = (By.XPATH, '//input[@id="salary"]')
    DEPARTMENT_INPUT = (By.XPATH, '//input[@id="department"]')
    SUBMIT_BUTTON = (By.XPATH, '//button[@id="submit"]')

    #table
    FULL_PEOPLE_LIST = (By.XPATH, '//div[@class="rt-tr-group"]')

    #search
    SEARCH_INPUT = (By.XPATH, '//input[@id="searchBox"]')

    #delete sign
    DELETE_BUTTON = (By.XPATH, '//span[@title="Delete"]')
    ROW_PARENT = '//ancestor::div[@class="rt-tr-group"]'

    #update
    UPDATE_BUTTON = (By.XPATH, '//span[@title="Edit"]')

    #delete
    NO_ROWS_FOUND = (By.XPATH, '//div[@class="rt-noData"]')

    #select rows
    COUNT_ROW_LIST = (By.XPATH, '//select[@aria-label="rows per page"]')

class ButtonPageLocators():

    DOUBLE_CLICK_BUTTON = (By.XPATH, '//button[@id="doubleClickBtn"]')
    RIGHT_CLICK_BUTTON = (By.XPATH, '//button[@id="rightClickBtn"]')
    CLICK_ME_BUTTON = (By.XPATH, '//div[3]/button')

    #click's result
    DOUBLE_CLICK_RESULT = (By.XPATH, '//p[@id="doubleClickMessage"]')
    RIGHT_CLICK_BUTTON_RESULT = (By.XPATH, '//p[@id="rightClickMessage"]')
    CLICK_ME_BUTTON_RESULT = (By.XPATH, '//p[@id="dynamicClickMessage"]')

class LinksPageLocators():

    SIMPLE_LINK = (By.XPATH,'//a[@id="simpleLink"]')
    BAD_REQUEST = (By.XPATH, '//a[@id="bad-request"]')

class UploadAndDownloadPageLocators():
    UPLOAD_FILE = (By.XPATH, '//input[@id="uploadFile"]')
    UPLOADED_RESULT = (By.XPATH, '//p[@id="uploadedFilePath"]')

    DOWNLOAD_FILE = (By.XPATH, '//a[@id="downloadButton"]')

class DynamicPropertiesPageLocators():
    COLOR_CHANGE_BUTTON = (By.XPATH, '//button[@id="colorChange"]')
    VISIBLE_AFTER_FIVE_SEC_BUTTON = (By.XPATH, '//button[@id="visibleAfter"]')
    ENABLE_BUTTON = (By.XPATH, '//button[@id="enableAfter"]')











