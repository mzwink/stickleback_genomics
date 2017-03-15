#PBS -S /bin/bash
#PBS -q batch
#PBS -N WCB
#PBS -l nodes=1:ppn=1:AMD
#PBS -l mem=10gb
#PBS -l walltime=12:00:00
#PBS -M mzwink@uga.edu
#PBS -m ae

cd /lustre1/mz00685/LD_pipeline/LW_ldpipe/

module load vcftools/0.1.12b
module load ldhat/2.2

export chr_list="chrXXI chrXX chrXIX chrXVIII chrXVII chrXVI chrXV chrXIV chrXIII chrXII chrXI chrX chrIX chrVIII chrVII chrVI chrV chrIV chrIII chrII chrI"
#export populations="G2_L No_L Ca_L Kob_M Ran_M Lm_M"
#export chr_list="chrI"
export populations="LW"

for pop in ${populations}
do
	#mkdir ${pop}
	for chr in ${chr_list}
	do
		vcf_file=phased_vcf/${pop}_jG_${chr}_phased.vcf
		vcftools --vcf ${vcf_file} --chr ${chr} --ldhat
		mv out.ldhat.locs locs/${pop}_${chr}.ldhat.locs
		mv out.ldhat.sites sites/${pop}_${chr}.ldhat.sites		
		export loc=locs/${pop}_${chr}.ldhat.locs
		export sites=sites/${pop}_${chr}.ldhat.sites

		convert -seq ${sites} -loc ${loc} > convert_sum/${pop}_${chr}_conSum.txt
		mv locs.txt convert_sum/${pop}_${chr}_locs.txt
		mv freqs.txt convert_sum/${pop}_${chr}_freqs.txt
		mv sites.txt convert_sum/${pop}_${chr}_sites.txt
			

	done

done
