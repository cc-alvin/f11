from pyvirtualdisplay import Display
from selenium import webdriver
import time
import config
import schedule


def sign(text):
    display = Display(visible=1, size=(800, 600))
    display.start()
    browser = webdriver.Chrome()
    browser.get("https://www.51hack.cn/member.php?mod=logging&action=login")
    time.sleep(5)

    account = browser.find_element_by_name('username')
    password = browser.find_element_by_name('password')
    login = browser.find_element_by_name('loginsubmit')

    account.send_keys(config.f11_account)
    password.send_keys(config.f11_password)
    login.click()

    time.sleep(5)

    btn_qd = browser.find_element_by_xpath("//a[@href='plugin.php?id=dsu_paulsign:sign']/div/p")
    btn_qd.click()

    time.sleep(5)

    browser.refresh()
    face_kx = browser.find_element_by_id('kx')
    today_say = browser.find_element_by_id('todaysay')

    face_kx.click()
    today_say.send_keys(text)

    browser.execute_script("showWindow('qwindow', 'qiandao', 'post', '0');return false")

    time.sleep(10)
    browser.quit()
    display.stop()


if __name__ == '__main__':
    # 签到内容，默认为开心表情
    text = '我签到啦'

    schedule.every().days.at("12:01").do(sign, text)

    while True:
        schedule.run_pending()
        time.sleep(1)
