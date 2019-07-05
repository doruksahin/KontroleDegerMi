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


def scrolling(browser):
	SCROLL_PAUSE_TIME = 0.5
	MAX_TRY = 10
	counter = 0
	length = 0
	jump_length = 1000

	new_height = 0
	while True:
		last_height = new_height
		browser.execute_script("window.scrollTo({}, {});".format(length, length + jump_length))
		length += jump_length
		time.sleep(0.5)
		new_height = browser.execute_script("return document.body.scrollHeight")
		print("last height: {}, new_height: {}".format(last_height, new_height))
		if last_height == new_height:
			print(counter)
			counter += 1
			if counter == MAX_TRY:
				break
		else:
			counter = 0


JSON_PATH = 'output/dogrulukpayi-com.json'
import os
try:
	os.remove(JSON_PATH)
except:
	pass

categories = ['sanayi-ticaret-ve-finans', 'savunma-ve-guvenlik', 'ekonomi', 'egitim', 'enerji', 'mali-politikalar', 'uluslararasi-iliskiler', 'adalet', 'sosyal-politikalar', 
	'bayindirlik-imar-ve-sehircilik', 'teknoloji', 'genel-politika', 'ic-politika', 'cevre', 'tarim-orman-ve-koyisleri']
if __name__ == '__main__':
	with open(JSON_PATH, 'a') as f:
		f.write("[\n")

	MAIN_URL = 'https://www.dogrulukpayi.com/kategori/'
	browser = init_driver(headless=True)

	for category in categories:
		url = MAIN_URL+category
		open_page(browser, url)
		print(url)
		scrolling(browser)
		for article in wait_until_find_xpaths("//div[contains(@class, 'card-content') and contains(@class, 'col-lg-9')]", browser):
			if wait_until_find_xpath("./a/div/span", article) != None: # Check if its claim check.
				pass
			else:
				continue

			claim_blob = {}
			claim_blob['date'] = wait_until_find_xpath(".//subtitle", article).text
			open_new_window(wait_until_find_xpath("./a", article).get_attribute('href'))
			claim_blob['claim'] =  wait_until_find_xpath("//div[contains(@class, 'hero-card') and contains(@class, 'statement')]/div/h2", browser).text
			claim_blob['claim'] += " "
			claim_blob['claim'] += wait_until_find_xpath("//div[contains(@class, col-lg-8) and contains(@class, 'col-sm-12') and contains(@class, 'bodycopy')]/h2", browser).text
			# claim_blob['date'] = wait_until_find_xpath("//*[contains(@class, 'entry-date') and contains(@class, 'updated') and contains(@class, 'td-module-date')]", browser).get_attribute('datetime')
			close_window()

			with open(JSON_PATH, 'a') as f:
				f.write(json.dumps(claim_blob))
				f.write(',\n')

	with open(JSON_PATH, 'a') as f:
		f.write("]")


		