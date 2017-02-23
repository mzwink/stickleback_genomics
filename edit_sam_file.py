
def edit_sam_file(sam_file):
    sam_file = open('/lustre1/mz00685/prdm_variance/RNA_data/sam/' + str(sam_file)).readlines()
    output=open('/lustre1/mz0685/prdm_variance/RNA_data/' + str(sam_file), 'w')

    for sam in sam_file:
        sam = sam.replace("group", "chr")
        output.write(sam)


edit_sam_file('JP_M1_accepted_hits.sam')
edit_sam_file('JP_M2_accepted_hits.sam')
edit_sam_file('JP_M3_accepted_hits.sam')
edit_sam_file('LW_09_F5_accepted_hits.sam')
edit_sam_file('LW_09_F6_accepted_hits.sam')
edit_sam_file('LW_09_F7_accepted_hits.sam')
edit_sam_file('LW_09_F8_accepted_hits.sam')
edit_sam_file('LW_09_M1_accepted_hits.sam')
edit_sam_file('LW_09_M1_accepted_hits.sam')
edit_sam_file('LW_09_M2_accepted_hits.sam')
edit_sam_file('LW_09_M3_accepted_hits.sam')
edit_sam_file('LW_10_F1_accepted_hits.sam')
edit_sam_file('LW_10_F2_accepted_hits.sam')
edit_sam_file('LW_10_M3_accepted_hits.sam')
edit_sam_file('LW_10_M4_accepted_hits.sam')
