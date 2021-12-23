from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from tickets.models import Ticket


class TicketsAPITestCase(APITestCase):

    def create_ticket(self):
        sample_ticket = {'title': 'Test',
                         'desc': 'This is test description'}
        response = self.client.post(reverse('tickets'), sample_ticket)
        return response

    def authenticate(self):
        self.client.post(reverse('register'), {'username': 'username',
                                               'email': 'email@mail.com',
                                               'password': 'password'})
        response = self.client.post(reverse('login'), {'username': 'username',
                                                       'email': 'email@mail.com',
                                                       'password': 'password'})

        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {response.data['token']}")

        #self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestListCreateTickets(TicketsAPITestCase):

    def test_should_not_create_ticket_without_authentication(self):
        response = self.create_ticket()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # this test didn't pass and all of other tests after
    # валится все начиная с этого теста. Хотя вроде верхние по аутентификации проходит
    # Unresolved attribute reference 'objects' for class 'Ticket' ???? WHY ?????
    def test_should_create_ticket(self):
        self.authenticate()
        previous_ticket_count = Ticket.objects.all().count()

        response = self.create_ticket()

        self.assertEqual(Ticket.objects.all().count(),
                         previous_ticket_count + 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Test')
        self.assertEqual(response.data['desc'], 'This is test description')

    def test_retrieves_all_tickets(self):
        self.authenticate()
        response = self.client.get(reverse('tickets'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data['results'], list)

        sample_ticket = {'title': 'Test',
                         'desc': 'This is test description'}
        self.client.post(reverse('tickets'), sample_ticket)

        resp = self.client.get(reverse('tickets'))
        self.assertIsInstance(resp.data['count'], int)
        self.assertEqual(resp.data['count'], 1)


class TestTicketDetailAPIView(TicketsAPITestCase):

    def test_retrieve_one_item(self):
        self.authenticate()
        self.create_ticket()
        response = self.create_ticket()

        resp = self.client.get(
            reverse('ticket', kwargs={'id': response.data['id']}))

        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        ticket = Ticket.objects.get(id=response.data['id'])

        self.assertEqual(ticket.title, resp.data['title'])

    def test_updates_one_item(self):
        self.authenticate()
        response = self.create_ticket()

        resp = self.client.patch(
            reverse('ticket', kwargs={'id': response.data['id']}),
            {'title': 'New title', 'is_complete': True})

        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        updated_ticket = Ticket.objects.get(id=response.data['id'])

        self.assertEqual(updated_ticket.is_complete, True)
        self.assertEqual(updated_ticket.title, 'New title')

    def test_deletes_one_item(self):
        self.authenticate()
        response = self.create_ticket()
        previous_db_count = Ticket.objects.all().count()

        self.assertGreater(previous_db_count, 0)
        self.assertEqual(previous_db_count, 1)

        resp = self.client.delete(
            reverse('ticket', kwargs={'id': response.data['id']}))

        self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)

        self.assertEqual(Ticket.objects.all().count(), 0)

