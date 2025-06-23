# 🌐 Multi-Cloud Application – Azure + AWS 🚀

This project demonstrates **interoperability between two cloud platforms**:  
Frontend hosted on **Azure Static Web App**, backend handled by **AWS Lambda** via **API Gateway**.

---

## 📌 Objective

To showcase cross-cloud integration using:
- 🟦 **Azure Static Web App** for frontend hosting
- 🟨 **AWS Lambda + API Gateway** for serverless backend

---

## 🛠 Tech Stack

| Layer     | Service Used                         |
|-----------|--------------------------------------|
| Frontend  | Azure Static Web App (HTML, JS)      |
| Backend   | AWS Lambda (Python) via API Gateway  |
| Communication | HTTP GET Request (Fetch API)     |

---

## 🔁 Flow Diagram
[ User ] → [ Azure Static Web App (HTML Form) ]
↓ HTTP GET
[ AWS API Gateway → Lambda ]
↓
Hello Guest, from AWS Lambda!
---

## 🌍 Live Demo

🔗 [Click here to open live app](https://white-pebble-03e8c8310.2.azurestaticapps.net/)

---

## 💻 Lambda Code (Python)

```python
def lambda_handler(event, context):
    name = event.get('queryStringParameters', {}).get('name', 'Guest')
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': f'Hello {name}, from AWS Lambda!'
    }//your-azure-url-here)
```
*(https://white-pebble-03e8c8310.2.azurestaticapps.net/)*


---

## 🖼️ Screenshots

| Feature             | Screenshot Name              |
|---------------------|------------------------------|
| Frontend UI         | azure-frontend.png           |
| Lambda Response     | lambda-response.png          |
| Cloud Architecture  | architecture-diagram.png     |

---

✅ Outcome
Successfully implemented a multi-cloud interoperable application using:
Azure Static Web App (hosting)
AWS Lambda (backend logic)
API Gateway (communication bridge)
This setup demonstrates real-world cloud integration across platforms.

---
