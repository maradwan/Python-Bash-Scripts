# Python-Bash-Scripts

Creates Bash/Python Scripts   

### phonebook_api.py Using API to create phone book records in Mysql

### To Get Record


    $ curl -i http://localhost:5000/todo/api/v1.0/tasks/XXX@XXX.com


### To Create New Record

    $ curl -i -H "Content-Type: application/json" -X POST -d '{"name":"XXXXX", "phonenumber":"XXXXXXX","email":"XXXX@XXX.com"}' http://localhost:5000/todo/api/v1.0/tasks
    
    
### To Delete Record

    $ curl -i -H "Content-Type: application/json" -X DELETE http://localhost:5000/todo/api/v1.0/tasks/XXX@XXX.com
    
    
### To Update Phone Number

    $ curl -i -H "Content-Type: application/json" -X PUT -d '{"phonenumber":"XXXX"}' http://localhost:5000/todo/api/v1.0/tasks/XXXX@XXX.com

