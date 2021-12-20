import time
import prim
import aldous_broder
import bfs

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
                pxcoord = int(input("Number of columns:"))
            except ValueError:
                print("Please type a number!")
                time.sleep(2)
                main()
            if pxcoord < 4:
                print("The size has to be bigger than 3.")
                time.sleep(2)
                main()
            try:
                pycoord = int(input("Number of rows:"))
            except ValueError:
                print("Please type a number!")
                time.sleep(2)
                main()
            if pycoord < 4:
                print("The size has to be bigger than 3.")
                time.sleep(2)
                main()
            primtime = prim.Prim(pxcoord, pycoord)
            print(f"The amount of time taken: {primtime}")
            try:
                asksp = int(input("Do you want to test the integrity of the maze? 1: Yes, 2: No"))
            except ValueError:
                print("Please type a number!")
                time.sleep(2)
                main()
            if asksp == 1:
                bfs.BreadthFirstSearch(primtime.maze)
            else:
                continue

        elif choice == 2:
            print("Choose the size of the maze:")
            try:
                abxcoord = int(input("Number of columns:"))
            except ValueError:
                print("Please type a number!")
                time.sleep(2)
                main()
            if abxcoord < 4:
                print("The size has to be bigger than 3.")
                time.sleep(2)
                main()
            try:
                abycoord = int(input("Number of rows:"))
            except ValueError:
                print("Please type a number!")
                time.sleep(2)
                main()
            if abycoord < 4:
                print("The size has to be bigger than 3.")
                time.sleep(2)
                main()
            al_brtime = aldous_broder.AldousBroder(abxcoord, abycoord)
            print(f"The amount of time taken: {al_brtime}")
            try:
                asksab = int(input("Do you want to test the integrity of the maze? 1: Yes, 2: No"))
            except ValueError:
                print("Please type a number!")
                time.sleep(2)
                main()
            if asksab == 1:
                bfs.BreadthFirstSearch(al_brtime.maze)
            else:
                continue

        elif choice == 3:
            break

        else:
            continue

if __name__ == "__main__":
    main()