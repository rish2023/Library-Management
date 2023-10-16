# Import the pandas library
import pandas as pd

# Read the data from the CSV file into a DataFrame(give your csv filethe path where you have stored )
file = pd.read_csv('/Users/RI20451258/Documents/LibraryManagement/books.csv')


# Main function to call sub-functions
def Lib():
    while True:
        print()
        print("Enter 'a' to add a book")
        print("Enter 'd' to delete a book")
        print("Enter 'l' to list books")
        print("Enter 's' to search for a book")
        print("Enter 'q' to exit")

        Text = input("Enter Key: ")
        if Text == 'a':
            a_book()
        elif Text == 'd':
            d_book()
        elif Text == 'l':
            list_books()
        elif Text == 's':
            search()
        elif Text == 'q':
            break
        else:
            print("Please enter a valid key from the options")
            print("\n")

# Function to check if a string contains only alphabetic characters
def check(string):
    count = 0
    for i in string:
        if i.isalpha():
            count += 1
    if count == len(string):
        return True

# Function to add a book to the list
def a_book():
    value = 'y'
    while value == 'Y' or value == 'y':
        # Enter the name of the book you want to add
        while True:
            Name_of_book = input("Enter book name: ")
            if check(Name_of_book):
                break
            else:
                print("You have entered invalid data for the book name")
                continue

        # Enter the author's name
        while True:
            Author_Name = input("Enter Author name: ")
            if check(Author_Name):
                break
            else:
                print("You have entered invalid data for the author's name")
                continue

        # Enter the price of the book
        while True:
            try:
                price = float(input("Enter Price: "))
                break
            except:
                print("You have entered invalid data for the price")

        # Enter the publisher of the book
        while True:
            Publisher = input("Enter Publisher name: ")
            if check(Publisher):
                break
            else:
                print("You have entered invalid data for the publisher")
                continue

        # Enter the edition of the book
        while True:
            try:
                Edition = int(input("Enter Edition: "))
                break
            except:
                print("You have entered invalid data for the edition")

        # Create a list with book information and add it to the DataFrame
        List = [Name_of_book, Author_Name, price, Publisher, Edition]
        file.loc[len(file)] = List
        # Save the DataFrame to the CSV file
        file.to_csv('/Users/RI20451258/Documents/LibraryManagement/books.csv', index=False)

        print("Book added successfully")
        value = input("Want to add more books? (y/n)")

    print(file)

# Function to delete a book from the list
def d_book():
    while True:
        # Enter the book name you want to delete
        b_Name = input("Enter the book name you want to delete: ")
        List_Book = []
        for book_Name in file['Name_of_book']:
            List_Book.append(book_Name)
        if b_Name not in List_Book:
            print("Entered book is not available")
        else:
            break

    # Remove the book from the DataFrame and save it back to the CSV file
    file.drop(List_Book.index(b_Name), inplace=True)
    print("Book deleted successfully")
    file.to_csv('/Users/RI20451258/Documents/LibraryManagement/books.csv', index=False)
    print(file)

# Function to list the books in the DataFrame
def list_books():
    print(file)

# Function to search for books in the list
def search():
    while True:
        b_Name = input("Enter the name you want to search: ")
        for i in range(len(file.Name_of_book)):
            if b_Name == file.Name_of_book[i]:
                print(file.iloc[i, :])
                break
        if i == len(file.Name_of_book) - 1:
            print("Entered book is not available")
            break
        else:
            break

# Call the main function to start the program
Lib()
