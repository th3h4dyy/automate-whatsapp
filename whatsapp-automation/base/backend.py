from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--verbose")
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument("--window-size=1920, 1200")
    options.add_argument('--disable-dev-shm-usage')
    #options.add_argument('--profile-directory=other_profile')
    options.add_argument("--user-data-dir=./statics/profile")
    options.add_argument('--profile-directory=./statics/profile')
    options.add_argument("user-agent=User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36")
    driver = webdriver.Chrome(options=options)
    print("Your driver is running")
    return driver




driver = get_driver()
driver.get("https://web.whatsapp.com/")



while True:
    sleep(10)
    driver.save_screenshot("statics/qr.png")
    break



app = FastAPI()




def send_message(phone, message):
    driver.get(f"https://web.whatsapp.com/send/?phone={phone}&text={message}&type=phone_number&app_absent=0")
    i = True
    while i:
        try:
            driver.find_element(by=By.XPATH, value='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').click()
            i = False
            break
        except:
            sleep(1)
         
    




class Message(BaseModel):
    message: str
    phone: str



@app.post("/")
async def send_message_api(item: Message):
    send_message(item.phone, item.message)


@app.head("/status")
async def check_status():
    return 'ok';


app.mount("/static", StaticFiles(directory="statics"), name="static")