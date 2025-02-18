# from rest_framework import viewsets
# from .models import Mətinlər, Müraciət, Əlaqə, Qeydiyyat, Sessiyalar, Nümayişlər, Sillabuslar, Təlimçilər,Məzunlar,Müəllimlər
# from .serializers import ScriptsSerializer, SessionsSerializer, BroadcastsSerializer, SyllabusSerializer, TrainerSerializer, ApplySerializer, ContactSerializer, SubscribeSerializer, TeachersSerializer, GraduatesSerializer





# class ApplyViewSet(viewsets.ModelViewSet):
#     queryset = Müraciət.objects.all()
#     serializer_class = ApplySerializer
    
# class ContactViewSet(viewsets.ModelViewSet):
#     queryset = Əlaqə.objects.all()
#     serializer_class = ContactSerializer
    
    

# class SubscribeViewSet(viewsets.ModelViewSet):
#     queryset = Qeydiyyat.objects.all()
#     serializer_class = SubscribeSerializer

# # SESSIONS API
# class SessionsViewSet(viewsets.ModelViewSet):
#     queryset = Sessiyalar.objects.all()
#     serializer_class = SessionsSerializer

# # BROADCASTS API
# class BroadcastsViewSet(viewsets.ModelViewSet):
#     queryset = Nümayişlər.objects.all()
#     serializer_class = BroadcastsSerializer

# # SYLLABUS API
# class SyllabusViewSet(viewsets.ModelViewSet):
#     queryset = Sillabuslar.objects.all()
#     serializer_class = SyllabusSerializer
# # TRAINERS API  
# class TrainerViewSet(viewsets.ModelViewSet):
#     queryset = Təlimçilər.objects.all()
#     serializer_class = TrainerSerializer


# class ScriptsViewSet(viewsets.ModelViewSet):
#     queryset = Mətinlər.objects.prefetch_related('sessions', 'syllabus','trainers').select_related('broadcast')
#     serializer_class = ScriptsSerializer

#     def get_serializer_context(self):
#         context = super().get_serializer_context()
#         context['request'] = self.request 
#         return context

# class TeachersViewSet(viewsets.ModelViewSet):
#     queryset = Müəllimlər.objects.all()
#     serializer_class = TeachersSerializer
    
# class GraduatesViewSet(viewsets.ModelViewSet):
#     queryset = Məzunlar.objects.all()
#     serializer_class = GraduatesSerializer







from .models import Müraciət, Əlaqə, Qeydiyyat, Bootcamps, BootcampTipi, Təlimlər, Mətinlər, Sessiyalar, Nümayişlər, Sillabuslar, Təlimçilər, Müəllimlər, Məzunlar,FAQ
from .serializers import MüraciətSerializer, ƏlaqəSerializer, QeydiyyatSerializer, BootcampsSerializer, BootcampTipiSerializer, TəlimlərSerializer, MətinlərSerializer, SessiyalarSerializer, NümayişlərSerializer, SillabuslarSerializer, TəlimçilərSerializer, MüəllimlərSerializer, MəzunlarSerializer,FAQSerializer
from rest_framework import viewsets

class MüraciətViewSet(viewsets.ModelViewSet):
    queryset = Müraciət.objects.all()
    serializer_class = MüraciətSerializer

class ƏlaqəViewSet(viewsets.ModelViewSet):
    queryset = Əlaqə.objects.all()
    serializer_class = ƏlaqəSerializer

class QeydiyyatViewSet(viewsets.ModelViewSet):
    queryset = Qeydiyyat.objects.all()
    serializer_class = QeydiyyatSerializer

class BootcampsViewSet(viewsets.ModelViewSet):
    queryset = Bootcamps.objects.all().prefetch_related(
        'bootcamp_tipi__telimler'
 
    )  
    serializer_class = BootcampsSerializer

class BootcampTipiViewSet(viewsets.ModelViewSet):
    queryset = BootcampTipi.objects.all()
    serializer_class = BootcampTipiSerializer

class TəlimlərViewSet(viewsets.ModelViewSet):
    queryset = Təlimlər.objects.all()
    serializer_class = TəlimlərSerializer

class MətinlərViewSet(viewsets.ModelViewSet):
    queryset = Mətinlər.objects.all()
    serializer_class = MətinlərSerializer

class SessiyalarViewSet(viewsets.ModelViewSet):
    queryset = Sessiyalar.objects.all()
    serializer_class = SessiyalarSerializer

class NümayişlərViewSet(viewsets.ModelViewSet):
    queryset = Nümayişlər.objects.all()
    serializer_class = NümayişlərSerializer

class SillabuslarViewSet(viewsets.ModelViewSet):
    queryset = Sillabuslar.objects.all()
    serializer_class = SillabuslarSerializer

class TəlimçilərViewSet(viewsets.ModelViewSet):
    queryset = Təlimçilər.objects.all()
    serializer_class = TəlimçilərSerializer

class MüəllimlərViewSet(viewsets.ModelViewSet):
    queryset = Müəllimlər.objects.all()
    serializer_class = MüəllimlərSerializer

class MəzunlarViewSet(viewsets.ModelViewSet):
    queryset = Məzunlar.objects.all()
    serializer_class = MəzunlarSerializer
    
class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    
    
