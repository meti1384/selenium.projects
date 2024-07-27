from time import sleep
import mysql.connector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from anticaptchaofficial.recaptchav2proxyless import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


services=Service()
driver=webdriver.Edge(service=services)
action=ActionChains(driver)
driver.implicitly_wait(20)

def get_url(url):
    try:
        driver.get(url)
        result=driver.execute_script("return document.readyState")
        if result!="complete":
            raise Exception("site is not loaded!")
    except:
        sleep(12)

WEBSITE_KEY="6Ldfg4koAAAAABKRQfve_GSGoPGJadjdKTnakeeD"


def connect_to_database():
    connect_database=mysql.connector.connect(
        host="",
        user="",
        password="",
        database=""
    )

    cursor=connect_database.cursor()    
    cursor.execute("select * from url_plugins")
    result=cursor.fetchall()
    cursor.execute("delete from url_plugins")
    cursor.close()
    connect_database.commit()
    connect_database.close
    return result

def captchat_solve(url, website_key):
    solver = recaptchaV2Proxyless()
    solver.set_verbose(1)
    solver.set_key("c47fa5e7f23c36ab7ed95ac11bdf57af")
    solver.set_website_url(url)
    solver.set_website_key(website_key)

    g_response = solver.solve_and_return_solution()
    if g_response!= 0:
        print("g_response"+g_response)
    else:
        print("task finished with error"+solver.error_code)


    driver.execute_script('document.getElementById("g-recaptcha-response").innerHTML = "<g_response>";')
    sleep(2)
    driver.execute_script(f"___grecaptcha_cfg.clients[0].S.S.callback('{g_response}');")
    sleep(15)




def submit_login_data():
    driver.find_element(By.CSS_SELECTOR , "input#username").send_keys("phone_number")
    driver.find_element(By.CSS_SELECTOR, "button[class^=btn]").click()
    driver.find_element(By.CSS_SELECTOR , "input#password").send_keys("password")
    driver.find_element(By.XPATH, "//button[@class='btn btn--orange btn--full' and @type='submit']").click()



def login(url, website_key):
            
                try:
                    try:
                        driver.find_element(By.CSS_SELECTOR , "input#username")
                    except:
                        return
                      
                    driver.find_element(By.XPATH, "//iframe[@title='reCAPTCHA']")
                except:
                    submit_login_data()
                    return
                
                try:
                    captchat_solve(url, website_key)
                    submit_login_data()
                    sleep(4)
                    return

                except:

                    try:
                        driver.refresh()
                        captchat_solve(url, website_key)
                        submit_login_data()
                    
                    except:
                        
                            if driver.find_element(By.XPATH, "#__next > div.page-sign > div > div > div > div > div > div.form__wrap > div > div]"):
                                raise Exception("Maby captcha service have mistake! please run program again!")
                              
                            raise ("Maby the callback path expired(for fix this go to the this site https://discourse.openbullet.dev/t/guide-recaptcha-v2-bypass-and-callbacks/3252)")
                     


def save_product():
    save_product_button=driver.find_element(By.XPATH, "//button[text()='ذخیره محصول']")
    action.move_to_element(save_product_button).click().perform()
    WebDriverWait(driver, 50).until(
         EC.presence_of_element_located((By.XPATH, "//*[@class='main-alerts']"))
    )   


def check_update_notification():
    checkbox_element=driver.find_element(By.CSS_SELECTOR, "#update_notify")
    action.move_to_element(checkbox_element).click()
    sleep(4)
    save_product()



def main():
    links=connect_to_database()
    for link in links:
        get_url(link[0])
        sleep(15)
        login(link[0], WEBSITE_KEY)
        check_update_notification()
        sleep(4)

main()