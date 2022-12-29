#!/usr/bin/env python3

def project(board, rock, rock_pos, rock_alt):
    if rock_alt >= len(board):
        return True

    rock_lines = rock.split("\n")
    board_lines = board[rock_alt:]

    for i, j in zip(rock_lines, board_lines):
        i = " " * rock_pos + i
        #print(f"r:{i}\nb:{j}")
        for k,l in zip(i, j):
            if k == "#" and l == "#":
                return False
    return True 

def can_move_sideways(board, rock, rock_pos, rock_alt, rock_width, direction):
    if 0 <= rock_pos + direction and rock_pos + direction + rock_width <= 7:
        return project(board, rock, rock_pos + direction, rock_alt)
    else:
        return False

def can_move_down(board, rock, rock_pos, rock_altitude, rock_width, rock_height):
    if rock_altitude <= 0:
        return False

    return project(board, rock, rock_pos, rock_altitude - 1)


def merge_rock(board, rock, rock_pos, rock_alt, rock_height):
    rock_lines = rock.split("\n")

    for idx, rock_line in enumerate(rock_lines):
        idx += rock_alt
        if idx < len(board):
            tmp = []
            rock_line = " " * rock_pos + rock_line + " " * (7 - len(rock_line) - rock_pos)
            for i, j in zip(board[idx], rock_line):
                if i == "#" or j == "#":
                    tmp.append("#")
                else:
                    tmp.append(" ")
            board[idx] = "".join(tmp)
        else:
            # add new lines
            line = " " * rock_pos + rock_line + " " * (7 - rock_pos - len(rock_line)) 
            board.append(line)
    return board

def fill_down(board):
    tmp = "       "
    for idx in range(len(board)-1, -1, -1):
        tmp2 = []
        for i, j in zip(board[idx], tmp):
            if i == "#" or j == "#":
                tmp2.append("#")
            else:
                tmp2.append(" ")
        tmp = "".join(tmp2)
        if tmp == "#######":
            board[idx] = tmp
    return board

def compact_board(board):
    ans = 0
    for line in board:
        if line == "#######":
            ans += 1
        else:
            break
    return ans, board[ans:]

def solution(data, iterations):


    rock_count = 1754
    tmp = 2779
    rock_idx = 4
    wind_index = 5
    ans = 15
    if rock_count + 1750 < iterations:
        tmp2 = (iterations - rock_count) // 1750
        tmp += 2781 * tmp2
        rock_count += tmp2 * 1750

    board = [" ##### ",
"#####  ",
"##  #  ",
"## ##  ",
"#####  ",
"## #   ",
"  ###  ",
" ## #  ",
" ## #  ",
" ####  ",
"    #  ",
"   ### ",
" ####  ",
"   #   ",
"   #   "]

    rocks = (("####", 4, 1), 
             (" # \n###\n # ", 3, 3), 
             ("###\n  #\n  #", 3, 3), 
             ("#\n#\n#\n#", 1, 4), 
             ("##\n##", 2, 2))




    while rock_count < iterations:
        prev_wind_index = wind_index
        new_rock, width, height = rocks[rock_idx]
        new_rock_alt = ans + 3
        new_rock_pos = 2
        rock_count += 1
        rock_idx = rock_count % len(rocks)

        falling = True
        while falling:
            #blow around
            wind = data[wind_index]
            wind_index += 1
            wind_index %= len(data)


            if wind == ">" and can_move_sideways(board, new_rock, new_rock_pos, new_rock_alt, width, 1):
                new_rock_pos += 1
            elif wind == "<" and can_move_sideways(board, new_rock, new_rock_pos, new_rock_alt, width, -1):
                new_rock_pos -= 1

            #fall
            if can_move_down(board, new_rock, new_rock_pos, new_rock_alt, width, height):
                new_rock_alt -= 1
            else:
                falling = False
                if ans < new_rock_alt + height:
                    ans = new_rock_alt + height
                board = merge_rock(board, new_rock, new_rock_pos, new_rock_alt, height)

        board = fill_down(board)
        tmp2, board = compact_board(board)
        tmp += tmp2
        ans -= tmp2
    return ans + tmp

if __name__ == '__main__':
    with open("day17.txt") as f:
        data = f.readline().strip()
    print(solution(data, 2022))
    print(solution(data, 1000000000000))
