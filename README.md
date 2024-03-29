# Cloud Resume Backend
The cloud resume challenge backend serves the website with the visitor count through a REST API. It consist of the following AWS cloud services, lambda function, API gateway and Dynamo DB.

Dynamo db, a NoSQL database, stores the visitor count, lambda function has the python code that fetches, increments and updates the visitor count on the database. 

The API gateway has the REST API that receives requests, triggers the lambda function which responds with the visitor count which the API then responds to the website with the count as seen from below architecture diagram. 

The repo also contains a Github action that packages the python code and uploads to lambda function.

![Architecture Diagram](MarkdownFiles/Architecture-Diagram.png)