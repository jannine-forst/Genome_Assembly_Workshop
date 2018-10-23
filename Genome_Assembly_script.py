#!/usr/bin/env python3
import re
from Bio import SeqIO

#number of contigs so look for >

filename = "ecoliPB-filtered_0.50.contigs.fasta"

count_L50 = 0
count_N50 = 0
L50 = 0
genome_size = 4800000 / 2 

length_list = []
for seq_record in SeqIO.parse(filename, "fasta"):
	contig_length = len(seq_record)
	length_list.append(contig_length)
	
	#print(contig_length)
	#print(length_list)

	sorted_list_small = sorted(length_list)
	sorted_list_big = sorted(length_list,reverse=True)
	
	shortest_contig = sorted_list_small[0]
	longest_contig = sorted_list_big[0]

	while count_L50 < genome_size:
		count_L50 += contig_length
		L50 += 1
	
	if count_L50 > genome_size:
		N50 = len(seq_record)

print("1. The number of contigs in the file is:",len(length_list))
print("2. The shortest contig length is:",shortest_contig)
print("3. The longest contig length is:",longest_contig)
print("4. The L50 size is:",L50)
print("5. The N50 size is:",N50)	

	




