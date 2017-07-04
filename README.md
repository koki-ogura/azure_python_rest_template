# How to built azure webapp python rest server

## test
replace \<project_name\> to your_project_name  
access root
curl -s http://\<project_name\>.azurewebsites.net/  
append user  
curl -s -H "Content-type: application/json; charset=UTF-8" -X POST -d "{\\"command\\":\\"append\\",\\"name\\":\\"foo\\",\\"age\\":\\"16\\"}" http://\<project_name\>.azurewebsites.net/api  
append another user  
curl -s -H "Content-type: application/json; charset=UTF-8" -X POST -d "{\\"command\\":\\"append\\",\\"name\\":\\"baa\\",\\"age\\":\\"26\\"}" http://\<project_name\>.azurewebsites.net/api  
list users  
curl -s -H "Content-type: application/json; charset=UTF-8" -X POST -d "{\\"command\\":\\"list\\"}" http://\<project_name\>.azurewebsites.net/api
