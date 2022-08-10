from unittest import TestCase
from rest_framework.test import APIClient


# class TestAktyor(TestCase):
#     def setUp(self) -> None:
#         self.client=APIClient()
#     def test_aktyor(self):
#         natija=self.client.get("/aktyorlar/1/")
#         assert natija.status_code==200
#         assert natija.data["id"]==2
    # def test_aktyor_invalid(self):
    #     natija = self.client.get("/aktyorlar/3/")
    #     assert natija.status_code == 404


# class TestKino(TestCase):
#     def setUp(self) -> None:
#         self.client=APIClient()

