## PYTHON E-MAIL SCRAPER OF HTML FILE ON VIA
## PLEASE VISIT OUR WEB SITES (OUR PROBLEM-SOLVING PROGRAMMING, CODING, & DEVELOPMENT SERVICES ARE AVAILABLE FOR HIRE):
## www.JerusalemProgrammer.com
## www.JerusalemProgrammers.com
## www.JerusalemProgramming.com

## IMPORT MODULES
## IMPORT MODULES
## IMPORT MODULES

import urllib
import bs4
import re
import pprint
import csv


## DECLARE VARIABLES
## DECLARE VARIABLES
## DECLARE VARIABLES

## EMPTY LIST FOR SCRAPED E-MAILS
ListOfEmails = []

# EMPTY SET FOR SCRAPED E-MAILS 
SetOfEmails = set()

## HEADERS FOR OUTPUT TO CSV FILE
##headers = ['emails'] 

## ROWS FOR E-MAILS FOR OUTPUT TO CSV FILE
ListWithOneTuple = []


## BEGIN MAIN PROGRAM
## BEGIN MAIN PROGRAM
## BEGIN MAIN PROGRAM

## CONNECT TO WEB SITE; READ THE HTML DOCUMENT
file = urllib.request.urlopen("https://www.jerusalemprogrammer.com").read()

##print(file)
##print(type(file))
##print("\n")

## PARSE THE HTML; MAKE BEAUTIFUL SOUP
soup = bs4.BeautifulSoup(file, features="html.parser")
##print(soup)
##print(type(soup))
##print("\n")

## FIND ALL <a> ANCHOR TAGS; MAKE LIST OF ANCHOR TAGS
ListOfAnchors = soup.find_all("a")
##pprint.pprint(ListOfAnchors)
##print("\n")
##print("Number of Anchor Tags = ", len(ListOfAnchors))
##print("\n")

## FOR EACH ELEMENT IN LIST OF ANCHORS...
for each in ListOfAnchors:
    ##print(each)
    
    ## CONVERT EACH BEAUTIFUL SOUP OBJECT INTO STRING
    each = str(each)
    ##print(type(each))
    
    ## REGEX TO EXTRACT E-MAILS TO LIST
    ListOfMatches = re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", each)     
    ##print("ListOfMatches = ", type(ListOfMatches))
    
    ## FOR EACH ELEMENT IN LIST, MAKE E-MAILS LOWERCASE
    for email in ListOfMatches:
        
        ## CONVERT E-MAILS TO LOWERCASE
        EmailLowercase = email.lower()
        ##print(EmailLowercase, type(EmailLowercase))
        ##print("\n")
        
        ## APPEND E-MAILS TO LIST OF E-MAILS
        ListOfEmails.append(EmailLowercase)

## TEST PRINT LIST OF E-MAILS
##print("\n")    
##print("ListOfEmails = ", ListOfEmails)
##print(type(ListOfEmails), len(ListOfEmails))

## CONVERT LIST OF E-MAILS TO SET OF E-MAILS
SetOfEmails = set(ListOfEmails)
    
## TEST PRINT SET OF E-MAILS
##print("\n") 
##print("SetOfEmails = ", SetOfEmails)
##print(type(SetOfEmails), len(SetOfEmails))

## CONVERT SET OF E-MAILS BACK TO LIST OF E-MAILS FOR NEXT STEP ALPHABETIC SORTING
ListOfEmailsAlphabetic = list(SetOfEmails)

## ALPHABETIZE LIST OF E-MAILS
ListOfEmailsAlphabetic.sort()

## TEST PRINT ALPHABETIC LIST OF E-MAILS
print("\n") 
print(ListOfEmailsAlphabetic, type(ListOfEmailsAlphabetic), len(ListOfEmailsAlphabetic))

## CONVERT ALPHABETIC LIST OF E-MAILS TO TUPLE OF ALPHABETIC E-MAILS    
TupleOfEmailsAlphabetic = tuple(ListOfEmailsAlphabetic)    
print(TupleOfEmailsAlphabetic, type(TupleOfEmailsAlphabetic), len(TupleOfEmailsAlphabetic))

## APPEND TUPLE OF ALPHABETIC E-MAILS TO LIST TO MAKE LIST OF ONE TUPLE ITEM
ListWithOneTuple.append(TupleOfEmailsAlphabetic)

## TEST PRINT ROWS FOR CSV OUTPUT
print("\n")
print(ListWithOneTuple, type(ListWithOneTuple), len(ListWithOneTuple))

## LIST COMPREHENSION
content = [[i] for i in ListWithOneTuple[0]]
print("\n")
print(content)

## OPEN CSV FILE TO OUTPUT LIST OF E-MAILS
with open('CSVofEmails.csv','w', newline='') as CSVFile:
    FileCSV = csv.writer(CSVFile, delimiter=';')
    ##FileCSV.writerow(headers)
    FileCSV.writerows(content)



## END MAIN PROGRAM
## END MAIN PROGRAM
## END MAIN PROGRAM

## GAME OVER
## GAME OVER
## GAME OVER

## WE HOPE YOU ENJOYED AND THAT THIS HELPS YOUR UNDERSTANDING OF USING PYTHON LANGUAGE TO SOLVE PROBLEMS WITH PROGRAMMING
## PLEASE COME BACK AGAIN SOON
## PLEASE VISIT OUR WEB SITES (OUR PROBLEM-SOLVING PROGRAMMING, CODING, & DEVELOPMENT SERVICES ARE AVAILABLE FOR HIRE):
## www.JerusalemProgrammer.com
## www.JerusalemProgrammers.com
## www.JerusalemProgramming.com
