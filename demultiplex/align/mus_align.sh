#PBS -S /bin/bash
#PBS -q batch
#PBS -N bowtie_trimmed
#PBS -l nodes=1:ppn=24:mwnode
#PBS -l mem=10gb
#PBS -l walltime=96:00:00
#PBS -M mzwink@uga.edu
#PBS -m ae
#PBS -j oe

cd /lustre1/mz00685/demultiplex/Mouse_GBS_SecondLane/trimmed_reads/
module load bowtie2/latest
export cores=12
export mapFilter=true
export runNum=999

export trimmed_reads=`ls -m *.trimmed.1.* | tr -d ','`
	
for read in ${trimmed_reads}
do
	iden=`basename ${read} .1.fq.gz`
	
	read1=${read}
	read2=${iden}.2.fq.gz
	bowtie2 -p ${cores} --no-unal --very-sensitive -x /db/bowtie2/20160729/mm9/mm9 \
		-1 ${read1} \
		-2 ${read2} \
		-S /lustre1/mz00685/demultiplex/Mouse_GBS_SecondLane/sam/${iden}.sam \
		>& ${iden}_summary.txt

done
