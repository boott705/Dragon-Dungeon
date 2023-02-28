def main():
    Player.movement()
class Player:
    def movement():
        direction = input("What way would you like to go: ")
        if direction == "North" or direction == "north":
            print("You went through the north door.")
        elif direction == "south" or direction == "South":
            print("You went through the south door.")
        elif direction == "East" or direction == "east":
            print("You went through the east door.")
        elif direction == "West" or direction == "west":
            print("You went through the west door.")
        else:
            print("invalid option")
        

if __name__=="__main__":
    main()
