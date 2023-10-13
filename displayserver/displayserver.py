from flask import Flask, request,render_template
import psycopg2

app = Flask(__name__)

hostname = 'db'
username = 'postgres'
password = 'scraper'
database = 'listings'
port='5432'

try: 
    conn = psycopg2.connect(database=database, user=username,
                            password=password, host=hostname,port=port)
    conn.autocommit = True
    cur = conn.cursor()

    print("Display server connected to database")
except:
    print("I am unable to connect to the database")




@app.route('/')
def listings():
    cur.execute("select exists(select * from information_schema.tables where table_name=%s)", ('listings',))
    tblexists = cur.fetchone()[0]
    if tblexists:
        cur.execute("SELECT * FROM listings")
        data = cur.fetchall()
    else:
        data = []

    return render_template('listings.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')
