from flask import Flask,render_template, request
app = Flask(__name__)


tables = {"student":["sid","email","fname","lname"], "university":["univid","univname","city"], "student_university":["univid", "sid"]}

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
    if request.method == 'POST':
        target_tables = findtables(request.form['target'])
        return render_template('data.html', target_tables=target_tables)

    return render_template('index.html')
if __name__ == "__main__":
    app.run(use_reloader=True)
