# DesireYang_web_test_v1
### ===>>web自动化项目框架搭建
## *Author：Desire*

### 环境：

- **python3.8**：项目环境
- **PyCharm**：项目编写工具
- **Typora**：Markdown编辑器
- **GitHub**：代码托管

### 项目中所用到的模块（pip install 库名）：

- **selenium**：与浏览器进行交互，web框架所需库
- **PyYAML**：YAML配置文件所需库
- **openpyxl**：操作excel所需库
- **pytest**：Pytest测试框架所需库
- **allure-pytest** ：pytest集成allure测试报告所需库
- **pytest-html** ：pytest生成HTML测试报告所需库
- **PyMySQL**：MySQL数据库所需库
- **jsonpath**：读取json格式所需库


### PO模式分层设计

- **[common](common)**：存放通用封装模块
  - ***[Base_Page.py](common/Base_Page.py)**：常用元素操作*
  - ***[Conf_Handle.py](common/Conf_Handle.py)**：操作配置文件(yaml/ini(config))模块*
  - ***[DB_Handle.py](common/DB_Handle.py)**：操作数据库模块*
  - ***[Email_Handle.py](common/Email_Handle.py)**：操作发送邮件模块*
  - ***[Excel_Handle.py](common/Excel_Handle.py)**：操作Excel表格模块*
  - ***[Func_Handle.py](common/Func_Handle.py)**：操作常用的功能函数模块*
  - ***[Logging_Handle.py](common/Logging_Handle.py)**：操作日志模块*
  - ***[Path_Handle.py](common/Path_Handle.py)**：操作项目路径模块*
- **[conf](conf)**：存放配置文件(.yaml/.ini/.config)
- **[data](data)**：存放数据(.xlsx/.yaml)
- **[drive](drive)**：存放浏览器驱动
- **[logs](logs)**：存放日志文件(.log)
- **[pages](pages)**：存放页面逻辑
  - **[Location](pages/Location)**：元素定位存放
- **[reports](reports)**：存放生成的测试报告
  - ***[allure](reports/allure)*：存放allure生成的测试报告**
  - ***[allure-plus](reports/allure-plus)*：存放allure升级版的测试报告（查看更加的方便，在PyCharm中可直接查看）**
- **[screenShot](screenShot)**：存放截图
- **[testcase](testcase)**：存放测试用例类
- **[conftest.py](conftest.py)**：存放pytest测试夹具
- **[pytest.ini](pytest.ini)**：pytest的配置文件(里面不要出现中文，否则有时候运行会报编码错误)
- **[run_test.py](run_test.py)**：整个项目的入口

### 第三方库导出文件
- **[pip3.8.txt](pip3.8.txt)**：所需第三方库导出文件，
#### 一键导出
```cmd
pip freeze >pip3.8.txt
```
#### 一键安装
```cmd
pip install -r pip3.8.txt
```
