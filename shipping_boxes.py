#height of large box
large_box = float(input("enter the height of the large box in inches:"))
#height of small box
small_box = float(input("enter the height of small box in inches:"))
#height/thickness of the book
books_height = float(input("enter the height or thickness of the books:"))
#number of books ordered
books_ordered = int(input("enter the number of books ordered:"))
#lets get how many books will fill a large box and a small box
no_of_books_for_largeBox = large_box / books_height
no_of_largefulBoxes = no_of_books_for_largeBox / books_ordered
rem_largebox = no_of_books_for_largeBox % books_ordered
#small box
no_of_books_for_smallBox = small_box / books_height
no_of_smallfulBoxes = no_of_books_for_smallBox / books_ordered 
rem_smallbox =  no_of_books_for_smallBox % books_ordered
# if statements
if large_box < 8.0:
    print("this is not a small box.")
elif small_box > 8.0:
    print("this is not a large box.")
elif no_of_largefulBoxes < 1:
    print("books should be at least 1 full box.")
elif no_of_smallfulBoxes < 1:
    print("can't ship this number of books.")
elif  rem_largebox < 1:
    print("shipping %s boxes"%(no_of_largefulBoxes))
    print(str(int(no_of_largefulBoxes)) + " large boxes")
elif rem_largebox > 1:
    print("shipping %s boxes"%(no_of_smallfulBoxes))
    print(str(int(no_of_smallfulBoxes)) + " small boxes")
elif no_of_largefulBoxes == 1:
    print("shipping 1 large box")
elif no_of_smallfulBoxes == 1:
    print("shipping 1 small box")
else:
    print("error")
