# Simple Todos Web Application

> The template source for this project [TODO-CSS-Template](https://github.com/Klerith/TODO-CSS-Template)

![](https://github.com/study-hary-id/simple-todos/blob/master/screenshot.png)

Based on this tutorial ['UpKoding'](https://www.youtube.com/playlist?list=PL8bBYpHH3RI6Pp-kA9lmVt18ZZ2TWmmtI). May not be entirely the same, just for learning

## How to run this project on Ubuntu

If command pip not found, install pip first
```
sudo apt install python3-pip
```
Install the depedencies
```
pip3 install Django==3.1.4
```
Run database migrations (Required)
```
python3 manage.py migrate
```
Create superuser (If you want to access admin feature)
```
python3 manage.py createsuperuser
```
Run the server for web app tests
```
python3 manage.py runserver
```
Open this URL on your browser
```
http://localhost:8000/todos
```
Open this URL If you want to login the admin feature
```
http://localhost:8000/admin
```
