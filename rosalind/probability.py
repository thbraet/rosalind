def probability_dominant_offspring(k, m, n):
    """
    Calculate the probability of offspring displaying a dominant phenotype 
    given the population of organisms with specific genotypes.
    Assume that any two organisms can mate.

    Parameters:
    k (int): Number of homozygous dominant organisms.
    m (int): Number of heterozygous organisms.
    n (int): Number of homozygous recessive organisms.

    Returns:
    float: Probability of an offspring having a dominant phenotype.
    """
    total = k + m + n
    
    prob_kk = k / total * (k - 1) / (total - 1)
    prob_mm = m / total * (m - 1) / (total - 1)
    prob_nn = n / total * (n - 1) / (total - 1)
    prob_km = k / total * m / (total - 1) + m / total * k / (total - 1)
    prob_kn = k / total * n / (total - 1) + n / total * k / (total - 1)
    prob_mn = m / total * n / (total - 1) + n / total * m / (total - 1)

    prob_kk_dom = 1
    prob_mm_dom = 3 / 4
    prob_nn_dom = 0
    prob_km_dom = 1
    prob_kn_dom = 1
    prob_mn_dom = 1 / 2

    prob_dom = (
        prob_kk * prob_kk_dom
        + prob_mm * prob_mm_dom
        + prob_nn * prob_nn_dom
        + prob_km * prob_km_dom
        + prob_kn * prob_kn_dom
        + prob_mn * prob_mn_dom
    )
    
    return prob_dom
