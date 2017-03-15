#PBS -S /bin/bash
#PBS -q batch
#PBS -N avg_theta
#PBS -l nodes=1:ppn=1:AMD
#PBS -l walltime=20:00:00
#PBS -l mem=10gb

module load python/3.4.3

python3 ~/LD_pipeline/python_scripts/average_theta.py
