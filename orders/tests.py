from django.test import TestCase

from orders.models import Order, OrderItem

import results


class OrderOrderingTestCase(TestCase):
    fixtures = ['test_orders.json']

    def test_orders_are_split_by_shipping_method(self):
        #fcm, pri = Order.split_by_shipping_method()
        pri=[O.id for O in Order.objects.filter(shipping_method = 'PRI')]
        fcm=[O.id for O in Order.objects.filter(shipping_method = 'FCM')]
        self.assertEqual(results.fcm, fcm)
        self.assertEqual(results.pri, pri)

    def test_orders_are_split_by_single_and_multiple(self):
        #singles, multiples = Order.split_by_single_and_multiple()
        singles=[O.id for O in Order.objects.all() if len(O.items.all()) == 1]
        multiples=[O.id for O in Order.objects.all() if len(O.items.all()) > 1]
        self.assertEqual(results.singles, singles)
        self.assertEqual(results.multiples, multiples)

    def test_single_orders_are_sorted(self):
        #single_sorted_orders = Order.single_orders_are_sorted()
        self.assertEqual(results.single_sorted_orders, single_sorted_orders)

    def test_multiple_orders_are_split_by_xxl_and_not(self):
        #xxl, not_xxl = Order.orders_split_by_xxl_and_not()
        xxl=[O.id for O in Order.objects.all() if len(O.items.all()) > 1 and 'XXL' in set([I.product for I in O.items.all()])]
        not_xxl=[O.id for O in Order.objects.all() if len(O.items.all()) > 1 and 'XXL' not in set([I.product for I in O.items.all()])]
        self.assertEqual(results.xxl, xxl)
        self.assertEqual(results.not_xxl, not_xxl)
