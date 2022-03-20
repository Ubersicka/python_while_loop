# "Тhe book you search is not here!"
# "You checked {брой} books."
#  Ако открие книгата си се отпечатва един ред:
# "You checked {брой} books and found it."

searched_book = input()
books_counter = 0
book_is_found = False
next_book = input()
while next_book != "No More Books": # searched_book също става вместо "No More Books"
    if next_book == searched_book:
        book_is_found = True
        break
    books_counter += 1
    next_book = input()
if book_is_found:  # if book_is_found == True (така се превежда тази команда)
    print(f"You checked {books_counter} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {books_counter} books.")
