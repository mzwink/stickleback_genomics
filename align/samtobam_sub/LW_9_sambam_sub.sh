#PBS -S /bin/bash
#PBS -j oe
#PBS -q batch
#PBS -N LW_9_sam2bam
#PBS -l nodes=1:ppn=4:AMD
#PBS -l walltime=48:00:00
#PBS -l mem=10gb

cd /lustre1/mz00685/downsize_read_cov/downsize_trial4/sam/
module load samtools/latest

export samFile=LW_9.sam
samtools view -bh -@ 3 LW_9.sam > LW_9.bam
samtools sort -o LW_9_sort.bam -T samfile_LW_9_s -@ 3 LW_9.bam
mv LW_9_sort.bam LW_9.bam
samtools index -b LW_9.bam
