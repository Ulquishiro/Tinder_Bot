import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

CORREO = "****"
CONTRA = "****"

# ------------SELENIUM DRIVER SET UP------------------#

chrome_driver_path = "C:/Users/ladg7/OneDrive/Documents/programacion/Chromedirver/chromedriver.exe"
service = Service(chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://tinder.com/")

time.sleep(5)
log_in = driver.find_element(By.XPATH, '//*[@id="u874623335"]/div/div[1]/div/main/div['
                                       '1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
time.sleep(1)
log_in.click()
time.sleep(5)
fb_button = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div[1]/div/div/div[3]/span/div['
                                          '2]/button/div[2]/div[2]/div/div')
fb_button.click()

time.sleep(0.5)
fb_login_window = driver.window_handles[1]
base_window = driver.window_handles[0]
driver.switch_to.window(fb_login_window)

e_mail = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/form/div/div[1]/div/input')
e_mail.send_keys(f"{CORREO}")
time.sleep(0.5)
password = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/form/div/div[2]/div/input')
password.send_keys(f"{CONTRA}")
time.sleep(1)
iniciar = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]/input')
iniciar.click()
driver.switch_to.window(base_window)

time.sleep(7)
ubicacion = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div/div[3]/button[1]/div[2]/div[2]')
ubicacion.click()
time.sleep(1)
interesa = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div/div[3]/button[2]/div[2]/div[2]')
interesa.click()
time.sleep(1)
acepto = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]')
acepto.click()
time.sleep(7)
like = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div['
                                     '3]/div/div[4]/button/span/span')
like.click()

comienzo = time.time()
final = comienzo + 60

while time.time() < final:
    try:
        time.sleep(3)
        like.click()
    except selenium.common.exceptions.ElementClickInterceptedException:
        no_me_interesa = driver.find_element(By.XPATH, '//*[@id="u-853757741"]/main/div/div[2]/button[2]/div[2]/div[2]')
        no_me_interesa.click()

