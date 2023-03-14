import random
begin = 0
start_room_index = 0
total_rooms = 0
dragon_room = 0
shield_room = 0
key_room = 0
sword_room = 0
terminal_rooms = []
player_y = 4
player_x = 0
quit = False

# Main function
def main():
    global dragon_room
    global shield_room
    global key_room
    global sword_room
    global player_y
    global player_x
    global quit
    global begin
    global total_rooms
    global terminal_rooms
    visited_rooms = []
    hasSword = False
    hasShield = False
    hasKey = False
    quit = False
    # Tests main
    print("")
    print("You enter the dungeon...")
    print("")
    print("Your goal is to find the key, the sword, and the shield before entering Bert the Dragon's lair.")
    print("If you fail to find all three before entering the Bert's lair, you will be eaten.")
    dungeon = Dungeon.generate()
    player_x = start_room_index
    while dungeon[player_y][player_x] != dragon_room:
        Player.checkRoar(dungeon, player_y, player_x, dragon_room)
        player_y, player_x = Player.movement(player_y, player_x, dungeon)
        if dungeon[player_y][player_x] == dragon_room:
            break
        if dungeon[player_y][player_x] not in visited_rooms:
            hasSword, hasShield, hasKey = Player.searchRoom(dungeon, player_y, player_x, sword_room, shield_room, key_room, hasSword, hasShield, hasKey)
            visited_rooms.append(dungeon[player_y][player_x])
    Player.endGame(hasSword, hasShield, hasKey)

class Player:

    def movement(player_y, player_x, dungeon):
        available_directions = []
        if player_y > 0:
            if dungeon[player_y - 1][player_x] < 0:
                available_directions.append("north")
        if player_x < 4:
            if dungeon[player_y][player_x + 1] < 0:
                available_directions.append("east")
        if player_y < 4:
            if dungeon[player_y + 1][player_x] < 0:
                available_directions.append("south")
        if player_x > 0:
            if dungeon[player_y][player_x - 1] < 0:
                available_directions.append("west")
        prompt = "You can go"
        for direction in available_directions:
            if direction != available_directions[-1]:
                prompt += f" {direction},"
            elif len(available_directions) > 1:
                prompt += f" and {direction}."
            else:
                prompt += f" {direction}."
        print("")
        print(prompt)
        print("Type Show Map to show the dungeon map.")
        validDirection = False
        while validDirection == False:
            #Type 'Show Map' to view dungeon map.
            direction = input("Your choice: ")
            if direction.lower() == "show map":
                Dungeon.print_ascii(dungeon, player_y, player_x)
                return player_y, player_x
            elif direction.lower() not in available_directions:
                print("")
                print("Sorry, you can't go that way.")
            elif direction == "North" or direction == "north":
                player_x = player_x 
                player_y = player_y - 1
                print("")
                print("You went through the north door.")
                return player_y, player_x
            elif direction == "South" or direction == "south":
                player_x = player_x 
                player_y = player_y + 1
                print("")
                print("You went through the south door.")
                return player_y, player_x
            elif direction == "East" or direction == "east":
                player_x = player_x + 1
                player_y = player_y
                print("")
                print("You went through the east door.")
                return player_y, player_x
            elif direction == "West" or direction == "west":
                player_x = player_x - 1
                player_y = player_y
                print("")
                print("You went through the west door.")
                return player_y, player_x 
    
    def searchRoom(dungeon, player_y, player_x, sword_room, shield_room, key_room, hasSword, hasShield, hasKey):
        valid_choice = False
        while valid_choice == False:
            print("Would you like to search the room? (Y or N)")
            search_choice = input("Your choice: ")
            if search_choice.lower() == "y" or search_choice.lower() == "yes":
                if dungeon[player_y][player_x] == sword_room:
                    print("")
                    print("You found the Sword of Death!")
                    hasSword = Player.takeChoice("sword")
                    return hasSword, hasShield, hasKey
                elif dungeon[player_y][player_x] == shield_room:
                    print("")
                    print("You found the Mighty Shield!")
                    hasShield = Player.takeChoice("shield")
                    return hasSword, hasShield, hasKey
                elif dungeon[player_y][player_x] == key_room:
                    print("")
                    print("You found the Skeleton Key!")
                    hasKey = Player.takeChoice("key")
                    return hasSword, hasShield, hasKey 
                else:
                    dungeon_objects = [
                        "Broken chains and shackles",
                        "Moldering tapestries",
                        "Cobweb-covered torches",
                        "Stone tablets with ancient inscriptions",
                        "A moldy spellbook",
                        "A tarnished silver chalice",
                        "Bones of long-dead creatures",
                        "A cryptic map",
                        "A mysterious potion",
                        "An enchanted crystal ball",
                        "A chest filled with gold coins and precious gems",
                        "A set of stone tablets with ancient text",
                        "A rusty chainmail shirt and helmet",
                        "A pile of rubble with hidden passages",
                        "A strange, pulsating crystal",
                        "A small statuette of a forgotten deity",
                        "A heavy mace with a silver head",
                        "A rusty iron maiden with spikes",
                        "A torch that never goes out",
                        "A pile of gold coins mixed with fake ones",
                        "A rope with a grappling hook",
                        "A set of rusty manacles with broken chains"
                    ]
                    room_object = random.choice(dungeon_objects)
                    print("")
                    print(f"You found {room_object.lower()}.")
                    Player.takeChoice(room_object)
                    dungeon_objects.remove(room_object)
                    return hasSword, hasShield, hasKey
            elif search_choice.lower() == "n" or search_choice.lower() == "no":
                print("")
                print("You decided to not search the room.")
                return hasSword, hasShield, hasKey
            else:
                print("")
                print("Sorry, your choice is invalid.")
            
    def takeChoice(room):
        valid_choice = False
        while valid_choice == False:
            print("What would you like to do? (Move or Take) ")
            choice = input("Your choice: ")
            if choice.lower() == "move":
                print("You've decided to not take it.")
                return False
            elif choice.lower() == "take":
                if room == "sword":
                    print("You took the Sword of Death.")
                    return True
                elif room == "shield":
                    print("You took the Mighty Shield.")
                    return True
                elif room == "key":
                    print("You took the Skeleton Key.")
                    return True
                else:
                    print("You took", room.lower())
                    valid_choice = True
            else:
                print("Sorry, your choice is invalid.")
    
    def checkRoar(dungeon, player_y, player_x, dragon_room):
        if player_y > 0 and dungeon[player_y-1][player_x] == dragon_room:
            print("")
            print("ROARRRRR")
        if player_x > 0 and dungeon[player_y][player_x-1] == dragon_room:
            print("")
            print("ROARRRRR")
        if player_y < 4 and dungeon[player_y+1][player_x] == dragon_room:
            print("")
            print("ROARRRRR")
        if player_x < 4 and dungeon[player_y][player_x+1] == dragon_room:
            print("")
            print("ROARRRRR")

    def endGame(hasSword, hasShield, hasKey):
        valid_choice = False
        print("")
        print("You've entered Bert's lair...")
        if hasSword == hasShield == hasKey == True:
            print("You have slain the Bert the Dragon! Great job!")
        else:
            print("Unfortunately, Bert the Dragon ate you.")
        print("")
        print("Would you like to play again? (Y or N)")
        while valid_choice == False:
            play_again_choice = input("Your choice: ")
            if play_again_choice.lower() == "y" or play_again_choice.lower() == "yes":
                main()
            elif play_again_choice.lower() == "n" or play_again_choice.lower() == "no":
                print("Thanks for playing! Come visit the dungeon again soon!")
                valid_choice = True
            else:
                print("Sorry, your choice is invalid.")


class Dungeon:
    def __init__(self):
        self.starting_room = None
        self.dragon_lair = None
        self.sword_room = None
        self.shield_room = None
        self.key_room = None
        self.roar_room = None
        self.num_dungeons_generated = 0
    
    def dfs(row, col, dungeon):
        #CHECK BOUNDS
        global total_rooms
        global terminal_rooms
        if total_rooms < 16:
            if row >= len(dungeon) and total_rooms <= 16:
                return
            if row < 0 and total_rooms <= 16:
                return
            if col >= len(dungeon[0]) and total_rooms <= 16:
                return
            if col < 0 and total_rooms <= 16:
                return
            #Check for 0
            if dungeon[row][col] < 0:
                total_rooms -= 1
            #WE'VE ALREADY BEEN HERE
            dungeon[row][col] = -abs(dungeon[row][col])
            total_rooms += 1
            directions = ['N', 'E', 'S', 'W']
            random.shuffle(directions)
            # Explore neighboring cells in a random order
            for direction in directions:
                if direction == 'N':
                    Dungeon.dfs(row-1, col, dungeon)
                elif direction == 'E':
                    Dungeon.dfs(row, col+1, dungeon)
                elif direction == 'S':
                    Dungeon.dfs(row+1, col, dungeon)
                elif direction == 'W':
                    Dungeon.dfs(row, col-1, dungeon)
        else:
            return

    def print_ascii(dungeon_map, player_y, player_x):
        global begin
        ascii_map = ""
        for row in dungeon_map:
            for room in row:
                if room == -begin:
                    ascii_map += "║  START  ║"
                elif room < 0:
                    ascii_map += "║  ROOM   ║"
                else:
                    ascii_map += "║         ║"
            ascii_map += "\n"
            for room in row:
                ascii_map += "║         ║"
            ascii_map += "\n"
            for room in row:
                if room == dungeon_map[player_y][player_x]:
                    ascii_map += "║ You Are ║"
                elif room < 0:
                    ascii_map += "║         ║"
                else:
                    ascii_map += "║         ║"
            ascii_map += "\n"
            for room in row:
                if room == dungeon_map[player_y][player_x]:
                    ascii_map += "║  Here   ║"
                elif room < 0:
                    ascii_map += "║         ║"
                else:
                    ascii_map += "║         ║"
            ascii_map += "\n"
        print(ascii_map)

    def countTerminal(beign, terminal_rooms, dungeon):
        neighbors = []
        rowNum = 0
        colNum = 0
        for row in dungeon:
            for col in row:
                if rowNum > 0 and dungeon[rowNum-1][colNum] < 0:
                    neighbors.append('+')
                if colNum > 0 and dungeon[rowNum][colNum-1] < 0:
                    neighbors.append('+')
                if rowNum < 4 and dungeon[rowNum+1][colNum] < 0:
                    neighbors.append('+')
                if colNum < 4 and dungeon[rowNum][colNum+1] < 0:
                    neighbors.append('+')
                if dungeon[rowNum][colNum] < 0 and dungeon[rowNum][colNum] != -begin and len(neighbors) == 1:
                    terminal_rooms.append(dungeon[rowNum][colNum])
                colNum += 1
                neighbors = []
            rowNum += 1
            colNum = 0
        return terminal_rooms

    def generateDungeon(dungeon, all_valid):
        global terminal_rooms
        global begin
        global start_room_index
        start_room_index = random.choice(range(len(dungeon[4])))
        begin = dungeon[4][start_room_index]
        Dungeon.dfs(4, start_room_index, dungeon)
        terminal_rooms = Dungeon.countTerminal(begin, terminal_rooms, dungeon)
        if len(terminal_rooms) > 0:
            all_valid = True
        return all_valid
    
    def placeObjects(dungeon, terminal_rooms, begin):
        available_rooms = []
        rowNum = 0
        colNum = 0
        for row in dungeon:
            for col in row:
                if col < 0:
                    available_rooms.append(col)
                colNum += 1
            rowNum += 1
            colNum = 0
        available_rooms.remove(-begin)
        dragon_room = random.choice(terminal_rooms)
        available_rooms.remove(dragon_room)
        sword_room = random.choice(available_rooms)
        available_rooms.remove(sword_room)
        shield_room = random.choice(available_rooms)
        available_rooms.remove(shield_room)
        key_room = random.choice(available_rooms)
        available_rooms.remove(key_room)
        return dragon_room, sword_room, shield_room, key_room
        
    def generate():
        global begin
        global start_room_index
        global total_rooms
        global terminal_rooms
        global dragon_room 
        global shield_room
        global key_room
        global sword_room
        all_valid = False
        while all_valid == False:
            dungeon_map = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
            ] 
            begin = 0
            start_room_index = 0
            total_rooms = 0
            all_valid = Dungeon.generateDungeon(dungeon_map, all_valid)
        dragon_room, sword_room, shield_room, key_room = Dungeon.placeObjects(dungeon_map, terminal_rooms, begin)
        return dungeon_map

if __name__ == "__main__":
    main()
