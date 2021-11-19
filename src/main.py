import prim

def main():
    while True:
        print("Welcome to the labyrinth program!")
        print("1: Prim's randomized algorithm")
        print("2: TBC")
        print("0: Exit")

        try:
            choice = int(input("Choose an option by typing its number:"))
        except ValueError:
            print("Please type a number!")
            break

        if choice == 1:
            print("Choose the size of the maze:")
            try:
                xcoord = int(input("Number of columns:"))
            except ValueError:
                print("Please type a number!")
                break
            try:
                ycoord = int(input("Number of rows:"))
            except ValueError:
                print("Please type a number!")
                break
            prim.Prim(xcoord, ycoord)

        elif choice == 2:
            pass

        elif choice == 0:
            break

        else:
            continue


if __name__ == "__main__":
    main()
