from flask import Flask, render_template
import datetime
app = Flask(__name__)


@app.route('/')
def hello():
    try:
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return render_template('index.html', message='Bienvenido a mi aplicación', datetime=current_datetime)
    except Exception as e:
        return str(e)
    
    finally:
       print("close app")

if __name__ == '__main__':
    app.run(debug=True)