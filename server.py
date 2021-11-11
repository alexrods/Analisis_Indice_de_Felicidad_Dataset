import joblib
import numpy as np

from flask import Flask
from flask import jsonify, request, render_template

app = Flask(__name__)

#POSTMAN para pruebas
@app.route('/predict', methods=['GET', 'POST'])
def predict():
	if request.method == 'POST':
		user_input = request.form.get(['high', 'low', 'gdp', 'family', 'lifexp', 'freedom', 'generosity', 'corruption', 'dystopia'])
		prediction = model.predict([user_input])
		for i in user_input:
			print(i)
		return "Hola"	
	else:

	    X_test = np.array([7.594444821,7.479555538,1.616463184,1.53352356,0.796666503,0.635422587,0.362012237,0.315963835,2.277026653])
	    prediction = model.predict(X_test.reshape(1, -1))
	    #return jsonify({'Prediction' : list(prediction)})
	    return render_template('index.html', prediction=list(prediction))
if __name__ == "__main__":
    model = joblib.load("./models/best_model.pkl")
    app.run(port=8080)