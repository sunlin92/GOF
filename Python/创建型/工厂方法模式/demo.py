#!/usr/bin/env python3

import itertools
import unicodedata

# 利用解包一次定义所有字符常量，方便编写调试和字符串驻留
DRAUGHT, PAWN, ROOK, KNIGHT, BISHOP, KING, QUEEN = (
    "DRAUGHT",
    "PAWN",
    "ROOK",
    "KNIGHT",
    "BISHOP",
    "KING",
    "QUEEN",
)
BLACK, WHITE = ("BLACK", "WHITE")


def console(char, background):
    return "\x1B[{background}m{char}\x1B[0m".format(
        background=43 if background == BLACK else 47, char=char or " "
    )


class AbstractBoard:
    def __init__(self, rows, columns):
        # 生成空棋盘二维数组
        self.board = [[None for _ in range(columns)] for _ in range(rows)]
        self.populate_board()

    def populate_board(self):
        raise NotImplementedError()

    def __str__(self):
        squares = []
        for y, row in enumerate(self.board):
            for x, piece in enumerate(row):
                square = console(piece, BLACK if (y + x) % 2 else WHITE)
                squares.append(square)
            squares.append("\n")
        return "".join(squares)


class CheckersBoard(AbstractBoard):
    def __init__(self):
        self.populate_board()

    def populate_board(self):
        def black():
            return create_piece(DRAUGHT, BLACK)

        def white():
            return create_piece(DRAUGHT, WHITE)

        rows = (
            (None, black()),
            (black(), None),
            (None, black()),
            (black(), None),  # 4 black rows
            (None, None),
            (None, None),  # 2 blank rows
            (None, white()),
            (white(), None),
            (None, white()),
            (white(), None),
        )  # 4 white rows
        print(list(rows))
        self.board = [
            list(itertools.islice(itertools.cycle(squares), 0, len(rows)))
            for squares in rows
        ]


class ChessBoard(AbstractBoard):
    def __init__(self):
        super().__init__(8, 8)

    def populate_board(self):
        rows = (
            ((0, 7), ROOK),
            ((1, 6), KNIGHT),
            ((2, 5), BISHOP),
            ((3,), QUEEN),
            ((4,), KING),
        )
        for row, color in ((0, BLACK), (7, WHITE)):
            for columns, kind in rows:
                for column in columns:
                    self.board[row][column] = create_piece(kind, color)
        for column in range(8):
            for row, color in ((1, BLACK), (6, WHITE)):
                self.board[row][column] = create_piece(PAWN, color)


def create_piece(kind, color):
    color = "White" if color == WHITE else "Black"
    name = {
        DRAUGHT: "Draught",
        PAWN: "ChessPawn",
        ROOK: "ChessRook",
        KNIGHT: "ChessKnight",
        BISHOP: "ChessBishop",
        KING: "ChessKing",
        QUEEN: "ChessQueen",
    }[kind]
    # 在全局命名空间中， 返回对应的类的对象
    return globals()[color + name]()


class Piece(str):

    __slots__ = ()


for code in itertools.chain((0x26C0, 0x26C2), range(0x2654, 0x2660)):
    # 获取旗子Unicode码位, 转换成字符
    char = chr(code)
    name = unicodedata.name(char).title().replace(" ", "")
    # name与之前的命名统一
    if name.endswith("sMan"):
        name = name[:-4]
    # type创建旗子类
    new = (lambda char: lambda cls: Piece.__new__(cls, char))(char)
    new.__name__ = "__new__"
    cls = type(name, (Piece,), dict(__slots__=(), __new__=new))
    # 在全局命名空间中， 创建对应的类
    globals()[name] = cls


def main():
    # board = ChessBoard()
    board = CheckersBoard()
    print(board)


if __name__ == "__main__":
    main()
