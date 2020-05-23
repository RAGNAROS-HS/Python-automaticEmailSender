
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 13:54:19 2020

@author: Hugo Katzer
"""

import smtplib
import time
while True:
    
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    
    mail.ehlo()
    
    mail.starttls()
    mail.login("your mail adress", "your password")
    
    mail.sendmail('your mail adress again', 'target adress', "content")
    
    mail.close
    time.sleep(60) #anything below a couple seconds may cause problems
    
    