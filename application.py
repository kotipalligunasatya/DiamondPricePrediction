from flask import Flask,request,render_template,jsonify
from src.pipelines.prediction_pipeline import CustomData,PredictPipeline


application=Flask(__name__)

app=application

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])

def predict_datapoint():
    if request.method=='GET':
        return render_template('index.html')
    
    else:
        data=CustomData(
            carat=float(request.index.get('carat')),
            depth = float(request.index.get('depth')),
            table = float(request.index.get('table')),
            x = float(request.index.get('x')),
            y = float(request.index.get('y')),
            z = float(request.index.get('z')),
            cut = request.index.get('cut'),
            color= request.index.get('color'),
            clarity = request.index.get('clarity')
        )
        final_new_data=data.get_data_as_dataframe()
        predict_pipeline=PredictPipeline()
        pred=predict_pipeline.predict(final_new_data)

        results=round(pred[0],2)

        return render_template('index.html',final_result=results)
    

if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)
