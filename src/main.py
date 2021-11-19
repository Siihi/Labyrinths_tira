import prim
import maze

def main():
    mazecommands = maze.Maze()
    while True:
        print("Welcome to the labyrinth program!")
        print("1: Prim's randomized algorithm")
        print("2: TBC")
        print("0: Exit")

        try:
            choice = int(input("Choose an option by typing its number:"))
        except:
            print("Please type a number!")
            break

        if choice == 1:
            print("Choose the size of the maze:")
            try:
                x = int(input("Number of columns:"))
            except:
                print("Please type a number!")
                break
            try:
                y = int(input("Number of rows:"))
            except:
                print("Please type a number!")
                break
            prim.Prim(x,y)

        elif choice == 2:
            pass

        elif choice == 0:
            break

        else:
            continue


if __name__ == "__main__":
    main()
