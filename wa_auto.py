from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time
import csv
import datetime
chrome_options = webdriver.ChromeOptions()
main_msg = """* " %0a
Main Message
"""

student_msg = """ _Custom Message,_

"""

browser = webdriver.Chrome("chromedriver.exe")

browser.get('https://web.whatsapp.com/')
time.sleep(20)
with open('test.csv', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    with open ('report_student_wa.csv','w',newline='') as stat_csv_file:
        writer = csv.writer(stat_csv_file)
        # writer.writerow(["id",'number','name','school','status','timeline'])
        writer.writerow(["id",'number','status','timeline'])
        for row in csv_reader:
            print(row['id'],row['number'])
            try:
                time.sleep(7)
                send_m = "https://web.whatsapp.com/send?phone=91"+str(row['number']) +"&text="+ student_msg
                
                new_msg = browser.get(send_m)
                time.sleep(4)
                sent_button = browser.find_element_by_xpath('//span[@data-icon="send"]')
                print(sent_button)
                sent_button.click()
                # print(row['id'])
                # writer.writerow([str(row['id']),str(row['number']),str(row['name']),str(row['school']),"Successfull",str(datetime.datetime.now())])
                writer.writerow([ str(row['id']),str(row['number']),"Successfull",str(datetime.datetime.now())])
            except Exception as e:
                time.sleep(7)
                print(e)
                # browser.switch_to_alert().accept()
                invalid_number = '(//div[@role = "button"][contains(text(),"OK")])[1]'
                ok_button = browser.find_element_by_xpath(invalid_number)
                time.sleep(4)
                ok_button.click()
                writer.writerow([str(row['id']),str(row['number']),"Invalid Number",str(datetime.datetime.now())])
                   
print("That's all folks")
browser.close()
