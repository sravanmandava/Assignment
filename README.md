
First clone the repository from Github and switch to the new directory:

     git clone https://github.com/sravanmandava/Assignment.git
     cd {{ Assignment }}


1. create a virtualenv directory and activate the virtual environment.

	   create :pythom -m venv virtualenv
	   Activate :source virtualenv/scripts/activate
	
2. Navigate to the UMS_Project directory and install required softwares using below command.

	   pip install -r requirements.txt
	
3. Apply migrations to the project.

	   python manage.py makemigrations
	   python manage.py migrate
	
  4.create superuser for the project to login to the application.
 
	   python manage.py createsuperuser
	
 5. Start the server by using the below command 

	   python manage.py runserver

 6. Navigate to webbrowser access the application at  http://127.0.0.1:8000/
