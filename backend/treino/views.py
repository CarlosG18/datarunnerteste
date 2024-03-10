from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Treino, Treino_tempo, Teste
from .serializers import TreinoSerializer, TreinoTempoSerializer, TesteSerializer

@api_view(['POST'])
def receber_dados(request):
    data = request.data
    serial_data = TesteSerializer(data=data)
    if serial_data.is_valid():
        response = {
            "status": "sucess",
            "messagem": "treino criado com sucesso!",
            "code": status.HTTP_201_CREATED,
            "dados": data
        }
        serial_data.save()
        return Response(response, status=status.HTTP_201_CREATED)
    else:
        return Response(serial_data.errors, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.

@api_view(['GET'])
def list_treinos(request):
    queryset = Teste.objects.all()
    queryset_serial = TesteSerializer(queryset, many=True)
    response = {
            "status": "sucess",
            "messagem": "todos os treinos obtidos com sucesso!",
            "code": status.HTTP_200_OK,
            "dados": queryset_serial.data
        }
    return Response(response, status=status.HTTP_200_OK)