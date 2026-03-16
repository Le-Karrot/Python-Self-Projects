'''
Author: Kevin Ramirez
Date: 3/2/2026
Program: ProjectGenerator.py
Purpose: Randomly outputs a project idea and lets user choose programming language like c++ or python.
Also allows user to choose how to implement these projects unless specified (e.g Console Base or Text Base), for python most projects should include a GUI. 
'''
import random as rd
import json

#will be creating a json file to store all ideas from a beginner, intermediate, and advance projects 
#the projects are from geeks for geeks and other sites that are similar
#goal is to tackle main concepts such as reading from file, enumeration, random, I/O error handling, GUI with tkinter

#creating generator function to output project
def proj_generator(language: str, difficulty: str) -> str | None:
    
    #reading from a file that randomly chooses a project idea from the json file
    with open('Projects.json', 'r') as IdeaFile:
        content = json.load(IdeaFile)

    #creating for loop to read through the dictionary
    for key in content["Language"]:
        if key["Name"] == language:
            project = key["Difficulty"].get(difficulty, [])
            if project:
                return rd.choice(project)
            else:
                print(f"Error has occured. No project for this {difficulty}")
        else:
            print(f"Error in locating language: {language}")
        
#creating a while loop to allow user to reenter input till accpetable
while True:

    #allowing user to select language 
    lang:str = input('Select Language: ').capitalize().strip()

    #input validation
    valid_lang = False

    if lang != 'C++' and lang != 'Python':
        print(f"Language {lang} not available")
        continue
    else: 
        valid_lang = True

    #user difficulty selection
    diff: str = input("Enter Difficulty: ").capitalize().strip()

    #input validation
    valid_diff = False

    if diff != 'Beginner' and diff != 'Intermediate' and diff != 'Advance':
        print(f"Difficulty {diff} does not exist.")
        continue
    else:
        valid_diff = True
    
    if(valid_lang == True and valid_diff == True):
        break

project_idea = proj_generator(lang, diff)
print(project_idea)