import random
import math
begin = 0
total_rooms = 0
i = 0
# Main function
def main():
    # Tests main
    print("This is a dragon game.")
    Dungeon.generate()


class Dungeon:
    def __init__(self):
        self.rooms = {}
        self.starting_room = None
        self.dragon_lair = None
        self.sword_room = None
        self.shield_room = None
        self.key_room = None
        self.roar_room = None
        self.num_dungeons_generated = 0
        
    def toPositive(dungeon):
        rowNum = 0
        colNum = 0
        for row in dungeon:
            for col in row:
                dungeon[rowNum][colNum] = abs(col)
                colNum += 1
            rowNum += 1
            colNum = 0
        return dungeon

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
    
    def checkDungeon(dungeon, all_valid):
        global total_rooms
        global begin
        start_valid = False
        connect_valid = False
        start_room = random.choice(range(len(dungeon[4])))
        begin = start_room
        Dungeon.dfs(4, start_room, dungeon)
        connect_valid = Dungeon.checkConnected(dungeon)
        if connect_valid == True and start_valid == True:
            all_valid = True
        return all_valid
    
    def checkConnected(dungeon):
        rooms_connected = 0
        rowNum = 0
        colNum = 0
        for row in dungeon:
            for col in row:
                if dungeon[rowNum][colNum] < 0:
                    rooms_connected += 1
                colNum += 1
            rowNum += 1
            colNum = 0
        print(rooms_connected)
        if rooms_connected < 16:
            return False
        else:
            return True

    
    def dfs(row, col, dungeon):
        #CHECK BOUNDS
        global total_rooms
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
            if dungeon[row][col] <= 0:
                return
            #WE'VE ALREADY BEEN HERE
            dungeon[row][col] = -dungeon[row][col]
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

    def findBegin(dungeon, begin):
        global i
        for room in dungeon[4]:
            if room > 0:
                i += 1
                print(i)
            else:
                begin = dungeon[4][i]
                break
        print(i)
        print(begin)
        return begin
    
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


    def generate():
        global begin
        dungeon_map = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
        ] 
        all_valid = False
        while all_valid == False:
            dungeon_map = Dungeon.toPositive(dungeon_map)
            dungeon_map = Dungeon.shuffleDungeon(dungeon_map)
            all_valid = Dungeon.checkDungeon(dungeon_map, all_valid)
            begin = Dungeon.findBegin(dungeon_map, begin)
            print(dungeon_map)
            Dungeon.print_ascii(dungeon_map)
            all_valid = True
    
if __name__ == "__main__":
    main()
