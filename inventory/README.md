# Social Networking API

This project is a Simple Inventory Management application built using Django and Django REST Framework (DRF). The API provides functionalities such as user authentication, login, add items, delete items, update items.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Prerequisites](#Prerequisites)
- [Setup](#setup)
- [API Endpoints](#api-endpoints)

## Features

- **JWT Authentication**: Secure user authentication using JSON Web Tokens.
- **User Search**: Search users by email or name with pagination.
- **Friend Requests**: Send, accept, reject, and list friend requests.
- **User Management**: Manage user profiles and friendships.

## Installation

### Prerequisites

- Python 3.12.4
- Django 5.1
- Django REST Framework 3.15.2
- PostgreSQL 
   
   Note - before goint to setup please create database in postgresql and add credentials in .env file
### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/.git
   cd social-networking-api
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver

### api-endpoints

    ### signup
        url: http://127.0.0.1:8000/users/signup/
        method: POST
        body: {
            "email":"test2@gmail.com",
            "name":"test2", 
            "password":"test2"
            }
        response: {
            "id": 3,
            "email":"test2@gmail.com",
            "name":"test2",
            "message": "User created successfully!"
            }
    
    ### login
        url: http://127.0.0.1:8000/users/login/
        method: POST
        body: {
            "email":"test2@gmail.com",
            "name":"test2", 
            "password":"test2"
            }
        response: {
            "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNzYyMjc1NSwiaWF0IjoxNzI3NTM2MzU1LCJqdGkiOiI4M2E5OGE4MmFhMWY0NDdkODQwNWIxMmNhNTg4NDViYiIsInVzZXJfaWQiOjJ9.KuDK4Zq1VnPcQFNjB-sLHHc9tU_nMl5pZ7JCuM8imoQ",
            "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI3NTM2NjU1LCJpYXQiOjE3Mjc1MzYzNTUsImp0aSI6IjhmMjViZDkzOTU4ZTQ2NDRiNzAzMzYwYmIyNDc1ZDJlIiwidXNlcl9pZCI6Mn0.s_K_CcI6Ec8gaHuO_Bq0Ba57ZJ5MKrvYz72NguO_QbM",
            "user": {
                "id": 2,
                "name": "test2",
                "email": "test2@gmail.com"
            }
            }
    
    ### add item
        url: http://127.0.0.1:8000/users/add_item/
        method: POST
        Query Parameters: {
            "name":"loptop5",
            "quantity":4,
            "description":"diewjjrwioiwe",
            "price":73747
            }
        response: {
            "id": 5,
            "name": "loptop5",
            "description": "diewjjrwioiwe",
            "quantity": 4,
            "price": "73747.00",
            "is_active": true,
            "created_at": "2024-09-28T15:24:13.756016Z",
            "updated_at": null,
            "created_by": 1,
            "updated_by": null
            }

    ### update item 
        url: http://127.0.0.1:8000/users/update_items/1/
        method: POST
        body: {
            "name": "loptop",
            "description": "123456789098765432345678",
            "quantity": 10,
            "price": "73747.00",
            "created_by": 2,
            "updated_by": null,
            "created_at": "2024-09-27T16:38:03.268825Z",
            "updated_at": null
            }
        response:{
            "id": 1,
            "name": "loptop",
            "description": "123456789098765432345678",
            "quantity": 10,
            "price": "73747.00",
            "is_active": true,
            "created_at": "2024-09-28T15:15:52.412755Z",
            "updated_at": "2024-09-28T15:38:03.149399Z",
            "created_by": 2,
            "updated_by": 1
            }
    

    ### get
        url: http://127.0.0.1:8000/users/items/2/
        method: GET
        response: [
            {
                "id": 2,
                "name": "loptop2",
                "description": "diewjjrwioiwe",
                "quantity": 4,
                "price": "73747.00",
                "is_active": true,
                "created_at": "2024-09-28T15:17:18.647654Z",
                "updated_at": null,
                "created_by": 1,
                "updated_by": null
            }
            ]

    ### delete
        url: http://127.0.0.1:8000/users/delete/1/
        method: DELETE
        response: {
            "message": "Item deleted successfully."
            }    

