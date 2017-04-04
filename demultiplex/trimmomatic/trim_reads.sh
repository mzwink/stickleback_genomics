#PBS -N trimmomatic
#PBS -q batch
#PBS -l nodes=1:ppn=1:AMD
#PBS -l mem=1gb
#PBS -l walltime=480:00:00

cd /lustre1/mz00685/demultiplex/Mouse_GBS_SecondLane/
module load java/latest
module load trimmomatic/0.33
export read1_list=`ls -m *.rem.1.fq.gz | tr -d ','`

for read in ${read1_list}
do
	
	export iden=`basename ${read} .rem.1.fq.gz`
	
	#Input files
	export read1=${iden}.1.fq.gz
	export read2=${iden}.2.fq.gz

	#Output files
	export read1_out=${iden}.trimmed.1.fq.gz
	export read2_out=${iden}.trimmed.2.fq.gz
	export read1_unpaired=${iden}.trimmed_unpaired.1.fq.gz
	export read2_unpaired=${iden}.trimmed_unpaired.2.fq.gz

	time java -jar /usr/local/apps/trimmomatic/latest/trimmomatic-0.33.jar PE -threads 1 ${read1} ${read2} ${read1_out} ${read1_unpaired} ${read2_out} ${read2_unpaired} SLIDINGWINDOW:4:20
done

