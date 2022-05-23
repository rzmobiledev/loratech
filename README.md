# loratech
Technical Assessment for Lora Technology
# created by Safrizal

# DOCKER INSTALATION PROCESS #

1. download project file and extract it or you can clone it directly to https://github.com/rzmobiledev/loratech.git

2. After extract or clone, cd to project directory and open terminal from project directory
3. Type docker-compose build, to build the image. Please wait until process is completed.

4. Type docker-compose run --rm django sh -c "python manage.py createsuperuser and hit enter. Next fill your username and password and hit enter

5. Type docker-compose up to run the app with docker image

6. when you see on terminal that database ready and gunicorn is ready as well, open browser and go to http://127.0.0.1:8000. There you will find endpoints which you can consume for mobile app or other front end

7. to go to admin page, just type http://127.0.0.1:8000/admin. Feel free to fill the form with your superuser credential that you created above

# PUSHING TO KUBERNETES

FYI : This app is working well with minikube running on virtualbox driver

# Instruction
1. run minikube by typing : minikube start --vm-driver=virtualbox
2. run docker login. please login with your docker credential. after login you should see "Login Succeeded"
3. check docker image for this project by type docker images and select the project image
4. in terminal run $docker tag djangokubernetesproject:latest your_dockerhub_username/your_dockerhub_repo_name:latest
5. Push the image to the repo: $docker push your_dockerhub_username/your_dockerhub_repo_name:latest. You’ll see some output that updates as image layers are pushed to Docker Hub.


docker build -t rzmobiledev/django:1.0.1 .
docker images
docker push rzmobiledev/django:1.0.1