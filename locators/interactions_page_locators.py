from selenium.webdriver.common.by import By


class SortablePageLocators():
    TAB_LIST = (By.XPATH, '//a[@id="demo-tab-list"]')
    LIST_ITEM = (By.XPATH, '//div[@id="demo-tabpane-list"]//div[@class="list-group-item list-group-item-action"]')
    TAB_GRID = (By.XPATH, '//a[@id="demo-tab-grid"]')
    GRID_ITEM = (By.XPATH, '//div[@id="demo-tabpane-grid"]//div[@class="list-group-item list-group-item-action"]')


class SelectablePageLocators():
    TAB_LIST = (By.XPATH, '//a[@id="demo-tab-list"]')
    LIST_ITEM = (By.XPATH, '//li[@class="mt-2 list-group-item list-group-item-action"]')
    LIST_ITEM_ACTIVE = (By.XPATH, '//li[@class="mt-2 list-group-item active list-group-item-action"]')
    GRID_LIST = (By.XPATH, '//a[@id="demo-tab-grid"]')
    GRID_ITEM = (By.XPATH, '//li[@class="list-group-item list-group-item-action"]')
    GRID_ITEM_ACTIVE = (By.XPATH, '//li[@class="list-group-item active list-group-item-action"]')

class ResizablePageLocators():
    RESIZABLE_BOX_HANDLE = (By.XPATH, '//div[@id="resizableBoxWithRestriction"]//span[@class="react-resizable-handle react-resizable-handle-se"]')
    RESIZABLE_BOX = (By.XPATH, '//div[@id="resizableBoxWithRestriction"]')
    RESIZABLE_HANDLE = (By.XPATH, '//div[@id="resizable"]//span[@class="react-resizable-handle react-resizable-handle-se"]')
    RESIZABLE = (By.XPATH, '//div[@id="resizable"]')

class DroppablePageLocators():
    #simple
    SIMPLE_TAB = (By.XPATH, '//a[@id="droppableExample-tab-simple"]')
    DRAG_ME_SIMPLE = (By.XPATH, '//div[@class="simple-drop-container"]//div[@id="draggable"]')
    DROP_HERE_SIMPLE = (By.XPATH, '//div[@class="simple-drop-container"]//div[@id="droppable"]')

    #accept
    ACCEPT_TAB = (By.XPATH, '//a[@id="droppableExample-tab-accept"]')
    ACCEPTABLE = (By.XPATH, '//div[@class="accept-drop-container"]//div[@id="acceptable"]')
    NOT_ACCEPTABLE = (By.XPATH, '//div[@class="accept-drop-container"]//div[@id="notAcceptable"]')
    DROP_HERE_ACCEPT = (By.XPATH, '//div[@class="accept-drop-container"]//div[@id="droppable"]')

    #prevent propogation
    PREVENT_TAB = (By.XPATH, '//a[@id="droppableExample-tab-preventPropogation"]')
    NOT_GREEDY_DROP_BOX_TEXT = (By.XPATH, '//div[@id="notGreedyDropBox"]//p')
    NOT_GREEDY_INNER_BOX = (By.XPATH, '//div[@id="notGreedyDropBox"]//div[@id="notGreedyInnerDropBox"]')
    GREEDY_DROP_BOX_TEXT = (By.XPATH, '//div[@id="greedyDropBox"]//p[text()="Outer droppable"]')
    GREEDY_INNER_BOX = (By.XPATH, '//div[@id="greedyDropBox"]//div[@id="greedyDropBoxInner"]')
    DRAG_ME_PREVENT = (By.XPATH, '//div[@class="pp-drop-container"]//div[@id="dragBox"]')

    #revert draggable
    REVERT_TAB = (By.XPATH, '//a[@id="droppableExample-tab-revertable"]')
    WILL_REVERT = (By.XPATH, '//div[@id="revertable"]')
    NOT_REVERT = (By.XPATH, '//div[@id="notRevertable"]')
    DROP_HERE_REVERT = (By.XPATH, '//div[@class="revertable-drop-container"]//div[@id="droppable"]')

class DraggablePageLocators():

    #simple
    SIMPLE_TAB = (By.XPATH, '//a[@id="draggableExample-tab-simple"]')
    DRAG_ME = (By.XPATH, '//div[@id="dragBox"]')

    #axis
    AXIS_TAB = (By.XPATH, '//a[@id="draggableExample-tab-axisRestriction"]')
    ONLY_X = (By.XPATH, '//div[@id="restrictedX"]')
    ONLY_Y = (By.XPATH, '//div[@id="restrictedY"]')







