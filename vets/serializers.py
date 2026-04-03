from rest_framework import serializers

from accounts.models import VetProfile, PawMedicUser


class VetSerializer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField()
    vet_id = serializers.SerializerMethodField()

    class Meta:
        model = PawMedicUser
        fields = ['slug', 'vet_id', 'first_name', 'last_name']

    def get_slug(self, obj):
        return obj.vet_profile.slug

    def get_vet_id(self, obj):
        return obj.vet_profile.pk