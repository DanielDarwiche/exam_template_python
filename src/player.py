class Player:
    marker = "@"

    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y

    # Flyttar spelaren. "dx" och "dy" är skillnaden
    def move(self, dx, dy):
        """Flyttar spelaren.\n
        dx = horisontell förflyttning, från vänster till höger\n
        dy = vertikal förflyttning, uppifrån och ned"""
        self.pos_x += dx
        self.pos_y += dy



# C. Man ska inte kunna gå igenom väggar.
    def can_move(self, x, y, grid):
        x_move = self.pos_x + x
        y_move = self.pos_y + y

        # Kontrollera om den nya positionen är inom gridens gränser
        if 0 <= x_move < grid.width and 0 <= y_move < grid.height:
            # Kontrollera om den nya positionen inte är en vägg
            if grid.get(x_move, y_move) != grid.wall:
                return True
            else:
                print("You can't walk into walls!")
                return False
        else:
            print("You can't move outside the grid!")
            return False
