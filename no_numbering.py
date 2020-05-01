#!/usr/bin/env python
# coding: utf-8

# In[11]:


import time
from selenium import webdriver


options = webdriver.ChromeOptions()
driver = webdriver.Chrome('./chromedriver', options=options)



# Optional argument, if not specified will search path.
driver.get('http://edu.alvas.org/learn/login/index.php');

import sys


email = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/section/div/div[2]/div/div/div/div/div/div[1]/form/div[1]/input')

email.send_keys('teacher')

password = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/section/div/div[2]/div/div/div/div/div/div[1]/form/div[2]/input')

password.send_keys('Teacher.123')

button = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/section/div/div[2]/div/div/div/div/div/div[1]/form/button')

button.click()


# In[12]:


url = 'http://edu.alvas.org/learn/mod/quiz/edit.php?cmid=76'



driver.get(url)


# In[13]:


outer_div = driver.find_element_by_class_name('content')


# In[14]:


question_list = outer_div.find_elements_by_tag_name('li')
times = len(question_list)


# In[15]:


for i in range(times ):
    import time
    if 'multichoice' in question_list[i].get_attribute('class'):
        
        
        question_list[i].click()
        time.sleep(0.3)
        default = driver.find_element_by_id('id_defaultmark')
        default.clear()
        default.send_keys('4')
        
        
        numbering = driver.find_element_by_id('id_answernumbering')
        numbering.click()
        required_option = driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/div/section/div/form/fieldset[1]/div/div[10]/div[2]/select/option[6]')
        required_option.click()
        time.sleep(0.2)
        save_changes = driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/div/section/div/form/div[4]/div[2]/fieldset/div/div[1]/span[2]/input')
        save_changes.click()
        
        outer_div = driver.find_element_by_class_name('content')
        question_list = outer_div.find_elements_by_tag_name('li')
       


# In[ ]:




