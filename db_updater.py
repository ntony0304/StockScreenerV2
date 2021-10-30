from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

""" real time data scrape to database """
def scrape_stock_data():

    #create option variable to hold setting for google chrome using Class Options
    options = Options()
    #options.add_argument("--headless") #run the google chrome without the GUI
    #create a variable that will represent the chrome driver
    with webdriver.Chrome(executable_path=r"C:\Users\quang nguyen\PycharmProjects\StockScreenerV2\chromedriver.exe", options=options) as driver:
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
    driver = webdriver.Chrome(executable_path=r"C:\Users\quang nguyen\PycharmProjects\StockScreenerV2\chromedriver.exe",
                              options=chrome_options)
    # login
    login(driver, "conceptnextinfo2@gmail.com", 123456, '''//*[@id="login_form"]/div[2]/div[1]/button''')
    # scrape_stock_data()
    url_to_scrape = "https://tradevsa.com/m/screener/eps"
    rows_xpath_to_scrape = '''//*[@id="screenerTable"]/tbody/tr'''
    scrape_stock_data_general(driver, url_to_scrape, rows_xpath_to_scrape, next_page_xpath=None)
    sleep(20)  # pause program for 20 sec
    driver.close()


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

    else: #the page doesn't have next page btn
        #just scrape 1 page
        rows = driver.find_elements_by_xpath(rows_xpath_to_scrape)  # get list of rows from the page
        for row in rows:  # Iterating over row by row
            #QTRLY EPS DATE |	TICKER	|STOCK CODE |	NAME |	ST TREND %	| LT TREND %
            #PRICE	|VOLUME|	TURNOVER	|MAIN INDUSTRY
            webelement_columns = row.find_elements_by_xpath("./td") #13 item
            eps_date = webelement_columns[0].text

            ticker_element = webelement_columns[1] #access the ticker web element
            ticker = ticker_element.find_element_by_xpath("./a").text #access the a tag inside the td and extract the text

            stock_code = webelement_columns[2].text
            company_name = webelement_columns[3].text
            st_trend_per = webelement_columns[4].text
            lt_trend_per = webelement_columns[5].text
            price = webelement_columns[6].text
            volume = webelement_columns[7].text
            turnover = webelement_columns[8].text
            industry = webelement_columns[9].text
            #    1  2  3  4   5   6  7  8  9  10
            print(
                "{} {} {} {} {}  {} {} {} {} {} ".format(eps_date, ticker, stock_code, company_name, st_trend_per, lt_trend_per,
                                                                   price, volume,turnover,industry
                                                                   ))
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