# Gallery
## Description
This is an app which users can view uploaded photos


## Screenshots
![Screenshot from 2021-07-06 16-09-20](https://user-images.githubusercontent.com/81610268/124711405-b4bcc500-df06-11eb-8f02-a83a499109d6.png)
![Screenshot from 2021-07-06 16-09-26](https://user-images.githubusercontent.com/81610268/124711429-bc7c6980-df06-11eb-9ab9-2ec676ebb495.png)
![Screenshot from 2021-07-06 16-16-03](https://user-images.githubusercontent.com/81610268/124711435-bedec380-df06-11eb-9e56-2df000cc6038.png)

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
The copy link and filter by category function's is not working.
## Technologies Used
- Django
- Python 3.8.5
- Postgresql
- Cloudinary
- Heroku
## Support and contact details
If you have any suggestions, questions or in case of a fire, you can reach the developer via [email](mailto:erenestmucheru254@gmail.com).

Copyright &copy; 2021 **[ernestmucheru](https://github.com/ernestmucheru)**
