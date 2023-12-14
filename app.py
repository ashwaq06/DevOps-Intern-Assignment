from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ashwaq:admin@db:5432/my_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
redis_client = StrictRedis(host='redis', port=6379, db=0)

class Visit(db.Model):
    id = db.Column(db.Integer, primary_key=True)

@app.route('/')
def index():
    # Increment visit count in Redis
    redis_client.incr('visits')

    # Fetch total visit count from Redis
    visit_count = redis_client.get('visits').decode('utf-8')

    return render_template('index.html', visit_count=visit_count)

# This block ensures that `db.create_all()` is executed within the application context.
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)