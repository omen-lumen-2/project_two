from selenium import webdriver

from fixture.common_action import CommonAction
from fixture.navigation import Navigation
from fixture.project import ProjectHelper
from fixture.session import Session


class Application:
    def __init__(self, browser, base_url):
        if browser == 'firefox':
            self.wd = webdriver.Firefox()
        elif browser == 'chrome':
            self.wd = webdriver.Chrome()
        elif browser == 'ie':
            self.wd = webdriver.Ie()
        else:
            raise ValueError(f"Not support type of browser: {browser}. May be firefox, chrome, ie")
        self.base_url = base_url
        self.wd.implicitly_wait(4)
        self.session = Session(self)
        self.navigation = Navigation(self)
        self.common_action = CommonAction(self)
        self.project_helper = ProjectHelper(self)


    def wd_quit(self):
        self.wd.quit()

    def is_not_valid(self):
        try:
            self.wd.current_url
            return False
        except:
            return True



