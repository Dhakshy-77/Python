# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 14:28:02 2019
For:Python Milestone Project 1
@author: Geetha
Spyder(Python 3.6)
"""
Movies_List =[
             {
              'Name':'The Boss Baby',
              'Year':'2017',
              'Director':'Tom McGrath'
              },
              {
              'Name':'Happy feet',
              'Year':'2006',
              'Director':'George Miller'
              },
              {
              'Name':'Coco',
              'Year':'2017',
              'Director':'Lee Unkrich'
              },
              {
              'Name':'Stick man',
              'Year':'2015',
              'Director':'Daniel'
              },
              {
              'Name':'Bolt',
              'Year':'2008',
              'Director':'Chris Williams'
              },
              {
              'Name':'Dear Dracula',
              'Year':'2012',
              'Director':'Chad Van De Keere'
              },
              {
              'Name':'Lilo and Stitch',
              'Year':'2002',
              'Director':'Chris Sanders'
              },
              {
               'Name':'The Pirate Fairy',
              'Year':'2014',
              'Director':'Peggy Holmes'
              },
              {
              'Name':'Tinker Bell',
              'Year':'2015',
              'Director':'Bradley Raymond'
              },
              {
              'Name':'Tarzan',
              'Year':'1999',
              'Director':'Kevin Lima'
              }
             ]
 

def get_userinput():
    while True:
        # Ask user for input while managing incorrect input
        list =input('Would you like to list the movies : By Year(type Year) :By Director(type Director):Complete list (type Complete List):year and director(type both):year or director(type any) ').lower()
        if list not in ('year', 'director', 'complete list','both','any'):
            print('\nYou didn\'t enter an availabe value. Please enter one of the list listed.\n'
                  'Returning you to the original input request:')
        else:
            break

#Use the input 

#Like to check the movies complete list
    
    if list == 'complete list':
        for i in range(0,10):
            print(Movies_List[i]['Name']+' -> '+ Movies_List[0]['Year']+' -> '+ Movies_List[0]['Director'])

#Like to check the movies by Year              
    
    elif list == 'year': 
        Year = input('Enter the Year?') 
        for j in range(0,10):     
            if(Year == Movies_List[j]['Year']):
                print('Movie_name: ' + Movies_List[j]['Name'] + '::' +'Director: ' + Movies_List[j]['Director'])

#Like to check the movies by Director
 
    elif list == 'director':
        Director_name = input('Enter the Director Name?')
        for k in range(0,10):     
            if(Director_name == Movies_List[k]['Director']):
                print('Movie_name: ' + Movies_List[k]['Name'] + '::' +'Year: ' + Movies_List[k]['Year'])

#Like to check the movies by Year and Director  
        
    elif list == 'both':
        Year = input('Enter the Year?') 
        Director_name = input('Enter the Director Name?') 
        for l in range(0,10):     
            if(Director_name == Movies_List[l]['Director'] and Year == Movies_List[l]['Year']):
                print('Movie_name: ' + Movies_List[l]['Name'] + ' ' +'Year: ' + Movies_List[l]['Year']+' '+'Director: ' + Movies_List[l]['Director'])
                
   '''             
    elif list == 'any':
        Year = input('Enter the Year?') 
        Director_name = input('Enter the Director Name?') 
        for m in range(0,10):     
            if any([Director_name == Movies_List[m]['Director']], [Year == Movies_List[m]['Year']]):
                print('Movie_name: ' + Movies_List[m]['Name'] + ' ' +'Year: ' + Movies_List[m]['Year']+' '+'Director: ' + Movies_List[m]['Director'])     
    '''
def main():      
    print('***********************WELCOME TO THE MOVIES WORLD****************************')
    get_userinput()
    
if __name__ == "__main__":
    main()






























