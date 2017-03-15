export chr_list=`chrI chrII chrIII chrIV chrV chrVI chrVII chrVIII chrIX chrX chrXI chrXII`

for chr in ${chr_list}
do
	touch ${chr}.test

done
