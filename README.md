# tasks = > To Do manager

got auto jump to startpage (http://127.0.0.1:8000/)

for requirements > requirements.txt

two options for working with the application:
from startpage or by admin panel http://127.0.0.1:8000/admin
(password and admin name: admin)


Added API - Django Rest Framework
GET	api/tasks/	- to get list of tasks
GET	api/tasks/{id}/	- to get by id
POST	api/tasks/	- creat new task (json)
PUT (или PATCH)	api/tasks/{id}/	- edit taks by id
DELETE	api/tasks/{id}/	- delete taks by id

api/tasks?title={word}  - filter by word
api/tasks?status=True  - filter by status
api/tasks/?page=2  - page navigation
api/tasks?ordering=id  - sort ascending
api/tasks?ordering=-id  - descending sort
