def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return dna1 > dna2

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    number = 0
    for num in dna:
        if num == nucleotide:
           number += 1
    return number

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna2 in dna1


def is_valid_sequence(dna):
    """(str) -> bool

    Return True if and only if the DNA sequence is valid
    contains no characters other than 'A' 'T' 'C' 'G'

    >>> is_valid_sequence('ABBD')
    False
    >>> is_valid_sequence('ATCG')
    True
    """

    for char in dna:
        if not (char in 'ATCG'):
            return False

    return True
    

def insert_sequence(dna1, dna2, i):
    """ (str, str, int) -> str

    Return the DNA sequence obtained by inserting the second
    DNA sequence into the first DNA sequence at the given index

    >>>insert_sequence('CCGG', 'AT', 2)
    'CCATGG'
    >>>insert_sequence('ATGG', 'CT', 0)
    'CBATGG'
    """

    dna3 = dna1[:i] + dna2 + dna1[i:]
    return dna3
    

def get_complement(n):
    """(str) -> str

    Return complement nucleotide. A and T can be bonded together, C and G and
    thus complement.

    >>>get_complement('A')
    'T'
    >>>get_complement('C')
    'G'
    """

    if n == 'A':
        return 'T'
    elif n == 'T':
        return 'A'
    elif n == 'C':
        return 'G'
    elif n == 'G':
        return 'C'
    else:
        return False
    

def get_complementry_sequence(dna):
    """(str) ->str

    Return the DNA sequence that is complementary to the given DNA sequence

    >>>get_complementry_sequence('AT')
    'TA'
    >>>get_complementry_sequence('GC')
    'CG'
    """

    sequence = ''
    for char in dna:
        sequence = sequence + get_complement(char)

    return sequence
