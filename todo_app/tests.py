from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Todo

class TodoTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_create_todo(self):
        url = reverse('todo-list')
        data = {'title': 'Test Todo', 'description': 'Test Description'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertEqual(Todo.objects.get().title, 'Test Todo')

    def test_get_todo_list(self):
        Todo.objects.create(user=self.user, title='Test Todo')
        url = reverse('todo-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_todo(self):
        todo = Todo.objects.create(user=self.user, title='Test Todo')
        url = reverse('todo-detail', kwargs={'pk': todo.id})
        data = {'title': 'Updated Todo', 'status': True}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.get().title, 'Updated Todo')
        self.assertEqual(Todo.objects.get().status, True)

    def test_delete_todo(self):
        todo = Todo.objects.create(user=self.user, title='Test Todo')
        url = reverse('todo-detail', kwargs={'pk': todo.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Todo.objects.count(), 0)

class UserAuthTests(APITestCase):
    def test_register(self):
        url = reverse('register')
        data = {'username': 'newuser', 'password': 'newpass', 'email': 'new@user.com'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'newuser')

    def test_login(self):
        User.objects.create_user(username='testuser', password='testpass')
        url = reverse('login')
        data = {'username': 'testuser', 'password': 'testpass'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)
