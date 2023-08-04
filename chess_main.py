import chess_check as chess

_NEED_OK_POSITIONS = 4 

if __name__ == "__main__":
    data: str = '12.01.1999'
    queens_positions = [
        [(0, 5), (1, 2), (4, 3), (2, 2), (7, 6), (5, 1), (2, 7), (3, 4)],
        [(0, 2), (1, 5), (2, 3), (3, 0), (4, 7), (5, 4), (6, 6), (7, 1)],
    ]


    for list_position in queens_positions:
        print(list_position)
        if chess.check_queen_8x8(list_position):
            print("Ферзи не бьют друг друга")
        else:
            print("Есть ферзи под ударом")

    total_case_generate = 0  
    case_ok = 0
    list_ok_positions = []  

    while case_ok < _NEED_OK_POSITIONS:
        generated_position = chess.gen_positions()
        total_case_generate += 1
        if chess.check_queen_8x8(generated_position):
            case_ok += 1
            list_ok_positions.append(generated_position)

    print(f" Всего сгенерировано {total_case_generate}, удачные:")
    for pos in list_ok_positions:
        print(pos)
