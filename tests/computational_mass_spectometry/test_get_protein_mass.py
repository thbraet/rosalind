import pytest

from rosalind.read_files import read_monoisotopic_mass
from rosalind.computational_mass_spectometry import get_protein_mass


def test_protein_mass_no_rounding():
    assert get_protein_mass("ACDE", rounding=None) == pytest.approx(
        71.03711 + 103.00919 + 115.02694 + 129.04259, rel=1e-9
    )


def test_protein_mass_with_rounding():
    assert get_protein_mass("ACDE", rounding=2) == 418.12


def test_protein_mass_empty_chain():
    assert get_protein_mass("", rounding=None) == 0.0


def test_protein_mass_single_amino_acid():
    assert get_protein_mass("A", rounding=None) == 71.03711


def test_protein_mass_repeated_amino_acids():
    assert get_protein_mass("AAAA", rounding=None) == 4 * 71.03711


def test_protein_mass_invalid_amino_acid():
    with pytest.raises(KeyError):
        get_protein_mass("ACXZ")


def test_protein_mass_no_rounding_large_chain():
    sequence = "ACDEFGHIKLMNPQRSTVWY"
    expected = sum(read_monoisotopic_mass()[aa] for aa in sequence)
    assert get_protein_mass(sequence, rounding=None) == pytest.approx(
        expected, rel=1e-9
    )


def test_protein_mass_with_rounding_large_chain():
    sequence = "ACDEFGHIKLMNPQRSTVWY"
    expected = sum(read_monoisotopic_mass()[aa] for aa in sequence)
    assert get_protein_mass(sequence, rounding=3) == round(expected, 3)


def test_rosalind_sample():
    sequence = "SKADYEK"
    assert get_protein_mass(sequence, rounding=3) == pytest.approx(821.392, 1e-9)


def test_rosalind_prtm():
    sequence = "EGMYPEICGKYAFIYTQSSMAEPGPTRAWLDITYSTCIKAVAPNIKPSQGMIAYVAALNYTYRCIHELIKYMCQCLGRIGTFDHGKWVCDYDNREWSHFSPWCTSCFGWTLKLTMKHDHKLVIFEYELPTDPEFFPRMKFMSRKQGCLNCKEVPSRVYYRIFNSNDGEGYDVIWNQISAGGIPTKKLEGYMKDAPVYCLKWFNRYMWFEMMNTIVLDCVTHKRAKVKCWYKLVWTCATTRFFGCNWDLNEGRGNHWSTGHCIIFGEGSLEPPFEWMHPWMSPAFTIFLFSKEPKGFRDYECDYLLQACNPLKFWLWDDGDNKSTTEPYSVQLIIVNKHNIAVQHPILETKYDNLLTQYPYGRINNCRDDGQMPPSYWKEKTCLQCEAKLYVALDSSNITRAIANNIDIQKPGIGLGGMAHPKMHLGADHRPYDYGDGAFDGYTMFNSNRWAKVAKNCLWSENMVDHEISAGSNVEMHKNNIPHKIEWPRDVEGSWDRLGEHCPMHRNQNQFLDLYIEINEASKDTVKWYGHSGQGQCLWMDETLGHIVPDLIHANYWEHSACDDLRVPGEWHCTFMKFFQDVWGKGLACYKNFFLLEHKRHKKPHNQECPDIARQCWWHNVDARFALCVSHSWKQNMTTPENVLAWCEGVTLLSFYEGPADEFMKLLKMHEPLICENRPCWYAHVQTSALNMMCWKFSEHQDCKVLEGWFPSQWWHFMKKEWHLGLCFAQVWHDHPYEYWVRVPNDFQSYEPMNKNIIITFYHFQNKWMCSVHHPVGWILRKCRNNSCKKGMTLWSTYGTQLDYPWPRGIEHDYICDRYPLKDKEKGYMPGWEPSRKPSERAEIDWCAIKCTWHQMNVDMSVFPVNKVRHLSFFAH"
    assert get_protein_mass(sequence, rounding=3) == pytest.approx(103372.12, 1e-9)
