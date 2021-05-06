def tally(rows):
    dict = {'Allegoric Alaskans': [0, 0, 0, 0, 0], 'Blithering Badgers' : [0, 0, 0, 0, 0], 'Courageous Californians': [0, 0, 0, 0, 0], 'Devastating Donkeys': [0, 0, 0, 0, 0]}

    rowsList =  [x.split(',') for x in rows]
    rowElements = [x.split(';') for x in rows]
    for i in rowElements:
        if i[2] == 'win':
            match_player_first = i[0]
            match_player_second = i[1]
            for key, val in dict.items():
                if(key == match_player_first):
                    (dict[match_player_first][0]) = dict[match_player_first][0] + 1
                    (dict[match_player_first][1]) = dict[match_player_first][1] + 1
                if(key == match_player_second):
                    (dict[match_player_second][0]) = dict[match_player_second][0] + 1
                    (dict[match_player_second][3]) = dict[match_player_second][3] + 1


        elif i[2] == 'loss':
            match_player_first = i[1]
            match_player_second = i[0]
            for key, val in dict.items():
                if(key == match_player_first):
                    (dict[match_player_first][0]) = dict[match_player_first][0] + 1
                    (dict[match_player_first][1]) = dict[match_player_first][1] + 1
                if(key == match_player_second):
                    (dict[match_player_second][0]) = dict[match_player_second][0] + 1
                    (dict[match_player_second][3]) = dict[match_player_second][3] + 1

        else:
            match_player_first = i[0]
            match_player_second = i[1]
            for key, val in dict.items():
                if(key == match_player_first):
                    (dict[match_player_first][0]) = dict[match_player_first][0] + 1
                    (dict[match_player_first][2]) = dict[match_player_first][2] + 1
                if(key == match_player_second):
                    (dict[match_player_second][0]) = dict[match_player_second][0] + 1
                    (dict[match_player_second][2]) = dict[match_player_second][2] + 1

    for key, val in dict.items():
        points = dict[key][1] * 3 +  dict[key][2]
        dict[key][4] = points

#Sortung the dictionary by the fourth item in each list
    # dict =  sorted(dict.items(), key = lambda e:e[1][4], reverse = True)

    FORMAT='{:<30} |{:>3} |{:>3} |{:>3} |{:>3} |{:>3}'
    table = [None] * 5
    # print(table)
    table[0] = FORMAT.format('Team', 'MP', 'W', 'D', 'L', 'P')
    i = 1
    for key, value in sorted(dict.items(), key = lambda e: e[1][4], reverse = True):
        if value[0] == 0:
            table.remove(None)
        else:
            table[i] = FORMAT.format(str(key), str(value[0]), str(value[1]), str(value[2]), str(value[3]), str(value[4]))
        i = i + 1


    return table
