import re
import unittest
from regex_service import PATTERN

class TestRegex(unittest.TestCase):
    pattern = re.compile(PATTERN)

    def test_full_match_valid(self):
        valid_cases = [
            "123-456-789-00",
            "987-654-321 12",
            "000-000-000-99",
            "001-001-001-01"
        ]
        for case in valid_cases:
            with self.subTest(case=case):
                self.assertIsNotNone(self.pattern.fullmatch(case))

    def test_full_match_invalid(self):
        invalid_cases = [
            "12345678900",      
            "123-45-6789-00",
            "123-456-789/00",   
            "abc-def-ghi-00",   
            "123-456-789",      
            " 123-456-789-00",  
            "123-456-789-00 ",
        ]
        for case in invalid_cases:
            with self.subTest(case=case):
                self.assertIsNone(self.pattern.fullmatch(case))

    def test_search_valid(self):
        strings = [
            "This is a test 123-456-789-00 string.",
            "Another valid number: 987-654-321 12 here.",
            "Edge case: 000-000-000-99.",
        ]
        for string in strings:
            with self.subTest(string=string):
                self.assertIsNotNone(self.pattern.search(string))

    def test_search_invalid(self):
        strings = [
            "No numbers here.",
            "Invalid 12345678900 format.",
            "123-456-789 is not complete.",
        ]
        for string in strings:
            with self.subTest(string=string):
                self.assertIsNone(self.pattern.search(string))

    def test_findall(self):
        string = "123-456-789-00 and 987-654-321 12 are valid numbers."
        expected_matches = ["123-456-789-00", "987-654-321 12"]
        self.assertEqual(self.pattern.findall(string), expected_matches)

    def test_substitution(self):
        string = "Replace 123-456-789-00 and 987-654-321 12 with placeholders."
        expected_result = "Replace [REDACTED] and [REDACTED] with placeholders."
        result = self.pattern.sub("[REDACTED]", string)
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()