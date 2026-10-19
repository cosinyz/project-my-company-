from django.test import TestCase

from apps.employees.models import Employee


class EmployeeListViewTests(TestCase):
    def test_root_displays_employees(self):
        Employee.objects.create(
            first_name='Alex',
            last_name='Smith',
            position='Developer',
            salary=75000,
        )

        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Alex')
        self.assertContains(response, 'Smith')
        self.assertContains(response, 'Developer')
        self.assertContains(response, '75000')

    def test_root_shows_empty_state(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Сотрудников пока нет.')
