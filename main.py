from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

user_name = r'k-a-b1891'
user_password = r'QweQaz123'


def yandex_authorization(user_name: str, user_password: str):
    opt = Options()
    opt.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                     'Chrome/101.0.4951.41 Safari/537.36')
    opt.add_argument('--headless')

    driver = webdriver.Firefox(options=opt)
    wait = WebDriverWait(driver, 60)

    driver.get('https://passport.yandex.ru/auth/')
    try:
        login = wait.until(ec.presence_of_element_located((By.ID, 'passp-field-login')))
    except:
        driver.quit()
        return 'error'
    login.send_keys(user_name)
    button = driver.find_element(by=By.ID, value=r'passp:sign-in')
    button.click()

    try:
        password = wait.until(ec.presence_of_element_located((By.ID, 'passp-field-passwd')))
    except:
        driver.quit()
        return 'error'
    password.send_keys(user_password)
    button = driver.find_element(by=By.ID, value=r'passp:sign-in')
    button.click()

    try:
        wait.until(ec.visibility_of_element_located((By.CLASS_NAME, 'n-footer__rights')))
    except:
        pass

    return driver


if __name__ == '__main__':
    drv = yandex_authorization(user_name, user_password)
    title = drv.title
    drv.quit()
    print(title)


