# way to upload image: endpoint
# way to save the image
# function to make prediction on the image
# show the results
import pickle
import json
import numpy as np
from sklearn.preprocessing import StandardScaler

from flask import Flask
from flask import request
from flask import render_template


classifier = pickle.load(open('./models/knn_model.pickle','rb'))
scaler = StandardScaler()

app = Flask(__name__)


def predict(request_json, classifier, scaler):
    male = request_json['male']
    age = request_json['age']
    salary = request_json['salary']
    price = request_json['price']
    row_values = [male, age, salary, price]
    x_new = np.array(row_values).reshape(-1,1)
    x_new_scale2 = scaler.fit_transform(x_new).reshape(1,-1)
    y_new_pred = classifier.predict(x_new_scale2)
    prediction = 'Yes' if y_new_pred[0] == 1 else 'No'

    return "Is this person going to purchase this product? {}".format(prediction)


@app.route("/", methods=["GET", "POST"])
def upload_predict():
    if request.method == "POST":
        input_data = request.form['input_data']
        if input_data:
            json_data = json.loads(input_data)
            pred = predict(json_data, classifier, scaler)
            # return render_template("index.html", prediction=pred)
            return pred, 200
    # return render_template("index.html", prediction="Is this person going to purchase this product? ")
    return "Is this person going to purchase this product? ", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

