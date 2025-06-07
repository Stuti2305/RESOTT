# 🍽️ RESOTT – Restaurant Reservation & Ordering System

**RESOTT** is a full-stack web application designed to streamline restaurant operations and enhance customer dining experiences. It reduces waiting times and improves order and reservation management by integrating a complete restaurant management system.

---

## 🚀 Features

### 🧑‍🍳 For Customers:
- 📅 **Table Reservation:** Book tables at your preferred restaurants in advance.
- 🍔 **Advance Food Ordering:** Pre-order meals and have them ready upon arrival.
- 💳 **Secure Payments:** Seamless online transactions via PayPal integration.
- 🔍 **Restaurant Discovery:** Browse restaurants, view menus, check timings, and get directions.
- 🛒 **Cart & Orders:** Add food to cart, place orders, track status, and view order history.
- ⭐ **Feedback System:** Rate and review your dining experience.

### 🏪 For Restaurant Owners:
- 🛠️ **Manage Listings:** Update restaurant details, timings, status (full/available), and images.
- 📋 **Menu Management:** Add/edit dishes and combos with categories, images, and prices.
- 📦 **Order Management:** Track customer orders in real time.
- 📊 **Dashboard:** View table bookings, incoming orders, and customer feedback.

### 🧑‍💼 For Admins:
- 🧾 **Platform Oversight:** Monitor all restaurant listings and platform operations via an admin panel.

---

## 🧱 Tech Stack

### Backend:
- **Python 3.x**
- **Django 4.0.1**
- **PostgreSQL** – Efficient handling of concurrent transactions
- **ASGI** – For asynchronous request handling

### Frontend:
- **HTML5**, **CSS3**, **JavaScript**
- **Django Templates**

### Libraries & Integrations:
- 🖼️ **Pillow 9.0.1** – Image processing
- 🌐 **Requests 2.27.1**, **urllib3 1.26.9** – HTTP operations
- 💰 **Django PayPal 2.0**, **PayPal IPN** – Payment processing
- 🔐 **Django Authentication** – User login and registration
- 🗃️ **Custom User Profiles** – Extended user functionality

---

## 🛠️ Installation

### Prerequisites:
- Python 3.x
- PostgreSQL
- pip (Python package manager)
- Virtual environment (optional but recommended)

### Steps:
```bash
# Clone the repository
git clone https://github.com/your-username/resott.git
cd resott

# Create virtual environment and activate
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (for admin access)
python manage.py createsuperuser

# Run the server
python manage.py runserver
