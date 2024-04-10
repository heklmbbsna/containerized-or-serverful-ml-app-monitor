import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler

def if_purchase_prediction(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """

    # Get response
    request_json = request.get_json()
	
    # Make Prediction
    serverless_classifier = pickle.load(open('knn_model.pickle','rb'))
    serverless_scaler = StandardScaler()
    male = request_json['male']
    age = request_json['age']
    salary = request_json['salary']
    price = request_json['price']
    row_values = [male, age, salary, price]
    x_new = np.array(row_values).reshape(-1,1)
    x_new_scale2 = serverless_scaler.fit_transform(x_new).reshape(1,-1)
    y_new_pred = serverless_classifier.predict(x_new_scale2)
    prediction = 'Yes' if y_new_pred[0] == 1 else 'No'

    return "Is this person going to purchase this product? {} \n".format(prediction)
