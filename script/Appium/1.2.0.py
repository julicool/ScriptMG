import time
import assists
import logging

# ===========日志配置===========
logging.basicConfig(filename='/Users/zhaojiaqi/Documents/AppiumTest/Android/Logs/' + assists.getDate() + '.log',
                    level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] [%(funcName)s]: %(message)s',
                    datefmt='%Y-%m-%d %H:%M')

# ===========初始化=============

driver = assists.getDriver()
driver.implicitly_wait(15)

# ===========检查点=============

def login():
    logging.info("登陆验证")
    driver.find_element_by_id("com.injoin.social:id/tv_next").click()
    driver.find_element_by_id("com.injoin.social:id/tv_back").click()
    driver.find_element_by_id("com.injoin.social:id/tv_next").click()
    driver.find_element_by_id("com.injoin.social:id/tv_next").click()
    driver.find_element_by_id("com.injoin.social:id/id_tv_open").click()

    logging.info("检查terms协议")
    driver.find_element_by_id('com.injoin.social:id/tv_login_protocol_terms').click()
    try:
        driver.find_element_by_xpath("//android.view.View[@text='Terms and Conditions']")
    except:
        logging.error('Terms加载失败')
    driver.back()

    logging.info("检查privacy协议")
    driver.find_element_by_id('com.injoin.social:id/tv_login_protocol_privacy').click()
    try:
        driver.find_element_by_xpath("//android.view.View[@text='Our Commitment to You']")
    except Exception as e:
        logging.error('Privacy加载失败')
    driver.back()

    logging.info("使用手机号6100000001登陆")
    driver.find_element_by_id('com.injoin.social:id/rl_login_mobile').click()
    driver.find_element_by_id('com.injoin.social:id/et_mobile_number').send_keys("6100000001")
    driver.find_element_by_id('com.injoin.social:id/btn_login_next').click()
    driver.find_element_by_id('com.injoin.social:id/et_verification_code').send_keys('2333')
    driver.find_element_by_id('com.injoin.social:id/btn_login_next').click()

def home():
    logging.info('进入主页')
    time.sleep(5)
    loc = assists.get_size()
    driver.tap([(loc[0] * 0.5, loc[1] * 0.46)], 100)
    driver.tap([(loc[0] * 0.5, loc[1] * 0.56)], 100)
    driver.tap([(loc[0] * 0.5, loc[1] * 0.66)], 100)
    driver.tap([(loc[0] * 0.5, loc[1] * 0.76)], 100)
    assists.givePer()

def filter():
    logging.info("附近人筛选")
    driver.find_element_by_id('com.injoin.social:id/iv_screening').click()
    driver.find_element_by_id('com.injoin.social:id/rb_gender_male').click()
    driver.swipe(85, 834, 200, 834, 1000)
    driver.swipe(640, 834, 500, 834, 1000)
    driver.find_element_by_id('com.injoin.social:id/tv_constellation').click()
    driver.find_element_by_id('com.injoin.social:id/cb1').click()
    driver.find_element_by_id('com.injoin.social:id/cb3').click()
    driver.find_elements_by_xpath("//android.widget.TextView")[5].click()
    driver.find_elements_by_xpath("//android.widget.TextView")[6].click()
    driver.find_elements_by_xpath("//android.widget.TextView")[7].click()
    driver.find_element_by_id('com.injoin.social:id/iv_close').click()
    driver.find_element_by_id('com.injoin.social:id/btn_done').click()

def chats():
    driver.find_elements_by_xpath('//android.widget.ImageView')[7].click()
    name = driver.find_element_by_id('com.injoin.social:id/tv_nickname').text
    assists.choSwipe('up')
    logging.info("和" + name + "进行聊天")

    try:
        follow = driver.find_element_by_id('com.injoin.social:id/rl_follow_button')
        if follow:  # 判断是否关注
            follow.click()
    except Exception as e:
        pass

    driver.find_element_by_id('com.injoin.social:id/rl_chat_button').click()
    driver.find_element_by_id('com.injoin.social:id/emoji_button').click()
    driver.find_elements_by_xpath('//android.widget.ImageView')[-12].click()
    driver.find_element_by_id('com.injoin.social:id/editTextMessage').send_keys("Hello friend, do you like apple?")
    driver.find_element_by_id('com.injoin.social:id/buttonSendMessage').click()
    driver.find_element_by_id('com.injoin.social:id/buttonMoreFuntionInText').click()
    driver.find_element_by_id('com.injoin.social:id/viewPager').find_elements_by_class_name('android.widget.ImageView')[1].click()
    assists.givePer()

    try:
        driver.find_element_by_id('com.injoin.social:id/viewPager').find_elements_by_class_name('android.widget.ImageView')[1].click()
    except Exception:
        pass

    logging.info("录像")
    driver.find_elements_by_class_name('android.widget.TextView')[2].click()
    driver.find_element_by_id('com.injoin.social:id/record_btn').click()
    driver.find_element_by_id('com.injoin.social:id/record_btn').click()
    driver.find_element_by_id('com.injoin.social:id/easy_dialog_positive_btn').click()

    logging.info("拍照")
    driver.find_element_by_id('com.injoin.social:id/viewPager').find_elements_by_class_name('android.widget.RelativeLayout')[-1].click()
    driver.find_element_by_xpath("//android.widget.TextView[@text='Take a photo']").click()
    driver.find_element_by_id('com.android.camera:id/camera_shutter_middle_button').click()
    driver.find_element_by_id('com.android.camera:id/save_btn').click()

    logging.info("文字表情")
    driver.find_element_by_id('com.injoin.social:id/buttonTextMessage').click()
    driver.find_element_by_id('com.injoin.social:id/editTextMessage').send_keys("It is a test message 😊")
    driver.find_element_by_id('com.injoin.social:id/buttonSendMessage').click()

    logging.info("录音")
    driver.find_element_by_id('com.injoin.social:id/buttonAudioMessage').click()
    record = driver.find_element_by_id('com.injoin.social:id/audioRecord')
    assists.touchLong(record)

    logging.info("印地文")
    driver.find_element_by_id('com.injoin.social:id/buttonTextMessage').click()
    driver.find_element_by_id('com.injoin.social:id/editTextMessage').send_keys("यह सब अलविदा है 👋😊")
    driver.find_element_by_id('com.injoin.social:id/buttonSendMessage').click()

    logging.info("返回")
    driver.press_keycode(4)
    driver.press_keycode(4)

    logging.info("取关")
    driver.find_element_by_id('com.injoin.social:id/iv_more').click()
    driver.find_element_by_xpath("//android.widget.TextView[@text='Unfollow']").click()
    driver.find_element_by_id('com.injoin.social:id/md_buttonDefaultPositive').click()
    time.sleep(5)
    driver.press_keycode(4)

def profile():
    logging.info('进入个人中心页面')
    driver.find_element_by_id('com.injoin.social:id/iv_my').click()

    logging.info("进入编辑")
    driver.find_element_by_id('com.injoin.social:id/tv_edit_profile').click()

    logging.info("上传背景图片")
    try:
        driver.find_element_by_id('com.injoin.social:id/nine_photo_wall_layout').find_elements_by_id('com.injoin.social:id/iv_item_nine_photo_photo')[-1].click()
        assists.givePer()
        driver.find_element_by_id('com.injoin.social:id/tv_profile_take_photo').click()
        driver.find_element_by_id('com.android.camera:id/content').find_element_by_id('com.android.camera:id/main_content').find_element_by_id('com.android.camera:id/camera_bottom_bar').find_element_by_id('com.android.camera:id/camera_shutter_middle_button').click()
        driver.find_element_by_id('com.android.camera:id/content').find_element_by_id('com.android.camera:id/camera_bottom_save_cancel_container').find_element_by_id('com.android.camera:id/save_btn').click()
        driver.find_element_by_id('com.google.android.apps.photos:id/cpe_save_button').click()
    except:
        logging.error("未找到图片添加按钮")

    logging.info("编辑昵称")
    driver.find_element_by_id('com.injoin.social:id/tv_nickname').click()
    oldnick = driver.find_element_by_id('com.injoin.social:id/et_content_with_delete').text
    driver.find_element_by_id('com.injoin.social:id/et_content_with_delete').clear()
    driver.find_element_by_id('com.injoin.social:id/et_content_with_delete').send_keys('Kapil Seema')
    driver.find_element_by_id('com.injoin.social:id/tv_save').click()

    logging.info("编辑生日")
    driver.find_element_by_id('com.injoin.social:id/linear_birthdate').click()
    time.sleep(5)
    assists.choSwipe("down")
    driver.find_element_by_id('com.injoin.social:id/btnSubmit').click()
    time.sleep(5)
    assists.choSwipe("up")

    logging.info("编辑签名")
    driver.find_element_by_id('com.injoin.social:id/linear_sign').click()
    oldwp = driver.find_element_by_id('com.injoin.social:id/et_content').text
    driver.find_element_by_id('com.injoin.social:id/et_content').clear()
    driver.find_element_by_id('com.injoin.social:id/et_content').send_keys('The best thing to do first thing in the morning is go right back to sleep.')
    driver.find_element_by_id('com.injoin.social:id/tv_save').click()
    time.sleep(5)
    assists.choSwipe("up")

    logging.info("编辑居住地")
    driver.find_element_by_id("com.injoin.social:id/linear_location").click()
    time.sleep(5)
    driver.find_elements_by_class_name("android.widget.LinearLayout")[2].click()
    driver.find_elements_by_class_name("android.widget.RelativeLayout")[0].click()
    driver.find_element_by_id("com.injoin.social:id/tv_save").click()
    time.sleep(5)
    assists.choSwipe("up")

    logging.info("编辑学校")
    driver.find_element_by_id("com.injoin.social:id/linear_school").click()
    driver.find_element_by_id("com.injoin.social:id/ll_school").click()
    driver.find_element_by_id("com.injoin.social:id/et_search").send_keys("aad")
    driver.find_elements_by_class_name("android.widget.RelativeLayout")[0].click()
    driver.find_element_by_id("com.injoin.social:id/ll_from").click()
    driver.find_element_by_id("com.injoin.social:id/btnSubmit").click()
    driver.find_element_by_id("com.injoin.social:id/tv_save").click()

    logging.info("编辑工作")
    driver.find_element_by_id("com.injoin.social:id/linear_job_title").click()
    oldjob = driver.find_element_by_id("com.injoin.social:id/et_content_with_delete").text
    driver.find_element_by_id("com.injoin.social:id/et_content_with_delete").clear()
    driver.find_element_by_id("com.injoin.social:id/et_content_with_delete").send_keys("astronaut")
    driver.find_element_by_id("com.injoin.social:id/tv_save").click()

    logging.info("编辑公司")
    driver.find_element_by_id("com.injoin.social:id/linear_company").click()
    oldcompany = driver.find_element_by_id("com.injoin.social:id/et_content_with_delete").text
    driver.find_element_by_id("com.injoin.social:id/et_content_with_delete").clear()
    driver.find_element_by_id("com.injoin.social:id/et_content_with_delete").send_keys("..")
    driver.find_element_by_id("com.injoin.social:id/tv_save").click()

    logging.info("编辑情感状态")
    driver.find_element_by_id('com.injoin.social:id/linear_relationship_status').click()
    driver.find_element_by_id('com.injoin.social:id/md_contentRecyclerView').find_elements_by_id('com.injoin.social:id/md_title')[assists.rt14()].click()
    time.sleep(5)

    logging.info("编辑标签")
    driver.find_element_by_id("com.injoin.social:id/linear_tags").click()
    time.sleep(5)
    driver.find_elements_by_class_name("android.widget.FrameLayout")[1].click()
    driver.find_element_by_id("com.injoin.social:id/tv_save").click()

    logging.info("编辑Introduction")
    driver.find_element_by_id("com.injoin.social:id/linear_introduction").click()
    oldint = driver.find_element_by_id('com.injoin.social:id/et_content').text
    driver.find_element_by_id('com.injoin.social:id/et_content').clear()
    driver.find_element_by_id('com.injoin.social:id/et_content').send_keys(
        'अपने दिल में स्वतंत्र रूप से उड़ें, और शानदार सितारे हमेशा के लिए रुकेंगे। सड़क की दिशा मेरे दिल पर चमकता है, और दूर की सीमाएं मेरे साथ जाती हैं।...')
    driver.find_element_by_id('com.injoin.social:id/tv_save').click()
    driver.press_keycode(4)
    time.sleep(5)
    driver.press_keycode(4)
    time.sleep(5)


    logging.info("删除背景照片")
    driver.find_element_by_id('com.injoin.social:id/tv_edit_profile').click()
    try:
        while driver.find_element_by_id('com.injoin.social:id/nine_photo_wall_layout').find_elements_by_id('com.injoin.social:id/iv_item_nine_photo_flag')[-1]:
            driver.find_element_by_id('com.injoin.social:id/nine_photo_wall_layout').find_elements_by_id('com.injoin.social:id/iv_item_nine_photo_flag')[-1].click()
    except:
        pass

    logging.info("恢复昵称")
    driver.find_element_by_id('com.injoin.social:id/tv_nickname').click()
    driver.find_element_by_id('com.injoin.social:id/et_content_with_delete').clear()
    driver.find_element_by_id('com.injoin.social:id/et_content_with_delete').send_keys(oldnick)
    driver.find_element_by_id('com.injoin.social:id/tv_save').click()

    logging.info("恢复生日")
    driver.find_element_by_id('com.injoin.social:id/linear_birthdate').click()
    time.sleep(3)
    assists.choSwipe("up")
    driver.find_element_by_id('com.injoin.social:id/btnSubmit').click()
    time.sleep(5)
    assists.choSwipe("up")

    logging.info("恢复签名")
    driver.find_element_by_id('com.injoin.social:id/linear_sign').click()
    driver.find_element_by_id('com.injoin.social:id/et_content').clear()
    driver.find_element_by_id('com.injoin.social:id/et_content').send_keys(oldwp)
    driver.find_element_by_id('com.injoin.social:id/tv_save').click()
    time.sleep(5)
    assists.choSwipe("up")

    logging.info("恢复工作")
    driver.find_element_by_id("com.injoin.social:id/linear_job_title").click()
    driver.find_element_by_id("com.injoin.social:id/et_content_with_delete").clear()
    driver.find_element_by_id("com.injoin.social:id/et_content_with_delete").send_keys(oldjob)
    driver.find_element_by_id("com.injoin.social:id/tv_save").click()

    logging.info("恢复公司")
    driver.find_element_by_id("com.injoin.social:id/linear_company").click()
    driver.find_element_by_id("com.injoin.social:id/et_content_with_delete").clear()
    driver.find_element_by_id("com.injoin.social:id/et_content_with_delete").send_keys(oldcompany)
    driver.find_element_by_id("com.injoin.social:id/tv_save").click()
    time.sleep(5)
    assists.choSwipe("up")

    logging.info("恢复Introduction")
    driver.find_element_by_id("com.injoin.social:id/linear_introduction").click()
    driver.find_element_by_id('com.injoin.social:id/et_content').clear()
    driver.find_element_by_id('com.injoin.social:id/et_content').send_keys(oldint)
    driver.find_element_by_id('com.injoin.social:id/tv_save').click()
    driver.press_keycode(4)

# ===========脚本执行============


try:
    login()
    home()
    # filter()
    # chats()
    profile()
except Exception as e:
    print(e)
    logging.error(e)
    assists.errPic()

logging.info("执行完成")
assists.resApp()
