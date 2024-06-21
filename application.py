from flask import Flask, request, render_template
from src.pipelines.prediction_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

@app.route('/')
def home_page():
    return render_template('form.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        print("GET request received")
        return render_template('index.html')
    elif request.method == 'POST':
        print("POST request received")
        try:
            data = CustomData(
                carat=float(request.form.get('carat')),
                depth=float(request.form.get('depth')),
                table=float(request.form.get('table')),
                x=float(request.form.get('x')),
                y=float(request.form.get('y')),
                z=float(request.form.get('z')),
                cut=request.form.get('cut'),
                color=request.form.get('color'),
                clarity=request.form.get('clarity')
            )
            final_new_data = data.get_data_as_dataframe()
            predict_pipeline = PredictPipeline()
            pred = predict_pipeline.predict(final_new_data)

            results = round(pred[0], 2)
            print(f"Prediction result: {results}")

            return render_template('index.html', final_result=results)
        except Exception as e:
            print(f"Error during prediction: {e}")
            return render_template('index.html', final_result="Error during prediction")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
