# Gallery
## Description
This is an app which users can view uploaded photos


- The expanded image view.
## Setup/Installation
On your terminal, clone the project.
    
    $ git clone https://github.com/ernestmucheru/gallery-django.git
    

Navigate into the cloned project.

    $ cd gallery-django

Create a `.env` file.

    $ touch .env

Inside `.env`, add the following and fill the empty fields with the appropriate values:

```python
SECRET_KEY=
DEBUG=True
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST='127.0.0.1'
MODE='dev'
ALLOWED_HOSTS='.localhost','.herokuapp.com','127.0.0.1'
DISABLE_COLLECTSTATIC=1

Create the virtual environment and install the requirements from `requirements.txt`

    $ python3 -m venv virtual
    $ . virtual/bin/activate
    $ pip install -r requirements.txt


Perform a migration.

    $ python3 manage.py migrate


Start the server.

    $ python3 manage.py runserver


## Known Bugs
No known bugs.
## Technologies Used
- Django
- Python 3.8.5
- Postgresql
- Cloudinary
- Heroku
## Support and contact details
If you have any suggestions, questions or in case of a fire, you can reach the developer via [email](mailto:erenestmucheru254@gmail.com).

Copyright &copy; 2021 **[ernestmucheru](https://github.com/ernestmucheru)**
