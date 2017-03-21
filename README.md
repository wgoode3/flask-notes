# flask-notes
Uses AJAX and python (Flask) to show easily updatable notecards.

## How to get it running
1. Make sure Python and pip are installed. On a Debian/Ubuntu based OS:
```
$ sudo apt-get update
$ sudo apt-get install python-pip
```
2. Create a virtual environment for Flask:
```
$ sudo apt-get update
$ pip install virtualenv
$ cd ~/flask-notes
$ virtualenv flaskenv
$ source flaskenv/bin/activate
$ pip install flask==0.10.1
```
3. Import notes_db_notes.sql into your MySQL.
4. Edit mysqlconnection.py to the correct user, password, and port:
```python
config = {
                'host': 'localhost',
                'database': db, # we got db as an argument
                'user': 'test',
                'password': 'Test1234',
                'port': '3306' # change the port to match the port your SQL server is running on
}
```
5. Run the server:
```
$ python server.py
```
