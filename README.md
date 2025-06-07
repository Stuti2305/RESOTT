

# 🍽️ RESOTT – Smart Restaurant Table & Order Management

**RESOTT** is a full-stack web application designed to revolutionize the dining experience by eliminating long wait times for tables and food. Whether you're a customer looking for a seamless dine-in experience, a restaurant owner aiming to streamline operations, or an administrator overseeing multiple establishments — RESOTT is built for you.

---

## 🚀 Project Highlights

### 🔑 Key Features

- 🪑 **Table Reservation System**  
  Customers can reserve specific tables at their favorite restaurants ahead of time.

- 🍔 **Advance Food Ordering**  
  Diners can pre-order their meals so food is ready when they arrive.

- 💳 **Secure Payment Gateway Integration**  
  Built-in PayPal integration enables fast and safe online payments.

- 📊 **Restaurant Owner Dashboard**  
  Manage listings, availability, menus, and incoming orders in one place.

- 🛠️ **Admin Panel**  
  Full control over restaurants, users, and platform-wide operations.

---

## 🛠️ Technology Stack

| Layer        | Technology |
|--------------|------------|
| **Backend**  | Python 3.x, Django 4.0.1 |
| **Database** | PostgreSQL |
| **Frontend** | HTML, CSS, JavaScript (Django Templates) |
| **Auth**     | Django Built-in Auth, Custom Profiles |
| **Payments** | Django PayPal v2.0, IPN (Instant Payment Notification) |
| **Media**    | Pillow 9.0.1, Django File/Image Handling |
| **HTTP**     | Requests 2.27.1, urllib3 1.26.9 |
| **Web Server**| ASGI |

---

## 🧩 System Modules

### 🏢 Restaurant Management
- Manage restaurant profiles with:
  - Name, location, overview, contact info, hours, and directions
  - Google Maps integration
  - Up to 3 images per restaurant
  - Real-time status (full/not full)
  - Discount support (`dis` field)

### 📋 Menu Management
- Organize food into **course categories**
- Add food items and combos with:
  - Descriptions, prices, images
  - Course type association
  - Restaurant-level filtering

### 🛒 Cart & Order System
- Real-time cart management:
  - Quantity tracking
  - Checkout status
- Order processing with:
  - Invoices
  - Multi-item handling
  - Time-stamped order history

### 📆 Table Booking
- Book tables by:
  - Date, time, number of guests
  - Contact info and restaurant preference
  - Timestamped reservations

### ⭐ Feedback System
- Collect and display:
  - User ratings & reviews
  - Profile-linked feedback
  - Timestamps for transparency

### 👥 User Management
- Django User Authentication
- Custom profile handling
- Role-based relationships:
  - Customers, Restaurant Owners, Admins

---

## 🎯 Why RESOTT?

- ⏱️ **Save Time**: Skip the line by reserving tables and ordering food in advance.
- 💼 **Optimize Operations**: Give restaurants better visibility into upcoming reservations and orders.
- 📈 **Scalable**: Built with robust technologies to handle concurrent transactions and real-world usage.

---



## 🧪 Setup & Installation



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
