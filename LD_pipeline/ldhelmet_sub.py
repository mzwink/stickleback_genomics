
chr_num=["chrI","chrII","chrIII","chrIV","chrV","chrVI","chrVII","chrVIII","chrIX","chrX","chrXI","chrXII","chrXIII","chrXIV","chrXV","chrXVI","chrXVII","chrXVIII","chrXIX","chrXX","chrXXI"]
pop = ["LW", "PS"]

for p in pop:
    for chrom in chr_num:

        output = str(p) + "_ldhelmet_" + chrom +".sh"
        output = open(output, 'w')


        output.write('#PBS -S /bin/bash\n')
        output.write('#PBS -q batch\n')
        output.write('#PBS -N ldhelmet\n')
        output.write('#PBS -l nodes=1:ppn=4:AMD\n')
        output.write('#PBS -l walltime=8:00:00\n')
        output.write('#PBS -l mem=10gb\n')

        output.write("module load boost/1.59.0/gcc447\n")
        output.write("module load gsl/1.16/gcc/4.4.7\n")
        output.write("module load ldhelmet/1.7\n")



        output.write("export dir=" + str(chrom) + "\n")
        output.write("export pop=" + str(p)+ "\n")

        output.write("cd /lustre1/mz00685/LD_pipeline/vcf/phased_data/fasta_files/" + p + "_fasta/" + str(chrom) + "/\n")

        output.write("export file_list=`ls -m *.fasta | tr -d ','`\n")

        output.write("for file in *.fasta\n")
        output.write("do\n")
        output.write("\tpython Change_fasta_header.py " + '${file}\n')
        output.write("done\n")

        output.write("mv " + str(p) + "_" + str(chrom) + ".fasta /lustre1/mz00685/LD_pipeline/vcf/phased_data/fasta_files/" + p + "_fasta/\n")
