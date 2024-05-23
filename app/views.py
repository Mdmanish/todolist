from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import UserSerializer, TodoSerializer, LoginSerializer, AddStepSerializer, CategorySerializer, FileSerializer
from django.contrib.auth import authenticate, login
from .models import Todo, AddStep, Category, File
from django.contrib.auth.models import User

class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(serializer.validated_data['password'])
            user.save()
            login(request, user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return Response({'message': 'Login successful'})
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print(request.user)
        user = User.objects.get(username=request.user)
        todos = Todo.objects.filter(user=user)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        user = User.objects.get(username=request.user)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateDeleteView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, todo_id):
        try:
            user = User.objects.get(username=request.user)
            todo = Todo.objects.get(id=todo_id, user=user)
            serializer = TodoSerializer(todo)
            return Response(serializer.data)
        except Todo.DoesNotExist:
            return Response({"error": "Todo not found"}, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, todo_id):
        try:
            user = User.objects.get(username=request.user)
            todo = Todo.objects.get(id=todo_id, user=user)
        except Todo.DoesNotExist:
            return Response({"error": "Todo not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, todo_id):
        user = User.objects.get(username=request.user)
        try:
            todo = Todo.objects.get(id=todo_id, user=user)
            todo.delete()
            return Response({"message": "Todo deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Todo.DoesNotExist:
            return Response({"error": "Todo not found"}, status=status.HTTP_404_NOT_FOUND)

class AddStepView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, todo_id):
        serializer = AddStepSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddStepDetailedView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, step_id):
        add_step_obj = AddStep.objects.get(id=step_id)
        serializer = AddStepSerializer(add_step_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, step_id):
        add_step_obj = AddStep.objects.get(id=step_id)
        if add_step_obj:
            add_step_obj.delete()
            return Response({"message": "Step deleted"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"message": "Step does not exist"}, status=status.HTTP_400_BAD_REQUEST)

class CategoryView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, todo_id):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetailedView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, category_id):
        category_obj = Category.objects.get(id=category_id)
        if category_obj:
            category_obj.delete()
            return Response({"message": "Category deleted"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"message": "Category not found"}, status=status.HTTP_400_BAD_REQUEST)
    

class FileView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, todo_id):
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class FileDetailedView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, file_id):
        file_obj = File.objects.filter(id=file_id)
        if file_obj:
            file_obj.delete()
            return Response({"message": "file deleted"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"message": "file does not exist"}, status=status.HTTP_400_BAD_REQUEST)
