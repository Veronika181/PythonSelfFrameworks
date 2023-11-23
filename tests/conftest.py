# jak zobecnit kód vyvolání prohlížeče

import pytest  # importuje potřebné modily pro ovládání webového prohlížeče
from selenium import webdriver
global driver  # inicializuje globální proměnnou driver na None. Slouží k cuhování instance webového prohlížeče


def pytest_addoption(
        parser):  # definuje volbu --browser_name pro framework pytest, která umožnuje specifikovat, který webový přohlížeč má být použit.
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(
    scope="class")  # definuje pytest fixture setup s rozcasehm scope, spustí jednou pro každou testovací třídu
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")  # na začátku metody se podle hodnoty volby inicializuje instance webového prohlížeče(Chrome, Firefo nebo IE)
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()  # otevře zadanou webovou stránku a maximilozuje okno prohlížeče

    request.cls.driver = driver  # přidává odkaz na instanci weobvého voladače do testovací třídy pomocí request.cls.driver
    yield  # slouží jako oddělovat, který umožnuje provést test před a po provdení testu
    driver.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, rep=None):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
            report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)



