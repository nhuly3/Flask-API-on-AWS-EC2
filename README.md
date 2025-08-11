# Homework 5 - Trucking Company Flask

---

## Deployment URL
http://3.82.94.68:8000/

---

## Files

myapp/
├── app.py                  # Main Flask application
├── truckinglist.json       # Data 

---

## Steps


```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```


```bash
python app.py
```


```bash
nohup gunicorn -b 0.0.0.0:8000 app:app &
```

---

##GET `/companies`

```bash
curl http://3.82.94.68:8000/companies
```

**Example Output**

```json
{
  "UPS": {
    "Company": "UPS",
    "Services": "Logistics, Shipping",
    "Hubs": {
      "New York": "JFK",
      "Los Angeles": "LAX"
    },
    "Revenue": "$30,000",
    "HomePage": "https://ups.com",
    "Logo": "https://example.com/ups-logo.png"
  }
}
```

---

## GET `/companies/<name>`

```bash
curl http://3.82.94.68:8000/companies/UPS
```

**Example Output**

```json
{
  "UPS": {
    "Company": "UPS",
    "Services": "Logistics, Shipping",
    "Hubs": {
      "New York": "JFK",
      "Los Angeles": "LAX"
    },
    "Revenue": "$30,000",
    "HomePage": "https://ups.com",
    "Logo": "https://example.com/ups-logo.png"
  }
}
```

---

##POST `/companies`


```bash
curl -X POST http://3.82.94.68:8000/companies \
  -H "Content-Type: application/json" \
  -d '{
        "Company": "New Truck Co",
        "Services": "Logistics",
        "Hubs": {"Dallas": "DAL Hub"},
        "Revenue": "$15,000",
        "HomePage": "https://newtruckco.com",
        "Logo": "https://example.com/newtruck-logo.png"
      }'
```

**Example Output**

```json
{
  "message": "Company New Truck Co added"
}
```

---

## PUT `/companies/<name>`

```bash
curl -X PUT http://3.82.94.68:8000/companies/UPS \
  -H "Content-Type: application/json" \
  -d '{"Revenue": "$35,000"}'
```

**Example Output**

```json
{
  "message": "Company UPS updated"
}
```

---

## DELETE `/companies/<name>`


```bash
curl -X DELETE http://3.82.94.68:8000/companies/New%20Truck%20Co
```

**Example Output**

```json
{
  "message": "Company New Truck Co deleted"
}
```

---

## Author

Ngan Nhu Ly  
