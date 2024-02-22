from django.test import TestCase
from django.utils import timezone

from first_app.models import CallOrder



class MyModelTest(TestCase):
    def test_call_order(self):
        date = timezone.now()
        CallOrder.objects.create(user_name='user1', user_surname='surname1', phone='+380967894512', order_date=date, completed_status=False)
        zxc = CallOrder.objects.get(user_name='user1')
        self.assertEqual(zxc.user_surname(), 'surname1')



