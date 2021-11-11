import joblib
import numpy as np

from flask import Flask
from flask import jsonify, request, render_template, url_for, redirect

app = Flask(__name__)

#POSTMAN para pruebas
@app.route('/predict', methods=['GET', 'POST'])
def predict():
# Datos de prueba
# [7.594444821,7.479555538,1.616463184,1.53352356,0.796666503,0.635422587,0.362012237,0.315963835,2.277026653]
	int_features = [float(x) for x in request.form.values()]
	features = np.array(int_features)
	print(int_features)
	print(features)
	prediction = model.predict(features.reshape(1, -1))
	
	return render_template('index.html', pred=prediction)    


if __name__ == "__main__":
    model = joblib.load("./models/best_model.pkl")
    app.run(debug=True, port=8080)