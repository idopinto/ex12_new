import boggle_board_randomizer
import itertools
import math

SIZE_BOARD = 4
MIN_PATH = 3
MAX_PATH = 16
BOARD_COORDINATES = [(i, j) for i in range(SIZE_BOARD) for j in range(SIZE_BOARD)]


def load_words_dict(file_path):
    """This function gets a filepath of file with records and returns it as a list of records."""
    with open(file_path) as data_file:
        word_dict = dict()
        for line in data_file:
            word = line.strip()
            if not word:
                word_dict[""] = True
            else:
                word_dict[word] = True
        return word_dict


def is_legal_coord(row, col):
    return 0 <= row < SIZE_BOARD and 0 <= col < SIZE_BOARD


def check_next_coord(current_coord, next_coord):
    if is_legal_coord(next_coord[0], next_coord[1]):
        return math.fabs(current_coord[0] - next_coord[0]) <= 1 and math.fabs(current_coord[1] - next_coord[1]) <= 1
    return False


def is_valid_path(board, path, words):
    if not path:
        return None
    word = ''
    for cur in range(len(path) - 1):
        if not is_legal_coord(path[cur][0], path[cur][1]) or not check_next_coord(path[cur], path[cur + 1]):
            return None
        word += board[path[cur][0]][path[cur][1]]
    word += board[path[-1][0]][path[-1][1]]
    if word in words.keys() and words[word]:
        return word
    else:
        return None


def find_length_n_words(n, board, words):
    if not isinstance(n, int) or n <= 0:  # MIN_PATH or n > MAX_PATH:
        return []
    n_length_paths_combinations = list(itertools.permutations(BOARD_COORDINATES, n))
    result_lst = list()
    for possible_path in n_length_paths_combinations:
        possible_word = is_valid_path(board, possible_path, words)
        if possible_word is not None:
            possible_path = [x for x in possible_path]
            result_lst.append((possible_word, possible_path))
    return result_lst


#
# class BoogleGui:
#     def __init__(self):
#         pass
#
#     def run(self):
#         pass
#
#     def set_display(self):
#         pass
#
#     def get_letters_on_board(self):
#         pass

# board = boggle_board_randomizer.randomize_board()
# # print(is_valid_path(board,[()]))
# my_dict = load_words_dict("boggle_dict.txt")
# # print(load_words_dict("boggle_dict.txt"))
# #
# board1 = [['A', 'A', 'B', "C"], ['E', 'S', 'D', 'E'], ['Z', 'QU', 'A', 'P'], ['A', 'B', 'S', 'D']]
# for line in board1:
#     print(line)
# # print(is_valid_path(board,[(4,2),(4,3),(4,4)],my_dict))
#
# print(find_length_n_words(3, board1, my_dict))
# # print(is_valid_path(board1,[(0, 2),(1, 3),(1, 2),(2,2),(3,2)],my_dict))
# # print(is_valid_path(board1,[(0, 2),(1, 3),(1, 2),(2,2),(3,2)],my_dict))
# board = [['QU', 'I', 'T', 'T'],
#         ['R', 'D', 'B', 'F'],
#         ['H', 'N', 'U', 'P'],
#                  ['N', 'A', 'S', 'N']]
# word_dict = load_words_dict("boggle_dict.txt")
# expected = [("QUIT", [(2, 0), (2, 1), (2, 2)])]
# # print(is_valid_path(board,[(0, 0), (1, 1), (2, 2), (1, 2), (0, 2),
# #                                  (0, 1)],word_dict))
# #
# print(find_length_n_words(3, board, word_dict))
#
#
#
#
# print(load_words_dict("spaces.txt"))
