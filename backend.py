from get_driver import get_driver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel





driver = get_driver()
driver.get("https://web.whatsapp.com/")



while True:
    sleep(10)
    driver.save_screenshot("static/qr.png")
    break

app = FastAPI()


def send_message(phone, message):
    driver.get(f"https://api.whatsapp.com/send/?phone={phone}&text={message}&type=phone_number&app_absent=0")
    driver.save_screenshot("static/send.png")
    sleep(5)


    try:  
        pre_screen = driver.find_element(by=By.ID, value="main_block").find_element(by=By.TAG_NAME, value="a")
        pre_screen.click()
        sleep(5)
        
        pre_screen_two = driver.find_element(by=By.XPATH, value='//*[@id="fallback_block"]/div/div/h4[2]/a')
        pre_screen_two.click()
        sleep(20)
        last_send_message()
        driver.save_screenshot("static/last_one.png")
     
    except NoSuchElementException:
      try:
        pre_screen_two = driver.find_element(by=By.XPATH, value='//*[@id="fallback_block"]/div/div/h4[2]/a')
        pre_screen_two.click()
        sleep(20)
        last_send_message()
        driver.save_screenshot("static/last_one.png")
      except NoSuchElementException:
         last_send_message()
         driver.save_screenshot("static/last_one.png")
         
    

def last_send_message():
    try:
        driver.find_element(by=By.XPATH, value='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').click()
        sleep(5)
    except:
      global app
      app = FastAPI()
    



class Message(BaseModel):
    message: str
    phone: str



@app.post("/")
async def send_message_api(item: Message):
    send_message(item.phone, item.message)


app.mount("/static", StaticFiles(directory="static"), name="static")