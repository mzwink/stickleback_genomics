cd /lustre1/mz00685/LD_pipeline/vcf/phased_vcf/

export chromosomes="chrXXI chrXX chrXIX chrXVIII chrXVII chrXVI chrXV chrXIV chrXIII chrXII chrXI chrX chrIX chrVIII chrVII chrVI chrV chrIV chrIII chrII chrI"
export populations="G2_L No_L Ca_L Kob_M Ran_M Lm_M"

echo -e POPULATION"\t"CHR"\t"SNP_COUNT >> phased_snp_count.txt

for pop in ${populations}
do
	for chr in ${chromosomes}
	do
		file=${pop}_jG_${chr}_phased.vcf
		export num_snp=`grep ^${chr} ${file} | wc -l`
		echo -e ${pop}"\t"${chr}"\t"${num_snp} >> phased_snp_count.txt

	done

done
