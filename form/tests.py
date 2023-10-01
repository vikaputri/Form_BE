import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from .models import Form
from .serializers import Formserializer

# initialize the APIClient app
client = Client()

class GetAllTest(TestCase):
    def setUp(self):
        Form.objects.create(
            name='Vika',
            identification_number='123456789012',
            email='vika@gmail.com',
            date_of_birth='2020-01-01'
        )
        Form.objects.create(
            name='Putri',
            identification_number='098765432123',
            email='putri@gmail.com',
            date_of_birth='2020-01-01'
        )
        Form.objects.create(
            name='Ariyanti',
            identification_number='675849302182',
            email='ariyanti@gmail.com',
            date_of_birth='2020-01-01'
        )

    def test_get_all_form(self):
        # get API response
        response = client.get(reverse('data'))
        # get data from db
        forms = Form.objects.all()
        serializer = Formserializer(forms, many=True)
        self.assertEqual(response.data, serializer.data)

class GetSingleTest(TestCase):
    def setUp(self):
        self.Vika = Form.objects.create(
            name='Vika',
            identification_number='123456789012',
            email='vika@gmail.com',
            date_of_birth='2020-01-01'
        )
        self.Putri = Form.objects.create(
            name='Putri',
            identification_number='098765432123',
            email='putri@gmail.com',
            date_of_birth='2020-01-01'
        )
        self.Ariyanti = Form.objects.create(
            name='Ariyanti',
            identification_number='675849302182',
            email='ariyanti@gmail.com',
            date_of_birth='2020-01-01'
        )

    def test_get_valid_single(self):
        response = client.get(reverse('data_detail', kwargs={'pk': self.Vika.pk}))
        form = Form.objects.get(pk=self.Vika.pk)
        serializer = Formserializer(form)
        self.assertEqual(response.data, serializer.data)

    def test_get_invalid_single(self):
        response = client.get(
            reverse('data_detail', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CreateFormTest(TestCase):
    def setUp(self):
        self.valid_payload = {
            'name' : 'Vika',
            'identification_number' : '123456789012',
            'email' : 'vika@gmail.com',
            'date_of_birth' : '2020-01-01'
        }

        self.invalid_payload = {
            'name' : '',
            'identification_number' : '123456789012',
            'email' : 'vika@gmail.com',
            'date_of_birth' : '2020-01-01'
        }

    def test_create_valid(self):
        response = client.post(
            reverse('data'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid(self):
        response = client.post(
            reverse('data'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class UpdateSinglePuppyTest(TestCase):
    """ Test module for updating an existing puppy record """

    def setUp(self):
        self.Vika = Form.objects.create(
            name='Vika',
            identification_number='123456789012',
            email='vika@gmail.com',
            date_of_birth='2020-01-01'
        )
        self.Putri = Form.objects.create(
            name='Putri',
            identification_number='098765432123',
            email='putri@gmail.com',
            date_of_birth='2020-01-01'
        )
        self.Ariyanti = Form.objects.create(
            name='Ariyanti',
            identification_number='675849302182',
            email='ariyanti@gmail.com',
            date_of_birth='2020-01-01'
        )
        self.valid_payload = {
            'name' : 'Vika Putri',
            'identification_number' : '123456789012',
            'email' : 'vika@gmail.com',
            'date_of_birth' : '2020-01-01'
        }

        self.invalid_payload = {
            'name' : '',
            'identification_number' : '123456789012',
            'email' : 'vikaputri@gmail.com',
            'date_of_birth' : '2020-01-01'
        }

    def test_valid_update(self):
        response = client.put(
            reverse('data_detail', kwargs={'pk': self.Vika.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_puppy(self):
        response = client.put(
            reverse('data_detail', kwargs={'pk': self.Vika.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class DeleteFormTest(TestCase):
    def setUp(self):
        self.Vika = Form.objects.create(
            name='Vika',
            identification_number='123456789012',
            email='vika@gmail.com',
            date_of_birth='2020-01-01'
        )
        self.Putri = Form.objects.create(
            name='Putri',
            identification_number='098765432123',
            email='putri@gmail.com',
            date_of_birth='2020-01-01'
        )
        self.Ariyanti = Form.objects.create(
            name='Ariyanti',
            identification_number='675849302182',
            email='ariyanti@gmail.com',
            date_of_birth='2020-01-01'
        )

    def test_valid_delete(self):
        response = client.delete(reverse('data_detail', kwargs={'pk': self.Vika.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete(self):
        response = client.delete(reverse('data_detail', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)