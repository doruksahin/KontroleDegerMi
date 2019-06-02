from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import json

def init_driver(headless=True, disable_gpu=False, enable_adblock=True, timeout=120, maximize=False):
	options = Options()
	options.add_argument('--headless') if headless else 1 == 1
	options.add_argument('--disable-gpu') if disable_gpu else 1 == 1
	#options.add_extension('./adblock.crx') if enable_adblock else 1 == 1

	browser = webdriver.Chrome(chrome_options=options)
	browser.set_page_load_timeout(timeout) # ----------- Throws timeout exception after 300 sec.
	browser.maximize_window() if maximize else 1 == 1

	return browser


def wait_until_find_xpaths(xpath, pathRoot):
	t = True
	failCount = 0
	maxFail = 2

	while t and failCount < maxFail:
		try:
			elements = pathRoot.find_elements_by_xpath(xpath)
			t = False
		except:
			t = True
			failCount = failCount + 1
			time.sleep(0.1)
	if (failCount == maxFail):
		return None
	else:
		return elements


def wait_until_find_xpath(xpath, pathRoot):
	t = True
	failCount = 0
	maxFail = 2

	while t and failCount < maxFail:
		try:
			element = pathRoot.find_element_by_xpath(xpath)
			t = False
		except:
			t = True
			failCount = failCount + 1
			time.sleep(0.1)
	if (failCount == maxFail):
		return None
	else:
		return element


def open_page(browser, URL):
	browser.get(URL)
	browser.execute_script("return window.stop")


def open_new_window(url):
	openingPageScript = '''window.open("{}");'''.format(url)
	browser.execute_script(openingPageScript)
	browser.switch_to_window(browser.window_handles[len(browser.window_handles) - 1])


def close_window():
	browser.close()
	browser.switch_to_window(browser.window_handles[len(browser.window_handles) - 1])


if __name__ == '__main__':
	MAIN_URL = 'https://dogrula.org/kategori/genel/page/'
	RESULT_FILE_PATH = 'dogrula-org.json'
	claims = []
	browser = init_driver(headless=False)
	
	for i in range(1, 100):
		url = MAIN_URL+str(i)
		open_page(browser, url)
		print(url)
		print(browser.current_url)
		print("======")
		for article in wait_until_find_xpaths("//div[@id='cb-content']/div/article", browser):
			open_new_window(wait_until_find_xpath(".//a", article).get_attribute('href'))
			try:
				claim_blob = {}
				claim = wait_until_find_xpath("//div/div[@class='iddia_text']", browser).text
				claim = claim[claim.find(":")+2:]
				claim_blob['claim'] = claim
				claim_blob['acknowledge'] =  wait_until_find_xpath("//div/div[@class='iddia_title']", browser).text
				claim_blob['date'] = wait_until_find_xpath("//time", browser).get_attribute('datetime')
				claims.append(claim_blob)
			except:
				pass
			close_window()
			
	with open(RESULT_FILE_PATH, 'w') as outfile:
		json.dump(claims, outfile, indent=4)



		