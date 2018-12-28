# 具体功能函数
# getDriver-返回driver
# getDate-返回当前日期
# getTime-返回当前时间
# get_size-返回屏幕大小
# choSwipe-滑动操作
# givePer-权限弹窗处理
# errPic-错误截图
# touchLong-长按操作
# resApp-重置应用


# !/usr/bin/python3
# Filename: assists.py
import subprocess
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
import time, os, random, string

# x = subprocess.run('appium &', shell=True)
# print(x)
# time.sleep(10)

# ===========配置参数=============

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = "7.0"
desired_caps['deviceName'] = "Q37500120MS10024148"
desired_caps['app'] = r'/Users/zhaojiaqi/Desktop/333.apk'
desired_caps['appPackage'] = 'com.injoin.social'
desired_caps['appActivity'] = 'com.injoin.social.ui.activity.StartPagerActivity'
desired_caps['automationName'] = 'UiAutomator2'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


# ===========具体函数=============

def getDriver():
    global driver
    return driver


def getDate():
    t = time.strftime("%Y%m%d", time.localtime())
    return t


def getTime():
    t = time.strftime("%H%M%S", time.localtime())
    return t


def get_size():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return x, y


def choSwipe(x):
    l = get_size()
    loc = random.randint(200,1500)
    chg = random.randint(0,500)
    x1 = int(l[0] * 0.22)
    x2 = int(l[0] * 0.52)
    x3 = int(l[0] * 0.84)
    y1 = int(l[1] * 0.75)
    y2 = int(l[1] * 0.90)
    y3 = int(l[1] * 0.50)
    y4 = int(l[1] * 0.25)
    if x == "down":
        driver.swipe(x1, y1, x1, y2, loc)
    elif x == "up":
        driver.swipe(x1, y2, x1, y1, chg)
    elif x == "upm":
        driver.swipe(x2, y2, x2, y1-chg, 1000)
    elif x == "upd":
        driver.swipe(x3, y2, x3, y1-chg, 1000)
    elif x == "upp":
        driver.swipe(x1, y3, x1, y4, 1000)
    elif x == "dop":
        driver.swipe(x1, y3, x1, y1, 500)


def givePer():
    try:
        while driver.find_element_by_id(
                'com.android.packageinstaller:id/permission_allow_button') or driver.find_element_by_id(
                'com.injoin.social:id/parentPanel'):
            try:
                driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
            except:
                driver.find_element_by_id('com.injoin.social:id/parentPanel').find_element_by_id(
                    'com.injoin.social:id/buttonPanel').find_element_by_id('android:id/button1').click()
                pass
    except:
        pass


def errPic():
    path = "/Users/zhaojiaqi/Documents/测试文件/" + getDate()
    if not os.path.exists(path):
        os.makedirs(path)
    path = path + '/' + getTime() + '-'
    driver.get_screenshot_as_file(path + 'err.png')


def touchLong(x):
    TouchAction(driver).long_press(x).perform()


def resApp():
    driver.reset()
    time.sleep(2)


def smName():
    i = "aaceeiimnstu"
    j = "DFGHJKLPQRWXYZ"
    a = random.randint(0, 13)
    b = random.randint(2, 5)
    c = ""
    for x in range(b):
        d = random.choice(i)
        c = c + d
    e = j[a] + c
    return e

def rt12():
    i = random.randint(1,4)
    if i % 2 == 0:
        return True
    else:
        return False

def saveAcc(acc, nic):
    fo = open("/Users/zhaojiaqi/Documents/account.txt", "a+")
    fo.write(acc + " " + nic + '\n')
    fo.close()

def rt14():
    i = random.randint(0,3)
    return i

def getToast(m):
    message = '//*[@text=\'{}\']'.format(m)
    toast_element = WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath(message))
    if toast_element.text == m:
        return True
    else:
        return False