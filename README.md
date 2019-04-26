# Conference_management
Conference recommender system allows for personalized recommendations of scientific conferences based on user's research interests. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
To run the project on a local machine you need to install a virtual environment. We can do this by using the following command: pip install virtualenv
All other dependencies will be installed in the virtual environment.

The packages that need to be installed in the environment: Django, Pillow, django-debugtools
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
0. Make sure you have pip and python3
1. Install the virtualenv package: pip install virtualenv
2. Create the working directory (e.x. the folder name "django"): mkdir django
3. Enter the directory: cd django 
   Inside the directory create a virtual environment with python3: virtualenv denvx -p python3
4. Clone the project from github: git clone https://github.com/Dementyevasl/Conference_management.git
5. Activate the virtual environment: source denvx/bin/activate
6. Install the django package in the virtual environment: pip install django
7. Install the pillow package in the virtual environment: pip install Pillow
8. Install the django debugger in the virtual environment: pip install django-debugtools
9. Not necessary, but very usefull: create a super user so you can controll the admin panell: python manage.py createsuperuser
10. Run the server: python manage.py runserver
11. Open the http://127.0.0.1:8000

If you did everything correct, you can now use and test the project

I don't know when, but sometimes you need to do this:
python manage.py makemigrations
python manage.py migrate

I think you do this when you change the model file, but that's not sure.


```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* Django
* Python

## Contributing


## Versioning



## Authors



## License



## Acknowledgments

Makarov Ilya 
