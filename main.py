import os
import time

import pytest

if __name__ == '__main__':
    # pytest.main(['-v']) #输出更加详细的信息
    # pytest.main(['-s']) #输出调试信息
    # pytest.main(['-vs'])
    # pytest.main(['-vs','--n=2']) #多线程运行
    # pytest.main(['-vs','--reruns=2']) #失败用例重跑2次
    # pytest.main(['-vs','--./report.html']) #当前目录下生成测试报告
    pytest.main()  # 此时main里面的命令可以配置在pytest.ini里面
    time.sleep(3)
    os.system("allure generate ./temp -o ./reports --clean")  # 在reports下生成报告并清除以前存在的报告：index.html
