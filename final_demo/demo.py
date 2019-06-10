import sqlite3
from flask import Flask, g, render_template, request

app = Flask(__name__)
SQLITE_DB_PATH = 'final_demo_result.db'
SQLITE_DB_SCHEMA = 'create_db_potential.sql'
MEMBER_CSV_PATH = 'final_demo_result.csv'
low_risk_keywords = ["人口販運", "性剝削", "兒童", "偽造貨幣", "殺人", "重傷害", "搶奪", "勒贖", "海盜", "恐怖主義", "資恐"]
medium_risk_keywords = ["非法販賣武器", "贓物", "竊盜", "綁架", "拘禁", "妨害自由", "環保犯罪", "偽造文書"]
high_risk_keywords = ["仿冒", "盜版", "侵害營業秘密"]
exhigh_risk_keywords = ["毒品販運", "詐欺", "走私", "稅務犯罪", "組織犯罪", "證券犯罪", "貪汙賄賂", "第三方洗錢"]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    # Get the database connection
    db = get_db()

    name = request.form.get('name', 'ALL')
    valid_name_sql = 'SELECT * FROM potentialCrime '

    # if name == 'ALL':
    #     cursor = db.execute(valid_name_sql)
    # else:
    valid_name_sql += 'WHERE name = ?'
    cursor = db.execute(valid_name_sql, (name,))

    valid_datas = []
    for row in cursor:
        # # Define risk
        # valid_risk = ''
        # for idx, val in enumerate(low_risk_keywords):
        #     if val == row[6]:
        #         valid_risk = '低'
        # for idx, val in enumerate(medium_risk_keywords):
        #     if val == row[6]:
        #         valid_risk = '中'
        # for idx, val in enumerate(high_risk_keywords):
        #     if val == row[6]:
        #         valid_risk = '高'
        # for idx, val in enumerate(exhigh_risk_keywords):
        #     if val == row[6]:
        #         valid_risk = '極高'

        valid_datas.append({
            'id': row[0],
            # 'profile_id': row[1],
            'name': row[1],
            'age': row[2],
            'title': row[3],
            'keyword': row[4],
            'crime_risk': row[5],
            'cnt': row[6],
            'news_title': row[7],
            'news_link': row[8],
            'other_suspect': row[9],
            'suspect_probability': row[10],
        })
    # If the result is not valid name, return noresult page
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
