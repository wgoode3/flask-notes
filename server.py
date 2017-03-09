from flask import Flask, render_template, request, redirect, jsonify
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'notes_db')

@app.route('/')
def index():
    query = "SELECT * FROM notes"
    notes = mysql.query_db(query)
    return render_template('index.html', notes=notes)

@app.route('/note', methods=['post'])
def note():
	query = "INSERT INTO notes(title, description, created_at, updated_at) VALUES('{}', '', NOW(), NOW())".format(request.form['title'])
	mysql.query_db(query)
	query = "SELECT * FROM notes"
	notes = mysql.query_db(query)
	return render_template('partials/note.html', notes=notes)

@app.route('/edit/<note_id>', methods=['post'])
def edit(note_id):
	query = "UPDATE notes SET description = '{}', updated_at = NOW() WHERE id = {}".format(request.form['description'], note_id)
	mysql.query_db(query)
	query = "SELECT * FROM notes"
	notes = mysql.query_db(query)
	return render_template('partials/note.html', notes=notes)

app.run(debug=True)
