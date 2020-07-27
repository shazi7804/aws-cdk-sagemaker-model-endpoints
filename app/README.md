# AWS SageMaker Invoke endpoint service 

## Default

- endpoint_name = 'demoEndpoint'

## Run service

```
$ pip install -r requirements.txt
$ python app.py
```

## How to invoke endpoint

request page `http://localhost` with `keyword` parameter insert

```
curl "http://localhost/?keyword='今天天氣真好'" | jq '.'
```

response `score: 0.2800988256931305` 

```
{
  "body": "{\"endpoint_name\": \"demoEndpoint\", \"score\": \"0.2800988256931305\"}",
  "statusCode": 200
}
```

## Author

@shazi7804