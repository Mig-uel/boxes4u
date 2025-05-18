## Boxes4U - E-Commerce Website (Full-Stack Project)

This is my second project in a [QCC Software Engineering Full Stack Web Development bootcamp](https://github.com/Mig-uel/ACE1025) where I built a fully functional **e-commerce web application** using both front-end and back-end technologies. The app simulates a real online shopping experience — from product browsing and cart management to user authentication and order confirmation.
The project was developed as part of the curriculum to solidify my understanding of full-stack development concepts and practices.

---

## 🔧 Tech Stack

- **Front-End**:
  - HTML
  - HTMX
  - Tailwind CSS
- **Back-End**:
  - Python
  - Flask
    - Flask-SQLAlchemy
    - Flask-Session
    - Flask-Migrate
  - SQLAlchemy
- **Database**:
  - PostgreSQL
- **Deployment**:
  - Render
  - GitHub
  - Supabase
- **Version Control**:
  - Git
  - GitHub
- **Other Tools**:
  - VS Code

---

## 💡 Features

### 🛍️ Product Catalog

- Includes **at least two categories** (e.g., _Electronics_, _Clothing_)
- Each category shows **at least six products**
- Each product displays:
  - Name
  - Image
  - Price
  - Quantity input
  - "Add to Cart" button

### 🛒 Shopping Cart

- Shows all items added by the user
- Users can:
  - Remove individual items
  - See the total cost (including tax and shipping/handling)
- Includes:
  - **Sign Up** button for new customers
  - **Login** button for returning users

### 👤 User Registration & Login

- Registration form collects:
  - First Name
  - Last Name
  - Email
  - Username
  - Password
  - Confirm Password
    - Passwords are hashed for security
- Checks for **duplicate usernames or emails**
- After registration, users are redirected to the **Home Page**
- Successful login redirects to the **Checkout Page**

### ✅ Checkout & Order Confirmation

- The Checkout Page shows:
  - Cart items
  - Total cost (with tax and shipping)
  - “Submit Order” button
- On submitting the order:
  - User is redirected to a **Completed Order** page
  - Displays a confirmation message with a **randomly generated Order Number**
  - Simulates that payment and shipping info were already provided

---

## 🗃️ Database Schema

### `user` Table

| Field      | Type         | Notes                                      |
| ---------- | ------------ | ------------------------------------------ |
| id         | Serial       | Primary key, auto-incrementing             |
| first_name | Varchar(25)  | Required                                   |
| last_name  | Varchar(25)  | Required                                   |
| username   | Varchar(8)   | Required, unique                           |
| email      | Varchar(50)  | Required, unique                           |
| password   | Varchar(128) | Required, hashed                           |
| isAdmin    | Boolean      | Optional                                   |
| address    | JSON         | Optional, stores structured address object |
| uuid       | UUID         | Optional, unique                           |

---

### `product` Table

| Field       | Type          | Notes                                  |
| ----------- | ------------- | -------------------------------------- |
| id          | Serial        | Primary key, auto-incrementing         |
| name        | Varchar(50)   | Required                               |
| description | Text          | Optional                               |
| price       | Numeric(10,2) | Required                               |
| stock       | Integer       | Optional, quantity available           |
| image_url   | Varchar(255)  | Optional, image link                   |
| category_id | Integer       | Foreign key to `category.id`, required |
| uuid        | UUID          | Optional, unique                       |

---

### `order` Table

| Field       | Type          | Notes                                    |
| ----------- | ------------- | ---------------------------------------- |
| id          | Serial        | Primary key, auto-incrementing           |
| user_id     | Integer       | Foreign key to `user.id`, required       |
| created_at  | Timestamp     | Optional                                 |
| status      | Varchar(20)   | Optional, e.g., `'pending'`, `'shipped'` |
| total_price | Numeric(10,2) | Required                                 |
| uuid        | UUID          | Optional, unique                         |

---

### `order_item` Table

| Field      | Type          | Notes                                                   |
| ---------- | ------------- | ------------------------------------------------------- |
| id         | Serial        | Primary key, auto-incrementing                          |
| order_id   | Integer       | Foreign key to `order.id`, required, cascades on delete |
| product_id | Integer       | Foreign key to `product.id`, required                   |
| qty        | Integer       | Required, number of units                               |
| price      | Numeric(10,2) | Required, unit price at the time of order               |
| uuid       | UUID          | Optional, unique                                        |

---

### `category` Table

| Field | Type   | Notes                          |
| ----- | ------ | ------------------------------ |
| id    | Serial | Primary key, auto-incrementing |
| name  | Text   | Required, unique               |
| uuid  | UUID   | Optional, unique               |

---

## 🎯 Project Goals

The goal was to bring together the core building blocks of a full-stack application by:

- Creating an interactive, styled front-end
- Building secure and functional back-end routes
- Managing user sessions and validations
- Integrating a relational database
- Delivering a complete e-commerce flow

By completing this project, I now have a strong foundation for building and deploying dynamic, database-driven web applications.

---

## 📸 Screenshots

_(Screenshots of catalog page, cart page, registration form, and order confirmation coming soon!)_

---

## 🌐 Live Demo

You can check out the live version of the app here:  
👉 [https://boxes4u.onrender.com](https://boxes4u.onrender.com)

---

## 🙏 Acknowledgments

- Special thanks to my instructor Hui Wu and peers at [QCC Software Engineering Bootcamp](https://www.qcc.edu/) for their support and guidance throughout this project.
- [QCC Software Engineering Bootcamp](https://www.qcc.edu/) provided the foundational knowledge and skills necessary for the successful completion of this project.

---
