# from django.test import TestCase
# from django.urls import reverse
# from .models import User  # Import your custom user model
# from rest_framework.authtoken.models import Token
# from rest_framework.test import APIClient
#
# class ProfileDetailsViewTest(TestCase):
#     # def setUp(self):
#     #     # Create a test user
#     #     self.user = User.objects.create_user(username='testuser', password='testpassword')
#     #
#     #     # Create an authentication token for the user
#     #     self.token = Token.objects.create(user=self.user)
#     #
#     #     # Create an API client for making authenticated requests
#     #     self.client = APIClient()
#     #     self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
#     # def setUp(self):
#     #     # Create a test user
#     #     self.user = User.objects.create_user(username='testuser', password='testpassword')
#     #
#     #     # Create a token for the user
#     #     self.token, created = Token.objects.get_or_create(user=self.user)
#     def setUp(self):
#         # Create a test user
#         self.user = User.objects.create_user(username='testuser', password='testpassword')
#
#         # Create a token for the user
#         self.token, created = Token.objects.get_or_create(user=self.user)
#
#         # Create an API client for making authenticated requests
#         self.client = APIClient()
#         self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
#
#     def test_profile_details_view_authenticated(self):
#
#         url = reverse('profile-details', kwargs={'pk': self.user.pk})
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 302)
#
#
#
#     def test_profile_details_view_unauthenticated(self):
#         # Set up the URL for the ProfileDetailsView using the user's PK
#         url = reverse('profile-details', kwargs={'pk': self.user.pk})
#
#         # Create a new API client without authentication
#         unauthenticated_client = APIClient()
#
#         # Perform a GET request to the view using the unauthenticated client
#         response = unauthenticated_client.get(url)
#
#         # Check if the response status code is 403 (Forbidden) since an unauthenticated user should not access it
#         self.assertEqual(response.status_code, 302)
#
#         # Add more assertions as needed to check the behavior for unauthenticated users
