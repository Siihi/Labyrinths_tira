import time
import prim
import aldous_broder

def main():
    while True:
        print("Welcome to the labyrinth program!")
        print("1: Prim's randomized algorithm")
        print("2: Aldous-Broder algorithm")
        print("3: Exit")

        try:
            choice = int(input("Choose an option by typing its number:"))
        except ValueError:
            print("Please type a number!")
            time.sleep(2)
            main()


        if choice == 1:
            print("Choose the size of the maze:")
            try:
                xcoord = int(input("Number of columns:"))
            except ValueError:
                print("Please type a number!")
                time.sleep(2)
                main()
            if xcoord < 4:
                print("The size has to be bigger than 3.")
                time.sleep(2)
                main()
            try:
                ycoord = int(input("Number of rows:"))
            except ValueError:
                print("Please type a number!")
                time.sleep(2)
                main()
            if ycoord < 4:
                print("The size has to be bigger than 3.")
                time.sleep(2)
                main()
            primtime = prim.Prim(xcoord, ycoord)
            print(f"The amount of time taken: {primtime}")

        elif choice == 2:
            print("Choose the size of the maze:")
            try:
                xcoord = int(input("Number of columns:"))
            except ValueError:
                print("Please type a number!")
                time.sleep(2)
                main()
            if xcoord < 4:
                print("The size has to be bigger than 3.")
                time.sleep(2)
                main()
            try:
                ycoord = int(input("Number of rows:"))
            except ValueError:
                print("Please type a number!")
                time.sleep(2)
                main()
            if ycoord < 4:
                print("The size has to be bigger than 3.")
                time.sleep(2)
                main()
            al_brtime = aldous_broder.AldousBroder(xcoord, ycoord)
            print(f"The amount of time taken: {al_brtime}")

        elif choice == 3:
            break

        else:
            continue


if __name__ == "__main__":
    main()
