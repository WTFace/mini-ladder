import sqlite3
import random


conn = sqlite3.connect('db.sqlite3')
start = ['L', 'R']

for x in range(1,481):
    upd = f"UPDATE canvas_result SET start='{random.choice(start)}', bridges={random.randint(3,4)} WHERE id={x}"
    # ins = f"""INSERT INTO canvas_result (start, bridges) 
    # VALUES ('{random.choice(start)}', {random.randint(3,4)})"""
    conn.execute(upd,)
conn.commit()
conn.close()
