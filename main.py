tables = {"student":["sid","email","fname","lname"], "university":["univid","univname","city"], "student_university":"univid", "sid"}

def findtables(substr):
    ans = []
    for table in tables:
        if table.find(substr) > -1:
            ans.append(table)
    return ans

def find_attr(substr):
    ans = []
    for table in tables:
        if substr in tables[table]:
            ans.append(table)
    return ans

def get_attr(name):
    return tables[field]

def main():


if __name__ == '__main__':
    main()
