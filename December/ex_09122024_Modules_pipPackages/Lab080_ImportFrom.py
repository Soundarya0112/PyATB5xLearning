from BrowserPackage.OpenBrowser import start_browser #importing from package
from BrowserPackage.CloseBrowser import close_browser
class TestCase:
    def test_case(self):
        start_browser()
        print("Hello running test case")
        close_browser()
o1=TestCase()
o1.test_case()