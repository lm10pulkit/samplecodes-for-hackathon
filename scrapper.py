import csv
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import time
option = webdriver.ChromeOptions()


driver = webdriver.Chrome(executable_path="C:/webdrivers/chromedriver.exe",  chrome_options=option)
with open('description.csv', mode='w') as descriptor:

	desc = csv.writer(descriptor, delimiter=',')
	with open('output3.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		for row in csv_reader:
			time.sleep(1.5)
			val ='treatment of '+row[0]
			driver.get("https://www.google.com/search?hl=en-IN&authuser=0&rlz=1C1CHBF_enIN786IN786&ei=QcafXPeFEcfZz7sP3_i_yAs&q="+val+"&oq=treatment+of+hiv&gs_l=psy-ab.3..0l7j0i20i263j0l2.11372.13791..14095...0.0..0.156.1267.0j9......0....1..gws-wiz.......0i71j35i39j0i67j0i131.KPN-wfAXiKg")

			titles_element = driver.find_elements_by_xpath("//div[@class='K9xsvf Uva9vc kno-fb-ctx']")
			print(row[0])
			print(len(titles_element))
			if (len(titles_element)==0):
				desc.writerow([row[0]])
			else:
				desc.writerow([row[0],titles_element[0].text])
		
# Clean up (close browser once completed task).
driver.close()

