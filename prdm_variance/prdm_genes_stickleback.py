from Bio import SeqIO

path_to_file = '/Volumes/MW_18TB/Madison_Zwink/stickleback_genome/rna_seq/Gasterosteus_aculeatus.BROADS1.ncrna.fa'
#fasta_id = '/Users/madisonzwink/Desktop/Glazer_project/protein_seq/gene_id_prdm.txt'

def find_prdm_genes(fasta_id):

    fasta_id = open(fasta_id).readlines()
    id_dict = {}

    for f_id in fasta_id:
        #print(f_id)
        id_strip = f_id.rstrip()
        id_split = id_strip.split(" ")

        gene_id = id_split[0].replace(">", "")
        #print(gene_id)

        if f_id in id_dict.keys():
            id_dict[gene_id].append(f_id)

        else:
            id_dict[gene_id] = [f_id]

    #print(id_dict)
    return id_dict


def write_prdm_fasta_output(filename, id_dict):
    output_file = filename.replace("Gasterosteus_aculeatus.BROADS1.pep.all.fa", "prdm_genes_rna.fa")
    output = open(output_file, 'w')
    fasta_parse = SeqIO.parse(open(filename), 'fasta')

    for fasta in fasta_parse:
        #print(fasta)

        if fasta.id in id_dict.keys():
            #output.write(str(id_dict[fasta.id]) + "\n")
            header = str(id_dict[fasta.id])
            edit_header = header.replace("[", "")
            edit_header = edit_header.replace("]", "")
            edit_header = edit_header.replace("\\n", "")
            edit_header = edit_header.replace("'", "")
            output.write(str(edit_header) + "\n")
            output.write(str(fasta.seq) + "\n")


id_dict = find_prdm_genes(fasta_id)
write_prdm_fasta_output(path_to_file, id_dict)
