
#conceptnextinfo2@gmail.com
#123456


#function to login a website
def login(browser, user_id, user_pass, sign_in_btn_xpath):
    browser.get("https://tradevsa.com/m/")#open the login page
    #get the username input box
    #usernam xpath = //*[@id="login_form"]/div[1]/div[1]/input
    usernam_xpath = '''//*[@id="login_form"]/div[1]/div[1]/input'''
    pass_xpath = '''//*[@id="login_form"]/div[1]/div[2]/input'''
    # send username to the input field on the site
    send_text(browser, usernam_xpath, user_id)
    # send password to the input field on the site
    send_text(browser, pass_xpath, user_pass)

    #click the signin button
    java_script_click(browser, sign_in_btn_xpath)

def send_text(browser, xpath, text):
    input_box = browser.find_element_by_xpath(xpath)
    input_box.send_keys(text)

def java_script_click(browser_driver, btn_xpath):
    button = browser_driver.find_element_by_xpath(btn_xpath) #find the sign in button using its xpath
    browser_driver.execute_script("arguments[0].click();", button) #click that button
#
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# options = Options()
#     #options.add_argument("--headless") #run the google chrome without the GUI
#     #create a variable that will represent the chrome driver
# with webdriver.Chrome(executable_path=r"C:\Users\quang nguyen\PycharmProjects\StockScreenerV2\chromedriver.exe",
#                       options=options) as driver:
#     # conceptnextinfo2@gmail.com
#     # 123456
#     login(driver, "conceptnextinfo2@gmail.com", 123456)
#     #get the login button
#     login_button = driver.find_element_by_xpath('''//*[@id="login_form"]/div[2]/div[1]/button''')
#     #click login button
#     java_script_click(driver, login_button)
#     #open the page to scrape
#     driver.get("https://tradevsa.com/m/screener/eps")
#     sleep(20)
#     #perform scrape