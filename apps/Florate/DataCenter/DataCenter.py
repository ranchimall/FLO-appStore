""" The DataCenter module uses sqlite3 for storage of Data By default."""
import sqlite3
conn = sqlite3.connect("Intern.db")
def checkState():
    """
    Function Name: checkState.

    Function Use: Rectify Integerity of the DataBase.
    """
    try:
        c = conn.cursor()
        c.execute("SELECT * from INTER_TAB")
    except:
        c = conn.cursor()
        c.execute("CREATE TABLE INTER_TAB(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,user_name TEXT)")
        
    try:
        c = conn.cursor()
        c.execute("SELECT * FROM RATING_TAB")
    except:
        c = conn.cursor()
        c.execute("CREATE TABLE RATING_TAB(user_name TEXT,rating INTEGER, FOREIGN KEY(user_name) REFERENCES INTER_TAB(user_name))")
        

def readAll():
    """
    Function Name: readAll.

    Function use: To Retrieve all the relavant Interns details.
    """

    c = conn.cursor()
    data =  c.execute("SELECT name,user_name FROM INTER_TAB").fetchall()
    conn.commit()
    
    return data


def write(intern_name,intern_user_name):
    """
    Function Name: write.

    Function Use: writes the Intern's Data to the DataBase.
    """
    c = conn.cursor()
    c.execute("INSERT INTO INTER_TAB(name,user_name) VALUES(?,?)",(intern_name,intern_user_name))
    
    conn.commit()

def delete(intern_name):
    """
    Function Name: delete.

    Function Use: Removes Intern data from the DataBase.
    """
    c = conn.cursor()
    c.execute("DELETE FROM INTER_TAB WHERE user_name=?",(intern_name,))
    conn.commit()


def update(intern_name,intern_user_name):
    #Updates Existing - Intern Details - Not Used Currently
    c = conn.cursor()
    c.execute("UPDATE INTER_TAB SET user_name = ? WHERE intern_name = ?",(intern_name,intern_user_name))
    conn.commit()


def insertRating(user_name,rating):
    """
    Function name:insert Rating.

    Function use: Adds/Updates ratings of the Intern's in the DB.
    """

    c = conn.cursor()
    try:
        k = c.execute("SELECT * FROM RATING_TAB WHERE user_name = ? ",(user_name,)).fetchone()
        if not k:
            raise sqlite3.OperationalError
        c.execute("UPDATE RATING_TAB SET rating = ? WHERE user_name = ?",(rating,user_name))
        conn.commit()
    except sqlite3.OperationalError:
        c.execute("INSERT INTO RATING_TAB(user_name,rating) VALUES(?,?)",(user_name,rating))
    conn.commit()


def clearRatings():
    """
    Function Name:clearRatings.

    Function Use:Delete Unwanted Ratings from the DataBase.

    """
    c = conn.cursor()
    c.execute("DELETE FROM RATING_TAB")


def retrieveRating():
    """
    Function Name: retrieveRating

    Function use: Get the Rating from Rating DataBase.
    """
    c = conn.cursor()
    data = c.execute("SELECT * FROM RATING_TAB").fetchall()
    return data


def removeRating(user_name):
    """
    Function Name: removeRating

    Function use: Delete a specific user rating Data.
    """
    c = conn.cursor()
    c.execute("DELETE FROM RATING_TAB where user_name = ?",(user_name,))
    conn.commit()