from flask import Flask, render_template, jsonify, redirect, request
import boto3
import json
import sys, os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'app/nlp_processing'))
from segmenter import JiebaSegmenter

endpoint_name = 'demoEndpoint'

app = Flask(__name__)

client = boto3.client('runtime.sagemaker')
segmenter = JiebaSegmenter()

@app.route('/', methods=['GET'])
def get_prediction_by_get():
    keyword = request.args.get('keyword')
    toks = segmenter.segment(keyword)
    
    tokenized_sentences = [' '.join(toks)]
    payload = {"instances" : tokenized_sentences}

    response = client.invoke_endpoint(
			EndpointName=endpoint_name,
			Body=json.dumps(payload),
			ContentType='application/json'
		)

    prediction = response['Body'].read().decode()
    score = str(json.loads(prediction)[0]['prob'][0])

    return {
        "statusCode": 200,
        "body": json.dumps({
            "endpoint_name": endpoint_name,
            "score": score
        }),
    }


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, threaded=True)

