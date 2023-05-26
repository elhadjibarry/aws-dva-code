## Invoke function synchronously

aws lambda invoke --function-name myTestFunction --payload ewogICJrZXkxIjogInZhbHVlMSIsCiAgImtleTIiOiAidmFsdWUyIiwKICAia2V5MyI6ICJ2YWx1ZTMiCn0= response.json

aws lambda invoke --function-name myTestFunction out

## Invoke function asynchronously

aws lambda invoke --function-name myTestFunction --invocation-type Event --payload ewogICJrZXkxIjogInZhbHVlMSIsCiAgImtleTIiOiAidmFsdWUyIiwKICAia2V5MyI6ICJ2YWx1ZTMiCn0= response.json

