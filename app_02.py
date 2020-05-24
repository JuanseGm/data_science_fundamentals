from flask import Flask
from datetime import datetime, date, time, timedelta
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def hello_world_json_list():
	tim=datetime.now()
	data =["Año",tim.year,"Mes:",tim.month, "Dia",tim.day,"hora:",tim.hour,"minutos:",tim.minute,"segundos: ",tim.second]
	
	return jsonify(data)

if __name__ == '__main__':
    app.run()