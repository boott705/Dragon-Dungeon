import random
# Main function
def main():
    # Tests main
    print("This is a dragon game.")
    dungeon = Dungeon()
    dungeon.generate()


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

        
    
    dungeon_map = [
        [],
        [],
        [],
        [],
        []
    ]

    def generate(self):
        dungeon_map = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
     ]
        cols = 5
        rows = 5
        print(dungeon_map)
        rooms = [1, 2, 3, 4, 5, 6, 
    7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 
    17, 18, 19, 20, 21, 22, 23, 24, 25]
        for row in range(rows):
            for col in range(cols):
                room = random.choice(rooms)
                print(room)
                dungeon_map[row][col] = room
                rooms.remove(room)
        print(dungeon_map)
        

    
# Creates main
if __name__=="__main__":
    main()
