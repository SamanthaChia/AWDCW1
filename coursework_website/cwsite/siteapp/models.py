from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.db.models.fields import CharField

class Organism(models.Model):
    taxa_id = models.IntegerField(primary_key=True)
    clade = models.CharField(null=False, max_length=256, default="E")
    genus =  models.CharField(null=False, max_length=256)
    species = models.CharField(null=False, max_length=256)

    def __str__(self):
        return str(self.taxa_id) + "," + self.clade + "," + self.genus + "," + self.species

class Protein(models.Model):
    protein_id = models.CharField(max_length=10, primary_key=True)
    protein_sequence = models.CharField(max_length=40000)
    length = models.IntegerField()
    organism = models.ForeignKey(Organism, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.protein_id + "," + self.protein_sequence + "," + str(self.length) + "," + str(self.organism)

class Domain(models.Model):
    domain_id = models.CharField(max_length=256, primary_key=True)
    domain_description = models.CharField(max_length=256)
    domain_start = models.IntegerField(null=False, default=0)
    domain_stop = models.IntegerField(null=False, default=0)
    protein = models.ForeignKey(Protein, on_delete=models.DO_NOTHING, db_column='protein')

    def __str__(self):
        return self.domain_id + "," + self.domain_description +  "," + str(self.domain_start) + "," + str(self.domain_stop) + "," + str(self.protein)

class DomainModel(models.Model):
    domain_id = models.CharField(max_length=256, primary_key=True)
    domain_description = models.CharField(max_length=256)
    domain_start = models.IntegerField(null=False, default=0)
    domain_stop = models.IntegerField(null=False, default=0)
    protein = models.ForeignKey(Protein, on_delete=models.DO_NOTHING, db_column='protein')

    def __str__(self):
        return self.domain_id + "," + self.domain_description +  "," + str(self.domain_start) + "," + str(self.domain_stop) + "," + str(self.protein)

class ProteinDomainLink(models.Model):
    protein = models.ForeignKey(Protein, on_delete=models.DO_NOTHING)
    domain = models.ForeignKey(DomainModel, on_delete=models.DO_NOTHING)

    def special_save(self):
        pass