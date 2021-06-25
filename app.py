import streamlit as st 
#import sqlite3
import mysql

#conn = sqlite3.connect('data.db')
#conn = mysql.connect('data.db')

import mysql.connector as mysql
from mysql.connector import Error


def DBConnect(dbName=None):
    """

    Parameters
    ----------
    dbName :
        Default value = None)

    Returns
    -------

    """
    conn = mysql.connect(host='localhost', user='root', password='root480%t100%',
                         database=dbName, buffered=True)
    cur = conn.cursor()
    return conn, cur

#functions

def createDB(dbName: str) -> None:
   
    conn, cur = DBConnect()
    cur.execute(f"CREATE DATABASE IF NOT EXISTS {dbName};")
    conn.commit()
    cur.close()
	#c.execute('CREATE TABLE IF NOT EXISTS blogtable(author TEXT,title TEXT,article TEXT,postdate DATE)')
def create_table():
	conn, cur = DBConnect(dbName)
	sqlFile = 'db.sql'
	fd = open(sqlFile, 'r')
	readSqlFile = fd.read()
	fd.close()
	sqlCommands = readSqlFile.split(';')
	for command in sqlCommands:
		try:
			res = cur.execute(command)
		except Exception as ex:
			print("Command skipped: ", command)
			print(ex)
	conn.commit()
	cur.close()
	return


def add_data(author,title,article,postdate):
	conn, cur = DBConnect(dbName)
	try:
		cur.execute('INSERT INTO blogtable(author,title,article,postdate) VALUES (?,?,?,?)',(author,title,article,postdate))
		conn.commit()
		print("Data Inserted Successfully")

	except Exception as e:
		conn.rollback()
		print("Error: ", e)
		return


def view_all_notes():
	c.execute('SELECT * FROM blogtable')
	data = c.fetchall()
	return data

def main():
	"""a simple crud app"""
	st.title("Simple blog")
	menu = ["Home", "View Posts", "Add Posts", "Search", "Manage Blog"]

	choice = st.sidebar.selectbox("Menu",menu)
	if choice == "Home":
		st.subheader("Home")
		result = view_all_notes()
		st.write(result)
	elif choice == "View Posts":
		st.subheader("View Posts")

	elif choice == "Add Posts":
		create_table()
		st.subheader("Add an article")

		blog_author = st.text_input("Enter Author Name", max_chars=50)
		blog_title = st.text_input("Enter Post Title")
		blog_article = st.text_area("Post article" ,height= 200)
		blog_post_date = st.date_input("Date")
		if st.button("Add"):
			add_data(blog_author,blog_title,blog_article,blog_post_date)
			st.success("Post:{} saved".format(blog_title))

	elif choice == "Search":
		st.subheader("Search articles")

	elif choice == "Manage Blog":
		st.subheader("setting")
















if __name__ == '__main__':
	main()

