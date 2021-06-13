def recite(start, take=1):
    song = list()
    for i in range(1, take+1):
        if start > 2:
            song.extend(["{} bottles of beer on the wall, {} bottles of beer.".format(start, start), "Take one down and pass it around, {} bottles of beer on the wall.".format(start-1)])
        elif (start == 2):
            song.extend(["{} bottles of beer on the wall, {} bottles of beer.".format(start, start), "Take one down and pass it around, {} bottle of beer on the wall.".format(start-1)])
        elif(start == 1):
            song.extend(["{} bottle of beer on the wall, {} bottle of beer.".format(start, start), "Take it down and pass it around, no more bottles of beer on the wall."])
        else:
            song.extend(["No more bottles of beer on the wall, no more bottles of beer.",
                "Go to the store and buy some more, 99 bottles of beer on the wall."])
        if i < (take):
            song.append("")
        start -= 1
    return song

print(recite(start=3, take = 4))
