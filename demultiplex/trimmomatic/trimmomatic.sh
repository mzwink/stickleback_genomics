#PBS -N trimmomatic
#PBS -q batch
#PBS -l nodes=1:ppn=1:AMD
#PBS -l mem=1gb
#PBS -l walltime=480:00:00

cd /lustre1/mz00685/demultiplex/Mouse_GBS_SecondLane/
module load java/latest
module load trimmomatic/0.33
export directories="L001 L002 L003 L004"

cd L001/
export read1_list=`ls -m *.rem.1.fq.gz | tr -d ','`

cd ..
#Cat all files to trim
for read in ${read1_list}
do
	export iden=`basename ${read} .rem.1.fq.gz`
	export read1=${iden}.1.fq.gz
	export read2=${iden}.2.fq.gz
	export read1_unpaired=${iden}.rem.1.fq.gz
	export read2_unpaired=${iden}.rem.2.fq.gz

	for dir in ${directories}
	do
		cat ${dir}/${read1} >> ${read1}
		cat ${dir}/${read2} >> ${read2}
		cat ${dir}/${read1_unpaired} >> ${read1_unpaired}
		cat ${dir}/${read2_unpaired} >> ${read2_unpaired} 
	
	done

	time java -jar /usr/local/apps/trimmomatic/latest/trimmomatic-0.33.jar PE -threads 1 ${read1} ${read2} ${read1_unpaired} ${read2_unpaired} ${iden}.R1.trimmed.fastq.gz ${iden}.R2.trimmed.fastq.gz ${iden}.R1.unpaired.trimmed.fastq.gz ${iden}.R2.unpaired.trimmed.fastq.gz SLIDINGWINDOW:4:20
done

