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
        next_page_btn = driver.find_element_by_xpath('''(//*[contains(@class, 'sic_next') and contains(@title, 'Next Page') ])[3]''')

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
        next_page_btn.click() #click on the next page button

        sleep(20)
scrape_stock_data()