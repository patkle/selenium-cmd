from cmd import Cmd
from shlex import split
try:
    from importlib import metadata
except ImportError:
    # Running on pre-3.8 Python; use importlib-metadata package
    import importlib_metadata as metadata

from selenium.webdriver import Chrome
from selenium.common.exceptions import InvalidArgumentException, NoSuchElementException
from selenium.webdriver.support.ui import Select
from parsel import Selector

def split_args(line):
    """split line in arguments"""
    # using @ in the first argument with posix=True will remove quotation marks
    # and therefore break most XPath expressions
    xpath = split(line, posix=False)[0]
    args = split(line)[1:]
    return xpath, args

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
        try:
            self.driver.get(url)
        except InvalidArgumentException:
            print(f'Could not navigate to {url}. Please check that you provided the full URL.')

    def do_click(self, xpath):
        """click [xpath]
        click element specified by given xpath expression"""
        e = self._find_element_by_xpath(xpath)
        e.click()

    def do_extract(self, xpath):
        """extract [xpath]
        display each element as string"""
        s = Selector(self.driver.page_source)
        try:
            for i, result in enumerate(s.xpath(xpath).getall(), 1):
                print(i, result)
        except ValueError as e:
            print(f'{e}. Please check your XPath expression.')

    def _find_element_by_xpath(self, xpath):
        try:
            return self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            print(f'Could not find element specified by {xpath}. Please check your XPath expression for errors.')

    def do_select(self, line):
        """select [xpath] [option]
        select option from select tag by value"""
        try:
            xpath, option = split_args(line)
            e = self._find_element_by_xpath(xpath)
            select = Select(e)
            select.select_by_value(option)
        except Exception as e:
            print(e)

    def do_exit(self, _):
        """exit
        stop execution of selenium-cmd"""
        return True

    def emptyline(self) -> None:
        # overwrite Cmd.emptyline to avoid default behaviour https://docs.python.org/3/library/cmd.html#cmd.Cmd.emptyline
        pass