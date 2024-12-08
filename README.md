
# Sanjeev's Favorite Drink API 🥤


Hosted at : https://huggingface.co/spaces/SanjeevB1/Drinks

This is a REST API with full CRUD (Create, Read, Update, Delete) operations that lets you manage a list of drinks. It is hosted on Hugging Face Spaces and serves as a fun way to access and explore my favorite drinks. 🍹

The API includes features such as retrieving the list of all drinks, getting details of a specific drink, adding new drinks, and deleting them. Note that due to the hosting limitations of Hugging Face Spaces, **POST** and **DELETE** operations are currently disabled. 🚫

---

## 📋 API Summary

| HTTP Method | Endpoint          | Description                                        |
|-------------|-------------------|----------------------------------------------------|
| **GET**     | `/`               | Returns a list of all drinks.                     |
| **GET**     | `/drinks`         | Same as `/`, returns all drinks.                  |
| **GET**     | `/drinks/<id>`    | Returns details of a specific drink by its ID.    |
| **POST**    | `/drinks`         | Add a new drink (not supported on Hugging Face).  |
| **DELETE**  | `/drinks/<id>`    | Delete a drink (not supported on Hugging Face).   |

---

## 📘 Database Design

| Column       | Type      | Description                               |
|--------------|-----------|-------------------------------------------|
| **id**       | INTEGER   | Unique identifier (Primary Key).          |
| **name**     | STRING(80)| Name of the drink (must be unique).        |
| **description** | STRING(120) | Short description of the drink.          |

---

## 🚀 How It Works

The API uses Flask and SQLAlchemy. The data is stored in a SQLite database. 🛠 Flask handles the incoming HTTP requests, queries the database, and returns the corresponding responses. CRUD operations can be performed locally, while only **GET** operations are supported on Hugging Face Spaces due to the read-only database restrictions. 📂

---

## 🖱️ Usage Instructions

### 1️⃣ View All Drinks
**Method**: `GET`  
**URL**: [https://sanjeevb1-drinks.hf.space/drinks](https://sanjeevb1-drinks.hf.space/drinks)  

**Example Response**:  
```json
{
    "drinks": [
        {
            "name": "Diet Coke",
            "description": "Tastes like Coke with no calories, great!!!"
        },
        {
            "name": "Fanta",
            "description": "Like the taste and color of it"
        }
    ]
}
```

---

### 2️⃣ View a Specific Drink
**Method**: `GET`  
**URL**: [https://sanjeevb1-drinks.hf.space/drinks/1](https://sanjeevb1-drinks.hf.space/drinks/1)  

**Example Response**:  
```json
{
    "name": "Diet Coke",
    "description": "Tastes like Coke with no calories, great!!!"
}
```

---

### 3️⃣ Add a New Drink (🚫 Not Supported on Hugging Face Spaces)
**Method**: `POST`  
**URL**: `/drinks`  
**Body (JSON)**:  
```json
{
    "name": "Mango Juice",
    "description": "Sweet and refreshing"
}
```

---

### 4️⃣ Delete a Drink (🚫 Not Supported on Hugging Face Spaces)
**Method**: `DELETE`  
**URL**: `/drinks/1`

---

## 🛑 Note

⚠️ **POST** and **DELETE** requests won't work on Hugging Face Spaces because the database is read-only. You can clone this repository and run it locally to enable all CRUD operations. 💻

---

## 👤 Author

Sanjeev's Favorite Drinks API is designed to provide an interactive experience with REST API operations while sharing a taste of my favorite drinks. 🍹 Cheers! 🥂
```

Let me know if you need further adjustments! 😊
