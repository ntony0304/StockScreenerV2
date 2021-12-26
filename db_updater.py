import random
import traceback
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from database import Database
from setting import Setting
import browser_action as br_act
import re

import logging


""" real time data scrape to database """
setting = Setting()
db = Database(setting)
def scrape_stock_data():

    #create option variable to hold setting for google chrome using Class Options
    options = Options()
    #options.add_argument("--headless") #run the google chrome without the GUI
    #create a variable that will represent the chrome driver
    with webdriver.Chrome(executable_path=r"C:\Users\Administrator\PycharmProjects\StockScreenerV2\chromedriver.exe", options=options) as driver:
        #driver.maximize_window()
        #open the website
        driver.get("https://www.shareinvestor.com/prices/stock_prices.html")

        #next page variable
        next_page_btn = driver.find_element_by_xpath(
            '''(//*[contains(@class, 'sic_next') and contains(@title, 'Next Page') ])[3]''')
        while next_page_btn != None:

            ''' scrape the data of the page '''
            rows = driver.find_elements_by_xpath('''//tbody/tr[contains(@id,'sic_pricesTable')]''') #get list of rows from the page
            for row in rows: #Iterating over row by row
                webelement_columns = row.find_elements_by_xpath("./td")
                name = webelement_columns[2].text
                rem = webelement_columns[3].text
                last_done = webelement_columns[4].text
                change = webelement_columns[5].text
                percent_change = webelement_columns[6].text
                volume = webelement_columns[7].text
                buy_volum = webelement_columns[8].text
                buy = webelement_columns[9].text
                sell = webelement_columns[10].text
                sell_volume = webelement_columns[11].text
                high = webelement_columns[12].text
                low = webelement_columns[13].text
                blot = webelement_columns[14].text
                      #2   3  4  5 6   7  8   9  10 11 12 13 14
                print("{} {} {} {} {}  {} {} {} {} {} {} {}   {}".format( name, rem, last_done,change,percent_change,volume,buy_volum,buy,
                                                                     sell, sell_volume,high,low,blot))
                #import to database . in database you have function to import corect data to correct label
            java_script_click(driver,next_page_btn)
        #next_page_btn.click() #click on the next page button

        sleep(20)

def wraper_for_scraping():
    from browser_action import login
    chrome_options = Options()
    # chrome_options.add_argument("--disable-notifications")  # disable the allow or disallow notification
    # # ''' codeBlock: disable automatic control to bypass cloudflare by remove navigator.webdriver flag
    # #            google chrome only'''
    # chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # chrome_options.add_experimental_option("useAutomationExtension", False)
    # chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    # options.add_argument("--headless") #run the google chrome without the GUI
    # create a variable that will represent the chrome driver
    driver = webdriver.Chrome(executable_path=r"C:\Users\Administrator\PycharmProjects\StockScreenerV2\chromedriver.exe",
                              options=chrome_options)
    # login
    login(driver, "conceptnextinfo2@gmail.com", 123456, '''//*[@id="login_form"]/div[2]/div[1]/button''')
    # scrape_stock_data()
    url_to_scrape = "https://tradevsa.com/m/screener/eps"
    rows_xpath_to_scrape = '''//*[@id="screenerTable"]/tbody/tr'''
    scrape_stock_data_general(driver, url_to_scrape, rows_xpath_to_scrape, next_page_xpath=None)
    sleep(20)  # pause program for 20 sec
    driver.close()

def wraper_for_scraping_stock_calendar(): #for url https://www.investingnote.com/stock_events/calendar?source=&country=my
    from browser_action import login
    chrome_options = Options()
    # chrome_options.add_argument("--disable-notifications")  # disable the allow or disallow notification
    # # ''' codeBlock: disable automatic control to bypass cloudflare by remove navigator.webdriver flag
    # #            google chrome only'''
    # chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # chrome_options.add_experimental_option("useAutomationExtension", False)
    # chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    # options.add_argument("--headless") #run the google chrome without the GUI
    # create a variable that will represent the chrome driver

    driver = webdriver.Chrome(executable_path=r"C:\Users\Administrator\PycharmProjects\StockScreenerV2\chromedriver.exe",
                              options=chrome_options)
    # login
    # login(driver, "conceptnextinfo2@gmail.com", 123456, '''//*[@id="login_form"]/div[2]/div[1]/button''')
    # scrape_stock_data()
    url_to_scrape = "https://www.investingnote.com/stock_events/calendar?source=&country=my"
    rows_xpath_to_scrape = '''//*[@id="events-calendar"]/div[2]/div/table/tbody/tr/td/div/div/div'''
    scrape_stock_calendar(driver, url_to_scrape, rows_xpath_to_scrape)
    sleep(20)  # pause program for 20 sec
    driver.close()
def scrape_stock_calendar(driver, url_to_scrape, rows_xpath_to_scrape, next_page_xpath=None):
    driver.get(url_to_scrape)

    # count=0
    # title_elements = driver.find_elements_by_xpath("//*[@class='fc-title']") #list of 1101 WebElements
    # print("element count", len(title_elements))
    # for element in title_elements:
    #     count+=1
    #     stock_data_text = element.text
    #     if stock_data_text is None or stock_data_text=='':
    #         stock_data_text = element.get_attribute("textContent")
    #     if stock_data_text: #if stock_data_text is not None
    #         try:
    #             splited= stock_data_text.split(" ")
    #             print(splited)
    #             first_column = splited[0] #'CCB'
    #             second_column = " ".join(splited[1:])#3Q Result
    #             print("column 1 = {}  \tcolumn 2= {}".format(first_column,second_column))
    #             print("count=",count)
    #             logging.debug("count={} column 1 = {}  \tcolumn 2= {}\n".format(count,first_column, second_column))
    #
    #         except:
    #             logging.info("error {}".format(traceback.format_exc()))
    #stock of each day
    list_monday = []
    list_tuesday = []
    list_wednesday = []
    list_thursday = []
    list_friday = []
    row_1 =[]
    row_2 = []
    row_3 =[]
    row_4 =[]
    #xpath for each week //*[@id="events-calendar"]/div[2]/div/table/tbody/tr/td/div/div/div
    #xpath for each row in one week //*[@id="events-calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[1]/div[2]/table/tbody/tr

    week_elements = driver.find_elements_by_xpath('//*[@id="events-calendar"]/div[2]/div/table/tbody/tr/td/div/div/div')
    for week_ele in week_elements: #iterating the each week
        rows_of_week = week_ele.find_elements_by_xpath('./div[2]/table/tbody/tr')
        for row_ele in rows_of_week:  #iterating each row of a week
            #xpath for 7 days //*[@id="events-calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[1]/div[2]/table/tbody/tr[1]/td
            #//*[@id="events-calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[1]/div[2]/table/tbody/tr[1]/td
            #//*[@id="events-calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[1]/div[2]/table/tbody/tr[1]/td[2]/a/div/span
            day_elements = row_ele.find_elements_by_xpath("./td")

            logging.info(f"date element {len(day_elements)}")
            try:
                list_monday.append(day_elements[0].find_element_by_xpath("./a/div/span").get_attribute("textContent"))
            except:
                pass
            try:
                list_tuesday.append(day_elements[1].find_element_by_xpath("./a/div/span").get_attribute("textContent"))
            except:
                pass
            try:
                list_wednesday.append(day_elements[2].find_element_by_xpath("./a/div/span").get_attribute("textContent"))
            except:
                pass
            try:
                list_thursday.append(day_elements[3].find_element_by_xpath("./a/div/span").get_attribute("textContent"))
            except:
                pass
            try:
                list_friday.append(day_elements[4].find_element_by_xpath("./a/div/span").get_attribute("textContent"))
            except:
                pass
        logging.info(list_monday)
        logging.info(list_tuesday)
        logging.info(list_wednesday)
        logging.info(list_thursday)
        logging.info(list_friday)
        break #finish week 1

""" real time data scrape to database """
def scrape_stock_data_general(driver, url_to_scrape , rows_xpath_to_scrape, next_page_xpath=None):

    #driver.maximize_window()
    #open the website
    driver.get(url_to_scrape)


    if next_page_xpath != None:
        # next page variable
        next_page_btn = driver.find_element_by_xpath(next_page_xpath)
        while next_page_btn != None:
            ''' scrape the data of the page '''
                                                   #//*[@id="screenerTable"]/tbody/tr[1]
            rows = driver.find_elements_by_xpath('''//tbody/tr[contains(@role,'row')]''') #get list of rows from the page
            for row in rows: #Iterating over row by row
                webelement_columns = row.find_elements_by_xpath("./td")
                code = webelement_columns[1].text
                name = webelement_columns[2].text
                st_trend_per = webelement_columns[3].text
                lt_trend_per = webelement_columns[4].text
                price = webelement_columns[5].text
                volume = webelement_columns[6].text
                turn_over = webelement_columns[7].text
                industry = webelement_columns[8].text
                qtrly_eps_date = webelement_columns[9].text
                      #2   3  4  5 6   7  8   9   #Code	Name	ST Trend %	LT Trend %	Price	Volume	Turnover	Main Industry	Qtrly EPS Date
                print("code: {}\nname: {}\nst_trend_per: {}\n lt_trend_per: {} \nprice{}\n volume {}\n turn_over: {}\n "
                      "industry {}\n qtrly_eps_date :{}\n".format( code, name,
                                                                   st_trend_per,
                                                                   lt_trend_per,price,
                                                                      volume,turn_over,
                                                                   industry,qtrly_eps_date))
                #import to database . in database you have function to import corect data to correct label
                db.insert_stock_data(code, name,
                                       st_trend_per,
                                       lt_trend_per,price,
                                          volume,turn_over,
                                       industry,qtrly_eps_date)

    else: #the page doesn't have next page btn
        #just scrape 1 page
        rows = driver.find_elements_by_xpath(rows_xpath_to_scrape)  # get list of rows from the page
        for row in rows:  # Iterating over row by row
            #QTRLY EPS DATE |	TICKER	|STOCK CODE |	NAME |	ST TREND %	| LT TREND %
            #PRICE	|VOLUME|	TURNOVER	|MAIN INDUSTRY
            webelement_columns = row.find_elements_by_xpath("./td") #13 item
            code = webelement_columns[1].text
            name = webelement_columns[2].text
            st_trend_per = webelement_columns[3].text
            lt_trend_per = webelement_columns[4].text
            price = webelement_columns[5].text
            volume = webelement_columns[6].text
            turn_over = webelement_columns[7].text
            industry = webelement_columns[8].text
            qtrly_eps_date = webelement_columns[9].text
            #    1  2  3  4   5   6  7  8  9  10
            print("code: {}\nname: {}\nst_trend_per: {}\n lt_trend_per: {} \nprice{}\n volume {}\n turn_over: {}\n "
                  "industry{}\n qtrly_eps_date :{}\n".format(code, name, st_trend_per,
                                                             lt_trend_per, price,
                                                             volume, turn_over, industry,
                                                             qtrly_eps_date))
def testing_scrape_button():
    print("this function scrape data from website to database")

def testing_scrape_return():
    return 10

#
# from browser_action import login
# chrome_options = Options()
# # chrome_options.add_argument("--disable-notifications")  # disable the allow or disallow notification
# # # ''' codeBlock: disable automatic control to bypass cloudflare by remove navigator.webdriver flag
# # #            google chrome only'''
# # chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
# # chrome_options.add_experimental_option("useAutomationExtension", False)
# # chrome_options.add_argument("--disable-blink-features=AutomationControlled")
#     #options.add_argument("--headless") #run the google chrome without the GUI
#     #create a variable that will represent the chrome driver
# driver = webdriver.Chrome(executable_path=r"C:\Users\quang nguyen\PycharmProjects\StockScreenerV2\chromedriver.exe", options=chrome_options)
# #login
# login(driver,"conceptnextinfo2@gmail.com", 123456, '''//*[@id="login_form"]/div[2]/div[1]/button''')
# #scrape_stock_data()
# url_to_scrape = "https://tradevsa.com/m/screener/eps"
# rows_xpath_to_scrape = '''//*[@id="screenerTable"]/tbody/tr'''
# scrape_stock_data_general(driver, url_to_scrape , rows_xpath_to_scrape, next_page_xpath=None)
# sleep(20) #pause program for 20 sec
# driver.close()