from prettytable import PrettyTable, DOUBLE_BORDER
from scipy.stats import chi2
from restricted_input import r_input

from ansi import RESET_C, UP_CURSOR, MAGENTA_C, LEFT_CURSOR, CYAN_C, YELLOW_C, SAVE_CURSOR, LOAD_CURSOR, RED_C, GREEN_C, CLEAR_TO_END


def chi_square_test(phenotypes, ratios):
    phenotypes = list(phenotypes)
    ratios = list(ratios)
    phenotypes_number = len(phenotypes)
    observed = [0 for i in range(phenotypes_number)]
    expected = [0 for i in range(phenotypes_number)]
    chi_values = [0 for i in range(phenotypes_number)]

    def calculation():
        expected = [i*sum(observed)/sum(ratios) for i in ratios]
        chi_values = list(map(lambda e, o: (o-e)**2/e, expected, observed))

        return expected, chi_values

    def print_chi(index, input_mood=True):
        chi_calculate = PrettyTable()
        chi_calculate.title = 'Chi-2 Calculatation'

        phenotypes_tmp = list(map(lambda x: str(x), phenotypes))
        if input_mood:
            phenotypes_tmp[index] = MAGENTA_C + phenotypes_tmp[index] + RESET_C
        chi_calculate.add_column('Phenotypes', phenotypes_tmp)

        ratios_tmp = list(map(lambda x: str(int(x)), ratios))
        chi_calculate.add_column('Ratios', ratios_tmp)

        expected_tmp = list(map(lambda x: str(round(x, 2)), expected))
        chi_calculate.add_column('Expected', expected_tmp)

        observed_tmp = list(map(lambda x: str(int(x)), observed))
        if input_mood:
            observed_tmp[:index] = list(
                map(lambda x: YELLOW_C + x + RESET_C, observed_tmp[:index]))
            observed_tmp[index] = LEFT_CURSOR(1) + SAVE_CURSOR
            chi_calculate.add_column(
                MAGENTA_C + 'Observed' + RESET_C, observed_tmp)
        else:
            observed_tmp = list(
                map(lambda x: YELLOW_C + x + RESET_C, observed_tmp))
            chi_calculate.add_column('Observed', observed_tmp)

        chi_values_tmp = list(map(lambda x: str(round(x, 2)), chi_values))
        chi_calculate.add_column('Chi-2', chi_values_tmp)

        chi_calculate.add_row(['', '', '', '', ''])
        chi_calculate.add_row([f'Sum:{len(phenotypes)}', sum(ratios), int(
            sum(expected)), sum(observed), CYAN_C + str(round(sum(chi_values), 2)) + RESET_C])
        chi_calculate.set_style(DOUBLE_BORDER)
        print(chi_calculate)

    print('\n'*5, end='')
    for i in range(phenotypes_number):
        print(UP_CURSOR(i+5) + RESET_C + CLEAR_TO_END, end='')
        print_chi(i)
        observed[i] = int(r_input(LOAD_CURSOR + MAGENTA_C +
                          LEFT_CURSOR(3) + '> ' + YELLOW_C, input_type='integer'))
        expected, chi_values = calculation()
    else:
        print(UP_CURSOR(i+6) + RESET_C + CLEAR_TO_END, end='')
        print_chi(None, input_mood=False)

    p_value = float(r_input(MAGENTA_C + 'p-value> ' +
                    YELLOW_C, input_type='float'))
    print(UP_CURSOR(1) + RESET_C)
    df = len(phenotypes) - 1
    calculated_chi2 = sum(chi_values)
    expected_chi2 = chi2.ppf(1-p_value, df)
    result = calculated_chi2 < expected_chi2

    chi_result = PrettyTable()
    chi_result.title = 'Chi-2 Test'
    chi_result.add_column('df', [df])
    chi_result.add_column('p-value', [p_value])
    chi_result.add_column('Calculated Chi-2', [calculated_chi2])
    chi_result.add_column('Expected Chi-2', [expected_chi2])
    if result:
        chi_result.add_column('Result', [GREEN_C + str(result) + RESET_C])
    else:
        chi_result.add_column('Result', [RED_C + str(result) + RESET_C])
    chi_result.set_style(DOUBLE_BORDER)
    print(chi_result)
