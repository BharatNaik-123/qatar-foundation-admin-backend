# 🚀 Qatar Foundation Admin Portal – Backend

<p align="center">
  <img src="https://img.shields.io/badge/Flask-Backend-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Auth-Flask--Login-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Database-SQLite-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge" />
</p>

---

## 📌 Overview

This project is a **Flask-based RESTful backend** developed for managing opportunities in an admin portal.
It implements **secure authentication**, **user-based access control**, and a **complete CRUD workflow**.

The system ensures:

* Only authenticated users can access APIs
* Users can only manage **their own data**
* Clean, predictable API responses following REST standards

---

## ✨ Key Highlights

* 🔐 Session-based authentication (Flask-Login)
* 🛡️ Secure password hashing (Werkzeug)
* 🔄 Full CRUD operations
* 👤 Ownership-based authorization
* 📦 Modular architecture (routes, utils, models)
* 🧪 Thoroughly tested with edge cases

---

## 🧰 Tech Stack

| Layer    | Technology             |
| -------- | ---------------------- |
| Backend  | Flask                  |
| ORM      | Flask-SQLAlchemy       |
| Auth     | Flask-Login            |
| Database | SQLite                 |
| Security | Werkzeug, itsdangerous |

---

## 📂 Project Structure

```id="projstruct"
qatar_foundation_admin/
│
├── app.py
├── config.py
├── models.py
├── requirements.txt
│
├── routes/
│   ├── auth_routes.py
│   └── opportunity_routes.py
│
├── utils/
│   ├── token.py
│   └── validators.py
│
└── README.md
```

---

## ⚙️ Setup & Run

### 1️⃣ Clone Repository

```id="clonecmd"
git clone <git clone https://github.com/yourusername/qatar-foundation-admin-backend.git>
cd qatar_foundation_admin
```

### 2️⃣ Create Virtual Environment

```id="venvcmd"
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```id="installcmd"
pip install -r requirements.txt
```

### 4️⃣ Run Server

```id="runcmd"
python app.py
```

👉 Server runs at:

```id="serverurl"
http://127.0.0.1:5000
```

---

## 🔐 Authentication Flow

```id="authflow"
Signup → Login → Session Cookie → Access Protected Routes → Logout
```

* Uses **session cookies**
* No token required for each request
* Automatically handled by Flask-Login

---

## 📬 API Endpoints

### 🔐 Auth

| Method | Endpoint           | Description          |
| ------ | ------------------ | -------------------- |
| POST   | `/signup`          | Register user        |
| POST   | `/login`           | Login user           |
| POST   | `/logout`          | Logout               |
| POST   | `/forgot-password` | Generate reset token |

---

### 📦 Opportunities (Protected)

| Method | Endpoint                  | Description |
| ------ | ------------------------- | ----------- |
| GET    | `/api/opportunities`      | Get all     |
| POST   | `/api/opportunities`      | Create      |
| GET    | `/api/opportunities/<id>` | Get one     |
| PUT    | `/api/opportunities/<id>` | Update      |
| DELETE | `/api/opportunities/<id>` | Delete      |

---

## 🧪 Example API Usage

### 🔹 Signup

```bash id="signupcurl"
curl -X POST http://127.0.0.1:5000/signup \
-H "Content-Type: application/json" \
-d '{"full_name":"Bharat","email":"bharat@test.com","password":"test1234"}'
```

---

### 🔹 Login

```bash id="logincurl"
curl -X POST http://127.0.0.1:5000/login \
-H "Content-Type: application/json" \
-d '{"email":"bharat@test.com","password":"test1234"}'
```

---

### 🔹 Create Opportunity

```bash id="createcurl"
curl -X POST http://127.0.0.1:5000/api/opportunities \
-H "Content-Type: application/json" \
-d '{"title":"Frontend Internship","category":"Internship","duration":"3 months"}'
```

---

### 🔹 Get Opportunities

```bash id="getcurl"
curl http://127.0.0.1:5000/api/opportunities
```

---

## 🛡️ Security Features

* Password hashing (Werkzeug)
* Session-based authentication
* Route protection with `@login_required`
* Ownership validation (user-specific data)
* Safe error handling
* Token-based password reset with expiration

---

## 🧪 Testing Strategy

Tested using **Postman** with:

* ✅ Authentication flow
* ✅ CRUD operations
* ✅ Unauthorized access
* ✅ Invalid inputs
* ✅ Edge cases (missing fields, wrong IDs, duplicate users)

---

## ⚠️ Limitations

* Backend only (no frontend UI)
* Uses SQLite (can be replaced with PostgreSQL/MySQL)
* No email service for password reset (console output only)

---

## 🚀 Possible Improvements

* JWT-based authentication
* Swagger / OpenAPI documentation
* Deployment (Render / Railway)
* Rate limiting & logging
* Pagination & filtering

---

## 👨‍💻 Author

**Bharat Naik**

---

## ✅ Status

✔ Completed
✔ Tested (including edge cases)
✔ Ready for submission

---
