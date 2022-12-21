import os
import sys
import django
import csv
from collections import defaultdict

sys.path.append('C:/Users/Samantha/Documents/Advanced Web Development/AWDCW1/coursework_website/cwsite')
os.environ.setdefault('DJANGO_SETTINGS_MODULE','cwsite.settings')
django.setup()

from siteapp.models import *

data_sequences_file = 'C:/Users/Samantha/Documents/Advanced Web Development/CW1/cwsite/siteapp/csv/assignment_data_sequences.csv'
data_set_file = 'C:/Users/Samantha/Documents/Advanced Web Development/CW1/cwsite/siteapp/csv/assignment_data_set.csv'
pfam_file = 'C:/Users/Samantha/Documents/Advanced Web Development/CW1/cwsite/siteapp/csv/pfam_descriptions.csv'

organism_dict=defaultdict(str)
domain_dict=defaultdict(str)
protein_dict=defaultdict(str)
protein_sequence_list = defaultdict(str)
pfam_list = defaultdict(str)

DomainModel.objects.all().delete()
Protein.objects.all().delete()
Organism.objects.all().delete()
ProteinDomainLink.objects.all().delete()

#Store sequences data
with open(data_sequences_file) as data_sequences_csv:
    csv_sequences_reader = csv.reader(data_sequences_csv, delimiter=',')
    for data_sequences_row in csv_sequences_reader:
        protein_sequence_list[data_sequences_row[0]] = data_sequences_row[1] 

#Store domain data from pfam
with open(pfam_file) as pfam_csv:
    csv_pfam_reader = csv.reader(pfam_csv, delimiter=",")
    for data_pfam_row in csv_pfam_reader:
        pfam_list[data_pfam_row[0]] = data_pfam_row[1]

with open(data_set_file) as data_set_csv:
    csv_set_reader = csv.reader(data_set_csv, delimiter=',')
    for data_set_row in csv_set_reader:
        genus_species_pair = data_set_row[3].split(' ')
        # genus = genus_species_pair[0] | species = genus_species_pair[1]
        
        # Entry for Organism
        if organism_dict[data_set_row[1]] == "done":
            continue
        else:
            organism_row = Organism.objects.create(taxa_id=data_set_row[1], clade=data_set_row[2], genus=genus_species_pair[0], species=genus_species_pair[1])
            organism_dict[data_set_row[1]] = "done"
            organism_row.save()

        #Entry for Protein
        if protein_dict[data_set_row[0] == "done"]:
            continue
        else:
            protein_row = Protein.objects.create(protein_id=data_set_row[0], protein_sequence=protein_sequence_list[data_set_row[0]], length= data_set_row[8], organism=organism_row)
            protein_dict[data_set_row[0]] = "done"
            protein_row.save()

        #Entry for Domain
        if domain_dict[data_set_row[5]] == "done":
            continue
        else:
            domain_row = DomainModel.objects.create(domain_id=data_set_row[5], domain_description=pfam_list[data_set_row[5]], domain_start=data_set_row[6], domain_stop=data_set_row[7], protein=protein_row)
            domain_dict[data_set_row[5]] = "done"
            domain_row.save()