1、终端里面执行如下命令，安装依赖：
cd 当前目录名称
pip install -r requirements.txt

2、由于登录存在加密，无接口文档，过程不清楚，该部分未做自动化，采用手动提取鉴权码Authorization形式，提取方法如下：
 1）登录该系统
 2）f12，任意查看一个接口的Headers->Response Headers,将Authorization和它的值复制到项目/data/cookie/cookie.yml中即可
 3）yml中的鉴权码是键值对形式，键值间有一个空格，如  key: value

3、如何切换所要测试的环境地址
 1）修改项目/pytest.ini文件中的base_url地址即可

windows下运行：
1、运行main.py
2、浏览器打开：项目/reports/index.html即可查看测试报告


*****