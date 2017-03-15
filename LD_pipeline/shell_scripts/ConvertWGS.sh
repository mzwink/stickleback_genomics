#PBS -S /bin/bash
#PBS -q batch
#PBS -N WCB
#PBS -l nodes=1:ppn=1:AMD
#PBS -l mem=10gb
#PBS -l walltime=12:00:00
#PBS -M alice.shanfelter@uga.edu
#PBS -m ae

cd /lustre1/afs16076/LD_Pipeline/Beagle/Sliding_window/Lake_Washington/Phased_Data/

module load vcftools/0.1.12b
module load ldhat/2.2

export chr="V"
for file in *5Bg*
do
	export group=${file%%Bg*}
	vcftools --vcf ${file} --chr chr${chr} --ldhat
	for file in out.ldhat.*
	do
		mv "$file" "${file/out.ldhat/${group}}"
	done
	export S=${group}.sites
	export L=${group}.locs

	convert -seq ${S} -loc ${L} > ${group}ConSum.txt

	mv locs.txt ${group}locs.txt
	mv freqs.txt ${group}freqs.txt
	mv sites.txt ${group}sites.txt
done
