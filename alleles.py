
def possible_gametes(genotype: str):

    gametes = []

    def main(genotype: str, gamete=''):

        if not genotype:
            #if gamete not in gametes: gametes.append(gamete)
            gametes.append(gamete)
            return True

        for i in range(2):
            gamete_tmp = gamete
            gamete_tmp += genotype[i]
            main(genotype[2:], gamete_tmp)

    main(genotype)

    return gametes


def geno_2_pheno(genotype: str):

    phenotype = ''

    for i in range(0, len(genotype), 2):
        if genotype[i].isupper() or genotype[i+1].isupper():
            phenotype += genotype[i].upper()
        else:
            phenotype += genotype[i].lower()

    return phenotype


def pheno_2_geno(phenotype: str):

    genotype = ''

    for i in phenotype:
        if i.isupper():
            genotype += i + '?'
        else:
            genotype += i * 2

    return genotype


def is_genotype(genotype: str):

    genotype = genotype.lower()

    for i in range(len(genotype)):
        if genotype.count(genotype[i]) % 2:
            return False
    return True


def fertilization(gamete_a, gamete_b):

    zygote = ''

    for i in range(len(gamete_a)):
        if gamete_a[i].isupper():
            zygote += gamete_a[i] + gamete_b[i]
        elif gamete_b[i].isupper():
            zygote += gamete_b[i] + gamete_a[i]
        else:
            zygote += gamete_a[i] + gamete_b[i]

    return zygote


def possible_zygotes(gametes_1: list, gametes_2: list):

    zygotes = []

    for gamete_1 in gametes_1:
        for gamete_2 in gametes_2:
            zygotes.append(fertilization(gamete_1, gamete_2))

    return(zygotes)
