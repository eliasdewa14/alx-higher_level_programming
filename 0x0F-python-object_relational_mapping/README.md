# 0x0F. Python - Object-relational mapping

# Before you start…

Please make sure your MySQL server is in 8.0 -> [How to install MySQL 8.0 in Ubuntu 20.04](https://phoenixnap.com/kb/install-mysql-ubuntu-20-04)

# Background Context
In this project, you will link two amazing worlds: Databases and Python!

In the first part, you will use the module MySQLdb to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module SQLAlchemy (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.

Without ORM:

    conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()

With an ORM:

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
        print("{}: {}".format(state.id, state.name))
    session.close()
Do you see the difference? Cool, right?

The biggest difficulty with ORM is: The syntax!

Indeed, all of them have the same type of syntax, but not always. Please read tutorials and don’t read the entire documentation before starting, just jump on it if you don’t get something.

# Resources

# Read or watch:
- [Object-relational mappers](https://www.fullstackpython.com/object-relational-mappers-orms.html)
- [SQLAlchemy tutorial](https://docs.sqlalchemy.org/en/13/orm/tutorial.html)
- [Introduction to SQLAlchemy](https://www.youtube.com/watch?v=woKYyhLCcnU)
- [Flask SQLAlchemy](https://www.youtube.com/playlist?list=PLXmMXHVSvS-BlLA5beNJojJLlpE0PJgCW)
- [SQLAlchemy Tutorial](https://overiq.com/sqlalchemy-101/)

# More Info

# Install MySQLdb module version 2.0.x
For installing MySQLdb, you need to have MySQL installed: How to install MySQL 8.0 in Ubuntu 20.04

    $ sudo apt-get install python3-dev
    $ sudo apt-get install libmysqlclient-dev
    $ sudo apt-get install zlib1g-dev
    $ sudo pip3 install mysqlclient
    ...
    $ python3
    >>> import MySQLdb
    >>> MySQLdb.version_info
    (2, 0, 3, 'final', 0)

# Install SQLAlchemy module version 1.4.x
    $ sudo pip3 install SQLAlchemy
    ...
    $ python3
    >>> import sqlalchemy
    >>> sqlalchemy.__version__
    '1.4.22'
Also, you can have this warning message:

    /usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be re
    moved in a future release.")
    cursor.execute(statement, parameters)
You can ignore it.

# Mandatory and advanced tasks

0. Write a script that lists all states from the database hbtn_0e_0_usa:

        Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
        You must use the module MySQLdb (import MySQLdb)
        Your script should connect to a MySQL server running on localhost at port 3306
        Results must be sorted in ascending order by states.id
        Results must be displayed as they are in the example below
        Your code should not be executed when imported

1. Write a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa:

        Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
        You must use the module MySQLdb (import MySQLdb)
        Your script should connect to a MySQL server running on localhost at port 3306
        Results must be sorted in ascending order by states.id
        Results must be displayed as they are in the example below
        Your code should not be executed when imported

2. Write a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.

        Your script should take 4 arguments: mysql username, mysql password, database name and state name searched (no argument validation needed)
        You must use the module MySQLdb (import MySQLdb)
        Your script should connect to a MySQL server running on localhost at port 3306
        You must use format to create the SQL query with the user input
        Results must be sorted in ascending order by states.id
        Results must be displayed as they are in the example below
        Your code should not be executed when imported

3. Wait, do you remember the previous task? Did you test "Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '" as an input?

        guillaume@ubuntu:~/0x0F$ ./2-my_filter_states.py root root hbtn_0e_0_usa "Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '"
        (2, 'Arizona')
        guillaume@ubuntu:~/0x0F$ ./0-select_states.py root root hbtn_0e_0_usa
        guillaume@ubuntu:~/0x0F$
   What? Empty?

   Yes, it’s an SQL injection to delete all records of a table…

   Once again, write a script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. But this time, write one that is safe from MySQL injections!

        Your script should take 4 arguments: mysql username, mysql password, database name and state name searched (safe from MySQL injection)
        You must use the module MySQLdb (import MySQLdb)
        Your script should connect to a MySQL server running on localhost at port 3306
        Results must be sorted in ascending order by states.id
        Results must be displayed as they are in the example below
        Your code should not be executed when imported

4. Write a script that lists all cities from the database hbtn_0e_4_usa

        Your script should take 3 arguments: mysql username, mysql password and database name
        You must use the module MySQLdb (import MySQLdb)
        Your script should connect to a MySQL server running on localhost at port 3306
        Results must be sorted in ascending order by cities.id
        You can use only execute() once
        Results must be displayed as they are in the example below
        Your code should not be executed when imported

5. Write a script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa

        Your script should take 4 arguments: mysql username, mysql password, database name and state name (SQL injection free!)
        You must use the module MySQLdb (import MySQLdb)
        Your script should connect to a MySQL server running on localhost at port 3306
        Results must be sorted in ascending order by cities.id
        You can use only execute() once
        The results must be displayed as they are in the example below
        Your code should not be executed when imported

6. First state model

   ![image](https://user-images.githubusercontent.com/54449260/209214182-d39599a8-4cbb-409c-8467-e6b582bacdc9.png)

   Write a python file that contains the class definition of a State and an instance Base = declarative_base():

        State class:
            inherits from Base
            links to the MySQL table states
            class attribute id that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
            class attribute name that represents a column of a string with maximum 128 characters and can’t be null
        You must use the module SQLAlchemy
        Your script should connect to a MySQL server running on localhost at port 3306
        WARNING: all classes who inherit from Base must be imported before calling Base.metadata.create_all(engine)

7. Write a script that lists all State objects from the database hbtn_0e_6_usa

        Your script should take 3 arguments: mysql username, mysql password and database name
        You must use the module SQLAlchemy
        You must import State and Base from model_state - from model_state import Base, State
        Your script should connect to a MySQL server running on localhost at port 3306
        Results must be sorted in ascending order by states.id
        The results must be displayed as they are in the example below
        Your code should not be executed when imported

8. Write a script that prints the first State object from the database hbtn_0e_6_usa

        Your script should take 3 arguments: mysql username, mysql password and database name
        You must use the module SQLAlchemy
        You must import State and Base from model_state - from model_state import Base, State
        Your script should connect to a MySQL server running on localhost at port 3306
        The state you display must be the first in states.id
        You are not allowed to fetch all states from the database before displaying the result
        The results must be displayed as they are in the example below
        If the table states is empty, print Nothing followed by a new line
        Your code should not be executed when imported

9. Write a script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa

        Your script should take 3 arguments: mysql username, mysql password and database name
        You must use the module SQLAlchemy
        You must import State and Base from model_state - from model_state import Base, State
        Your script should connect to a MySQL server running on localhost at port 3306
        Results must be sorted in ascending order by states.id
        The results must be displayed as they are in the example below
        Your code should not be executed when imported

10. Write a script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa

        Your script should take 4 arguments: mysql username, mysql password, database name and state name to search (SQL injection free)
        You must use the module SQLAlchemy
        You must import State and Base from model_state - from model_state import Base, State
        Your script should connect to a MySQL server running on localhost at port 3306
        You can assume you have one record with the state name to search
        Results must display the states.id
        If no state has the name you searched for, display Not found
        Your code should not be executed when imported

11. Write a script that adds the State object “Louisiana” to the database hbtn_0e_6_usa

        Your script should take 3 arguments: mysql username, mysql password and database name
        You must use the module SQLAlchemy
        You must import State and Base from model_state - from model_state import Base, State
        Your script should connect to a MySQL server running on localhost at port 3306
        Print the new states.id after creation
        Your code should not be executed when imported

12. Write a script that changes the name of a State object from the database hbtn_0e_6_usa

        Your script should take 3 arguments: mysql username, mysql password and database name
        You must use the module SQLAlchemy
        You must import State and Base from model_state - from model_state import Base, State
        Your script should connect to a MySQL server running on localhost at port 3306
        Change the name of the State where id = 2 to New Mexico
        Your code should not be executed when imported

13. Write a script that deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa

        Your script should take 3 arguments: mysql username, mysql password and database name
        You must use the module SQLAlchemy
        You must import State and Base from model_state - from model_state import Base, State
        Your script should connect to a MySQL server running on localhost at port 3306
        Your code should not be executed when imported

14. Write a Python file similar to model_state.py named model_city.py that contains the class definition of a City.

        City class:
            inherits from Base (imported from model_state)
            links to the MySQL table cities
            class attribute id that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
            class attribute name that represents a column of a string of 128 characters and can’t be null
            class attribute state_id that represents a column of an integer, can’t be null and is a foreign key to states.id
        You must use the module SQLAlchemy
    Next, write a script 14-model_city_fetch_by_state.py that prints all City objects from the database hbtn_0e_14_usa:

        Your script should take 3 arguments: mysql username, mysql password and database name
        You must use the module SQLAlchemy
        You must import State and Base from model_state - from model_state import Base, State
        Your script should connect to a MySQL server running on localhost at port 3306
        Results must be sorted in ascending order by cities.id
        Results must be display as they are in the example below (<state name>: (<city id>) <city name>)
        Your code should not be executed when imported
