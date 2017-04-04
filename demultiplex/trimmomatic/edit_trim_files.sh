cd /lustre1/mz00685/demultiplex/Mouse_GBS_SecondLane/

export read1_list=`ls -m *trimmed.1.fq.gz | tr -d ','`


for read in ${read1_list}
do

	export iden=`basename ${read} .trimmed.1.fq.gz`
	read1=${iden}.trimmed.1.fq.gz
	read2=${iden}.trimmed.2.fq.gz

	#Need to switch read1_unpaired with read2_trimmed
	
	read1_unpaired=${iden}.trimmed_unpaired.1.fq.gz
	read2_unpaired=${iden}.trimmed_unpaired.2.fq.gz
	
	#original trim - ${read1} ${read2} ${read1_out} ${read2_out} ${read1_unpaired} ${read2_unpaired}
	#Change this to  ${read1} ${read2} ${read1_out} ${read1_unpaired} ${read2_out} ${read2_unpaired}


	mv ${read1_unpaired} temp.txt
	mv ${read2} ${read1_unpaired}
	mv temp.txt ${read2}	

done
