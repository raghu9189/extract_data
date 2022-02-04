from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import csv

#ready the driver object
PATH = 'chromedriver.exe' #download chromedriver according to user chrome version
s = Service(PATH)
driver = webdriver.Chrome(service=s)

#define a function to convert A grade to Numeric grade (9) 
def grade_convert(K):
    if(K == 'S'):
        return 10
    if(K == 'A'):
        return 9
    if(K == 'B'):
        return 8
    if(K == 'C'):
        return 7
    if(K == 'D'):
        return 6
    if(K == 'E'):
        return 5
    if(K == 'FAIL'):
        return 0

#read the csv file
with open('list_of_students.csv') as input_csv:
    input_reader = csv.reader(input_csv, delimiter=',')
    for row in input_reader:
        #my college uiversity website
        URL = 'https://www.osmania.ac.in/res07/20220132.jsp' 

        #auto enter every Hall ticket number
        driver.get(URL)
        set_input = driver.find_element(By.XPATH, '//*[@id="AutoNumber6"]/tbody/tr[1]/td/b/font/input[1]')
        set_input.send_keys(row) 
        set_input.submit()
        

        #collect the student information
        get_ht = driver.find_element(By.XPATH,'/html/body/form/div/center/table/tbody/tr[3]/td/div/center/table/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/b/font').text
        get_name = driver.find_element(By.XPATH,'//*[@id="AutoNumber3"]/tbody/tr[3]/td[2]/b/font').text
        PC201 = driver.find_element(By.XPATH,'//*[@id="AutoNumber4"]/tbody/tr[3]/td[4]/b/font').text
        PC202 = driver.find_element(By.XPATH,'//*[@id="AutoNumber4"]/tbody/tr[4]/td[4]/b/font').text
        PC203 = driver.find_element(By.XPATH,'//*[@id="AutoNumber4"]/tbody/tr[5]/td[4]/b/font').text
        PC204 = driver.find_element(By.XPATH,'//*[@id="AutoNumber4"]/tbody/tr[6]/td[4]/b/font').text
        PC205 = driver.find_element(By.XPATH,'//*[@id="AutoNumber4"]/tbody/tr[7]/td[4]/b/font').text
        PC206 = driver.find_element(By.XPATH,'//*[@id="AutoNumber4"]/tbody/tr[8]/td[4]/b/font').text
        PC251 = driver.find_element(By.XPATH,'//*[@id="AutoNumber4"]/tbody/tr[9]/td[4]/b/font').text
        PC252 = driver.find_element(By.XPATH,'//*[@id="AutoNumber4"]/tbody/tr[10]/td[4]/b/font').text
        PC253 = driver.find_element(By.XPATH,'//*[@id="AutoNumber4"]/tbody/tr[11]/td[4]/b/font').text
        final_result = driver.find_element(By.XPATH,'//*[@id="AutoNumber5"]/tbody/tr[3]/td[3]/b/font').text
        
        print(get_ht)
        print(get_name)
        pc_201 = grade_convert(str(PC201).strip())
        pc_202 = grade_convert(str(PC202).strip())
        pc_203 = grade_convert(str(PC203).strip())
        pc_204 = grade_convert(str(PC204).strip())
        pc_205 = grade_convert(str(PC205).strip())
        pc_206 = grade_convert(str(PC206).strip())
        pc_251 = grade_convert(str(PC251).strip())
        pc_252 = grade_convert(str(PC252).strip())
        pc_253 = grade_convert(str(PC253).strip())
        print(final_result)
        time.sleep(2)

        #write in a csv file
        with open('students_grades.csv', mode='a') as csv_file:
            fieldnames = ['ht_num', 'name', 'pc201','pc202','pc203','pc204','pc205','pc206','pc251','pc252','pc253','final_result']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writerow({'ht_num': get_ht, 'name': get_name, 'pc201': pc_201,'pc202': pc_202,'pc202': pc_202,'pc203': pc_203,'pc204': pc_204,'pc205': pc_205,'pc206': pc_206,'pc251': pc_251,'pc252': pc_252,'pc253': pc_253,'final_result': final_result})

        #final grade cgpa
        with open('final_cgpa.csv',mode='a') as csv_file_1:
            cgpa = ((3 * pc_201) + (4 * pc_202) + (3 * pc_203) + (4 * pc_204) + (3 * pc_205) + (3 * pc_206) + (2 * pc_251) + (2 * pc_252) + (2 * pc_253))/260
            csv_file_1.write((str(get_ht )+','+str(round(cgpa * 10,2))+'\n'))
