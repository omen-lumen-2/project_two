from random import randint

from model.project import Project


class ProjectHelper:
    def __init__(self, app):
        self.app = app
        self.project_cash = None

    def create(self, project):
        wd = self.app.wd
        # go to project page
        self.app.navigation.go_to_project_page()
        # move to create new project
        wd.find_element_by_xpath("//button[text()='Создать новый проект']").click()
        # fill contact group
        self.fill_project_form(project)
        # submit create project
        wd.find_element_by_xpath("//input[@value='Добавить проект']").click()
        # wait update screen
        wd.find_element_by_xpath("//button[text()='Создать новый проект']")
        # invalidate contact cash
        self.project_cash = None

    def fill_project_form(self, project):
        self.app.common_action.type_in_input_field_with_name(name="name", input_value=project.name)
        self.app.common_action.type_in_input_field_with_name(name="description", input_value=project.description)
        self.app.common_action.select_option_on_text(name_select='status', text="выпущен")
        self.app.common_action.select_option_on_text(name_select='view_state', text="приватный")


    def delete_project_by_id(self, id):
        wd = self.app.wd
        # go to project page
        self.app.navigation.go_to_project_page()
        # move to edit page for project by index
        wd.find_element_by_xpath(f"//a[contains(@href,'manage_proj_edit_page.php?project_id={id}')]").click()
        # select DELETE
        wd.find_element_by_xpath("//input[@value='Удалить проект']").click()
        # submit deleting on dialog
        wd.find_element_by_xpath("//input[@value='Удалить проект']").click()
        # wait update screen
        wd.find_element_by_xpath("//button[text()='Создать новый проект']")
        # invalidate contact cash
        self.project_cash = None

    def project_must_exist(self):
        # go to project page
        self.app.navigation.go_to_project_page()
        # create contact if contact not exist
        if self.get_count_project() == 0:
            self.create(project=Project(name=f'тест{randint(1,100)}'))

    def get_count_project(self):
        wd = self.app.wd
        return len(wd.find_elements_by_xpath(f"//a[contains(@href,'manage_proj_edit_page.php?project_id=')]"))

    def get_project_list(self):
        if self.project_cash is None:
            wd = self.app.wd
            # go to project page
            self.app.navigation.go_to_project_page()
            self.project_cash = []
            for elements in wd.find_elements_by_xpath(
                    "//html/body/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/table/tbody/tr"):
                id = int(elements.find_element_by_xpath("./td[1]/a").get_attribute('href').split("=")[1])
                name = elements.find_element_by_xpath("./td[1]").text
                state = elements.find_element_by_xpath("./td[2]").text
                is_active = True if len(elements.find_element_by_xpath("./td[3]").find_elements_by_xpath('*')) > 0 else False
                visible = elements.find_element_by_xpath("./td[4]").text
                description = elements.find_element_by_xpath("./td[5]").text
                self.project_cash.append(Project(id=id,
                                                 name=name,
                                                 state=state,
                                                 is_active=is_active,
                                                 use_global_setting=None,
                                                 visible=visible,
                                                 description=description))
        return self.project_cash.copy()





