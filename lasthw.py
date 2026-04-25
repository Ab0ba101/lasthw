import sqlite3

# Створення бази даних та з'єднання
conn = sqlite3.connect('FruitBasket.db')
cursor = conn.cursor()

# Створення таблиці Fruits
cursor.execute('''
CREATE TABLE Fruits (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    FruitName TEXT NOT NULL,
    Color TEXT NOT NULL
)
''')

# Вставка записів
cursor.execute("INSERT INTO Fruits (FruitName, Color) VALUES ('Apple', 'Red')")
cursor.execute("INSERT INTO Fruits (FruitName, Color) VALUES ('Banana', 'Yellow')")
cursor.execute("INSERT INTO Fruits (FruitName, Color) VALUES ('Orange', 'Orange')")

# Зміна кольору фрукта "Apple" на "Green"
cursor.execute("UPDATE Fruits SET Color = 'Green' WHERE FruitName = 'Apple'")

# Вибір всіх фруктів, які жовті
cursor.execute("SELECT * FROM Fruits WHERE Color = 'Yellow'")
yellow_fruits = cursor.fetchall()

# Друк всіх записів для фруктів
cursor.execute("SELECT * FROM Fruits")
all_fruits = cursor.fetchall()

# Закриття з'єднання
conn.commit()
conn.close()

# Виведення результатів
print("Жовті фрукти:", yellow_fruits)
print("Всі фрукти:", all_fruits)
