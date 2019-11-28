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
    
    c.execute("INSERT INTO questions VALUES (?,?)",insertion)
    conn.commit()
    conn.close()

def removequestion(question):
    conn = sqlite3.connect('requests.db')
    c = conn.cursor()
    c.execute("DELETE FROM questions WHERE qjson = (?)",(str(question),))
    conn.commit()
    conn.close()
    
def run_request(question, current_dict):
    conn = sqlite3.connect('requests.db')
    c = conn.cursor()
    for row in c.execute("SELECT * FROM questions"):
        if row[0] == str(question):
            if row[1]["success"]:
        
                current_dict["question"] = question["question"]
                current_dict["answers"] = row[1]["answer"]
                current_dict["websites"] = row[1]["domain"]
                removequestion(question)

            else:
                current_dict["question"] = question["question"]
                current_dict["answers"] = "ERROR"
                current_dict["websites"] = "NOT FOUND"

        

        
