import allure

from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage, DraggablePage


@allure.suite("Interactions")
class TestInteractions:
    @allure.feature("SortablePage")
    class TestSortablePage():
        @allure.title("Check Sortable")
        def test_sortable(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            list_before, list_after = sortable_page.change_list_order()
            grid_before, grid_after = sortable_page.change_grid_order()
            assert list_before != list_after, "the order of list has not been changed"
            assert grid_before != grid_after, "the order of grid has not been changed"

    @allure.feature("SelectablePage")
    class TestSelectablePage():
        @allure.title("Check Selectable")
        def test_selectable(self, driver):
            selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            item_list = selectable_page.select_list_item()
            item_grid = selectable_page.select_grid_item()
            assert len(item_list) > 0, "no elements were selected"
            assert len(item_grid) > 0, "no elements were selected"

    @allure.feature("ResizablePage")
    class TestResizablePage:

        @allure.title("Check Resizable")
        def test_resizable(self, driver):
            resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
            resizable_page.open()
            max_box, min_box = resizable_page.change_size_resizable_box()
            max_resize, min_resize = resizable_page.change_size_resizable()
            assert ('500px', '300px') == max_box, "maximum size not equal to '500px', '300px'"
            assert ('150px', '150px') == min_box, "minimum size not equal to '150px', '150px'"
            assert min_resize != max_resize, "resizable has not been changed"

    @allure.feature("DroppablePage")
    class TestDroppablePage:

        @allure.title("Check Simple Droppable")
        def test_simple_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            text = droppable_page.drop_simple()
            assert text == "Dropped!", "the element has not been dropped"

        @allure.title("Check Accept Droppable")
        def test_accept_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            not_accepted, accepted = droppable_page.drop_accept()
            assert not_accepted == "Drop here", "the dropped element has been accepted"
            assert accepted == "Dropped!", "the dropped element has not been accepted"

        @allure.title("Check Prevent Propogation Droppable")
        def test_prevent_propogation_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            not_greedy, not_greedy_inner, greedy, greedy_inner = droppable_page.drop_prevent_propogation()
            assert not_greedy == "Dropped!", "the element text has not been changed"
            assert not_greedy_inner == "Dropped!", "the element text has not been changed"
            assert greedy == "Outer droppable", "the element text has been changed"
            assert greedy_inner == "Dropped!", "the element text has not been changed"

        @allure.title("Check Revert Draggable Droppable")
        def test_revert_draggable_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            will_after_move, will_after_revert = droppable_page.drop_revert_draggable('will')
            not_will_after_move, not_will_after_revert = droppable_page.drop_revert_draggable('not_will')
            assert will_after_move != will_after_revert, "the element has not reverted"
            assert not_will_after_revert == not_will_after_move, "the element has reverted"

    @allure.feature("DraggablePage")
    class TestDraggablePage:
        @allure.title("Check Simple Draggable")
        def test_simple_draggable(self, driver):
            draggable_page = DraggablePage(driver, 'https://demoqa.com/dragabble')
            draggable_page.open()
            before, after = draggable_page.simple_drag_box()
            assert before != after, "The box position has not been changed"

        @allure.title("Check Axis Restricted Draggable")
        def test_axis_restricted_draggable(self, driver):
            draggable_page = DraggablePage(driver, 'https://demoqa.com/dragabble')
            draggable_page.open()
            draggable_page.axis_restricted_x()
            top_x, left_x = draggable_page.axis_restricted_x()
            top_y, left_y = draggable_page.axis_restricted_y()
            assert top_x[0][0] == top_x[1][0] and int(top_x[1][0]) == 0, "box position has not changed or box was moved by y axis"
            assert left_x[0][0] != left_x[1][0] and int(left_x[1][0]) != 0, "box position has not changed or box was moved by y axis"
            assert top_y[0][0] != top_y[1][0] and int(top_y[1][0]) != 0, "box position has not changed or box was moved by x axis"
            assert left_y[0][0] == left_y[1][0] and int(left_y[1][0]) == 0, "box position has not changed or box was moved by y axis"

