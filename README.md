# sandeepsinghnegi

# copy the project path to clone project in your local machine

# using git clone <git_repo_url>

# dependencies to install
# requirements.txt file using - pip install -r requirements.txt

# create .env file in project folder and set these value 

# - SECRET_KEY=+ylsaf8c*ja2+gj80^u0%8_4mv93wug7ksry4=ijvbd!38jyfu
# - DEBUG=True
# - EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
# - EMAIL_HOST=smtp.gmail.com
# - EMAIL_USE_TLS=True
# - EMAIL_PORT=587
# - EMAIL_HOST_USER=***
# - EMAIL_HOST_PASSWORD=***

# command to run project

# - python manage.py makemigrations
# - python manage.py migrate
# - python manage.py runserver

# command to run celery 
# - python -m celery -A sandeepsinghnegi worker -l info

# postman for calling api endpoints

# - create postman collection
# - create postman request
# - copy http://127.0.0.1:8000/ for [GET, POST]