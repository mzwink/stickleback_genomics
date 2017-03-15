#PBS -S /bin/bash
#PBS -j oe
#PBS -q batch
#PBS -N LW_12_sam2bam
#PBS -l nodes=1:ppn=4:AMD
#PBS -l walltime=48:00:00
#PBS -l mem=10gb

cd /lustre1/mz00685/downsize_read_cov/downsize_trial4/sam/
module load samtools/latest

export samFile=LW_12.sam
samtools view -bh -@ 3 LW_12.sam > LW_12.bam
samtools sort -o LW_12_sort.bam -T samfile_LW_12_s -@ 3 LW_12.bam
mv LW_12_sort.bam LW_12.bam
samtools index -b LW_12.bam
