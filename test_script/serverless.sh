curl -X POST \
  https://us-west1-windy-fortress-419600.cloudfunctions.net/cmpt756-g15-serverless-ml-app \
  -H 'Content-Type: application/json' \
  -d '{
    "male":0,
    "age":49,
    "salary":61000,
    "price":2000
}'
