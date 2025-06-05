## CREATE LAYER
- Membuat folder python
```
mkdir python
```
- Membuat virtual environtmet
```
python3 -m venv venv
```
atau
```
python -m venv venv
```
- Aktivasi folder virtual environment
```
source venv/bin/activate # Di Linux/macOS
```
atau
```
.\venv\Scripts\activate # Di Windows (PowerShell)
```
- Install pymysql
```
pip install pymysql -t python/
```
- Kompres folder python yang berisi pymysql
```
zip -r layer.zip python/
```

## INVOKE
### GET
```
{
  "httpMethod": "GET",
  "path": "/tasks",
  "headers": {
    "Content-Type": "application/json"
  },
  "queryStringParameters": null,
  "pathParameters": null,
  "body": null
}
```
### POST
```
{
  "httpMethod": "POST",
  "path": "/tasks",
  "headers": {
    "Content-Type": "application/json",
    "Accept": "application/json"
  },
  "queryStringParameters": null,
  "pathParameters": null,
  "requestContext": {
    "resourcePath": "/tasks",
    "httpMethod": "POST",
    "identity": {
      "sourceIp": "192.0.2.1"
    }
  },
  "body": "{\"title\": \"Mengerjakan Proyek Go Backend\", \"description\": \"Selesaikan semua fitur API untuk To-Do List\", \"due_date\": \"2025-06-30\", \"priority\": \"High\", \"completed\": false}",
  "isBase64Encoded": false
}
```
### GET {id}
```
{
  "httpMethod": "GET",
  "path": "/tasks/123",
  "headers": {
    "Content-Type": "application/json"
  },
  "queryStringParameters": null,
  "pathParameters": {
    "id": "123"
  },
  "body": null
}
```
### PUT {id}
```
{
  "httpMethod": "PUT",
  "path": "/tasks/1",
  "headers": {
    "Content-Type": "application/json",
    "Accept": "application/json"
  },
  "queryStringParameters": null,
  "pathParameters": {
    "id": "1"
  },
  "requestContext": {
    "resourcePath": "/tasks/{id}",
    "httpMethod": "PUT",
    "identity": {
      "sourceIp": "192.0.2.1"
    }
  },
  "body": "{\"title\": \"Mengerjakan Proyek Go Backend - SELESAI\", \"description\": \"Semua fitur API telah diimplementasikan dan diuji.\", \"completed\": true, \"priority\": \"High\"}",
  "isBase64Encoded": false
}
```
### DELETE {id}
```
{
  "httpMethod": "DELETE",
  "path": "/tasks/1",
  "headers": {
    "Accept": "*/*"
  },
  "queryStringParameters": null,
  "pathParameters": {
    "id": "1"
  },
  "requestContext": {
    "resourcePath": "/tasks/{id}",
    "httpMethod": "DELETE",
    "identity": {
      "sourceIp": "192.0.2.1"
    }
  },
  "body": null,
  "isBase64Encoded": false
}
```



