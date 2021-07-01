from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException

path = r"chromedriver_win32\chromedriver.exe"
# web_link = "https://www.linkedin.com/jobs/search/?currentJobId=2614182835&f_AL=true&f_PP=103112676&keywords=python&sortBy=R"
web_link = "https://www.linkedin.com/jobs/search/?f_AL=true&f_PP=103112676&keywords=python&sortBy=R"

driver = webdriver.Chrome(executable_path=path)
driver.get(web_link)

print("Wait to load...")
time.sleep(4)
print("Click sign in")

sign_in_button = driver.find_element_by_class_name("nav__button-secondary")
sign_in_button.click()


print("Input User")
user_name = driver.find_element_by_id("username")
user_name.send_keys("")

pw = driver.find_element_by_id("password")
pw.send_keys("")

#Sign in
sign_in_button = driver.find_element_by_css_selector(".btn__primary--large.from__button--floating")
sign_in_button.click()

input("Press Any Key to Continue....")

#Remember account? Not now
try:
    sign_in_button = driver.find_element_by_css_selector(".btn__secondary--large-muted")
    sign_in_button.click()
except:
    print("No remember required")

print("Wait to start job Listing...")
time.sleep(2)
print("Get Job Listing...")
driver.maximize_window()

#Get the job listing
job_list = driver.find_elements_by_css_selector(".jobs-search-results__list.list-style-none li")

# with open("job_list.txt","a") as file:
#     messege = ""
#     for job in job_list:
#         print(job.text)
#         messege = messege + job.text + ","

#         if("Easily Apply" in job.text):
#             file.write(messege + "\n" + "\n")
#             messege = ""
#             job.click()
#             time.sleep(2)
        
#             try:
#                 apply_button = driver.find_element_by_css_selector(".jobs-apply-button.artdeco-button.artdeco-button--3.artdeco-button--primary.ember-view")
#                 apply_button.click()
#             except NoSuchElementException:
#                 pass
            
            
#             #Close the apply window
#             X_button = driver.find_element_by_xpath('/html/body/div[3]/div/div/button')
#             X_button.click()
#             discard_button = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[3]/button[1]')
#             discard_button.click()

# pages = driver.find_elements_by_css_selector(".artdeco-pagination__pages.artdeco-pagination__pages--number li")
# pages = driver.find_elements_by_css_selector(".artdeco-pagination__indicator.artdeco-pagination__indicator--number.ember-view button")

job_list = driver.find_elements_by_css_selector(".jobs-search-results__list.list-style-none li")

    # ------------------------ Iterate through job and apply or close window ------------------------ #    

def IterateThroughJob():
    job_list = driver.find_elements_by_css_selector(".jobs-search-results__list.list-style-none li")

    with open("job_list.txt","a") as file:
        messege = ""
        for job in job_list:
            print(job.text)
            messege = messege + job.text + ","

            if("Easily Apply" in job.text):
                file.write(messege + "\n" + "\n")
                messege = ""
                job.click()
                time.sleep(1)
            
                try:
                    apply_button = driver.find_element_by_css_selector(".jobs-apply-button.artdeco-button.artdeco-button--3.artdeco-button--primary.ember-view")
                    apply_button.click()
                except NoSuchElementException:
                    pass
                
                
                #Close the apply window
                X_button = driver.find_element_by_xpath('/html/body/div[3]/div/div/button')
                X_button.click()
                discard_button = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[3]/button[1]')
                discard_button.click()

while(True):
    IterateThroughJob();
    input("Change Page and Press Enter to Continue Apply \n")
    


# --------------- Failed Attempt to iterate through all the pages... Too dynamic ----------#
# total_pages = int(pages[-1].text)
# #iterate from the first to last page

# i = 0
# while(i < total_pages):
#     updated_pages = driver.find_elements_by_css_selector(".artdeco-pagination__indicator.artdeco-pagination__indicator--number.ember-view button")
#     print("===")
#     print([x.text for x in updated_pages])
#     print(f"i= {i}, cur_page= {updated_pages[i].text}")
    
#     if(updated_pages[i].text != "…"):
#         cur_page = int(updated_pages[i].text)
#         next_page = str(cur_page+1)
#         print("Guess next page: ", next_page)
    
#     if(updated_pages[i].text != "…"):
#         updated_pages[i].click()
#         i+=1
#     elif(updated_pages[i].text == "…"):
#         print("found ...")
#         updated_pages[i].click()
#         i-=3
#     print("==========")
#     time.sleep(5)