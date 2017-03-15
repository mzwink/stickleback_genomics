#PBS -S /bin/bash
#PBS -j oe
#PBS -q batch
#PBS -N LW_16_sam2bam
#PBS -l nodes=1:ppn=4:AMD
#PBS -l walltime=48:00:00
#PBS -l mem=10gb

cd /lustre1/mz00685/downsize_read_cov/downsize_trial4/sam/
module load samtools/latest

export samFile=LW_16.sam
samtools view -bh -@ 3 LW_16.sam > LW_16.bam
samtools sort -o LW_16_sort.bam -T samfile_LW_16_s -@ 3 LW_16.bam
mv LW_16_sort.bam LW_16.bam
samtools index -b LW_16.bam
