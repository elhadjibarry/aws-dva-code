curl https://5lqqe1gq7g.execute-api.us-west-2.amazonaws.com/dev/movies -H "Content-Type: application/json" -X DELETE -d "{
  \"year\": 1972,
  \"title\": \"The Godfather\",
  \"actors\": \"Testactor\",
  \"rating\": \"9.2\",
  \"plot\": \"The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.\"
}"

curl https://5lqqe1gq7g.execute-api.us-west-2.amazonaws.com/dev/movies/Testmovie -H "Content-Type: application/json" -X DELETE