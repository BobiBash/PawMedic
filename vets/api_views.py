from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination

from accounts.choices import PawMedicUserType
from accounts.models import PawMedicUser
from vets.serializers import VetSerializer


class VetSearchPagination(PageNumberPagination):
    page_size = 5
class VetSearchApiView(generics.ListAPIView):
    serializer_class = VetSerializer
    pagination_class = VetSearchPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name']

    def get_queryset(self):
        query = self.request.query_params.get('search', '')
        if not query:
            return PawMedicUser.objects.none()
        return PawMedicUser.objects.filter(role=PawMedicUserType.VET, vet_profile__is_published=True).select_related('vet_profile')