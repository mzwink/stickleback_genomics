file_list=`ls -m filter_sort_chr*.sh | tr -d ','`

for file in ${file_list}
do

	qsub ${file}
done
