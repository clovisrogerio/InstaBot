from selenium import webdriver
class WebDriver:
    def __init__(self):
        self.driver_path = 'chromedriver.exe' #put your chromedriver path here
        self.options = webdriver.ChromeOptions()
        self.options.add_argument = ('user-data-dir=Perfil')
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )

    def close_browser(self):
        self.chrome.quit()