# rest_api_server_home_task
rest_api_server_home_task
Mission 1 :AWS Rest api that stores and retrives data from Dynamo db 
The DynamoDb table
![alt text](https://github.com/dimastar2310/rest_api_server_home_task/blob/main/img/dynamo_db.png)
My lamda function named by serverless_api_lamda that connects to Dynamo db and api gateway and clockwatch by roles, code mantioned in one of the github files.


![alt text](https://github.com/dimastar2310/rest_api_server_home_task/blob/main/img/lamda.png)


Go to api gateway in search bar you see 2 rest apis choose serverless-api2
![alt text](https://github.com/dimastar2310/rest_api_server_home_task/blob/main/img/serverless-api.png)


My api gateway serverless-api2 with Get method choose v2 in Action diployment stage v2 to take the link
![alt text](https://github.com/dimastar2310/rest_api_server_home_task)

Get health method,first of all lets check health method which integrated with lamda function to check if server works,get methods don't require using postman

For checking the health of the server without postman lets take the url that listed in the picutre and past it in web browser if you see blank its means its 1 thaths it works.https://juddkokbrh.execute-api.ap-northeast-1.amazonaws.com/v2/health
for checking the Get product that is we mention our resourse too https://juddkokbrh.execute-api.ap-northeast-1.amazonaws.com/v2/product?_id=10001411,you will get 
response message => _id	"10001411"
For the PUT method open postman switch to put method list in the bode {

    "_id":"10001411"
}

and you will see in the down response body 

{
    "Operation": "Put",
    "Message": "SUCCES",
    "Item": {
        "_id": "10001411"
    }
}

Task2:
Nginx basic web server go to EC2 you will see instanse(virtual machine) you will see there
![alt text](https://github.com/dimastar2310/rest_api_server_home_task/blob/main/img/server.png)

you can see the server by this link thath i provided only for you
18.181.179.153
Iam making change for this github 
![alt text](https://github.com/dimastar2310/rest_api_server_home_task/blob/main/img/server_pic.png)








































