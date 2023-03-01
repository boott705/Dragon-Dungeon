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

    def create_branch(rooms, room_amount, new_room_probability, dungeon_map, good_dungeon, current_room_y, current_room_x, break_off_points):
        if room_amount == 3:
            return dungeon_map
        while good_dungeon == False:
            new_room_probability = room_amount
            adjacent_rooms = []
            if current_room_y + 1 < 5:
                if dungeon_map[current_room_y + 1][current_room_x] == 0:
                    adjacent_rooms.append(1)
            if dungeon_map[current_room_y][current_room_x + 1] == 0 and current_room_x + 1 <= 5:
                adjacent_rooms.append(2)
            if dungeon_map[current_room_y - 1][current_room_x] == 0 and current_room_y - 1 >= 0:
                adjacent_rooms.append(3)
            if dungeon_map[current_room_y][current_room_x - 1] == 0 and current_room_x - 1 >= 0:
                adjacent_rooms.append(4)
            for room in adjacent_rooms:
                new_room = random.choice(range(new_room_probability))
                if new_room <= new_room_probability[new_room_probability//2]:
                    next_room = random.choice(adjacent_rooms)
                    if room == next_room and room == 1:
                        room_amount += 1
                        dungeon_map[current_room_y + 1][current_room_x] = rooms[0]
                        rooms.pop(0)
                        current_room_y = current_room_y + 1
                        current_room_x = current_room_x
                        rooms.remove()
                        Dungeon.create_branch(rooms, room_amount, new_room_probability, dungeon_map, good_dungeon, current_room_y, current_room_x, break_off_points)
                    if room == next_room and room == 2:
                        room_amount += 1
                        dungeon_map[current_room_y + 1][current_room_x] = rooms[0]
                        rooms.pop(0)
                        current_room_y = current_room_y + 1
                        current_room_x = current_room_x
                        rooms.remove()
                        Dungeon.create_branch(rooms, room_amount, new_room_probability, dungeon_map, good_dungeon, current_room_y, current_room_x, break_off_points)
                    if room == next_room and room == 3:
                        room_amount += 1
                        dungeon_map[current_room_y + 1][current_room_x] = rooms[0]
                        rooms.pop(0)
                        current_room_y = current_room_y + 1
                        current_room_x = current_room_x
                        rooms.remove()
                        Dungeon.create_branch(rooms, room_amount, new_room_probability, dungeon_map, good_dungeon, current_room_y, current_room_x, break_off_points)
                    if room == next_room and room == 4:
                        room_amount += 1
                        dungeon_map[current_room_y + 1][current_room_x] = rooms[0]
                        rooms.pop(0)
                        current_room_y = current_room_y + 1
                        current_room_x = current_room_x
                        rooms.remove()
                        Dungeon.create_branch(rooms, room_amount, new_room_probability, dungeon_map, good_dungeon, current_room_y, current_room_x, break_off_points)




    def generate(self):
        dungeon_map = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
        ]
        good_dungeon = False
        cols = 5
        rows = 5
        print(dungeon_map)
        rooms = [1, 2, 3, 4, 5, 6, 
    7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 
    17, 18, 19, 20, 21, 22, 23, 24, 25]
        
        start_room_num = rooms[0]
        starting_room_y = 4
        starting_room_x = random.choice(range(4))
        dungeon_map[starting_room_y][starting_room_x] = start_room_num
        rooms.remove(start_room_num)
        room_amount = 1
        current_room_y = starting_room_y
        current_room_x = starting_room_x
        new_room_probability = 1
        break_off_points = []
        dungeon_map = Dungeon.create_branch(rooms, room_amount, new_room_probability, dungeon_map, good_dungeon, current_room_y, current_room_x, break_off_points)
        print(dungeon_map)
        
    
# Creates main
if __name__=="__main__":
    main()
