# loratech
Technical Assessment for Lora Technology
# created by Safrizal

# INSTALATION PROCESS ON DOCKER

1. download project file from email and extract it or you can clone it directly to https://github.com/rzmobiledev/loratech.git

2. After extract or clone, cd to project directory and open terminal from project directory

3. Type docker-compose up, to build the image. Please wait until process is completed.

4. when you see on terminal that database ready and gunicorn is ready as well, open browser and go to http://127.0.0.1. There you will find endpoints with documentation which you can consume for mobile app or other front end

5. If you want to gain access as root priviledges, stop terminal by pressing Ctrl + C on your keyboard, then type docker-compose run --rm django sh -c "python manage.py createsuperuser and hit enter. Next fill your username and password and hit enter

7. to go to admin page, just type http://127.0.0.1/admin. Feel free to fill the form with your superuser credential that you created above


# PUSHING TO KUBERNETES

FYI : This app is working and testing with minikube running on virtualbox driver

# Instruction
1. run minikube by typing : minikube start --vm-driver=virtualbox

2. run docker login. please login with your docker credential. after login you should see "Login Succeeded"

3. check docker image for this project by typing "docker images" and check the project image name. You should see the project image name like rzmobiledev/django:1.0.0.

5. To push it to your Docker Hub repository, re-tag the image with your Docker Hub username and repo name. In terminal run $docker tag rzmobiledev/django:1.0.0 your_dockerhub_username/your_dockerhub_repo_name

5. Push the image to the repo: $docker push your_dockerhub_username/your_dockerhub_repo_name. You’ll see some output that updates as image layers are pushed to Docker Hub. Now that your image is available to Kubernetes on Docker Hub, you can begin deploy it in your cluster.

6. Create the Deployment in your cluster using $kubectl delete -f kubernetes/deployments/deployment.yaml && kubectl apply -f kubernetes/deployments/deployment.yaml. You will see something like "deployment.apps/django-deploy created".

7. type "$kubectl get deploy" to gain deploy name. Check that the Deployment rolled out correctly using $kubectl get deploy your-app-deploy-name.

8. next type $kubectl delete -f kubernetes/services/service.yaml && kubectl apply -f kubernetes/services/service.yaml

9. check your app service by typing $kubectl get svc. copy your app service name, and type $minikube service your-app-service-name --url. 

10. Copy the url you see on terminal and paste it to the browser. You should see the same Django app interface that you accessed locally in first step above
