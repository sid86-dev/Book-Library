import time
from playsound import playsound
loc2 = "right.mp3"
localtime = time.asctime(time.localtime(time.time()))


while True:
    print("""
    --------------------------------------
            1 for New Login
            2 for existing Login 
            """)
    print(f"Loged in: {localtime}\n")
    input1 = input('    --> ')
    if input1 == "1":
        # for new user update username in file
        newlog = input("USERNAME: ").lower()
        f = open('library_users.txt', 'a')
        f.write(f' {newlog}')
        f.close()
        print("Data updating...")
        time.sleep(2)
    elif input1 == "2":
        log = input("USERNAME: ").lower()
        # for old user check for username from file
        f = open('library_users.txt', 'r')
        read = f.read()
        sp = read.split(' ')
        if log in sp:
            print("""
                1 to Add Book
                2 to Lend Book
                3 to Display Book""")
        input2 = input('    --> ')
        # to add a book
        if input2 == "1":
            bname = input("ENTER NAME OF THE BOOK: ").lower()
            # for the file
            f = open('library_booksname.txt', 'a')
            f.write(f' {bname}')
            f.close()
            print('Successfully Added to the library!')
        # to lend a book
        elif input2 == '2':
            bname = input("ENTER NAME OF THE BOOK: ").lower()
            i = open('library_booksname.txt', 'r')
            b = i.read()
            c = list(b.split(' '))
            if bname in c:
                f = open("library_booksname.txt", 'r')
                read = f.read()

                # list to dictionary
                def Convert(a):
                    it = iter(a)
                    res_dct = dict(zip(it, it))
                    return res_dct
                lst = read.split(";")
                mydic = Convert(lst)
                # if book is with someone else
                if bname in mydic:
                    lend_to = mydic[f"{bname}"]
                    print("\nSORRY BOOK NOT AVAILABLE!!")
                    print(f"The Book is with {lend_to}")
                # if book is available in the library
                else:
                    # data import to file
                    t = open('library_lend.txt', 'a')
                    t.write(f'{bname};{log};')
                    print("\nBOOK LENDED TO YOU!!")
                    playsound(loc2)
                    t.close()
            elif bname not in c:
                print("\nSORRY BOOK NOT AVAILABLE!!")
        # displays the available books
        elif input2 == '3':
            f = open('library_booksname.txt', 'r')
            read = f.read()
            sp = read.split(' ')
            j = ', '.join(sp)
            from camelcase import CamelCase

            c = CamelCase()
            cased = c.hump(j)
            print("THE AVAILABLE BOOKS ARE: \n")
            print(cased)
        else:
            print("\nENTER A VALID INFO!!")
    else:
        print("\nENTER A VALID INFO!!")
