class Navigation:
    def __init__(self, app):
        self.app = app

    def go_to_project_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_overview_page.php")):
            # select drive in sidebar
            wd.find_element_by_xpath(f"//a[contains(@href,'/mantisbt-2.25.3/manage_overview_page.php')]").click()
            # select drive project in nav tabs
            wd.find_element_by_xpath(f"//a[contains(@href,'/mantisbt-2.25.3/manage_proj_page.php')]").click()
            # wait tab was active
            wd.find_element_by_xpath(f"//li[@class='active']/a[contains(@href,'/mantisbt-2.25.3/manage_proj_page.php')]")

