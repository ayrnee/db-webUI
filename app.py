from flask import Flask,render_template, request
app = Flask(__name__)


tables = {"student":["sid","email","fname","lname"], "university":["univid","univname","city"], "student_university":["univid", "sid"]}

def findtables(substr):
    ans = {}
    for table in tables:
        if table.find(substr) > -1:
            ans[table] = tables[table]
    return ans

def find_attr(substr):
    ans = []
    for table in tables:
        if substr in tables[table]:
            ans.append(table)
    return ans

def get_attr(name):
    return tables[field]



@app.route('/', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        target_tables = findtables(request.form['target'])
        return render_template('age.html', target_tables=target_tables)

    return render_template('index.html')
if __name__ == "__main__":
    app.run()
