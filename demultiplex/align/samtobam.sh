#PBS -S /bin/bash
#PBS -q batch
#PBS -N samtobam
#PBS -l nodes=1:ppn=8:mwnode
#PBS -l mem=2gb
#PBS -l walltime=96:00:00
#PBS -M mzwink@uga.edu
#PBS -m ae
#PBS -j oe

cd /lustre1/mz00685/demultiplex/Mouse_GBS_SecondLane/sam/

module load samtools/latest
module load bedtools/2.26.0

export sam_files=`ls -m *.sam | tr -d ','`

for sam in ${sam_files}
do
	iden=`basename ${sam} .sam`
	samtools view -bh ${sam} > ${iden}.bam
	samtools sort -o ${iden}_sorted.bam -T ${iden}_s ${iden}.bam
	mv ${iden}_sorted.bam ${iden}.bam
	samtools index -b ${iden}.bam
	mv *.bam* /lustre1/mz00685/demultiplex/Mouse_GBS_SecondLane/bam/
done
