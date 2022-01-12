import joblib
import numpy as np

from flask import Flask
from flask import jsonify, request, render_template

app = Flask(__name__)

#POSTMAN para pruebas
@app.route('/predict', methods=['GET', 'POST'])
def predict():
# Datos de prueba
	# features = [7.594444821,7.479555538,1.616463184,1.53352356,0.796666503,0.635422587,0.362012237,0.315963835,2.277026653]
	if request.method == "POST":
	
		int_features = [float(x) for x in request.form.values()]
		features = np.array(int_features).reshape(1,-1)
		prediction = model.predict(features)
	
		return render_template('index.html', pred=f"El Score de felicidad es: {round(prediction[0], 4)}")
	

	return render_template('index.html')

if __name__ == "__main__":
    model = joblib.load("./models/best_model.pkl")
    app.run(debug=True, port=8080)
