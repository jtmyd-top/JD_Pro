README.md
 # JD_Pro
**JD_Pro** is an automation tool designed to streamline and expedite the login process for JD.com users. This project is ideal for users who frequently need to log in to their JD accounts, such as shopping enthusiasts, market analysts, and developers.
**JD_Pro** 是一个用于简化和加速京东用户登录过程的自动化工具。这个项目主要面向需要频繁登录京东账户的用户，如购物狂热者、市场分析人员和开发者。

## Features / 功能特性
- **多账户支持**: 支持多个京东账户的管理和切换。
- **Secure Storage**: Encrypts and securely stores your username and password.
- **安全存储**: 使用加密技术存储用户信息，确保信息安全。

## Technology Stack / 技术架构
- **Python**: The core programming language used for development.
- **Python**: 项目使用的核心编程语言。
- **Requests**: Handles HTTP requests to communicate with JD servers.
- **Requests**: 用于处理与京东服务器通信的 HTTP 请求。
- **Selenium**: Simulates user browser behavior to handle complex interactions.
- **Selenium**: 模拟用户的浏览器行为，处理复杂的交互操作。
- **SQLite**: Lightweight database for storing user information and login logs.
- **SQLite**: 轻量级数据库，用于存储用户信息和登录日志。

## Prerequisites / 前提条件

Ensure you have the following installed:
确保你已安装以下内容：

- Python 3.x
- Git
- Apache2/nginx

## Python Dependencies / Python 依赖

Install the required Python packages using pip:
使用 pip 安装所需的 Python 包：

``` 
pip install -r requirements.txt

Setup and Deployment / 设置与部署
Follow these steps to set up and deploy JD_Pro:
按照以下步骤设置和部署 JD_Pro：
1. Clone the Repository / 克隆仓库
    git clone https://github.com/jtmyd-top/JD_Pro.git
    cd JD_Pro
2. Install Python Dependencies / 安装 Python 依赖
     pip install -r requirements.txt
3.配置数据库：
   推荐使用主流的京东代挂登录pro的数据库  路径一般为/root/Pro/DB/Pro.db
   需要在本项目proweb/settings.py中配置数据库路径等信息
4.配置青龙容器:
    需要在本项目proAppp/views.py中修改以下内容
        base_url = ""
        client_id = ""
        client_secret = ""
4.Migrate Django Database / 迁移 Django 数据库
    Make migrations /创建迁移文件:
        python3 manage.py makemigrations
    Apply migrations /应用迁移文件：
        python3 manage.py migrate
 5.测试服务/部署web服务：
     cd JD_Pro
     python3 ./manage.py runserver 0.0.0.0:8000
测试无bug后使用apache/nginx部署该应用

Contribution / 贡献
Contributions are welcome! Please fork this repository, make your changes, and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.
欢迎贡献！请 fork 这个仓库，做出你的修改，然后提交 pull request。如果有重大更改，请先开一个 issue 讨论你想修改的内容。

License / 许可证
This project is licensed under the MIT License - see the LICENSE file for details.
这个项目是根据 MIT 许可证授权的 - 详情请参见 LICENSE 文件。

By following these steps, you should be able to set up and deploy JD_Pro successfully. If you encounter any issues or need further assistance, please feel free to open an issue in the repository.
通过这些步骤，你应该能够成功设置和部署 JD_Pro。如果遇到任何问题或需要进一步的帮助，请随时在仓库中开 issue。

This `README.md` includes bilingual (English and Chinese) sections for a comprehensive understanding of the project, ensuring both English and Chinese-speaking users can effectively use and contribute to the project.
