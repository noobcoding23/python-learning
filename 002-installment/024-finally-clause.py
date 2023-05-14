def errorFunc():
    try:
        fruits = ["Mango", "Apple", "Pineapple", "Guava", "Papaya"]
        n = int(input("Enter the index number: "))
        print(fruits[n])
        return True
    except ValueError:
        print("Invalid value entered")
        return False
    except:
        print("Invalid index number")
        return False
    finally:
        print("This line of code will always excute even when inside of a function")
    print("This line won't print cause this is inside of a function")
funcReturn = errorFunc()
print(funcReturn)