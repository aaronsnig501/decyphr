"""Reading Sessions views

The views module of the reading session app. These views will be responsible
for handling the interactions between a user and any actions that they perform
during their reading sessions.

This view will be responsible for creating new reading sessions, return
reading sessions, maintain the state of a reading session (if it's in progress,
not started, finished, etc), updating reading sessions and deleting sessions.
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from reading_sessions.models import ReadingSession
from . import serializers


class ReadingSessionViewSet(viewsets.ModelViewSet):
    """ReadingSessionViewSet Viewset

    The viewset that will handle the interactions between the user and their
    reading sessions
    """
    permission_classes = [IsAuthenticated,]
    serializer_class = serializers.ReadingSessionSerializer
    queryset = ReadingSession.objects.all()

    def create(self, request):
        """Create reading session

        This method will process in the incoming data and use it to initialise
        a new reading session for the user.

        Args:
            library_item (int): The ID of the library item that this reading
            session will map too
            duration (str): A string representation of the value that will be
            stored as the duration of the session
            pages (float): The number of pages that the user read during the
            session
            status (string): A one letter status indicator to inform what part of
            the process the reading session
        """
        create_serializer = self.serializer_class(data=request.data)

        if create_serializer.is_valid():
            model = create_serializer.save()
            return_serializer = self.serializer_class(model)
            return Response(return_serializer.data)
        else:
            return Response(create_serializer.errors)
    
    def partial_update(self, request, pk):
        session = ReadingSession.objects.get(id=pk)
        serializer = self.serializer_class(
            session, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        else:
            return Response(serializer.errors)
