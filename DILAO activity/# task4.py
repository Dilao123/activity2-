# task4.py

class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def describe(self):
        print(f"Book: {self.title} by {self.author} ({self.year_published})")


book1 = Book("1984", "makatawtaw", 1950)
book2 = Book("To Kill all enemies", "bangbang", 1961)
book3 = Book("superman", "A. Switswerland", 1966)


book1.describe()
book2.describe()
book3.describe()