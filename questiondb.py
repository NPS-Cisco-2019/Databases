import sqlite3
def create_table(name):
    conn = sqlite3.connect('requests.db')
    c = conn.cursor()
    c.execute('CREATE TABLE questions(qjson, ajson)')
    conn.commit()
    conn.close()
    
def addquestion(question, answer):                                        
    conn = sqlite3.connect('requests.db')
    c = conn.cursor()
    insertion = [str(question), str(answer)]
    
    c.executemany("INSERT INTO questions VALUES (?,?)",insertion)
    conn.commit()
    conn.close()
    
def run_request():
    conn = sqlite3.connect('requests.db')
    c = conn.cursor()
    for row in c.execute("SELECT * FROM questions"):
        
