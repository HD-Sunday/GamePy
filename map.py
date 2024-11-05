# # 0 - поле🟩
# 1 - дерево 🌳
# 2 - река 💦
# 3 - госпиталь 🏥
# 4 - апгрейдШоп 🛒

CELL_TYPES = "🟩🌳💦🏥🛒"

class Map:

    # def generate_rivers(self):
    #
    # def generate_forest(self):

    def print_map(self):
        print("🧱" * (self.w + 2))
        for row in self.cells:
            print("🧱", end="")
            for cell in row:
                if (cell >= 0 and cell < len(CELL_TYPES)):
                    print(CELL_TYPES[cell], end="")
            print("🧱")
        print("🧱" * (self.w + 2))

    def check_bounds(self, x, y):
        if (x < 0 or y < 0 or x>= self.h or y >= self.w):
            return False
        return True
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for i in range(w)] for j in range(h)]


tmp = Map(30, 6)
tmp.cells[1][1] = 1
tmp.cells[2][2] = 2
tmp.cells[3][3] = 3
tmp.cells[4][4] = 4