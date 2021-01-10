from cmd import Cmd
try:
    from importlib import metadata
except ImportError:
    # Running on pre-3.8 Python; use importlib-metadata package
    import importlib_metadata as metadata

from selenium.webdriver import Chrome
from selenium.common.exceptions import InvalidArgumentException, NoSuchElementException
from parsel import Selector


class SeleniumCmd(Cmd):
    def __init__(self, driver=None) -> None:
        if driver is not None:
            self.driver = driver
        else:
            self.driver = Chrome()
        self.prompt = '>'
        self.intro = f'selenium-cmd version {metadata.version("selenium-cmd")}'
        super().__init__()

    def do_get(self, url):
        """get [url]
        navigate to provided url"""
        try:
            self.driver.get(url)
        except InvalidArgumentException:
            print(f'Could not navigate to {url}. Please check that you provided the full URL.')

    def do_click(self, xpath):
        """click [xpath]
        click element specified by given xpath expression"""
        try:
            e = self.driver.find_element_by_xpath(xpath)
            e.click()
        except NoSuchElementException:
            print(f'Could not find element specified by {xpath}. Please check your XPath expression for errors.')

    def do_extract(self, xpath):
        """extract [xpath]
        displays each matched element as string"""
        s = Selector(self.driver.page_source)
        try:
            for i, result in enumerate(s.xpath(xpath).getall(), 1):
                print(i, result)
        except ValueError as e:
            print(f'{e}. Please check your XPath expression.')
