from restricted_input import r_input
from string import ascii_lowercase, ascii_uppercase
from os import system

from alleles import possible_gametes, possible_zygotes, geno_2_pheno
from punnett_square import punnett_square_draw
from chi_square import chi_square_test
from ansi import MAGENTA_C, RESET_C, YELLOW_C

# clear shell
system('clear')

# get number of traits
print()
traits_number = int(r_input(
    MAGENTA_C + 'How many traits to check> ' + YELLOW_C, input_type='integer'))
print(RESET_C)
# create parents
PARENT_1 = ''
PARENT_2 = ''
for i in range(traits_number):
    PARENT_1 += ascii_uppercase[i] + ascii_lowercase[i]
    PARENT_2 += ascii_uppercase[i] + ascii_lowercase[i]

# create gametes of parents
GAMETES_1 = possible_gametes(PARENT_1)
GAMETES_2 = possible_gametes(PARENT_2)

# create zygote filials of gametes
ZYGOTES = possible_zygotes(GAMETES_1, GAMETES_2)

# create punnett square
punnett = punnett_square_draw(GAMETES_1, GAMETES_2, ZYGOTES)
# print punnett square
# print(punnett)

# create phenotypes of zygote filials & phenotype ratios
phenotypes = []
ratios = []
for genotype in ZYGOTES:
    phenotype = geno_2_pheno(genotype)
    if phenotype not in phenotypes:
        phenotypes.append(phenotype)
        ratios.append(list(map(geno_2_pheno, ZYGOTES)).count(phenotype))
# sort phenotypes of zygote filials & phenotype ratios
tmp = list(phenotypes)
phenotypes.sort(key=lambda x: ratios[tmp.index(x)], reverse=True)
ratios.sort(reverse=True)
del tmp


chi_square_test(phenotypes, ratios)
