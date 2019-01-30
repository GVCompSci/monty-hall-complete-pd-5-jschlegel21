'''
jack Schlegel
11/20
Door switching problem
pitt project
mr. Ellis
'''

from random import randint
#Guess=1
times=int(input('Enter a number between 10 and 10000 '))
while times >10000 or times<10:
    times=int(input('Please try again'))
    
switch=input('Would you like to switch?')
while switch.lower() !='yes' and switch.lower() !='no':
    switch=input('Please enter either yes or no')
correct=0


for i in range(1,times,1):
    car=randint(1,3)
    guess=randint(1,3)

    if guess==1 and car==1:
        if switch.lower()=='no':
            correct+=1
    if guess==1 and car==2:
        if switch.lower()=='yes': 
            correct+=1
    if guess==1 and car==3:
        if switch.lower()=='yes':
            correct+=1
            
    if guess==2 and car==1:
        if switch.lower()=='yes':
            correct+=1
    if guess==2 and car==2:
        if switch.lower()=='no': 
            correct+=1
    if guess==2 and car==3:
        if switch.lower()=='yes':
            correct+=1
    
    if guess==3 and car==1:
        if switch.lower()=='yes':
            correct+=1
    if guess==3 and car==2:
        if switch.lower()=='yes': 
            correct+=1
    if guess==3 and car==3:
        if switch.lower()=='no':
            correct+=1
percent=correct/times

print('The player won ',correct,'/',times,' Games. Thats ',format(percent,'4.2f'),'%',sep='')