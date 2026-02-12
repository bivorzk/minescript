import minescript
import time

while True:
    # Get the player's current position inside the loop
    for i in range(15):
        minescript.execute(f"/particle lava {-42} {118  } {132 + i} 0 0 0 1 1 normal")
        minescript.execute(f"/particle lava {-42 - i} {118 } {132} 0 0 0 1 1 normal")
        minescript.execute(f"/particle lava {-56 + i} {118 } {145} 0 0 0 1 1 normal")
        minescript.execute(f"/particle lava {-56} {118 } {146 - i} 0 0 0 1 1 normal")

#        minescript.execute(f"/particle lava {-42 - i} {118 - i } {132 - i} 0 0 0 0.5 25 normal")