from rest_framework.response import Response
from rest_framework import viewsets
from Advisor.models import Advisormodel
from .serializer import Advisorserializer


class AdvisorViewset(viewsets.ModelViewSet):
     serializer_class = Advisorserializer
     
     def get_queryset(self):
       advisor_list = Advisormodel.objects.all()
       return advisor_list
    
     def create(self,request,*args,**kwargs):
         advisor_data = request.data
         
         new_advisor = Advisormodel.objects.create(name = advisor_data["name"],profile_url = advisor_data["profile_url"])
         new_advisor.save()
         serializer = Advisorserializer(new_advisor)

         return Response(serializer.data) 