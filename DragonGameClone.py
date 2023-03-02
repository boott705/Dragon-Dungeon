def create_branch(rooms, room_amount, dungeon_map, good_dungeon, current_room_y, current_room_x, unused_rooms, previous_x, previous_y):
        print(dungeon_map)
        possible_rooms = []
        isBreakOff = False
        if random.choice(range(100)) > 95:
            isBreakOff = True
        if room_amount == 16:
            good_dungeon = True
            return dungeon_map
        while good_dungeon == False:
            adjacent_rooms = []
            if current_room_y + 1 < 5:
                if dungeon_map[current_room_y + 1][current_room_x] == 0:
                    adjacent_rooms.append(1)
            if current_room_x + 1 < 5:
                if dungeon_map[current_room_y][current_room_x + 1] == 0:
                    adjacent_rooms.append(2)
            if current_room_y - 1 >= 0:
                if dungeon_map[current_room_y - 1][current_room_x] == 0:
                    adjacent_rooms.append(3)
            if current_room_x - 1 >= 0:
                if dungeon_map[current_room_y][current_room_x - 1] == 0:
                    adjacent_rooms.append(4)
            for room in adjacent_rooms:
                new_room = random.choice(range(99))
                if new_room < 33:
                    possible_room = random.choice(adjacent_rooms)
                    if room == possible_room and room == 1:
                        adjacent_rooms.remove(1)
                        possible_rooms.append(room)
                    if room == possible_room and room == 2:
                        adjacent_rooms.remove(2)
                        possible_rooms.append(room)
                    if room == possible_room and room == 3:
                        adjacent_rooms.remove(3)
                        possible_rooms.append(room)
                    if room == possible_room and room == 4:
                        adjacent_rooms.remove(4)
                        possible_rooms.append(room)
            if len(possible_rooms) > 0 and isBreakOff == False:
                next_room = random.choice(possible_rooms)
                possible_rooms.remove(next_room)
                for room in possible_rooms:
                        unused_rooms.append(rooms[0])
                        if room == 1:
                            dungeon_map[current_room_y + 1][current_room_x] = rooms[0]
                            rooms.pop(0)
                        if room == 2:
                            dungeon_map[current_room_y][current_room_x + 1] = rooms[0]
                            rooms.pop(0)
                        if room == 3:
                            dungeon_map[current_room_y - 1][current_room_x] = rooms[0]
                            rooms.pop(0)
                        if room == 4:
                            dungeon_map[current_room_y][current_room_x - 1] = rooms[0]
                            rooms.pop(0)
                if next_room == 1:
                    room_amount += 1
                    dungeon_map[current_room_y + 1][current_room_x] = rooms[0]
                    rooms.pop(0)
                    previous_x = current_room_x
                    previous_y = current_room_y
                    current_room_y = current_room_y + 1
                    current_room_x = current_room_x                    
                if next_room == 2:
                    room_amount += 1
                    dungeon_map[current_room_y][current_room_x + 1] = rooms[0]
                    rooms.pop(0)
                    previous_x = current_room_x
                    previous_y = current_room_y
                    current_room_y = current_room_y
                    current_room_x = current_room_x + 1
                if next_room == 3:
                    room_amount += 1
                    dungeon_map[current_room_y - 1][current_room_x] = rooms[0]
                    rooms.pop(0)
                    previous_x = current_room_x
                    previous_y = current_room_y
                    current_room_y = current_room_y - 1
                    current_room_x = current_room_x
                if next_room == 4:
                    room_amount += 1
                    dungeon_map[current_room_y][current_room_x - 1] = rooms[0]
                    rooms.pop(0)
                    previous_x = current_room_x
                    previous_y = current_room_y
                    current_room_y = current_room_y
                    current_room_x = current_room_x - 1
                Dungeon.create_branch(rooms, room_amount, dungeon_map, good_dungeon, current_room_y, current_room_x, unused_rooms, previous_x, previous_y)
            else:
                if len(unused_rooms) > 0:
                    next_room = unused_rooms[0]
                    for y in range(5):
                        for x in range(5):
                            if dungeon_map[y][x] == next_room:
                                current_room_y = y
                                current_room_x = x
                    Dungeon.create_branch(rooms, room_amount, dungeon_map, good_dungeon, current_room_y, current_room_x, unused_rooms, previous_x, previous_y)
