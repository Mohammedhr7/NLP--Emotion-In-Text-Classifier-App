import sqlite3

def create_connection():
    return sqlite3.connect('data/track.db')

def create_page_visited_table():
    conn = create_connection()
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS pageTrackTable(pagename TEXT, timeOfvisit TIMESTAMP)')
    conn.commit()
    conn.close()

def add_page_visited_details(pagename, timeOfvisit):
    conn = create_connection()
    c = conn.cursor()
    c.execute('INSERT INTO pageTrackTable(pagename, timeOfvisit) VALUES (?, ?)', (pagename, timeOfvisit))
    conn.commit()
    conn.close()

def view_all_page_visited_details():
    conn = create_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM pageTrackTable')
    data = c.fetchall()
    conn.close()
    return data

def add_prediction_details(rawtext, prediction, probability, timeOfvisit):
    conn = create_connection()
    c = conn.cursor()
    c.execute('INSERT INTO predictionTable(rawtext, prediction, probability, timeOfvisit) VALUES (?, ?, ?, ?)', (rawtext, prediction, probability, timeOfvisit))
    conn.commit()
    conn.close()

def view_all_prediction_details():
    conn = create_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM predictionTable')
    data = c.fetchall()
    conn.close()
    return data

def create_emotionclf_table():
    conn = create_connection()
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS predictionTable(rawtext TEXT, prediction TEXT, probability REAL, timeOfvisit TIMESTAMP)')
    conn.commit()
    conn.close()