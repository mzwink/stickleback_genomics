#PBS -S /bin/bash
#PBS -q batch
#PBS -N sortfilter_VCF
#PBS -l nodes=1:ppn=8:AMD
#PBS -l walltime=20:00:00
#PBS -l mem=10gb


cd /lustre1/mz00685/LD_pipeline/LW_ldpipe/vcf/
module load vcftools

export vcf=LW_jG.vcf
export chr_list="chrII chrIII chrIV chrV chrVI chrVII chrVIII chrIX chrX chrXI chrXII chrXIII chrXIV chrXV chrXVI chrXVII chrXVIII chrXIX chrXX chrXXI"

export iden=`basename ${vcf} .vcf`
for chr in ${chr_list}
do
	vcftools --vcf ${vcf} --chr ${chr} --min-meanDP 10 --max-meanDP 75 --minQ 30 --maf 0.05 --max-maf 0.95 --max-missing 0.75 --remove-indels --min-alleles 2 --max-alleles 2 --recode --recode-INFO-all --stdout > ${iden}_${chr}.vcf
done
