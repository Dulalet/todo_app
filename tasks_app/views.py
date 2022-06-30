from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK

from tasks_app.models import Task
from tasks_app.serializers import TaskSerializer
from tasks_app.tasks import send_email_notification


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [AllowAny]

    def update(self, request, *args, **kwargs):
        if not request.user:
            return Response("User is not authenticated", HTTP_400_BAD_REQUEST)

        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        if instance.executed != serializer.validated_data['executed']:
            if serializer.validated_data['executed']:
                message = 'Your task was marked as executed!'
            else:
                message = 'Your task was marked as not executed!'
            send_email_notification.delay(instance.user.email, message)
            send_email_notification.delay(request.user.email, message)
        self.perform_update(serializer)

        return Response(serializer.data)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated], url_name='execute', url_path='execute')
    def execute(self, request, pk=None):
        if not request.user:
            return Response("User is not authenticated", HTTP_400_BAD_REQUEST)
        task = get_object_or_404(Task, id=pk)
        task.executed = True
        send_email_notification.delay(task.user.email, 'Your task was executed!')
        send_email_notification.delay(request.user.email, 'Your task was executed!')

        return Response('email sent', HTTP_200_OK)
