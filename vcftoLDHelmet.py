#Converts vcf files (ex: phased Beagle output) to LDHelmet input sequence and position files
#Author: Alice Shanfelter August 2016

'''Input format for:
Seq file:
>ID1
Sequence1
>ID2
sequence2
...

Position file:
Pos1
Pos2
...
'''

'''
bash script to run ldhelmet
for file in LW*.fasta
do
  export iden=${file%%.*}
  export vcf=${iden}.vcf
  export phase=${iden}Bg.vcf
  export pos=${iden}_pos.txt
  export sites=${iden}_sites.txt
  python3 vcftoLDHelmet.py
  ldhelmet find_confs --num_threads 48 -w 50 -o ${iden}.conf ${file}
  ldhelmet table_gen --num_threads 24 -c ${iden}.conf -t 0.002 -r 0.0 0.1 10.0 1.0 100.0 -o LW_002_table.lk
  ldhelmet pade --num_threads 24 -c ${iden}.conf -t 0.002 -x 11 -o ${iden}_002.pade
  ldhelmet rjmcmc --num_threads 24 -w 50 -l LW_002_table.lk -p ${iden}_002.pade -b 10 --pos_file ${pos} --snps_file ${sites} --burn_in 100000 -n 1000000 -o ${iden}_002.output
  ldhelmet post_to_text -m -p0.5 -p0.025 -p0.0975 -o ${iden}_002_recombrates.txt ${iden}_002.output
done

'''

import os

#Pulls sample IDs and returns them
def Sample():
	read = str(os.environ["vcf"])
	with open(read, 'r') as input:
		for line in input:
			if line.startswith('#CHROM'):
				x = line.split()
				samples = x[9:len(x)]
	return samples

#Pulls positions and returns them
#will only need to change step size as sample size decreases
#each line will always have 9 values before the samples start
#should check files
def Pos():
    data = []
	read = str(os.environ["vcf"])
    with open(read, 'r') as input:
        for line in input:
            if line.startswith("chr"):
                data += line.split()
		#for step size add 8 + number of samples + 1 to get back to next position
        pos = data[1::29]
    return pos

#Pulls reference alleles from unphased vcf file
#Step size is same as for pos function; will need to change based on number of samples
#step size should be the same throughout the file
def ref():
	data = []
	new = []
	read = str(os.environ["vcf"])
	with open(read, 'r') as input:
		for line in input:
			if line.startswith('chr'):
				data += line.split()
		ref = data[3::29]
	return ref

#Pulls alternate alleles from unphased vcf file
#same as pos function for step size
def alt():
	data = []
	read = str(os.environ["vcf"])
	with open(read,'r') as input:
		for line in input:
			if line.startswith("chr"):
				data += line.split()
		alt = data[4::29]
	return alt

#Pull data from phased vcf file
#how the chromosome is identified might change; if so will need to change chr to whatever is with chromosome Number
def data():
	data = []
	read2 = str(os.environ["phase"])
	with open(read2, 'r') as input:
		for line in input:
			if line.startswith("chr"):
				new_line = line.split()
				data.append(new_line[9:len(new_line)])
	return data

#Converts from phased haplotypes back to ref and alt alleles
#Haplotype 1
def Convert():
	haplo1 = []
	read = str(os.environ["vcf"])
	read2 = str(os.environ["phase"])
	with open(read, 'r') as input, open(read2, 'r') as input2:
		ref_allele = ref()
		alt_allele = alt()
		all_data = data()
		for x, y, z in zip(ref_allele, alt_allele, all_data):
			for val in z:
				if val.startswith("0"):
					haplo1 += str(x)
				elif val.startswith("1"):
					haplo1 += str(y)
	return haplo1


#Converts from phased haplotypes back to ref and alt alleles
#haplotype 2
def Convert2():
	haplo2 = []
	read = str(os.environ["vcf"])
	read2 = str(os.environ["phase"])
	with open(read, 'r') as input, open(read2, 'r') as input2:
		ref_allele = ref()
		alt_allele = alt()
		all_data = data()
		for x, y, z in zip(ref_allele, alt_allele, all_data):
			for val in z:
				if val.endswith("0"):
					haplo2 += str(x)
				elif val.endswith("1"):
					haplo2 += str(y)
	return haplo2


#writes haplotypes and sample ids to sequence file for LDHelmet
def write():
	read = str(os.environ["vcf"])
	sites = str(os.environ["sites"])
	with open(read, 'r') as file, open(sites, 'a') as file2:
		haplo1 = Convert()
		haplo2 = Convert2()
		samples = Sample()
		x = 20
		for value in haplo1:
			if x > 0:
				sample_id = '>' + samples[0]
				new_list = haplo1[0::x]
				new_list2 = haplo2[0::x]
				data_line = ''.join(new_list) + '\n'
				data_line2 = ''.join(new_list2) + '\n'
				file2.write(sample_id + "_a" + '\n')
				file2.write(data_line)
				file2.write(sample_id + "_b" + '\n')
				file2.write(data_line2)
				del samples[0]
				del haplo1[0::x]
				del haplo2[0::x]
				x -= 1
write()


#writes positions to position file for LDHelmet
def write_pos():
	read = str(os.environ["vcf"])
	pos = str(os.environ["pos"])
    with open(read, 'r') as input, open(pos, 'a') as output:
        pos = Pos()
        for value in pos:
            new_value = value + '\n'
            output.write(new_value)

write_pos()
