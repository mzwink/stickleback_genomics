export snp_files=`ls -m *snp_variance.txt | tr -d ','`

for snp in ${snp_files}
do
	name=`basename ${snp} snp_variance.txt`

	sort -k1,1 ${snp} > ${name}_snp_variance_sorted.txt

	mv ${name}_snp_variance_sorted.txt ${snp}

done
