
class Session:
    def __init__(self, app):
        self.app = app

    def login(self, login, password):
        app = self.app
        wd = app.wd
        # open authorize page
        wd.get(self.app.base_url)
        # input login
        app.common_action.type_in_input_field_with_name(name="username", input_value=login)
        # submit inputed login
        wd.find_element_by_xpath("//input[@value='Вход']").click()
        # input password
        app.common_action.type_in_input_field_with_name(name="password", input_value=password)
        # submit
        wd.find_element_by_xpath("//input[@value='Вход']").click()

    def logout(self):
        wd = self.app.wd
        # call dropdown menu
        wd.find_element_by_xpath("//span[@class='user-info']").click()
        # select logout
        wd.find_element_by_link_text("Выход").click()
        wd.find_element_by_name("username")

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_xpath("//div[@id='navbar']")) > 0

    def is_logged_as(self, user_name):
        wd = self.app.wd
        return wd.find_element_by_xpath("//span[@class='user-info']").text == f"({user_name})"

    def ensure_login(self, login, password):
        if self.is_logged_in():
            if self.is_logged_as(user_name=login):
                return
            else:
                self.logout()
        self.login(login=login, password=password)

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()


