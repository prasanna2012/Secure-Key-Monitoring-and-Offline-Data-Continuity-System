from flask import Flask, render_template, jsonify
import psutil, time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    response_time = round(time.time() % 10, 2)  # simulate response time
    return jsonify(cpu=cpu, memory=memory, response_time=response_time)

if __name__ == '__main__':
    app.run(debug=True)



#Backend