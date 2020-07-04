# Project
Django Project Overview
#########################################################
1.A django app implementing django rest framework with only one api end point.
2.Implements  User and ActivityPeriod orm models which have a one to many relationship.
3.Default database is sqlite3
4.Implements factory pattern to generate user and activityperiod objects.
5.Implements custom management command to populate database initially.
6.Uses factory_boy and  faker python packages for fake data generation.

#################################################
Instructions.
1. Download/git-clone the file
2.Extract to a suitable directory
3.create a virtual environment if needed.
4.install all the packages/requirements in requirements.txt.
5.open cmd in the extracted project directory.
6.run the following commands:-(commands are in "")
      6.1 "python manage.py makemigrations" ##########  migrates User and Activity Models and create a sqlitedb
      6.2 "python manage.py migrate" #####creates database tables based on models
      6.3 "python manage.py populatedb" #####custom management command to populate database with fake data
      6.4 "python manage.py runserver" ####runs the django app on localhost:8000
      
      
7. Go to localhost:8000/ in your browser
8.Shows the output in required json format in the webpage
