import json
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler

def handler(event, context):
    try:
        # Load model and scaler
        regmodel = pickle.load(open('functions/model/regmodel.pkl', 'rb'))
        scaler = pickle.load(open('functions/model/scaling.pkl', 'rb'))

        # Get JSON input from request
        body = json.loads(event['body'])
        data = np.array(list(body.values())).reshape(1, -1)

        # Scale input and make prediction
        new_data = scaler.transform(data)
        output = regmodel.predict(new_data)[0]

        return {
            'statusCode': 200,
            'body': json.dumps({"prediction": float(output)})
        }

    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({"error": str(e)})
        }
