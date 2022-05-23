# loratech
Technical Assessment for Lora Technology
# created by Safrizal

# INSTALATION PROCESS #

1. download project file and extract it or you can clone it directly to https://github.com/rzmobiledev/loratech.git

2. After extract or clone, cd to project directory and open terminal from project directory
3. Type docker-compose build, to build the image. Please wait until process is completed.

4. Type docker-compose run --rm django sh -c "python manage.py createsuperuser and hit enter. Next fill your username and password and hit enter

5. Type docker-compose up to run the app with docker image

6. when you see on terminal that database ready and gunicorn is ready as well, open browser and go to http://127.0.0.1:8000


5. docker-compose run --rm django sh -c "python manage.py createsuperuser"

