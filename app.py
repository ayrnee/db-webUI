from flask import Flask,render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'sql9.freemysqlhosting.net'
app.config['MYSQL_USER'] = 'sql9231640'
app.config['MYSQL_PASSWORD'] = 'ckaVTchxBC'
app.config['MYSQL_DB'] = 'sql9231640'
mysql = MySQL(app)

# tables = {"student":["sid","email","fname","lname"], "university":["univid","univname","city"], "student_university":["univid", "sid"]}
tables = {}
def findtables(substr):
    ans = {}
    for table in tables:
        if table.find(substr) > -1:
            ans[table] = tables[table]
    return ans

def find_attr(item):
    ans = {}
    for table in tables:
        if item in tables[table]:
            ans[table] = tables[table]
    return ans

def get_attr(name):
    return tables[field]

@app.route('/<item>', methods=['GET', 'POST'])
def attr_router(item):
    target_tables = find_attr(item)
    return render_template('data.html', target_tables=target_tables)

@app.route('/', methods=['GET', 'POST'])
def index():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT table_name FROM information_schema.tables where table_type="base table"''')
    t_names = cur.fetchall()
    i = 0
    print t_names
    for name in t_names:
            print name
            str = "DESCRIBE" +' '+ name[0]
            print str
            cur.execute(str)
            t_vals = cur.fetchall()
            vals = []
            # print t_vals

            for j in range(len(t_vals)):
                vals.append(t_vals[j][0])
                print t_vals[j][0]
                ++j
            tables[name[0]] = vals
            ++i
    print tables
    # print str
    # cur.execute(str)
    # ans2 = cur.fetchall()
    # print ans2
    if request.method == 'POST':
        target_tables = findtables(request.form['target'])
        return render_template('data.html', target_tables=target_tables)

    return render_template('index.html')
if __name__ == "__main__":
    app.run(use_reloader=True)
