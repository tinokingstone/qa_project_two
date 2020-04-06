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

Service 1 2 and 3 genarate random objects. my character and location genarators use a json web api to genarate details such as age, name, gender and city. my character stats are genarated using the random module from python.

all of the 3 services have version one and 2.
for my location genarator version one outputs citys from the U.K and version 2 genarates only american cities.

my character genarator is defined by gender, one version creates only female characters and the other only males.

the last object genarator creates random stats, one version is capped at a max skil level of 50 and the other goes all the way to 100.

![alt text](https://github.com/tinokingstone/qa_project_two/blob/master/DOCUMENTATION%20IMAGES/application-architecture.jpg "Logo Title Text 1")

in the diagram above the middle tiers use information from my random objects to create something new.

unfortunatly i did not manage to impliment a mission genarator into my final app due to time constraints, instead i focused on my weapon genarator which creates an object from my stats and charaters first and last name.

the image below shows how i used the character name and stat values to determin the tier of weapon the player recieves.
i made 4 tiers, 1 being the weakest weapon choices and 4 the highest. Depending on the tier a random choice is made to select and item from a list of choices.

![alt text](https://github.com/tinokingstone/qa_project_two/blob/master/DOCUMENTATION%20IMAGES/weapongen.jpg "Logo Title Text 1")

## Project Planning and Managment

#### MVP (minimal viable product)

before starting my project i took into account what my minimal viable product would be for my application and Ci pipeline.
i made a trello board (seen bellow) that highligted my tasks in terms of priority, the ones labled in green must be completed for my mvp.
On top of this i used lists written on paper to keep track of smaller objectives.
![alt text](https://github.com/tinokingstone/qa_project_two/blob/master/DOCUMENTATION%20IMAGES/kanban1.jpg "Logo Title Text 1")
when making this board i decided that i should start my project by creating and completing my ci pipeline and then move on to dveloping my application.

The image below is a visual representation of the micro service architecture i designed for my MVP, i reduced the complexity and number of my services so that i could spend more time developing my pipeline
![alt text](https://github.com/tinokingstone/qa_project_two/blob/master/DOCUMENTATION%20IMAGES/mvp-architecture.jpg "Logo Title Text 1")
#### MVP sprints
below is a an imaage showing some of the sprints i done while working on this project, i made a new branch everytime i wanted to make a new feature. i treated avery new feature as an agile sprint. 
![alt text](https://github.com/tinokingstone/qa_project_two/blob/master/DOCUMENTATION%20IMAGES/sprints.jpg "Logo Title Text 1")

## MVP Application

##### MVP Service 1 and 2 
below is an image of my tests results for my random string and intiger genarators, i wanted to get good results and testing coverage before moving on to my main application and pipeline. 
The majority of tests during this project where done through static analysis and debugging, in the beggining the error messages i faced where a challange to understand but by the end of the project i was a lot more comfortable with handlng and solving them within a reasonable timeframe.

![alt text](https://github.com/tinokingstone/qa_project_two/blob/master/DOCUMENTATION%20IMAGES/rand_int_test_cov.jpg "Logo Title Text 1")
random string and int genarator + testing results
![alt text](https://github.com/tinokingstone/qa_project_two/blob/master/DOCUMENTATION%20IMAGES/rand_str_test_cov.jpg "Logo Title Text 1")
the code from the tests above was resued to make all  of my other services, knowing that i had tested the code gave me some peace of mind while developig the rest of the application.

##### MVP Service 3 and 4
all of the testing for service 3 and 4 was done using static analysis.

## Nginx
![alt text](https://github.com/tinokingstone/qa_project_two/blob/master/DOCUMENTATION%20IMAGES/NGINX.jpg "Logo Title Text 1")"Logo Title Text 1")

## Docker compose
## Azure virtual machines
## Docker swarm
## Ansible






123
45
