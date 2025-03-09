OCEAN_WAVES = ["`", "~"]
NUM_COLUMNS = 60
NUM_ROWS = 15
MAX_ROW_DIGITS = len(str(NUM_ROWS))

NUM_CHESTS = 3
NUM_SONAR_DEVICES = 20
SONAR_RANGE = 10

INSTRUCTIONS = f"""
Instructions:
You are the captain of a treasure-hunting ship. 
Your current mission is to use sonar devices to find {NUM_CHESTS} sunken treasure chests at the bottom of the ocean. 
But you only have cheap sonar that finds distance, not direction.

Enter the coordinates to drop a sonar device. 
The ocean map will be marked with how far away the nearest chest is, 
or an X if it is beyond the sonar device's range. 

For example, the C marks are where chests are. 
The sonar device shows a 3 because the closest chest is 3 spaces away.
(In the real game, the chests are not visible in the ocean.)

                    1         2         3
          012345678901234567890123456789012
        0 ~~~~`~```~`~``~~~``~`~~``~~~``~`~ 0
        1 ~`~`~``~~`~```~~~```~~`~`~~~`~~~~ 1
        2 `~`C``3`~~~~`C`~~~~`````~~``~~~`` 2
        3 ````````~~~`````~~~`~`````~`~``~` 3
        4 ~`~~~~`~~`~~`C`~``~~`~~~`~```~``~ 4
          012345678901234567890123456789012
                    1         2         3

Press enter to continue...
"""