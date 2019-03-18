def countingValleys(n, s):
    altitude = 0
    valleys = 0
    reset = True

    for step in s:
        print(altitude)
        #print(valleys)
        if step == 'U':
            altitude += 1
        else:
            altitude -= 1

        if altitude == 0:
            reset = True
        if altitude < 0 and step == 'U':
            reset = False

        if reset and altitude < -1:
            valleys += 1

    return valleys

s = 'DUDUUUUUUUUDUDDUUDUUDDDUUDDDDDUUDUUUUDDDUUUUUUUDDUDUDUUUDDDDUUDDDUDDDDUUDDUDDUUUDUUUDUUDUDUDDDDDDDDD'

print(countingValleys(100,s))