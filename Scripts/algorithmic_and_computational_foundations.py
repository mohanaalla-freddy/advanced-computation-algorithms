#!/usr/bin/env python
# coding: utf-8

# In[11]:


from Bio import SeqIO
input_file = "/Users/mohanavenkataphaneendrareddyalla/Downloads/Sars_cov_2.fasta"
genomes = list(SeqIO.parse(input_file, "fasta"))
total_genomes = len(genomes)

print('Total genomes:', (total_genomes))


# In[9]:


count_with_N = 0
count_without_N = 0
for genome in genomes:
    if 'N' in str(genome.seq):
        count_with_N += 1
    else:
        count_without_N += 1
print("Number of genomes with letter 'N':" ,(count_with_N))
print("Number of genomes without letter 'N':", (count_without_N))


# In[8]:


count_with_N = 0
count_without_N = 0
unique_genomes_without_N = set()
for genome in genomes:
    sequence_str = str(genome.seq)
    if 'N' in sequence_str:
        count_with_N += 1
    else:
        count_without_N += 1
        unique_genomes_without_N.add(sequence_str)

# Print counts
print("Number of genomes with letter 'N':" ,(count_with_N))
print("Number of genomes without letter 'N':" ,(count_without_N))
print("Number of unique genomes without 'N':" ,(len(unique_genomes_without_N)))


# In[12]:


from Bio.SeqRecord import SeqRecord
output_file = "Selected_Unique_COVID19_Genomes_Asia_new1.fasta"
unique_genomes_without_N = set()
unique_records_without_N = []
for genome in genomes:
    sequence_str = str(genome.seq)  
    if 'N' not in sequence_str:
        unique_genomes_without_N.add(sequence_str)
        unique_records_without_N.append(SeqRecord(genome.seq, id=genome.id, description=""))
print("Number of unique genomes without 'N': ",(len(unique_genomes_without_N)))
with open(output_file, "w") as handle:
    SeqIO.write(unique_records_without_N, handle, "fasta")
print(f"Unique genomes saved to: {output_file}")



# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




