class Piece:
    def __init__(self, color, is_king=False):
        self.color = color
        self.is_king = is_king
        self.position = None  # You can represent the position using (row, column)
