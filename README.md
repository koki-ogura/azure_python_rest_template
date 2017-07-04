# How to built azure webapp python rest server

## test
access root
curl -s http://<project>.azurewebsites.net/  
append user  
curl -s -H "Content-type: application/json; charset=UTF-8" -X POST -d "{\"command\":\"append\",\"name\":\"foo\",\"age\":\"16\"}" http://<project>.azurewebsites.net/api  
append another user  
curl -s -H "Content-type: application/json; charset=UTF-8" -X POST -d "{\"command\":\"append\",\"name\":\"baa\",\"age\":\"26\"}" http://<project>.azurewebsites.net/api  
list users  
curl -s -H "Content-type: application/json; charset=UTF-8" -X POST -d "{\"command\":\"list\"}" http://<project>.azurewebsites.net/api
