def phenotype_probability(parent1, parent2):
    """
    Calculate the probability of a child's phenotype based on the genotypes of both parents.

    This function uses Mendelian genetics and the principles of a Punnett square to determine
    the likelihood of different genotypes (AA, Aa, aa) in the offspring, given the genotypes
    of the parents.

    Args:
        parent1 (str): The genotype of the first parent. Must be one of 'AA', 'Aa', or 'aa'.
        parent2 (str): The genotype of the second parent. Must be one of 'AA', 'Aa', or 'aa'.

    Returns:
        dict: A dictionary where the keys are possible offspring genotypes ('AA', 'Aa', 'aa')
              and the values are their respective probabilities (0.0 to 1.0).

    Raises:
        ValueError: If either parent genotype is invalid (not 'AA', 'Aa', or 'aa').

    Example:
        >>> phenotype_probability('Aa', 'Aa')
        {'AA': 0.25, 'Aa': 0.5, 'aa': 0.25}
    """
    # Define possible offspring combinations based on Punnett Square
    combinations = {
        ("AA", "AA"): {"AA": 1.0, "Aa": 0.0, "aa": 0.0},
        ("AA", "Aa"): {"AA": 0.5, "Aa": 0.5, "aa": 0.0},
        ("AA", "aa"): {"AA": 0.0, "Aa": 1.0, "aa": 0.0},
        ("Aa", "Aa"): {"AA": 0.25, "Aa": 0.5, "aa": 0.25},
        ("Aa", "aa"): {"AA": 0.0, "Aa": 0.5, "aa": 0.5},
        ("aa", "aa"): {"AA": 0.0, "Aa": 0.0, "aa": 1.0},
    }

    # Determine offspring probabilities
    if (parent1, parent2) in combinations:
        return combinations[(parent1, parent2)]
    else:
        raise ValueError("Invalid parent genotypes. Use 'AA', 'Aa', or 'aa'.")


def probability_dominant_offspring(AA=0, Aa=0, aa=0):
    """
    Calculate the probability of offspring displaying a dominant phenotype
    given the population of organisms with specific genotypes.
    Assume that any two organisms can mate.

    The genotypes are as follows:
    - Homozygous dominant (AA)
    - Heterozygous (Aa)
    - Homozygous recessive (aa)

    Parameters:
    AA (int): Number of homozygous dominant (AA) organisms.
    Aa (int): Number of heterozygous (Aa) organisms.
    aa (int): Number of homozygous recessive (aa) organisms.

    Returns:
    float: Probability of an offspring having a dominant phenotype (AA or Aa).

    Example:
        >>> probability_dominant_offspring(10, 20, 5)
        0.625

    Raises:
        ValueError: If any genotype count is less than 0.
    """
    # Check for valid inputs (non-negative numbers)
    if any(x < 0 for x in [AA, Aa, aa]):
        raise ValueError("Genotype counts must be non-negative integers.")

    total = AA + Aa + aa

    print(total)

    # Calculate the probabilities for all genotype combinations
    prob_AA_AA = AA / total * (AA - 1) / (total - 1)
    prob_Aa_Aa = Aa / total * (Aa - 1) / (total - 1)
    prob_aa_aa = aa / total * (aa - 1) / (total - 1)
    prob_AA_Aa = AA / total * Aa / (total - 1) + Aa / total * AA / (total - 1)
    prob_AA_aa = AA / total * aa / (total - 1) + aa / total * AA / (total - 1)
    prob_Aa_aa = Aa / total * aa / (total - 1) + aa / total * Aa / (total - 1)

    print(
        prob_AA_AA, prob_Aa_Aa, prob_aa_aa, prob_AA_Aa, prob_AA_aa, prob_Aa_aa
    )

    # Get probabilities for dominant phenotypes from the Punnett square
    prob_AA_AA_dom = (
        phenotype_probability("AA", "AA")["AA"]
        + phenotype_probability("AA", "AA")["Aa"]
    )
    prob_Aa_Aa_dom = (
        phenotype_probability("Aa", "Aa")["AA"]
        + phenotype_probability("Aa", "Aa")["Aa"]
    )
    prob_aa_aa_dom = (
        phenotype_probability("aa", "aa")["AA"]
        + phenotype_probability("aa", "aa")["Aa"]
    )
    prob_AA_Aa_dom = (
        phenotype_probability("AA", "Aa")["AA"]
        + phenotype_probability("AA", "Aa")["Aa"]
    )
    prob_AA_aa_dom = (
        phenotype_probability("AA", "aa")["AA"]
        + phenotype_probability("AA", "aa")["Aa"]
    )
    prob_Aa_aa_dom = (
        phenotype_probability("Aa", "aa")["AA"]
        + phenotype_probability("Aa", "aa")["Aa"]
    )

    print(prob_Aa_aa_dom)

    # Calculate the overall probability for a dominant phenotype
    prob_dom = (
        prob_AA_AA * prob_AA_AA_dom
        + prob_Aa_Aa * prob_Aa_Aa_dom
        + prob_aa_aa * prob_aa_aa_dom
        + prob_AA_Aa * prob_AA_Aa_dom
        + prob_AA_aa * prob_AA_aa_dom
        + prob_Aa_aa * prob_Aa_aa_dom
    )

    return prob_dom


def expected_dominant_offspring(
    AA_AA, AA_Aa, AA_aa, Aa_Aa, Aa_aa, aa_aa, nr_of_offspring_per_couple=2
):
    """
    Calculate the expected number of offspring displaying a dominant phenotype
    given the number of couples with specific genotypes and the number of offspring per couple.

    This function uses the probabilities of offspring genotypes (dominant phenotypes)
    derived from a Punnett square for each couple's genotype combination. The expected
    number of dominant offspring is calculated by summing the probabilities for dominant
    phenotypes across different genotype combinations.

    Parameters:
        AA_AA (int): Number of couples with genotype AA-AA.
        AA_Aa (int): Number of couples with genotype AA-Aa.
        AA_aa (int): Number of couples with genotype AA-aa.
        Aa_Aa (int): Number of couples with genotype Aa-Aa.
        Aa_aa (int): Number of couples with genotype Aa-aa.
        aa_aa (int): Number of couples with genotype aa-aa.
        nr_of_offspring_per_couple (int, optional): The number of offspring per couple. Default is 2.

    Returns:
        float: Expected number of offspring displaying a dominant phenotype (AA or Aa).

    Example:
        >>> expected_dominant_offspring(10, 20, 15, 10, 25, 5)
        57.0

    Raises:
        ValueError: If any genotype count is less than 0.
    """

    # Check for valid inputs (non-negative numbers)
    if any(x < 0 for x in [AA_AA, AA_Aa, AA_aa, Aa_Aa, Aa_aa, aa_aa]):
        raise ValueError("Genotype counts must be non-negative integers.")

    # Calculate probabilities for dominant phenotypes from the Punnett square
    prob_dom_AA_AA = (
        phenotype_probability("AA", "AA")["AA"]
        + phenotype_probability("AA", "AA")["Aa"]
    )
    prob_dom_AA_Aa = (
        phenotype_probability("AA", "Aa")["AA"]
        + phenotype_probability("AA", "Aa")["Aa"]
    )
    prob_dom_AA_aa = (
        phenotype_probability("AA", "aa")["AA"]
        + phenotype_probability("AA", "aa")["Aa"]
    )
    prob_dom_Aa_Aa = (
        phenotype_probability("Aa", "Aa")["AA"]
        + phenotype_probability("Aa", "Aa")["Aa"]
    )
    prob_dom_Aa_aa = (
        phenotype_probability("Aa", "aa")["AA"]
        + phenotype_probability("Aa", "aa")["Aa"]
    )
    prob_dom_aa_aa = (
        phenotype_probability("aa", "aa")["AA"]
        + phenotype_probability("aa", "aa")["Aa"]
    )

    # Calculate expected dominant offspring
    expected_dominant = nr_of_offspring_per_couple * (
        AA_AA * prob_dom_AA_AA
        + AA_Aa * prob_dom_AA_Aa
        + AA_aa * prob_dom_AA_aa
        + Aa_Aa * prob_dom_Aa_Aa
        + Aa_aa * prob_dom_Aa_aa
        + aa_aa * prob_dom_aa_aa
    )

    return expected_dominant
