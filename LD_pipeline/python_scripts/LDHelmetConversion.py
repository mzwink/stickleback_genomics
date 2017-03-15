#Converting Hotspots identified from Mike's perl scripts to readable format for R and further analysis
#Author: Alice Shanfelter December 2016

#Number of Hotspots per Pop and records hotspot rho, background rho, and relative rho
#Need hotspot fasta file
#outputs file with just the hotspot positions
'''bash script to run this script on mutliple files
for file in PS2.hotspots.fa
do
    export file=${file}
    export iden=${file%%.hot*}
    export output=${iden}_hotspots.txt
    python3 ~/Documents/UGA/White\ Lab/Project/Scripts/My_scripts/Analysis/LDHelmetConversion.py
done
'''
import os

def Count():
    data = []
    hotwindow = []
    inp = str(os.environ["file"])
    out = str(os.environ["output"])
    with open(inp, 'r') as input, open(out, 'a') as output:
        for line in input:
            if line != "\n":
                new_line = line.strip()
                new_line = new_line.split(".")
                hotwindow.append(new_line[2])
        no_hotspots = len(hotwindow)
        output.write("Number of Hotspots: " + str(no_hotspots) + '\n')
        for value in hotwindow:
            output.write('\n' + "Hotspot Window: " + value + '\n')

Count()
