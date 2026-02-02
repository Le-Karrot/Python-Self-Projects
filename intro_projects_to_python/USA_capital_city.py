'''
Author: Kevin Ramirez
Date: 2/2/2026
Program: USA_capital_city.py
Purpose: creating an app that outputs the states capitol and major city using dictionaries
'''
#creating dictionary with state as key and captiol and major city
USAmap: dict = {
    "Alabama": "Capital - Montgomery; Major cities - Birmingham, Huntsville, Mobile, Tuscaloosa",
    "Alaska": "Capital - Juneau; Major cities - Anchorage, Fairbanks",
    "Arizona": "Capital - Phoenix; Major cities - Phoenix, Tucson, Mesa, Chandler, Gilbert",
    "Arkansas": "Capital - Little Rock; Major cities - Little Rock, Fayetteville, Fort Smith",
    "California": "Capital - Sacramento; Major cities - Los Angeles, San Diego, San Jose, San Francisco, Fresno",
    "Colorado": "Capital - Denver; Major cities - Denver, Colorado Springs, Aurora",
    "Connecticut": "Capital - Hartford; Major cities - Bridgeport, New Haven, Stamford",
    "Delaware": "Capital - Dover; Major cities - Wilmington",
    "Florida": "Capital - Tallahassee; Major cities - Jacksonville, Miami, Tampa, Orlando",
    "Georgia": "Capital - Atlanta; Major cities - Atlanta, Augusta, Columbus",
    "Hawaii": "Capital - Honolulu; Major cities - Honolulu",
    "Idaho": "Capital - Boise; Major cities - Boise, Meridian, Nampa",
    "Illinois": "Capital - Springfield; Major cities - Chicago, Aurora, Joliet",
    "Indiana": "Capital - Indianapolis; Major cities - Indianapolis, Fort Wayne",
    "Iowa": "Capital - Des Moines; Major cities - Des Moines, Cedar Rapids",
    "Kansas": "Capital - Topeka; Major cities - Wichita, Overland Park",
    "Kentucky": "Capital - Frankfort; Major cities - Louisville, Lexington",
    "Louisiana": "Capital - Baton Rouge; Major cities - New Orleans, Baton Rouge, Shreveport",
    "Maine": "Capital - Augusta; Major cities - Portland",
    "Maryland": "Capital - Annapolis; Major cities - Baltimore",
    "Massachusetts": "Capital - Boston; Major cities - Boston, Worcester, Springfield",
    "Michigan": "Capital - Lansing; Major cities - Detroit, Grand Rapids, Warren",
    "Minnesota": "Capital - St. Paul; Major cities - Minneapolis, St. Paul",
    "Mississippi": "Capital - Jackson; Major cities - Jackson, Gulfport",
    "Missouri": "Capital - Jefferson City; Major cities - Kansas City, St. Louis",
    "Montana": "Capital - Helena; Major cities - Billings, Missoula",
    "Nebraska": "Capital - Lincoln; Major cities - Omaha, Lincoln",
    "Nevada": "Capital - Carson City; Major cities - Las Vegas, Henderson",
    "New Hampshire": "Capital - Concord; Major cities - Manchester, Nashua",
    "New Jersey": "Capital - Trenton; Major cities - Newark, Jersey City",
    "New Mexico": "Capital - Santa Fe; Major cities - Albuquerque, Las Cruces",
    "New York": "Capital - Albany; Major cities - New York City, Buffalo, Rochester",
    "North Carolina": "Capital - Raleigh; Major cities - Charlotte, Raleigh, Greensboro",
    "North Dakota": "Capital - Bismarck; Major cities - Fargo, Bismarck",
    "Ohio": "Capital - Columbus; Major cities - Columbus, Cleveland, Cincinnati",
    "Oklahoma": "Capital - Oklahoma City; Major cities - Oklahoma City, Tulsa",
    "Oregon": "Capital - Salem; Major cities - Portland, Salem",
    "Pennsylvania": "Capital - Harrisburg; Major cities - Philadelphia, Pittsburgh",
    "Rhode Island": "Capital - Providence; Major cities - Providence",
    "South Carolina": "Capital - Columbia; Major cities - Charleston, Columbia",
    "South Dakota": "Capital - Pierre; Major cities - Sioux Falls",
    "Tennessee": "Capital - Nashville; Major cities - Nashville, Memphis",
    "Texas": "Capital - Austin; Major cities - Houston, San Antonio, Dallas, Austin",
    "Utah": "Capital - Salt Lake City; Major cities - Salt Lake City, West Valley City",
    "Vermont": "Capital - Montpelier; Major cities - Burlington",
    "Virginia": "Capital - Richmond; Major cities - Virginia Beach, Norfolk, Chesapeake",
    "Washington": "Capital - Olympia; Major cities - Seattle, Spokane",
    "West Virginia": "Capital - Charleston; Major cities - Charleston, Huntington",
    "Wisconsin": "Capital - Madison; Major cities - Milwaukee, Madison",
    "Wyoming": "Capital - Cheyenne; Major cities - Cheyenne, Caspe"
}

#creating variable
state: str = ''

#using loop will user quits app
while state != 'q':
    
    state = input('Enter a United States of America state: e.g California, Texas, New York(q to quit):')

    if state == 'q':
        break
    '''
    A less case-sensitive key input so far; .title() does the job
    '''
    state = state.title() 

    #conditions for input
    if state in USAmap:
        print(USAmap[state])
    else:
        print('State does not exist.')

print('Exiting...')  
    
