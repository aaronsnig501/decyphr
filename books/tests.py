"""
This section of functionality is difficult to test as the information comes
from the Google Books API, however I should still be able to test:

    - A request can be made to the endpoint
    - An appropriate error message will be returned if the API requirements
        aren't met
    - An error is thrown if the request isn't authenticated
    - The Google Books will not be called if the data already exists within
        Decyphr
"""
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from books.models import Book
from accounts.models import UserProfile
from languages.models import Language


class BooksTests(APITestCase):
    """The test cases for the book API
    """
    fixtures = ['fixtures.json']

    def test_a_client_cant_access_create_entries_without_a_token(self):
        """A client that tries to access the books endpoint recieves a 401 if they
        don't provide a token
        """
        url = reverse("books-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_a_client_can_access_the_endpoint_with_a_token(self):
        """Authorized clients will be able to access the endpoint and search
        for books
        """
        url = reverse("books-list")
        user = UserProfile.objects.first()

        self.client.force_authenticate(user=user)
        response = self.client.get(url, {"name": "harry"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_a_client_cant_retrieve_an_individual_book_without_a_token(self):
        """Unauthorized attempt to retrieve a book based on the ID will result
        in a 
        """
        create_book_url = reverse("books-list")
        url = reverse("books-detail", kwargs={"pk": 1})
        self.client.get(create_book_url, {"name": "harry"})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    
    def test_a_client_can_retrieve_an_individual_book_based_on_the_id(self):
        """An authorized user an retrieve a single book based on that book's
        ID
        """
        create_book_url = reverse("books-list")
        url = reverse("books-detail", kwargs={"pk": 1})
        user = UserProfile.objects.first()

        self.client.force_authenticate(user=user)
        self.client.get(create_book_url, {"name": "harry"})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(1, response.data["language"])
