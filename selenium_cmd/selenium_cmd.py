from cmd import Cmd
try:
    from importlib import metadata
except ImportError:
    # Running on pre-3.8 Python; use importlib-metadata package
    import importlib_metadata as metadata

from selenium.webdriver import Chrome
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from parsel import Selector

from .decorators import decorate_do_methods, exception_printer
from .argument_parser import split_args


@decorate_do_methods(exception_printer)
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
        navigate to url"""
        self.driver.get(url)

    def do_click(self, xpath):
        """click [xpath]
        click element specified by given xpath expression"""
        e = self._find_element_by_xpath(xpath)
        e.click()

    def do_extract(self, xpath):
        """extract [xpath]
        display each element as string"""
        s = Selector(self.driver.page_source)
        for i, result in enumerate(s.xpath(xpath).getall(), 1):
            print(i, result)

    def _find_element_by_xpath(self, xpath):
        try:
            return self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            print(f'Could not find element specified by {xpath}. Please check your XPath expression for errors.')

    def do_select(self, line):
        """select [xpath] [option]
        select option from select tag by value"""
        xpath, option = split_args(line)
        e = self._find_element_by_xpath(xpath)
        select = Select(e)
        select.select_by_value(option)

    def do_write(self, line):
        """write [xpath] [text] 
        write text to a text input field"""
        xpath, text = split_args(line)
        e = self._find_element_by_xpath(xpath)
        e.send_keys(text)

    def do_exit(self, _):
        """exit
        stop execution of selenium-cmd"""
        return True

    def emptyline(self) -> None:
        # overwrite Cmd.emptyline to avoid default behaviour https://docs.python.org/3/library/cmd.html#cmd.Cmd.emptyline
        pass
