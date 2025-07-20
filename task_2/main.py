from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient(
    "mongodb+srv://4attye:<password>@clusters.s150f.mongodb.net/",
    server_api=ServerApi('1')
)

db = client.animals


def show_all(database):
    try: 
        result = database.cats.find({})
        for el in result:
            print(el)
    except Exception as e:
        print("Error:", e)


def show_one(database):
    try:
        cat_name = input("Введіть ім'я кота: ")
        result = database.cats.find_one({"name": cat_name})
        print(result if result else "Кіт не знайдений.")
    except Exception as e:
        print("Error:", e)


def update_age(database):
    try:
        cat_name = input("Введіть ім'я кота: ")
        cat_age = input("Введіть вік кота: ")
        database.cats.update_one({"name": cat_name}, {"$set": {"age": cat_age}})
        result = database.cats.find_one({"name": cat_name})
        print(result if result else "Кіт не знайдений.")
    except Exception as e:
        print("Error:", e)


def update_features(database):
    try:
        cat_name = input("Введіть ім'я кота: ")
        cat_features = input("Введіть особливість кота: ")
        database.cats.update_one({"name": cat_name}, {"$push": {"features": cat_features}})
        result = database.cats.find_one({"name": cat_name})
        print(result if result else "Кіт не знайдений.")
    except Exception as e:
        print("Error:", e)


def delete_one(database):
    try:
        cat_name = input("Введіть ім'я кота: ")
        database.cats.delete_one({"name": cat_name})
        result = database.cats.find_one({"name": cat_name})
        print("Кіт видалений." if result is None else "Кіт не знайдений.")
    except Exception as e:
        print("Error:", e)


def delete_all(database):
    try:
        result = database.cats.delete_many({})
        print(f"{result.deleted_count} котів видалено.")
    except Exception as e:
        print("Error:", e)


print("Всі коти:")
show_all(db)
print("\nПошук кота:")
show_one(db)
print("\nОновлення віку кота:")
update_age(db)
print("\nОновлення особливостей кота:")
update_features(db)
print("\nВидалення кота:")
delete_one(db)
print("\nВидалення всіх котів:")
delete_all(db)
