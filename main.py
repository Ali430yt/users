from flask import Flask
import mysql.connector
import requests,random,string
mydb = mysql.connector.connect(host = "remotemysql.com",user = "WTaUK7bNkM",passwd = "iMD7dgW9nG",database = "WTaUK7bNkM",)
mycursor = mydb.cursor()

def read_all_id():
    ls = []
    sql = f"SELECT id FROM users_tool"
    mycursor.execute(sql)
    file = mycursor.fetchall()
    for data in file:
        ls.append(str(data[0]))
    return ls

def read_all_code():
    ls = []
    sql = f"SELECT code FROM users_tool"
    mycursor.execute(sql)
    file = mycursor.fetchall()
    for data in file:
        ls.append(str(data[0]))
    return ls
    
def read_all_ip():
    ls = []
    sql = f"SELECT ip FROM users_tool"
    mycursor.execute(sql)
    file = mycursor.fetchall()
    for data in file:
        ls.append(str(data[0]))
    return ls

def gen_random(rg=16):
    id = str("".join(random.choice(string.ascii_letters)for _ in range(rg)))
    return id

def add_info(id,code,ip):
    sql = f"INSERT INTO users_tool(id,code,ip) VALUES('{id}','{code}','{ip}')"
    mycursor.execute(sql)
    mydb.commit()
app = Flask(__name__)

@app.route("/code/<id>",)
def post(id):
    list_id = read_all_id()
    if str(id) in list_id:
        return id
    else:
        return "Erorr : 404"

@app.route("/add/code/<code>")
def add_code(code):
    ip = str(requests.get("https://api.ipify.org?format=json").json()["ip"])
    list_id = read_all_id()
    if str(code) in list_id:
        return "Error : code in data"
    else:
        add_info(id=code,code=code,ip=ip)
        return code
app.run()