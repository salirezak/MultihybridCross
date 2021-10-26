from prettytable import PrettyTable, DOUBLE_BORDER
from ansi import CYAN_C, RESET_C


def punnett_square_draw(gametes_1: list, gametes_2: list, zygotes: list):

    rows = []
    gamete_index = 0
    for i in range(0, len(zygotes), len(gametes_2)):
        gamete = [gametes_1[gamete_index]]
        zygote = zygotes[i:i+len(gametes_2)]
        rows.append(list(map(lambda x: CYAN_C + x + RESET_C, gamete)) + zygote)
        gamete_index += 1

    punnett = PrettyTable()
    punnett.title = 'Punnet Square'
    punnett.field_names = [''] + \
        list(map(lambda x: CYAN_C + x + RESET_C, gametes_2))
    punnett.add_rows(rows)
    punnett.set_style(DOUBLE_BORDER)

    return punnett
