from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Usuario
from .serializers import UsuarioSerializer

class UsuarioAPI(APIView):
    def get(self, request):
        usuarios = [ 
        Usuario('Carlos', 'Carlos@email.com'), 
        Usuario('João', 'João@email.com') 
                ]
    
        serializer = UsuarioSerializer(usuarios, many=True)

        print(serializer.data)
        return Response(serializer.data)

