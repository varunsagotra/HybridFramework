from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        chromebrowser = Service("/Users/purelifeonearth/Documents/Drivers/chromedriver")
        driver = webdriver.Chrome(service=chromebrowser)
        print("************Chrome Browser Initialized")
    elif browser == 'Safari':
        firefoxbrowser = Service("/Users/purelifeonearth/Documents/Drivers/firefox")
        driver = webdriver.firefox(service=firefoxbrowser)
        print("************Safari Browser Initialized")
    else:
        chromebrowser = Service("/Users/purelifeonearth/Documents/Drivers/chromedriver")
        driver = webdriver.Chrome(service=chromebrowser)
        print("**********Default Chrome Browser Initialized")

    return driver


def pytest_addoption(parser):  # This will get the value from CLI/hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")


###### Pytest HTML Report #########

# It is hook for adding environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = "Hybrid Testing"
    config._metadata['Module Name'] = "Login Module"
    config._metadata['Tester Name'] = "Varun"


# It is hook for delete/Modify environment info to HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
