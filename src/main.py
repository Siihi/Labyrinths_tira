import prim
import aldous_broder

def main():
    while True:
        print("Welcome to the labyrinth program!")
        print("1: Prim's randomized algorithm")
        print("2: Aldous-Broder algorithm")
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
            primtime = prim.Prim(xcoord, ycoord)
            print(f"The amount of time taken: {primtime}")

        elif choice == 2:
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
            aldous_broder.AldousBroder(xcoord, ycoord)

        elif choice == 0:
            break

        else:
            continue


if __name__ == "__main__":
    main()
