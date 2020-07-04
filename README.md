# Project
Django Project Overview <br />
<br />#########################################################<br />
<br />
<br />
1.A django app implementing django rest framework with only one api end point.<br />
2.Implements  User and ActivityPeriod orm models which have a one to many relationship.<br />
3.Default database is sqlite3.<br />
4.Implements factory pattern to generate user and activityperiod objects.<br />
5.Implements custom management command to populate database initially.<br />
6.Uses factory_boy and  faker python packages for fake data generation.<br />


#################################################<br />
Instructions.<br />
1. Download/git-clone the file.<br />
2.Extract to a suitable directory.<br />
3.create a virtual environment if needed.<br />
4.install all the packages/requirements in requirements.txt.<br />
5.open cmd in the extracted project directory.<br />
6.run the following commands:-(commands are in "").<br />
      6.1 "python manage.py makemigrations" ##########  migrates User and Activity Models and create a sqlitedb.<br />
      6.2 "python manage.py migrate" #####creates database tables based on models.<br />
      6.3 "python manage.py populatedb" #####custom management command to populate database with fake data.<br />
      6.4 "python manage.py runserver" ####runs the django app on localhost:8000.<br />
      
      
7. Go to localhost:8000/ in your browser.<br />
8.Shows the output in required json format in the webpage.<br />




###################################<br />

Special Features<br />

Tested on aws elastic beanstalk<br />
