import sqlite3
from flask import Flask, g, render_template, request

app = Flask(__name__)
SQLITE_DB_PATH = 'final_demo_result.db'
SQLITE_DB_SCHEMA = 'create_db_potential.sql'
MEMBER_CSV_PATH = 'final_demo_result.csv'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    # Get the database connection
    db = get_db()

    # Draw member ids from given group
    name = request.form.get('name', 'ALL')
    valid_name_sql = 'SELECT * FROM potentialCrime '

    # if name == 'ALL':
    #     cursor = db.execute(valid_name_sql)
    valid_name_sql += 'WHERE name = ?'
    cursor = db.execute(valid_name_sql, (name,))

    valid_datas = []
    for row in cursor:
        valid_datas.append({
            'id': row[0],
            'profile_id': row[1],
            'name': row[2],
            'age': row[3],
            'title': row[4],
            'cnt': row[5],
            'keyword': row[6],
        })
    # If the result is not valid name, return 404
    if not valid_datas:
        err_msg = "找不到人名: '%s'" % name
        return render_template('noresult.html', search_results=err_msg)

    return render_template('result.html', search_results=valid_datas)


# SQLite3-related operations
# See SQLite3 usage pattern from Flask official doc
# http://flask.pocoo.org/docs/0.10/patterns/sqlite3/
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(SQLITE_DB_PATH)
        # Enable foreign key check
        db.execute("PRAGMA foreign_keys = ON")
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


if __name__ == '__main__':
    app.run()
    # app.run(debug=True)
