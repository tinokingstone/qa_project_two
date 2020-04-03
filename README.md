# QA Practical SFIA Project 2
## Project Brief

For this project I was asked to make an application that used concepts from previous training modules that I have done through QA academy such as Software Development with Python, Continuous integration and Cloud Fundamentals.
The project brief had 2 main predefined rules that my final application had to meet, one was for how the application functions and the other was for how I architected my services.
#### Ci pipeline constraints
The other constraints
Version Control: Git 
CI Server: Jenkins 
Configuration Management: Ansible
Containerisation: Docker 
Orchestration Tool: Docker Swarm
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

#### MVP (minimal viable product)
before starting my project i took into account what my minimal viable product would be for my application and ci pipeline.
i made a trello board (seen bellow) that highligted my tasks in terms of priority, the ones labled in green must be completed for my mvp.
![alt text](https://github.com/tinokingstone/qa_project_two/blob/master/DOCUMENTATION%20IMAGES/kanban1.jpg "Logo Title Text 1")
when making this board i decided that i should start my project by creating and completing my ci pipeline and then move on to dveloping my application.
The image below is a visual representation of the micro service architecture i designed for my MVP, i reduced the complexity and number of my services so that i could spend more time developing my pipeline.
![alt text](https://github.com/tinokingstone/qa_project_two/blob/master/DOCUMENTATION%20IMAGES/mvp-architecture.jpg "Logo Title Text 1")
#### MVP sprints
