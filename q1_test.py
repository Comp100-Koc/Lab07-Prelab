import unittest
from copy import deepcopy

from q1 import custom_sort


def _people_fixture():
    return [
        {"name": "Alice", "age": 30, "salary": 75000, "address": {"city": "New York", "zip_code": 10001}},
        {"name": "Bob", "age": 25, "salary": 62000, "address": {"city": "Boston", "zip_code": 20001}},
        {"name": "Charlie", "age": 25, "salary": 68000, "address": {"city": "Boston", "zip_code": 15001}},
        {"name": "David", "age": 30, "salary": 90000, "address": {"city": "New York", "zip_code": 20002}},
        {"name": "Eve", "age": 30, "salary": 75000, "address": {"city": "Chicago", "zip_code": 60007}},
    ]


class TestCustomSort(unittest.TestCase):
    def test_matches_readme_example(self):
        people = _people_fixture()[:-1]  # drop Eve
        expected_names = ["Charlie", "Bob", "Alice", "David"]
        result = custom_sort(people, "age", "address.zip_code")
        self.assertEqual([p["name"] for p in result], expected_names)

    def test_secondary_tiebreaker(self):
        people = _people_fixture()
        result = custom_sort(people, "salary", "address.city")
        expected_order = ["Bob", "Charlie", "Eve", "Alice", "David"]
        self.assertEqual([p["name"] for p in result], expected_order)

    def test_final_name_tiebreaker(self):
        people = [
            {"name": "Aaron", "age": 25, "salary": 50000, "address": {"city": "Dallas", "zip_code": 75001}},
            {"name": "Zara", "age": 25, "salary": 50000, "address": {"city": "Dallas", "zip_code": 75001}},
        ]
        result = custom_sort(people, "age", "salary")
        self.assertEqual([p["name"] for p in result], ["Aaron", "Zara"])

    def test_does_not_mutate_input(self):
        people = _people_fixture()
        original = deepcopy(people)
        custom_sort(people, "age", "salary")
        self.assertEqual(people, original)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCustomSort)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
