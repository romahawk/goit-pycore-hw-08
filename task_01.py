import pickle

class Contact:
    def __init__(self, name: str, email: str, phone: str, favorite: bool = False):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __repr__(self):
        return f"Contact(name={self.name}, email={self.email}, phone={self.phone}, favorite={self.favorite})"

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact: Contact):
        self.contacts.append(contact)

    def list_contacts(self):
        return self.contacts

    def save_to_file(self, filename="addressbook.pkl"):
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def load_from_file(cls, filename="addressbook.pkl"):
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            return cls()  # Повертає новий AddressBook, якщо файл не знайдено

def main():
    # Завантажуємо адресну книгу
    book = AddressBook.load_from_file()

    # Основний цикл програми
    while True:
        print("\n1. Додати контакт")
        print("2. Переглянути контакти")
        print("3. Вийти")

        choice = input("Виберіть дію: ")

        if choice == "1":
            name = input("Введіть ім'я: ")
            email = input("Введіть електронну пошту: ")
            phone = input("Введіть номер телефону: ")
            favorite = input("Чи є улюбленим (True/False)? ") == 'True'

            contact = Contact(name, email, phone, favorite)
            book.add_contact(contact)

        elif choice == "2":
            print("\nКонтакти:")
            for contact in book.list_contacts():
                print(contact)

        elif choice == "3":
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

    # Зберігаємо дані перед виходом з програми
    book.save_to_file()

if __name__ == "__main__":
    main()
