from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
def test_Baidu():
    # Hub的地址
    hub_url = "http://localhost:4444"

    # 指定你想要运行的浏览器，例如Chrome
    chrome_options = Options()

    # 创建一个远程WebDriver，连接到Grid
    driver = webdriver.Remote(command_executor=hub_url,
                              options=chrome_options)

    # 剩下的测试代码保持不变
    driver.get("https://www.baidu.com")
    print(driver.title)
    driver.quit()


if __name__=='__main__':
    test_Baidu()
