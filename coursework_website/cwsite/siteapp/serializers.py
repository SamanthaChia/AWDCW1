from rest_framework import serializers
from .models import *

class OrganismSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organism
        fields = ['taxa_id', 'clade', 'genus', 'species']

class ProteinSerializer(serializers.ModelSerializer):
    organism = OrganismSerializer()
    class Meta:
        model = Protein
        fields = ['protein_id', 'protein_sequence', 'length', 'organism']

    def create(self, validated_data):
        organism_data = self.initial_data.get('organism')
        protein = Protein(**{**validated_data,
                            'taxonomy':Organism.objects.get(pk=organism_data['taxa_id'])
                            })
        protein.save()
        return protein
