from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class Poe:
    def __init__(self):
        s = Service('chromedriver_mac64/chromedriver')
        self.driver = webdriver.Chrome(service=s)
        self.driver.get("https://poe.com/ChatGPT")
        time.sleep(2)
    def getlatlng(self, cur_url):
        try:
            coords = re.search(r"@?\d{1,3}?\.\d{4,8},?\d{1,3}?\.\d{4,8},16z", cur_url).group()
            coord = coords.split('@')[1]

            lat = float(coord.split(',')[0])

            long = float(coord.split(',')[1])
            return [lat,long]
        except:
            return (-1000,-1000)
    def scrape(self):
            button = self.driver.find_element_by_class_name('Button_buttonBase__0QP_m Button_primary__pIDjn ChatMessageInputView_sendButton__reEpT')
            button.click()
            time.sleep(2.5)
            button.click()
            time.sleep(1.5)
            coords = self.getlatlng(self.driver.current_url)
            return [coords[0],coords[1]]