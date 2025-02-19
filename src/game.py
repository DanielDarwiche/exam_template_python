from operator import index

from .grid import Grid
from .pickups import pickup_objects, randomize, trap_objects, Item, Trap, steps, drop_new_item
from .player import Player

# A. Spelare börjar nära mitten av rummet pga nedanstående rads koordinater
player = Player(17, 5)
score = 0
inventory = []

g = Grid()
g.set_player(player)
g.make_walls()
randomize(g, pickup_objects)
randomize(g, trap_objects)

def print_status(game_grid):
    """Visa spelvärlden och antal poäng."""
    print("--------------------------------------")
    print(f"You have {score} points.")
    print(game_grid)


command = "a"
# Loopa tills användaren trycker Q eller X.
while not command.casefold() in ["q", "x"]:
    maybe_item = None
    print_status(g)

    command = input("Use WASD to move, Q/X to quit. ")
    command = command.casefold()[:1]
    if command == "d" and player.can_move(1, 0, g):  # move right
        maybe_item = g.get(player.pos_x + 1, player.pos_y)
        player.move(1, 0)

# B. Förflyttningar i alla 4 riktningar. (WASD) => Lägger till fler val här

    elif command == "a" and player.can_move(-1, 0, g):  # move left
        maybe_item = g.get(player.pos_x - 1, player.pos_y)
        player.move(-1, 0)

    elif command == "w" and player.can_move(0, -1, g):  # move up
        maybe_item = g.get(player.pos_x, player.pos_y - 1)
        player.move(0, -1)

    elif command == "s" and player.can_move(0, 1, g):  # move down
        maybe_item = g.get(player.pos_x, player.pos_y + 1)
        player.move(0, 1)

# F. Nytt kommando: "i", skriver ut innehållet i spelarens inventory.
    elif command == "i":
        print("You pressed command 'i', to see Inventory:")
        if len(inventory) == 0 :
            print("The inventory is empty..")
        for i in range(len(inventory)):
            print(f"Fruit {i + 1}: {inventory[i]}")

# E. Inventory - alla saker som man plockar upp ska sparas i en lista.
    if isinstance(maybe_item, Item):
        inventory.append(maybe_item.name)
        score += maybe_item.value
        print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
        g.clear(player.pos_x, player.pos_y)

    elif isinstance(maybe_item, Trap):
        score += maybe_item.value
        print(f"You found a trap, a {maybe_item.name}! {maybe_item.value} points.")
        g.clear(player.pos_x, player.pos_y)

    if steps % 25 == 0 and steps > 0:
        drop_new_item(g, pickup_objects)
        print("A new item has appeared on the map!")

# G. The floor is lava - för varje steg man går ska man tappa 1 poäng.
    if command == "d" or command == "a" or command == "w" or command == "s":
        score -= 1
        steps += 1

# Hit kommer vi när while-loopen slutar
print("Thank you for playing!")
