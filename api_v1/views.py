from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from api_v1.serializers import PlotSerializer, CultureSerializer
from geoapp.models import Plot, Culture


class PlotsListView(generics.ListAPIView):
    queryset = Plot.objects.all()
    serializer_class = PlotSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if not self.request.user.is_staff:
            return Plot.objects.filter(farmer__user=self.request.user)
        return super().get_queryset()


class PlotDetailView(generics.RetrieveUpdateAPIView):
    queryset = Plot.objects.all()
    serializer_class = PlotSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if not self.request.user.is_staff:
            return Plot.objects.filter(farmer__user=self.request.user)
        return super().get_queryset()


class CulturesListView(generics.ListAPIView):
    queryset = Culture.objects.all()
    serializer_class = CultureSerializer
    permission_classes = [IsAuthenticated]
