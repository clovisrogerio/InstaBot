from instafollow import InstaFollow
from web_driver import WebDriver
print('Welcome to InstaBot')
while True:
    menu = ['[Exit]', '[Likes]']
    for i , lista in enumerate(menu):
        print (i,lista)
    choice = int(input('Select a function:'))

    if choice == 0:
        break
    elif choice == 1:

        chrome = InstaFollow()
        chrome.log_in()
        chrome.follow_by_url()
        chrome.close_browser()
    else:
        print('Opção invalida')
