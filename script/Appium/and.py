# 基本说明：
# assists辅助函数集
# 初始化负责建立session，连接设备
# login-登陆
# sigin-注册
# home-首页弹窗权限处理
# filter-首页筛选
# chats-用户聊天
# profile-个人资料编辑


import time
import assists
import logging

# ===========日志配置===========
logging.basicConfig(filename='/Users/zhaojiaqi/Documents/测试文件/' + assists.getDate() + '.log',
                    level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] [%(funcName)s]: %(message)s',
                    datefmt='%Y-%m-%d %H:%M')

# ===========初始化=============

driver = assists.getDriver()
driver.implicitly_wait(5)

# ===========检查点=============
logging.info('Initialization is completed, to begin testing...')


def login(account):
    logging.info("check the agreements")
    driver.find_element_by_id('com.injoin.social:id/ll_login_facebook').click()  # 点击facebook
    driver.find_element_by_id('com.injoin.social:id/tv_login_protocol_terms').click()  # 点击协议1
    time.sleep(3)
    try:
        driver.find_element_by_xpath("//android.view.View[@text='Terms and Conditions']")
    except Exception as e:
        logging.error('Terms load failed')
    driver.back()
    driver.find_element_by_id('com.injoin.social:id/tv_login_protocol_privacy').click()  # 点击协议2
    time.sleep(3)
    try:
        driver.find_element_by_xpath("//android.view.View[@text='Our Commitment to You']")
    except Exception as e:
        logging.error('Privacy load failed')
    driver.back()
    logging.info("login with phone number " + str(account))
    driver.find_element_by_id('com.injoin.social:id/ll_login_mobile').click()  # 点击手机输入框
    driver.find_element_by_id('com.injoin.social:id/et_mobile_number').send_keys(account)  # 输入手机号码
    driver.find_element_by_id('com.injoin.social:id/btn_login_next').click()  # 点击Next
    if not assists.getToast("SMS verification code has been sent in " + str(account)):
        logging.error(
            'Failed to request SMS')
    driver.find_element_by_id('com.injoin.social:id/et_verification_code').send_keys('2333')  # 输入密码
    driver.find_element_by_id('com.injoin.social:id/btn_login_next').click()  # 点击Next

def sigin(nickname):
    logging.info('start to sigin')
    try:
        driver.find_element_by_id('com.injoin.social:id/iv_profile_avatar').click()  # 点击选择头像
    except Exception as e:
        logging.info('User has registered, login directly')
    assists.givePer()
    driver.find_element_by_id('com.injoin.social:id/tv_profile_take_photo').click()
    driver.find_element_by_id('com.android.camera:id/content').\
        find_element_by_id('com.android.camera:id/main_content').\
        find_element_by_id('com.android.camera:id/camera_bottom_bar').\
        find_element_by_id('com.android.camera:id/camera_shutter_middle_button').click()
    driver.find_element_by_id('com.android.camera:id/content').\
        find_element_by_id('com.android.camera:id/camera_bottom_save_cancel_container').\
        find_element_by_id('com.android.camera:id/save_btn').click()
    driver.find_element_by_id('com.google.android.apps.photos:id/cpe_save_button').click()
    driver.find_element_by_id('com.injoin.social:id/et_nick_name').send_keys(nickname)  # 添加昵称
    if assists.rt12():
        driver.find_element_by_id('com.injoin.social:id/tv_male').click()  # 选择性别
    else:
        driver.find_element_by_id('com.injoin.social:id/tv_female').click()  # 选择性别
    driver.find_element_by_id('com.injoin.social:id/et_birthday').click()  # 选择生日
    time.sleep(3)
    assists.choSwipe("down")
    assists.choSwipe("upm")
    assists.choSwipe("upd")
    driver.find_element_by_id('com.injoin.social:id/btnSubmit').click()
    driver.find_element_by_id('com.injoin.social:id/btn_done').click()  # 点击提交
    time.sleep(5)


def home():
    logging.info('start to home')
    time.sleep(5)
    loc = assists.get_size()
    driver.tap([(loc[0] * 0.5, loc[1] * 0.46)], 100)
    driver.tap([(loc[0] * 0.5, loc[1] * 0.56)], 100)
    driver.tap([(loc[0] * 0.5, loc[1] * 0.66)], 100)
    driver.tap([(loc[0] * 0.5, loc[1] * 0.76)], 100)
    assists.givePer()


def filter():
    logging.info('start to filter')
    driver.find_element_by_id('com.injoin.social:id/iv_screening').click()  # 点击筛选
    driver.find_element_by_id('com.injoin.social:id/rb_gender_male').click()  # 选择女性
    driver.swipe(85, 834, 200, 834, 1000)
    driver.swipe(640, 834, 500, 834, 1000)
    driver.find_element_by_id('com.injoin.social:id/tv_constellation').click()  # 点击星座
    driver.find_element_by_id('com.injoin.social:id/cb1').click()
    driver.find_element_by_id('com.injoin.social:id/cb3').click()
    driver.find_elements_by_xpath("//android.widget.TextView")[5].click()
    driver.find_elements_by_xpath("//android.widget.TextView")[6].click()
    driver.find_elements_by_xpath("//android.widget.TextView")[7].click()
    driver.find_element_by_id('com.injoin.social:id/iv_close').click()
    driver.find_element_by_id('com.injoin.social:id/btn_done').click()


def chats():
    try:
        driver.find_elements_by_xpath('//android.widget.ImageView')[1].click()
        name = driver.find_element_by_id('com.injoin.social:id/tv_name').text
        assists.choSwipe('upp')
        id = driver.find_element_by_id('com.injoin.social:id/tv_injoin_id').text
        logging.info('start chat with ' + name + "[" + id + "]")
    except Exception:
        logging.error('no anyone found')
        return True
    try:
        follow = driver.find_element_by_id('com.injoin.social:id/tv_follow')
        if follow:  # 判断是否关注
            follow.click()
    except Exception as e:
        print(e)
        pass
    driver.find_element_by_id('com.injoin.social:id/tv_chat').click()
    driver.find_element_by_id('com.injoin.social:id/emoji_button').click()
    driver.find_elements_by_xpath('//android.widget.ImageView')[-12].click()
    driver.find_element_by_id('com.injoin.social:id/editTextMessage').send_keys("Hello friend, do you like apple?")
    driver.find_element_by_id('com.injoin.social:id/buttonSendMessage').click()

    driver.find_element_by_id('com.injoin.social:id/buttonMoreFuntionInText').click()

    driver.find_element_by_id('com.injoin.social:id/viewPager').find_elements_by_class_name(
        'android.widget.ImageView')[1].click()
    assists.givePer()
    try:
        driver.find_element_by_id('com.injoin.social:id/viewPager').find_elements_by_class_name(
            'android.widget.ImageView')[1].click()
    except Exception:
        pass
    driver.find_elements_by_class_name('android.widget.TextView')[2].click()
    driver.find_element_by_id('com.injoin.social:id/record_btn').click()
    time.sleep(5)
    driver.find_element_by_id('com.injoin.social:id/record_btn').click()
    driver.find_element_by_id('com.injoin.social:id/easy_dialog_positive_btn').click()

    driver.find_element_by_id('com.injoin.social:id/viewPager').find_element_by_class_name(
        'android.widget.GridView').find_elements_by_class_name('android.widget.LinearLayout')[
        1].find_element_by_class_name('android.widget.RelativeLayout').click()
    driver.find_elements_by_class_name('android.widget.TextView')[1].click()

    driver.find_element_by_id('com.android.camera:id/camera_shutter_middle_button').click()
    driver.find_element_by_id('com.android.camera:id/save_btn').click()

    driver.find_element_by_id('com.injoin.social:id/buttonTextMessage').click()
    driver.find_element_by_id('com.injoin.social:id/editTextMessage').send_keys("It is a test message 😊")
    driver.find_element_by_id('com.injoin.social:id/buttonSendMessage').click()

    driver.find_element_by_id('com.injoin.social:id/buttonAudioMessage').click()
    record = driver.find_element_by_id('com.injoin.social:id/audioRecord')
    assists.touchLong(record)
    time.sleep(5)

    driver.find_element_by_id('com.injoin.social:id/buttonTextMessage').click()
    driver.find_element_by_id('com.injoin.social:id/editTextMessage').send_keys("यह सब अलविदा है 👋😊")
    driver.find_element_by_id('com.injoin.social:id/buttonSendMessage').click()

    driver.find_element_by_id('com.injoin.social:id/iv_back').click()
    time.sleep(2)
    assists.choSwipe('dop')
    # driver.find_element_by_id('com.injoin.social:id/relative_top').find_element_by_id('com.injoin.social:id/iv_canel_follow').click()
    # driver.find_element_by_xpath("//android.widget.TextView[@text='Unfollow']").click()
    # driver.find_element_by_id('com.injoin.social:id/md_buttonDefaultPositive').click()
    driver.find_element_by_id('com.injoin.social:id/relative_top').find_element_by_id(
        'com.injoin.social:id/iv_back').click()

def profile():
    logging.info('start to profile')
    #  测试验证

    logging.info("first edit")
    driver.find_element_by_id('com.injoin.social:id/iv_my').click()
    driver.find_element_by_id('com.injoin.social:id/tv_edit_profile').click()
    driver.find_element_by_id('com.injoin.social:id/nine_photo_wall_layout').find_elements_by_id(
        'com.injoin.social:id/iv_item_nine_photo_photo')[-1].click()
    assists.givePer()
    driver.find_element_by_id('com.injoin.social:id/tv_profile_take_photo').click()
    driver.find_element_by_id('com.android.camera:id/content').find_element_by_id(
        'com.android.camera:id/main_content').find_element_by_id(
        'com.android.camera:id/camera_bottom_bar').find_element_by_id(
        'com.android.camera:id/camera_shutter_middle_button').click()
    driver.find_element_by_id('com.android.camera:id/content').find_element_by_id(
        'com.android.camera:id/camera_bottom_save_cancel_container').find_element_by_id(
        'com.android.camera:id/save_btn').click()
    driver.find_element_by_id('com.google.android.apps.photos:id/cpe_save_button').click()
    driver.find_element_by_id('com.injoin.social:id/tv_nickname').click()
    oldnick = driver.find_element_by_id('com.injoin.social:id/et_content').text
    driver.find_element_by_id('com.injoin.social:id/et_content').clear()
    driver.find_element_by_id('com.injoin.social:id/et_content').send_keys('in45')
    driver.find_element_by_id('com.injoin.social:id/iv_save').click()
    driver.find_element_by_id('com.injoin.social:id/tv_birthdate').click()
    time.sleep(3)
    assists.choSwipe("down")
    driver.find_element_by_id('com.injoin.social:id/btnSubmit').click()
    driver.find_element_by_id('com.injoin.social:id/tv_gender').click()
    driver.find_element_by_id('com.injoin.social:id/tv_sign').click()
    oldwp = driver.find_element_by_id('com.injoin.social:id/et_content').text
    driver.find_element_by_id('com.injoin.social:id/et_content').clear()
    driver.find_element_by_id('com.injoin.social:id/et_content').send_keys(
        'Fly freely in your heart, and the brilliant stars will eternally linger. और शानदार सितारे हमेशा के लिए रुकेंगे। सड़क की दिशा मेरे दिल पर चमकता है, और दूर की सीमाएं मेरे साथ जाती हैं।')
    driver.find_element_by_id('com.injoin.social:id/iv_save').click()
    time.sleep(3)
    assists.choSwipe("up")
    driver.find_element_by_id('com.injoin.social:id/tv_relationship_status').click()
    rs = assists.rt14()
    driver.find_element_by_id('com.injoin.social:id/md_contentRecyclerView').find_elements_by_id(
        'com.injoin.social:id/md_title')[rs].click()
    time.sleep(3)
    assists.choSwipe("up")
    driver.find_element_by_id('com.injoin.social:id/et_introduce').click()
    oldint = driver.find_element_by_id('com.injoin.social:id/et_content').text
    driver.find_element_by_id('com.injoin.social:id/et_content').clear()
    driver.find_element_by_id('com.injoin.social:id/et_content').send_keys(
        'Fly freely in your heart, and the brilliant stars will eternally linger. The direction of the road shines on my heart, and the distant frontiers go with me.अपने दिल में स्वतंत्र रूप से उड़ें, और शानदार सितारे हमेशा के लिए रुकेंगे। सड़क की दिशा मेरे दिल पर चमकता है, और दूर की सीमाएं मेरे साथ जाती हैं।')
    driver.find_element_by_id('com.injoin.social:id/iv_save').click()
    driver.find_element_by_id('com.injoin.social:id/tv_save').click()
    driver.find_element_by_id('com.injoin.social:id/tv_canel').click()

    # 数据恢复
    logging.info('second edit')
    driver.find_element_by_id('com.injoin.social:id/tv_edit_profile').click()
    driver.find_element_by_id('com.injoin.social:id/nine_photo_wall_layout').find_elements_by_id(
        'com.injoin.social:id/iv_item_nine_photo_photo')[-2].click()
    driver.find_element_by_id('com.injoin.social:id/md_contentRecyclerView').find_elements_by_id(
        'com.injoin.social:id/md_title')[1].click()
    driver.find_element_by_id('com.injoin.social:id/tv_nickname').click()
    driver.find_element_by_id('com.injoin.social:id/et_content').clear()
    driver.find_element_by_id('com.injoin.social:id/et_content').send_keys(oldnick)
    driver.find_element_by_id('com.injoin.social:id/iv_save').click()
    driver.find_element_by_id('com.injoin.social:id/tv_birthdate').click()
    time.sleep(3)
    assists.choSwipe("up")
    driver.find_element_by_id('com.injoin.social:id/btnSubmit').click()
    driver.find_element_by_id('com.injoin.social:id/tv_gender').click()
    # driver.find_element_by_id('com.injoin.social:id/tv_sign').click()
    # driver.find_element_by_id('com.injoin.social:id/et_content').clear()
    # driver.find_element_by_id('com.injoin.social:id/et_content').send_keys(oldwp)
    # driver.find_element_by_id('com.injoin.social:id/iv_save').click()
    # time.sleep(3)
    # assists.choSwipe("down")
    # driver.find_element_by_id('com.injoin.social:id/tv_relationship_status').click()
    # driver.find_element_by_id('com.injoin.social:id/md_contentRecyclerView').find_elements_by_id('com.injoin.social:id/md_title')[1].click()
    # time.sleep(3)
    # assists.choSwipe("up")
    # driver.find_element_by_id('com.injoin.social:id/et_introduce').click()
    # driver.find_element_by_id('com.injoin.social:id/et_content').clear()
    # driver.find_element_by_id('com.injoin.social:id/et_content').send_keys(oldint)
    # driver.find_element_by_id('com.injoin.social:id/iv_save').click()
    driver.find_element_by_id('com.injoin.social:id/tv_save').click()
    driver.find_element_by_id('com.injoin.social:id/tv_canel').click()


# ===========脚本执行============


z = 0
for i in range(14, 500):
    z += 1
    account = "7777171" + str(i).zfill(3)
    nickname = assists.smName()
    logging.info("========This is the " + str(z) + " circle with the user " + account + "[" + nickname + "]========")
    try:
        login(account)
        sigin(nickname)
        assists.saveAcc(account, nickname)
    except Exception as e:
        pass

    try:
        home()
        chats()
        filter()
        chats()
        profile()
    except Exception as e:
        print(e)
        logging.error(e)
        assists.errPic()
        pass

    assists.resApp()
