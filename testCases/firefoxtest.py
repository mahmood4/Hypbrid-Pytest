import selenium
from selenium.webdriver.firefox import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from webdriver_manager.chrome import ChromeDriverManager

gecko_path = "c:\\Test\\geckodriver.exe"

path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
s = Service("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
binary = FirefoxBinary(path)
options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15')
options.add_argument('--disable-plugins-discovery')
options.add_argument('referer=https://www.youtube.com/')
options.add_argument('--disable-extensions')
options.add_argument('--profile-directory=Default')
options.add_argument('--disable-blink-featuresi=AutomationControlled')
options.add_argument('--disable-blink-features')


ser = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=ser)
#driver = selenium.webdriver.firefox(firefox_profile=profile, options=options, executable_path=gecko_path)
#driver = selenium.webdriver.Firefox(options=options,executable_path=gecko_path,firefox_binary=binary)
driver = selenium.webdriver.Firefox(options=options,executable_path=gecko_path,firefox_binary=binary)
#webdriver.se
#driver.get("https://www.google.com")
