import sys
import mcb185
import itertools

k = 0
found = False
missing_kmer = []
max_k = 8

while not found:
	k+=1 
	kcount = {}
	for defline, seq in mcb185.read_fasta(sys.argv[1]):
		rev_seq = mcb185.anti_seq(seq)
		for i in range(len(seq)-k +1):
			kmer = seq[i:i+k]
			if kmer not in kcount: 
				kcount[kmer]=0
			kcount[kmer]+=1
		for i in range(len(rev_seq)-k +1):
			kmer = rev_seq[i:i+k]
			if kmer not in kcount: 
				kcount[kmer]=0
			kcount[kmer]+=1
			
	for nts in itertools.product('ACGT', repeat=k):
		kmer = ''.join(nts)
		if kmer not in kcount:
			found = True
			missing_kmer.append(kmer)
			
missing_count = 0
for kmer in missing_kmer:
	missing_count +=1			

print(missing_kmer)
print('missing kmers:',missing_count)