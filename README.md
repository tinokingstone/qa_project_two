# QA Practical SFIA Project 2
## Project Brief

For this project I was asked to make an application that used concepts from previous training modules that I have done through QA academy such as Software Development with Python, Continuous integration and Cloud Fundamentals.
The project brief had 2 main predefined rules that my final application had to meet, one was for how the application functions and the other was for how I architected my services.
#### Application Functions
I had to limit the scope of my application to a random object generator for example:
* A prize generator.
* D&D style character generator.
* Theme and setting generator for short stories
#### Application Architecture 
My applications architecture had to be micro-service orientated with at least 4 services working together.

## My Application Idea 
#### Survival Game Mission Generator
For my application I wanted to make a mission generator for a survival themed video game where the character, map location (objective start and end), character stats and weapon would be randomised before a player enters a mission.

#### Application Architecture 
The image below is a visual representation of the micro service architecture i designed for my web app.
![alt text](https://github.com/tinokingstone/qa_project_two/blob/master/DOCUMENTATION%20IMAGES/application-architecture.jpg "Logo Title Text 1")
my app creates a mission and weapon objects from the information it gets from my random location and character services and then displays them on my front end service where a user can choose to save the random combinations into a database (play)
## Project Planning and Managment
![alt text](https://github.com/tinokingstone/qa_project_two/blob/master/DOCUMENTATION%20IMAGES/kanban1.jpg "Logo Title Text 1")
