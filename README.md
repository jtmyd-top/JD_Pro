### README.md

```markdown
# JD_Pro

**JD_Pro** is an automation tool designed to streamline and expedite the login process for JD.com users. This project is ideal for users who frequently need to log in to their JD accounts, such as shopping enthusiasts, market analysts, and developers.

**JD_Pro** 是一个用于简化和加速京东用户登录过程的自动化工具。这个项目主要面向需要频繁登录京东账户的用户，如购物狂热者、市场分析人员和开发者。

## Features / 功能特性

- **Automatic Login**: Quickly log in to your JD account by automatically entering your username and password.
- **自动登录**: 自动输入用户名和密码，快速登录京东账户。
- **Captcha Handling**: Integrated captcha recognition to automatically solve most common captchas.
- **验证码处理**: 集成了验证码识别功能，能够自动处理大部分常见的验证码。
- **Multi-Account Support**: Manage and switch between multiple JD accounts effortlessly.
- **多账户支持**: 支持多个京东账户的管理和切换。
- **Secure Storage**: Encrypts and securely stores your username and password.
- **安全存储**: 使用加密技术存储用户名和密码，确保信息安全。

## Technology Stack / 技术架构

- **Python**: The core programming language used for development.
- **Python**: 项目使用的核心编程语言。
- **Requests**: Handles HTTP requests to communicate with JD servers.
- **Requests**: 用于处理与京东服务器通信的 HTTP 请求。
- **Selenium**: Simulates user browser behavior to handle complex interactions.
- **Selenium**: 模拟用户的浏览器行为，处理复杂的交互操作。
- **Tesseract-OCR**: Recognizes and processes captchas.
- **Tesseract-OCR**: 用于识别和处理验证码。
- **SQLite**: Lightweight database for storing user information and login logs.
- **SQLite**: 轻量级数据库，用于存储用户信息和登录日志。

## Prerequisites / 前提条件

Ensure you have the following installed:
确保你已安装以下内容：

- Python 3.x
- Git

## Python Dependencies / Python 依赖

Install the required Python packages using pip:
使用 pip 安装所需的 Python 包：

```bash
pip install -r requirements.txt
```
## Setup and Deployment / 设置与部署

Follow these steps to set up and deploy JD_Pro:
按照以下步骤设置和部署 JD_Pro：

### 1. Clone the Repository / 克隆仓库

```bash
git clone https://github.com/jtmyd-top/JD_Pro.git
cd JD_Pro
```

### 2. Install Python Dependencies / 安装 Python 依赖

```bash
pip install -r requirements.txt
```

### 3. Configure Tesseract-OCR / 配置 Tesseract-OCR

Make sure Tesseract-OCR is installed and properly configured. You can download it from [here](https://github.com/tesseract-ocr/tesseract).
确保已安装并正确配置 Tesseract-OCR。你可以从[这里](https://github.com/tesseract-ocr/tesseract)下载。

Add Tesseract to your system path. For example, on Windows:
将 Tesseract 添加到系统路径。例如，在 Windows 上：

```plaintext
C:\Program Files\Tesseract-OCR
```

### 4. Modify Configuration / 修改配置

Update the configuration file `config.json` with your JD account details and other necessary settings:
用你的京东账户详情和其他必要设置更新配置文件 `config.json`：

```json
{
    "username": "your_username",
    "password": "your_password",
    "tesseract_path": "path_to_tesseract_executable"
}
```

### 5. Run the Application / 运行应用程序

```bash
python main.py
```

## Future Plans / 未来计划

- **Enhanced Captcha Recognition**: Further optimize the captcha recognition algorithm for better accuracy and success rates.
- **增强验证码识别**: 进一步优化验证码识别算法，提高识别率和成功率。
- **Mobile Support**: Add support for JD mobile app login.
- **移动端支持**: 添加对京东移动端应用登录的支持。
- **User Interface Improvements**: Develop a user-friendly graphical interface to enhance user experience.
- **用户界面改进**: 开发用户友好的图形界面，提升用户体验。

## Contribution / 贡献

Contributions are welcome! Please fork this repository, make your changes, and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.
欢迎贡献！请 fork 这个仓库，做出你的修改，然后提交 pull request。如果有重大更改，请先开一个 issue 讨论你想修改的内容。

## License / 许可证

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
这个项目是根据 MIT 许可证授权的 - 详情请参见 [LICENSE](LICENSE) 文件。

---

By following these steps, you should be able to set up and deploy JD_Pro successfully. If you encounter any issues or need further assistance, please feel free to open an issue in the repository.
通过这些步骤，你应该能够成功设置和部署 JD_Pro。如果遇到任何问题或需要进一步的帮助，请随时在仓库中开 issue。
```

This `README.md` includes bilingual (English and Chinese) sections for a comprehensive understanding of the project, ensuring both English and Chinese-speaking users can effectively use and contribute to the project.
