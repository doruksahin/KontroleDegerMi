#!/usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import json
from urllib import unquote

YUZDE_SIFIR = 'https://dogrula.org/wp-content/uploads/2018/10/yÃ¼zde-sÄ±fÄ±r-1024x388.png'
YUZDE_YUZ = 'https://dogrula.org/wp-content/uploads/2018/12/yÃ¼zde-100.png'


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


JSON_PATH = 'output/gununyalanlari-com.json'
import os
try:
	os.remove(JSON_PATH)
except:
	pass

if __name__ == '__main__':
	with open(JSON_PATH, 'a') as f:
		f.write("[\n")

	MAIN_URL = 'https://gununyalanlari.com/etiket/sik-yalanlar?&sayfa='
	browser = init_driver(headless=True)

	for i in range(1, 100):
		url = MAIN_URL+str(i)
		open_page(browser, url)
		print(url)

		big_article = wait_until_find_xpath("//*[contains(@class, 'news-overlay') and contains(@class, 'tag-featured') and contains(@class, 'col-xs-12')]", browser)
		claim_blob = {}
		claim_blob['date'] = wait_until_find_xpath("./div/span[@class='news-meta']", big_article).text
		claim_blob['claim'] = wait_until_find_xpath("./div/h2", big_article).text
		open_new_window(wait_until_find_xpath("./a", big_article).get_attribute('href'))
		claim_blob['context'] = wait_until_find_xpath("//div[@class='content-body']", browser).text
		close_window()
		with open(JSON_PATH, 'a') as f:
			f.write(json.dumps(claim_blob))
			f.write(',\n')

		for middle_article in wait_until_find_xpaths("//*[contains(@class, 'news-summary-big') and contains(@class, 'col-md-6')]", browser):
			claim_blob = {}
			claim_blob['date'] = wait_until_find_xpath("./div[@class='news-meta']/span", middle_article).text
			claim_blob['claim'] = wait_until_find_xpath("./a/h2", middle_article).text
			open_new_window(wait_until_find_xpath("./a", middle_article).get_attribute('href'))
			claim_blob['context'] = wait_until_find_xpath("//div[@class='content-body']", browser).text
			close_window()
			with open(JSON_PATH, 'a') as f:
				f.write(json.dumps(claim_blob))
				f.write(',\n')


		for little_article in wait_until_find_xpaths("//*[contains(@class, 'news-summary-small') and contains(@class, 'media') and contains(@class, 'col-xs-12')]", browser):
			claim_blob = {}
			claim_blob['claim'] =  wait_until_find_xpath("./div[@class='media-right']/a/h2", little_article).text
			claim_blob['date'] = wait_until_find_xpath("./div[@class='media-right']/a/div/span", little_article).text
			open_new_window(wait_until_find_xpath("./div[@class='media-right']/a", little_article).get_attribute('href'))
			claim_blob['context'] = wait_until_find_xpath("//div[@class='content-body']", browser).text
			close_window()			
			# claim_blob['date'] = wait_until_find_xpath("//*[contains(@class, 'entry-date') and contains(@class, 'updated') and contains(@class, 'td-module-date')]", browser).get_attribute('datetime')
			with open(JSON_PATH, 'a') as f:
				f.write(json.dumps(claim_blob))
				f.write(',\n')

	with open(JSON_PATH, 'a') as f:
		f.write("]")


		