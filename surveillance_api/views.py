import json

from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from .serializers.serializers import *
from .models import *


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['get'], permission_classes=permission_classes)
    def get_users(self, request, pk=None):
        try:
            user = User.objects.get(id=pk)

            page = self.paginate_queryset(user)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return Response(self.get_paginated_response(serializer.data), status=status.HTTP_200_OK)

            serializer = self.get_serializer(user, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


class NodeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows node to be viewed or edited.
    """
    queryset = Node.objects.all()
    serializer_class = NodeSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        """
        Get all the list of nodes (without partners)
        """
        try:
            nodes = self.get_queryset()
            serializer = self.get_serializer(nodes, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['GET'])
    def get_partner_list(self, request):
        """
        Get all the list of nodes (with partners)
        """
        try:
            nodes = Node.objects.values()

            if len(nodes) > 1:

                # Update each partner dict value to array of adjacent surveillance object
                for item in nodes:
                    item['partners'] = Partner.objects.filter(from_person=item['id']).values('to_person_id', 'angle_start', 'angle_end', 'date_created', 'date_updated')

                    for partner in item['partners']:
                        partner['to_person_id'] = Node.objects.filter(pk=partner['to_person_id']).values('name')[0]

            return Response(nodes, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            super().update(request, pk=pk)
            instance = self.get_object()
            return Response(NodeSerializer(instance.author).data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        print(request)
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response({'message': 'success', 'pk': serializer.instance.pk}, content_type='application/json', status=status.HTTP_200_OK)

        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            super().destroy(self)
            return Response("Node Deleted", status=status.HTTP_200_OK)

        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    #  permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        try:
            partners = self.get_queryset()
            serializer = self.get_serializer(partners, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            result = self.perform_update(serializer, pk=pk)
            return Response(result, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response({'status': 'success', 'pk': serializer.instance.pk}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            result = self.perform_destroy(serializer)
            return Response("Node Deleted", status=status.HTTP_200_OK)

        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def generate_report(request):
    """
    Generate Report for user
    """
    try:
        # Prepare to call external python file for report generation
        # result = <python class>.generate_report()
        # if result is not None:
        #    return Response(result, status=status.HTTP_200_OK)
        return Response(request.data, status=status.HTTP_200_OK)

    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
