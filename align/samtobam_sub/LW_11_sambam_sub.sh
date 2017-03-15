#PBS -S /bin/bash
#PBS -j oe
#PBS -q batch
#PBS -N LW_11_sam2bam
#PBS -l nodes=1:ppn=4:AMD
#PBS -l walltime=48:00:00
#PBS -l mem=10gb

cd /lustre1/mz00685/downsize_read_cov/downsize_trial4/sam/
module load samtools/latest

export samFile=LW_11.sam
samtools view -bh -@ 3 LW_11.sam > LW_11.bam
samtools sort -o LW_11_sort.bam -T samfile_LW_11_s -@ 3 LW_11.bam
mv LW_11_sort.bam LW_11.bam
samtools index -b LW_11.bam
