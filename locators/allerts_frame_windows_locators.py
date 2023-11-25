from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators():
    NEW_TAB_BUTTON = (By.XPATH, '//button[@id="tabButton"]')

    NEW_TAB_TITLE = (By.XPATH, '//h1[@id="sampleHeading"]')
    NEW_WINDOW_BUTTON = (By.XPATH, '//button[@id="windowButton"]')

class AlertsPageLocators():
    SEE_ALERT_BUTTON = (By.XPATH, '//button[@id="alertButton"]')
    APPEAR_ALERT_AFTER_FIVE_SECOND_BUTTON = (By.XPATH, '//button[@id="timerAlertButton"]')
    CONFIRM_BOX_ALERT_BUTTON = (By.XPATH, '//button[@id="confirmButton"]')
    PROMPT_BOX_ALERT_BUTTON = (By.XPATH, '//button[@id="promtButton"]')

    #results
    CONFIRM_RESULT = (By.XPATH, '//span[@id="confirmResult"]')
    PROMPT_RESULT = (By.XPATH, '//span[@id="promptResult"]')

class FramesPageLocators():
    FIRST_FRAME = (By.XPATH, '//iframe[@id="frame1"]')
    SECOND_FRAME = (By.XPATH, '//iframe[@id="frame2"]')

    TITLE_FRAME = (By.XPATH, '//h1[@id="sampleHeading"]')

class NestedFramesPageLocators():
    PARENT_FRAME = (By.XPATH, '//iframe[@id="frame1"]')
    PARENT_TEXT = (By.XPATH, '//body[text()="Parent frame"]')
    CHILD_FRAME = (By.XPATH, '//iframe[@srcdoc="<p>Child Iframe</p>"]')
    CHILD_TEXT = (By.XPATH, '//*[text()="Child Iframe"]')

class ModalDialogsPageLocators():
        SMALL_MODAL_BUTTON = (By.XPATH, '//button[@id="showSmallModal"]')
        CLOSE_SMALL_MODAL_BUTTON = (By.XPATH, '//button[@id="closeSmallModal"]')
        BODY_SMALL_MODAL = (By.XPATH, '//div[@class="modal-body"]')
        TITLE_MODAL = (By.XPATH, '//div[@class="modal-title h4"]')

        LARGE_MODAL_BUTTON = (By.XPATH, '//button[@id="showLargeModal"]')
        CLOSE_LARGE_MODAL_BUTTON = (By.XPATH, '//button[@id="closeLargeModal"]')
        BODY_LARGE_MODAL = (By.XPATH, '//p[@class]')
