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
    cur = conn.cursor()

    print("Display server connected to database")
except:
    print("I am unable to connect to the database")




@app.route('/')
def listings():
    cur.execute("""
    CREATE TABLE IF NOT EXISTS listings (
        id serial PRIMARY KEY, 
        title text,
        imageURL text
        )
    """)

    cur.execute("SELECT * FROM listings")
    data = cur.fetchall()

    return render_template('listings.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')
