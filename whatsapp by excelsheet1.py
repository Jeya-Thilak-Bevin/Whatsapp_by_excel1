from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from time import sleep
import pandas

excel_data = pandas.read_excel('C:/Customer/Customer bulk email data.xlsx', sheet_name='Customers')

message = 'Hello! This is a sample message.'  # Add your desired message here

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com')
input("Press ENTER after logging into WhatsApp Web and your chats are visible.")

for contact in excel_data['Contact']:
    try:
        url = 'https://web.whatsapp.com/send?phone=' + str(contact) + '&text=' + message
        sent = False
        driver.get(url)
        try:
            send_btn = WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.XPATH, '//span[@data-testid="send"]')))
            send_btn.click()
            sent = True
            sleep(5)
            print('Message sent to: ' + str(contact))
        except TimeoutException:
            print("Sorry, the message could not be sent to " + str(contact))
    except Exception as e:
        print('Failed to send message to ' + str(contact) + str(e))

driver.quit()
print("The script executed successfully.")