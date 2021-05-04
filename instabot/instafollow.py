from web_driver import WebDriver
from selenium.webdriver.common.keys import Keys
from time import sleep




class InstaFollow(WebDriver):
    def __init__(self):
        super().__init__()


    def log_in(self):
        try:
            user = input(str('Insert your e-mail or your username:'))
            password = input(str('Insert your password:'))
            self.chrome.get('https://www.instagram.com/accounts/login/')
            sleep(5)
            input_login = self.chrome.find_element_by_name("username")
            sleep(3)
            input_password = self.chrome.find_element_by_name("password")
            self.chrome.implicitly_wait(2)
            input_login.send_keys(user)
            input_password.send_keys(password)
            input_password.send_keys(Keys.ENTER)
            sleep(8)


        except Exception as err:
            print('Error: ', err)

    def follow_by_url(self):
        click_number = 0
        try:
            target = input(str('Insert the username of the target page to get the followers:'))
            self.chrome.get('https://www.instagram.com/' + target)
            self.chrome.implicitly_wait(3)
            followers = self.chrome.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
            followers.click()
            sleep(5)
            button = self.chrome.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
            for n in range(40):
                self.chrome.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", button)
                sleep(1)
        except:
            pass
        all_buttons = self.chrome.find_elements_by_css_selector("li button")
        for button in all_buttons:
            if button.text == 'Seguir':
                button.click()
                sleep(20)
                click_number +=1
                print(f'{click_number} usuarios seguidos de 40...')
            if click_number >= 40:
                break







if __name__ == '__main__':
    chrome = InstaFollow()
    chrome.log_in()
    chrome.follow_by_url()
    chrome.close_browser()