from django.urls import path

from vets.api_views import VetSearchApiView
from vets.views import VetListView, VetPublishView, VetDetailView, VetSearchView

urlpatterns = [
    path('', VetListView.as_view(), name='vets-list'),
    path('<slug:slug>/<int:pk>', VetDetailView.as_view(), name='vets-detail'),
    path('publish-vet', VetPublishView.as_view(), name='publish-vet'),
    path('api/vets/', VetSearchApiView.as_view(), name='vet-api-search'),
    path('search', VetSearchView.as_view(), name='vet-search')
]