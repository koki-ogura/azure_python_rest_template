# How to built azure webapp python rest server in the terminal environment of mac

## How to change your rest command
The only file to change is main.py.  

## How to deploy to azure webapp
1 Make new WebApp (in azure portal)  
```
  New -> Web + Mobile ->Web App
  Decide <app_name>
  Decide Resource Group
  Select OS to Windows
  Check Pin to dashboard
  and
  Create
```
2 If not yet, decide Deployment credentials  
```
  Select Deployment credentials
  Decide deployment_name and password
```
3 Enable deployment with Local Git  
```
  Select Deployment options
  Select Configure required setting
  Select Local Git Repository
  Push OK button
```
4 Check repository  
```
  Select Overview
  Git clone url is your WebApp's <repository>
```
5 Preparation for deployment (one time only in the mac's terminal)  
```
$ git remote add azure <repository>
```
7 Deploy to azure (Deployment credentials's password required)  
```
$ git commit -am 'your comment'
$ git push azure master
```
8 After editing the program repeat 7  

## How to test from mac's terminal
replace \<app_name\> to your webapp name  

access root  
```
$ curl -s http://<app_name>.azurewebsites.net/  
```
append user  
```
$ curl -s -H "Content-type: application/json; charset=UTF-8" -X POST -d "{\"command\":\"append\",\"name\":\"foo\",\"age\":\"16\"}" http://<app_name>.azurewebsites.net/api  
```
append another user  
```
$ curl -s -H "Content-type: application/json; charset=UTF-8" -X POST -d "{\"command\":\"append\",\"name\":\"baa\",\"age\":\"26\"}" http://<app_name>.azurewebsites.net/api  
```
list users  
```
$ curl -s -H "Content-type: application/json; charset=UTF-8" -X POST -d "{\"command\":\"list\"}" http://<app_name>.azurewebsites.net/api
```
