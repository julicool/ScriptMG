
 基于python3.6，Django2.1.7，数据库mysql 8.0
 
##### 目录结构：

    auto: 主目录，存放h5，api和modal文件
    - templates:：存放html页面
    - api.py：存放后台接口
    - models.py：Django数据库文件
    - views.py：配置html关联到url
    
    autotest：存放程序路由文件和配置文件
    - settings：系统配置文件
    - urls：系统路由文件
    - common_static：存放静态文件

##### 数据库：
	1. 在settings.py文件中配置数据库连接信息（文件中的注释处）；
	2. 执行python manage.py makemigrations; python manage.py migrate;两个命令自动生成数据库表结构；
	3. 执行完成后需要手动维护sys_dict，手机品牌字典表。
	
##### 图片地址配置：
	手机图片存储在阿里云oss，如果需要调换地址，请修改以下几个地方：
	1. auto/api.py   阿里云oss配置部分
	2. auto/templates/auto/index.html  最下方js中的oss_host
	3. auto/models.py  mobileinfo表中的imgurl，default参数
	
##### 其它
    新部署项目请先注册admin账号，该账户默认拥有审核权限	
