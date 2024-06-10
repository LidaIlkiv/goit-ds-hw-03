from pymongo import MongoClient, errors
from pymongo.server_api import ServerApi

try:
    client = MongoClient(
        "mongodb+srv://ilkivlidavol:Ilkiv1lida1vol@ilkivlida.vuvn8rt.mongodb.net/?retryWrites=true&w=majority&appName=IlkivLida",
        server_api=ServerApi('1')
    )

    db = client.cats
    data_db_cats = db.cats.insert_many(
        [
            {
                "name": "Lama",
                "age": 2,
                "features": ["ходить в лоток", "не дає себе гладити", "сірий"],
            },
            {
                "name": "Liza",
                "age": 4,
                "features": ["ходить в лоток", "дає себе гладити", "білий"],
            },
            {
                "name": "Barsik",
                "age": 3,
                "features": ["ходить в капці", "дає себе гладити", "рудий"]
            },
            {
                "name": "Mila",
                "age": 2,
                "features": ["ходить в лоток", "шипить на чужих", "сірий"]
            }

        ]
    )
    def read_all_data_db():
        result = db.cats.find({})
        for el in result:
            print(el)

    def read_info_one_cat(cat):
        result = db.cats.find_one({"name": cat})
        print(result)

    def update_age_one_cat(cat, new_age):
        db.cats.update_one({"name": cat}, {"$set": {"age": new_age}}, upsert = False)
        result = db.cats.find_one({"name": cat})
        print(result)      

    def add_feature_one_cat(cat, new_feature):
        db.cats.update_one({"name": cat}, {"$push": {"features": new_feature}})
        result = db.cats.find_one({"name": cat})
        print(result)


    def delete_record(cat):
        db.cats.delete_one({"name" : cat})

    def delete_all_records():
        result = db.cats.find({})
        for el in result:
            db.cats.delete_one(el)

except errors.ConnectionError:
        print("Відсутнє з'єднання з сервером MongoDB")
except errors.OperationFailure:
        print("Перевірте права доступу або налаштування сервера")
except errors.ConfigurationError:
        print("Проблема з конфігурацією")
except errors.InvalidName as e:
        print(f"Неправильне ім'я бази даних або колекції: {e}")
except Exception as e:
        print(f"Виникла  помилка: {e}")


