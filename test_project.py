from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import requests
import time
import random

options = Options()     #Блокирую запуск браузера
options.headless = False # True - вебдрайвер работает в фоновом режиме; False - браузер работает в активном окне 
driver = webdriver.Firefox(options=options, executable_path=r'C:\Users\PC\AppData\Local\Programs\Python\Python37-32\Lib\site-packages\selenium\webdriver\firefox\geckodriver') 

def openStatrLink (start_link):
	status = requests.get(start_link)
	request_code = status.status_code
	if request_code == 200:
		print('Test 1. Open start page') 
		driver.get(start_link)
		print(f'Request code {request_code} -  Test passed') 
	else:
		print('Test 1. Open start page - Test failed')

def findAndClick_btn_career():
	try:
		button = driver.find_element_by_xpath('//*[@id="main-menu"]/ul/li[5]/a')
		button.click()
		print('Test 2. Career button is active - Test passed')
	except NoSuchElementException:
		print('Test 2. Career button is active - Test failed')

def findAndClick_btn_iWantWork():
	try:
		driver.implicitly_wait(10)
		button = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[5]/div/a')
		button.click()
		print('Test 3. I want work button is active - Test passed')
	except NoSuchElementException:
		print('Test 3. I want work button is active - Test failed')

def uploadWrongFile(filePath, errorMessage):
	try:
		uploadButton = driver.find_element_by_xpath('/html/body/input')
		uploadButton.send_keys(filePath)
		time.sleep(7) 
		message = driver.find_element_by_xpath('//*[@id="up_file_name"]/label').text
		if message == errorMessage:
			print('Test 4. Error message about wrong upload file - Test passed')
		else:
			print('Test 4. Error message about wrong upload file - Test failed')
			print('Error message have another text')
	except NoSuchElementException:
		print('Test 4. Error message about wrong upload file - Test failed')
		print('Something is wrong with the button')

def inputSomeValue_textArea(nameSurnameMailPhone):
	try:
		for name in nameSurnameMailPhone:						
			textArea = driver.find_element_by_id(f"input{name}")
			textArea.send_keys(nameSurnameMailPhone[name])
		print('Test 5.1. Input some value in text area - Test passed')
	except:
		print('Test 5.1. Input some value in text area - Test failed')

def inputSomeValue_DDlist():
	try:
		for x in range(2,5):
			driver.find_element_by_xpath(f'//*[@id="user-main-info"]/div[11]/div[{x}]/select').click()
			value = (driver.find_element_by_xpath(f'//*[@id="user-main-info"]/div[11]/div[{x}]/select').text).split()
			index = random.randrange(1, len(value))
			select = Select(driver.find_element_by_xpath(f'//*[@id="user-main-info"]/div[11]/div[{x}]/select'))
			select.select_by_visible_text(value[index])
		print('Test 5.2. Input some value in drop-down list - Test passed')	
	except:
		print('Test 5.2. Input some value in drop-down list - Test failed')

def findAndClick_btn_sendCV():
	try:
		button = driver.find_element_by_xpath('//*[@id="submit"]')
		button.click()
		print('Test 6. Send a questionnaire button is active - Test passed')
	except NoSuchElementException:
		print('Test 6. Send a questionnaire button is active - Test failed')

def colorСomparison(color):
	getColor_warningMessage = driver.find_element_by_xpath('/html/body/div[2]/div/p').value_of_css_property('color')
	if color == getColor_warningMessage:
		print('Test 7. Color warning message is red - Test passed')
	else:
		print('Test 7. Color warning message is red - Test failed')

def GoToCoursesPage(validURL):
	(driver.find_element_by_xpath('//*[@id="main-menu"]/ul/li[4]/a')).click()
	currentURL = driver.current_url
	if validURL == currentURL:
		print('Test 8. Open courses page - Test passed')
	else:
		print('Test 8. Open courses page - Test failed')




start_link = "https://netpeak.ua/"
filePath = r'C:\Users\PC\Desktop\img\1.png'
errorMessage = 'Ошибка: неверный формат файла (разрешённые форматы: doc, docx, pdf, txt, odt, rtf).'

nameSurnameMailPhone = {'Name' : 'SomeName',
						'Lastname' : 'someSurname', 
						'Email' : 'SomeText@gmail.com', 
						'Phone' : '+380667513546'}

validURL = 'https://school.netpeak.ua/courses/'
color = 'rgb(255, 0, 0)'

openStatrLink (start_link)
findAndClick_btn_career()
findAndClick_btn_iWantWork()
uploadWrongFile(filePath, errorMessage)
inputSomeValue_textArea(nameSurnameMailPhone)
inputSomeValue_DDlist()
findAndClick_btn_sendCV()
colorСomparison(color)
GoToCoursesPage(validURL)


