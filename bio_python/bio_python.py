import re

class BioPython:
        
    def __init__(self, genome):
        self.genome = genome.upper()

    @property
    def genome(self):
        return self._genome

    @genome.setter
    def genome(self, val):
        val = self.clean_genome_input(val)
        self._genome = val

    def clean_genome_input(self, val):
        return "".join(re.findall("[a-zA-Z]", val))

    def is_mRNA(self):
        return True if "U" in list(self.genome) else False

    def is_DNA(self):
        return True if "T" in list(self.genome) else False

    def to_DNA(self):

        if self.is_DNA():
            return self.genome

        compliment = {
            "G": "C",
            "C": "G",
            "U": "A",
            "A": "T"
        }

        ret_val = ""

        for l in self.genome:
            ret_val += compliment[l]

        return ret_val
    
    def to_mRNA(self):

        if self.is_mRNA():
            return self.genome

        compliment = {
            "G": "C",
            "C": "G",
            "A": "U",
            "T": "A"
        }

        ret_val = ""

        for l in self.genome:
            ret_val += compliment[l]

        return ret_val

    def get_codons(self):
        all_codons = []
        o_mRNA = self.genome

        while True:
            codons, i = self.find_codons(o_mRNA)
            if not i:
                break
            all_codons.append(codons)
            o_mRNA = o_mRNA[i:]
            
        return all_codons

    def find_codons(self, genome):
        codons = []
        stops = ["UAA", "UAG", "UGA"]
        start_i = genome.find("AUG")
        
        if start_i == -1:
            return codons, False
        
        n_mRNA = genome[start_i:]
        ii = 0
        for i in range(0, len(n_mRNA), 3):
            codon = n_mRNA[i:i+3]
            codons.append(codon)
            if codon in stops:
                ii = i
                break
            
        return codons, start_i+ii+3
