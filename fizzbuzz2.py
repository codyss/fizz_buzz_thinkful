from sys import argv

if len(argv) == 1:
    while True:
        try:   
            n = int(input("What number should we count to?"))
            break
        except ValueError:
            print("You must provide an integer")
else:
    try: 
        n = int(argv[1])
    except ValueError:
        while True:    
            print("You must provide an integer")
            try:
                n = int(input("What number should we count to?"))
                break
            except ValueError:
                pass

for i in range(1,n+1):
    if i % 3 == 0 and i % 5 == 0:
        print("fizz buzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)

