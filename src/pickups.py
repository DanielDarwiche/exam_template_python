import random

from .grid import Grid

steps = 0

class Item:
    """Representerar saker man kan plocka upp."""
    # D. Fruktsallad - alla frukter ska vara värda 20 poäng i stället för 10.
    def __init__(self, name, value = 20, symbol="*"):
        self.name = name
        self.value = value
        self.symbol = symbol

    def __str__(self):
        return self.symbol


class Trap:
    def __init__(self, name, value = -10, symbol="O"):
        self.name = name
        self.value = value
        self.symbol = symbol

    def __str__(self):
        return self.symbol

pickup_objects = [Item("carrot"), Item("apple"), Item("strawberry"), Item("cherry"), Item("watermelon"), Item("radish"), Item("banana"), Item("litchi")]
trap_objects = [Trap("Bomb"), Trap("PoopBomb"), Trap("Chemical Bomb"), Trap("Banana peel")]
# I(VG). Fällor - introducera valfri fälla till spelplanen. Om man går på en ruta med en fälla
# ska man förlora 10 poäng. Fällan ska ligga kvar så att man kan falla i den flera gånger

def randomize(grid, objects):
    for item in objects:
        while True:
            x = grid.get_random_x()
            y = grid.get_random_y()
            if grid.is_empty(x, y):
                grid.set(x, y, item)
                break  # avbryt while-loopen, fortsätt med nästa varv i for-loopen

# L(VG). Bördig jord - efter varje 25:e drag skapas en ny frukt/grönsak någonstans på kartan.
def drop_new_item(grid, objects):
    item = random.choice(objects)
    while True:
        x = grid.get_random_x()
        y = grid.get_random_y()
        if grid.is_empty(x, y):
            grid.set(x, y, item)
            break
