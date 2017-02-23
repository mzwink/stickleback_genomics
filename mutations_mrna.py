
#Mutation summaries path: /Volumes/MW_18TB/Madison_Zwink/stickleback_genome/mutation_summaries/
amino_acid_dict = {
    'UUU': ['F'],
    'UUC': ['F'],
    'UUA': ['L'],
    'UUG': ['L'],
    'CUU': ['L'],
    'CUC': ['L'],
    'CUA': ['L'],
    'CUG': ['L'],
    'AUU': ['I'],
    'AUC': ['I'],
    'AUA': ['I'],
    'AUG': ['M'],
    'GUU': ['V'],
    'GUC': ['V'],
    'GUA': ['V'],
    'GUG': ['V'],
    'UCU': ['S'],
    'UCC': ['S'],
    'UCA': ['S'],
    'UCG': ['S'],
    'CCU': ['P'],
    'CCC': ['P'],
    'CCA': ['P'],
    'CCG': ['P'],
    'ACU': ['T'],
    'ACC': ['T'],
    'ACA': ['T'],
    'ACG': ['T'],
    'GCU': ['A'],
    'GCC': ['A'],
    'GCA': ['A'],
    'GCG': ['A'],
    'UAU': ['Y'],
    'UAC': ['Y'],
    'UGA': ['Stop'],
    'UAA' : ['Stop'],
    'UAG' : ['Stop'],
    'UGG': ['W'],
    'CAU': ['H'],
    'CAC': ['H'],
    'CAA': ['Q'],
    'CAG': ['Q'],
    'AAU': ['N'],
    'AAC': ['N'],
    'AAA': ['K'],
    'AAG': ['K'],
    'GAU': ['D'],
    'GAC': ['D'],
    'GAA': ['E'],
    'GAG': ['E'],
    'UGU': ['C'],
    'UGC': ['C'],
    'CGU': ['R'],
    'CGC': ['R'],
    'CGA': ['R'],
    'CGG': ['R'],
    'AGA': ['R'],
    'AGG': ['R'],
    'AGU': ['S'],
    'AGC': ['S'],
    'GGU': ['G'],
    'GGC': ['G'],
    'GGA': ['G'],
    'GGG': ['G']
 }

from Bio import SeqIO
import math

prdm_genes = [['mecom', '755:2235'], ['prdm1a' , '1348:1749'] ,['prdm1c', '1468:1869'], ['prdm2b', '1007:4221'], ['prdm4', '1577:2190'], ['prdm8', '478:1516'], ['prdm9', '446:2227'], ['prdm10', '851:2451'],
['prdm12b', '757:993'], ['prdm13', '415:1743'], ['prdm14', '697:990']]

def parse_population_seq(directory, prdm_list, amino_acid_dict):

    for prdm in prdm_list:
        zf_domain = prdm[1]
        prdm = prdm[0]

        output = directory + prdm + "_mutations.txt"
        output = open(output, 'w')
        output.write("Population\t" + prdm +".ZF_domain_dS\t"+ prdm +".ZF_domain_dN\t"+ prdm +".Non_domain_dS\t"+ prdm +".Non_domain_dN\n")

        reference_mrna = directory + 'ref_mrna_seq/' + prdm + '_mrna_ref.fasta'
        reference_mrna = SeqIO.parse(open(reference_mrna), 'fasta')
        reference_seq = ''

        num_codons = 0
        zf_domain = zf_domain.split(":")
        zf_start = int(zf_domain[0])
        zf_end = int(zf_domain[1])

        population_mrna = directory + 'population_mrna_seq/' + prdm + '_populations_mrna.fasta'
        population_mrna = SeqIO.parse(open(population_mrna), 'fasta')

        for fasta in reference_mrna:
            reference_seq = fasta.seq

            num_codons = math.ceil(len(reference_seq)/3)

        for fasta in population_mrna:

            if fasta.id.startswith("group") or fasta.id.startswith("scaffold"):
                continue
            else:
                pop_mrna = fasta.seq

                snp_positions = []
                for i in range(0, num_codons):
                    start = i * 3
                    end = start + 3

                    first_nucl = start
                    second_nucl = first_nucl +1
                    third_nucl = second_nucl + 1

                    ref_codon = reference_seq[start:end]
                    pop_codon = pop_mrna[start:end]


                    if ref_codon in amino_acid_dict.keys() and pop_codon in amino_acid_dict.keys():
                        ref_amino_seq = amino_acid_dict[str(ref_codon)]
                        ref_amino_seq = ref_amino_seq[0]

                        pop_amino_seq = amino_acid_dict[str(pop_codon)]
                        pop_amino_seq = pop_amino_seq[0]

                        if ref_codon == pop_codon:
                            continue

                        else:
                            mutation = ''
                            position = 0
                            category = ''

                            if pop_amino_seq == ref_amino_seq:
                                mutation = 'S'
                            else:
                                mutation = 'NS'

                            if reference_seq[first_nucl] != pop_mrna[first_nucl]:
                                position = first_nucl

                            elif reference_seq[second_nucl] != pop_mrna[second_nucl]:
                                position = second_nucl

                            else:
                                position = third_nucl


                            if position >= zf_start and position <= zf_end:
                                category = 'ZF_DOMAIN'
                            else:
                                category = 'NON_DOMAIN'


                            snp_positions.append([position, mutation, category])


            population = fasta.id
            population = population.split(":")[0].replace("_" + prdm, "")
            #print(population + "_" + prdm)
            #print(snp_positions)

            #dS = synonymous
            #dN = nonsyn

            print(population)
            zf_dS_counter = 0
            zf_dN_counter = 0
            nf_dS_counter = 0
            nf_dN_counter = 0

            for snp in snp_positions:
                print(snp)
                if len(snp) == 0:
                    null = 0
                    output.write(population + "\t" + str(null) + "\t" + str(null) + "\t" + str(null) +"\t" +str(null) + "\n")

                else:
                    category = snp[2]
                    mutation = snp[1]

                    if mutation == 'NS':
                        if category == 'ZF_DOMAIN':
                            zf_dN_counter += 1
                        else:
                            nf_dN_counter += 1

                    elif mutation == 'S':
                        if category == 'ZF_DOMAIN':
                            zf_dS_counter += 1
                        else:
                            nf_dS_counter += 1

                    #print(category + " " + mutation)

            #"Population\tZF_domain_dS\tZF_domain_dN\tNon_domain_dS\tNon_domain_dN\n"
            output.write(population + "\t" + str(zf_dS_counter) + "\t" + str(zf_dN_counter) + "\t" + str(nf_dS_counter) + "\t" + str(nf_dN_counter) + "\n")
            #print(zf_dS_counter)
            #print(zf_dN_counter)
            #print(nf_dS_counter)
            #print(nf_dN_counter)






#########
directory='/Volumes/MW_18TB/Madison_Zwink/stickleback_genome/prdm_exons/'
parse_population_seq(directory, prdm_genes, amino_acid_dict)
