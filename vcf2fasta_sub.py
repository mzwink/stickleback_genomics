chr_num=["chrI","chrII","chrIII","chrIV","chrV","chrVI","chrVII","chrVIII","chrIX","chrX","chrXI","chrXII","chrXIII","chrXIV","chrXV","chrXVI","chrXVII","chrXVIII","chrXIX","chrXX","chrXXI"]
pop = ["G2_L_jG", "Ca_L_jG", 'Lm_M_jG', 'No_L_jG', 'Ran_M_jG', 'Kob_M_jG']

for chrom in chr_num:
    output = open(chrom + "_vcf2fasta.sh", 'w')

    output.write('export chrom=' + str(chrom) + "\n")
    output.write("export vcf_list=`ls -m Phased_vcf/${chrom}/*vcf | tr -d ','`\n")
    output.write("for vcf in ${vcf_list}\ndo\n")
    output.write("\t./vcf2fasta –f Glazer_unmasked.fa ${vcf}\ndone\n")

#./vcf2fasta –f reference.fasta(Glazer assembly fasta from alignments) –p out.prefix <input.file>
