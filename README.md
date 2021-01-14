# selenium-cmd
selenium-cmd is a small tool with which you can perform basic actions using a selenium webdriver object. Currently it only supports navigating to a website, selecting, clicking and extracting strings using XPath. 

## installation
You can simply use
```
pip install selenium-cmd
```

## usage
You can use the SeleniumCmd class wherever you want in your script.  
You can do so by importing SeleniumCmd from selenium_cmd.
```
from selenium_cmd import SeleniumCmd

SeleniumCmd(your_driver).cmdloop()
```
If you do not provide your own driver, SeleniumCmd will instantiate one using `Chrome()` from `selenium.webdriver`.  
This will open a prompt where you can type your commands looking like this:
```
selenium-cmd version 0.0.1
>
```

## commands
### get
With get you can navigate to different websites.  
The following will navigate to http://example.com:
```
>get http://example.com
```

### click
The `click` command will click the first element found specified by an XPath.  
The following example will click the first link on http://example.com:
```
>get http://example.com
>click //a
```

### extract
The `extract` command will print all elements matched by the provided XPath expression to your command line.  
The following example will print all quotes from https://quotes.toscrape.com/:
```
>get https://quotes.toscrape.com/
>extract //span[@class="text"]/text()
1 The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.
2 It is our choices, Harry, that show what we truly are, far more than our abilities.
3 There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.
4 The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.
5 Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.
6 Try not to become a man of success. Rather become a man of value.
7 It is better to be hated for what you are than to be loved for what you are not.
8 I have not failed. I've just found 10,000 ways that won't work.
9 A woman is like a tea bag; you never know how strong it is until it's in hot water.
10 A day without sunshine is like, you know, night.
```

### select
The syntax for the select command is: `select xpath option`  
The `select` command will select an option by value from a select tag. The select tag needs to be specified by an XPath expression.  
The following example will select the option "css" in the first select tag on https://www.w3docs.com/learn-html/html-select-tag.html:
```
>get https://www.w3docs.com/learn-html/html-select-tag.html
>select //select[@aria-label="Books"] css
```
