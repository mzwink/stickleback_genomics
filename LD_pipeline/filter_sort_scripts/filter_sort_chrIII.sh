module load vcftools
mkdir /lustre1/mz00685/LD_pipeline/vcf/chrIII/
cd /lustre1/mz00685/LD_pipeline/vcf/
export vcf_list=Ran_M_jG.vcf
export chrom=chrIII
for file in ${vcf_list}
do
	iden=`basename ${file} .vcf`
	vcftools --vcf ${file} --chr ${chrom} --min-meanDP 10 --max-meanDP 75 --minQ 30 --maf 0.05 --max-maf 0.95 --max-missing 0.75 --remove-indels --min-alleles 2 --max-alleles 2 --recode --recode-INFO-all --stdout > ${iden}_${chrom}.vcf
	mv ${iden}_${chrom}.vcf ${chrom}/
done
