
import jsonpickle
import os.path

import pytest

from fixture.application import Application

application = None
target = None


def load_config(file):
    global target
    if target is None:
        file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(file) as config_file:
            target = jsonpickle.decode(config_file.read())
    return target


@pytest.fixture()
def app(request):
    """ Fixture for work with class Application in each test function"""
    global application
    browser = request.config.getoption('--browser')
    web_config = load_config(request.config.getoption('--config_file'))['web']
    if application is None or application.is_not_valid():
        application = Application(browser=browser, base_url=web_config['base_url'])
    application.session.ensure_login(login=web_config['admin_login'], password=web_config['admin_password'])
    return application

@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def _inner():
        application.session.ensure_logout()
        application.wd_quit()
    request.addfinalizer(_inner)


def pytest_addoption(parser):
    parser.addoption("--browser", action='store', default='firefox', help='type of browser')
    parser.addoption("--config_file", action='store', default='config.json', help='file with config')

