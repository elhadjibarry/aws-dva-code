## Run the API using this URL format:

https://6q1nvk6nl9.execute-api.us-east-1.amazonaws.com/prod/helloworld?name=Elhadji&city=Mtl

## Or use curl:

curl -v -X POST "https://6q1nvk6nl9.execute-api.us-east-1.amazonaws.com/prod/helloworld?name=Elhadji&city=Mtl" -H "content-type: application/json" -H "day: Sunday" -d "{ \"time\": \"Afternoon\" }"