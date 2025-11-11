#!/bin/python

import os

dic_inputs = {}
dic_inputs["name"] = input("What is your name?")
dic_inputs["age"] = input("How old are you?")
dic_inputs["colour"] = input("What's your favourite colour?")
dic_inputs["python"] = input("Do you like Python?")
dic_inputs["flat"] = input("Is the world flat - True or False?")

def checking_inputs(name,age,colour,python,flat):
	if any(character.isdigit() for character in name):
		return print("You're not Elon Musk (please. we don't need more of em). Please stop using numbers in your name.")
	try:
		name_int = float(age)
	except ValueErros:
		return print("Please input a number for your age. Let's get SERIOUS with it.")
	if colour.lower() != "green":
		return print("Well, you're wrong.")
	if python == "No":
		return print("Yeah, but like, grow up.")
	if flat != "False":
		return print("hmm....")
	else:
		return print(f"Okay, this seems like chill input. You said \n name: {name} \n age: {age} \n colour: {colour} \n opinion on python: {python} \n and you don't believe the world is flat! congrats.")

checking_inputs(**dic_inputs)
