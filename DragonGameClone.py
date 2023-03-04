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
    # Tests main
    print("This is a dragon game.")
    dungeon = Dungeon.generate()
    player_x = start_room_index
    while quit == False:
        print(player_y, player_x)
        player_y, player_x = Player.movement(player_y, player_x, dungeon)
        quit = True

class Player:
    def __init__(self):
         self.x = begin
         self.y = 4
         self.hasSword = False
         self.hasShield = False
         self.hasKey = False

    def movement(player_y, player_x, dungeon):
        available_directions = []
        if player_y > 0:
            if dungeon[player_y - 1][player_x] < 0:
                available_directions.append("North")
        if player_x < 4:
            if dungeon[player_y][player_x + 1] < 0:
                available_directions.append("East")
        if player_y < 4:
            if dungeon[player_y + 1][player_x] < 0:
                available_directions.append("South")
        if player_x > 0:
            if dungeon[player_y][player_x - 1] < 0:
                available_directions.append("West")
        prompt = "Which way would you like to go:"
        for direction in available_directions:
            if direction != available_directions[-1]:
                prompt += f" {direction},"
            else:
                prompt += f" {direction}"
        print(prompt)
        validDirection = False
        while validDirection == False:
            direction = input("Your choice: ")
            if direction == "Quit":
                exit()
            if direction.capitalize() not in available_directions:
                print("Sorry, you can't go that way.")
            if direction == "North" or direction == "north":
                player_x = player_x 
                player_y = player_y - 1
                print("You went through the north door.")
                return player_y, player_x
            elif direction == "South" or direction == "south":
                player_x = player_x 
                player_y = player_y + 1
                print("You went through the south door.")
                return player_y, player_x
            elif direction == "East" or direction == "east":
                player_x = player_x + 1
                player_y = player_y
                print("You went through the east door.")
                return player_y, player_x
            elif direction == "West" or direction == "west":
                player_x = player_x - 1
                player_y = player_y
                print("You went through the west door.")
                return player_y, player_x 

    def choice(current_room_y, current_room_x):
        doing = input("What would you like to do (Move or Take): ")
        if doing == "Move" or doing == "move":
            Player.movement(current_room_y, current_room_x)
        elif doing == "Take" or doing == "take":
            pass
        pass

class Dungeon:
    def __init__(self):
        self.starting_room = None
        self.dragon_lair = None
        self.sword_room = None
        self.shield_room = None
        self.key_room = None
        self.roar_room = None
        self.num_dungeons_generated = 0

    def shuffleDungeon(arr2d): #Randomized rooms
    #Shuffes entries of 2-d array arr2d, preserving shape.
        reshape = [ ]
        data = [ ]
        iend = 0
        for row in arr2d:
            data.extend (row)
            istart, iend = iend, iend+len (row)
            reshape. append ((istart, iend))
        random.shuffle(data)
        return [data[istart: iend] for (istart, iend) in reshape]
    
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

    def print_ascii(dungeon_map):
        global begin
        ascii_map = ""
        for row in dungeon_map:
            for room in row:
                if room == begin:
                    ascii_map += "╔════════╗"
                elif room < 0:
                    ascii_map += "║ ROOM   ║"
                else:
                    ascii_map += "║        ║"
            ascii_map += "\n"
            for room in row:
                if room == begin:
                    ascii_map += "║ Start  ║"
                else:
                    ascii_map += "║        ║"
            ascii_map += "\n"
            for room in row:
                if room == begin:
                    ascii_map += "║        ║"
                elif room < 0:
                    ascii_map += "║        ║"
                else:
                    ascii_map += "║        ║"
            ascii_map += "\n"
            for room in row:
                if room == begin:
                    ascii_map += "╚════════╝"
                elif room < 0:
                    ascii_map += "║        ║"
                else:
                    ascii_map += "║        ║"
            ascii_map += "\n"
        print(ascii_map)

    def countTerminal(terminal_rooms, dungeon):
        global begin
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

    def checkDungeon(dungeon, all_valid):
        global terminal_rooms
        global begin
        global start_room_index
        start_room_index = random.choice(range(len(dungeon[4])))
        begin = dungeon[4][start_room_index]
        Dungeon.dfs(4, start_room_index, dungeon)
        terminal_rooms = Dungeon.countTerminal(terminal_rooms, dungeon)
        print(terminal_rooms)
        if len(terminal_rooms) > 0:
            all_valid = True
        return all_valid

    def generate():
        global begin
        global start_room_index
        global total_rooms
        global terminal_rooms
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
            #dungeon_map = Dungeon.shuffleDungeon(dungeon_map)
            all_valid = Dungeon.checkDungeon(dungeon_map, all_valid)
            print(dungeon_map)
            Dungeon.print_ascii(dungeon_map)
        return dungeon_map

if __name__ == "__main__":
    main()
