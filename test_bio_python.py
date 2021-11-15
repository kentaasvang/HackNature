import pytest
from bio_python import BioPython


@pytest.fixture
def mRNAs():
    mRNA_a = "AUG  CCA  GUG  ACU  UCA  GGG  ACG  AAU  GAC  UUA"
    mRNA_b = "AUGCCAGUGACUUCAGGGACGAAUGACUUA"
    mRNA_c = "1235AUG  CCA  GUG  ACU  UCA  GGG  ACG  AAU  GAC  UUA  "
    mRNA_expected = mRNA_b
    return ([mRNA_a, mRNA_b, mRNA_c], mRNA_expected)


@pytest.fixture
def DNAs():
    DNA_a = "TAC  GGT  CAC  TGA  AGT  CCC  TGC  TTA  CTG  AAT"
    DNA_b = "TACGGTCACTGAAGTCCCTGCTTACTGAAT"
    DNA_c = "1235TAC  GGT  CAC  TGA  AGT  CCC  TGC  TTA  CTG  AAT   "
    DNA_expected = DNA_b
    return ([DNA_a, DNA_b, DNA_c], DNA_expected)


class TestBioPython:

    def test_init(self, mRNAs):
        mRNAs, expected = mRNAs

        for mRNA in mRNAs:
            # arrange
            bpy = BioPython(mRNA)
            # act
            genome = bpy.genome
            # assert
            assert genome == expected

    def test_mRNA_property_should_be_true_if_genome_type_is_mRNA(self, mRNAs):
        for mRNA in mRNAs[0]:
            bpy = BioPython(mRNA)
            assert bpy.is_mRNA() == True
    
    def test_mRNA_property_should_be_false_if_genome_type_is_DNA(self, DNAs):
        for DNA in DNAs[0]:
            bpy = BioPython(DNA)
            assert bpy.is_mRNA() == False

    def test_from_DNA_to_mRNA(self):
        mRNA_b = "AUGCCAGUGACUUCAGGGACGAAUGACUUA"
        DNA_b = "TACGGTCACTGAAGTCCCTGCTTACTGAAT"
        
        for a,e in [[DNA_b, mRNA_b], [mRNA_b, mRNA_b]]:
            bpy = BioPython(a)
            assert bpy.to_mRNA() == e
    
    def test_from_mRNA_to_DNA(self):

        mRNA_b = "AUGCCAGUGACUUCAGGGACGAAUGACUUA"
        DNA_b = "TACGGTCACTGAAGTCCCTGCTTACTGAAT"

        for a,e in [[mRNA_b, DNA_b], [DNA_b, DNA_b]]:
            bpy = BioPython(a)
            assert bpy.to_DNA() == e

    def test_get_codons_from_mRNA(self):
        genome = "GUAUGCACGUGACUUUCCUCAUGAGCUGAU"
        expected = [["AUG", "CAC", "GUG", "ACU", "UUC", "CUC", "AUG", "AGC", "UGA"]]

        bpy = BioPython(genome)

        assert bpy.get_codons() == expected






