"""Unit tests for dynamic-temperature-annealer."""
import unittest
from dynamic_temperature_annealer.annealer import TemperatureAnnealer


class TestTemperatureAnnealer(unittest.TestCase):
    def setUp(self):
        self.annealer = TemperatureAnnealer()

    def test_code_mode_selection(self):
        params = self.annealer.recommend_params("Write a class with def compute(self)")
        self.assertEqual(params.task_mode, "code_structured")
        self.assertLessEqual(params.temperature, 0.2)

    def test_creative_mode_selection(self):
        params = self.annealer.recommend_params("Brainstorm new names for my startup")
        self.assertEqual(params.task_mode, "creative_ideation")
        self.assertGreaterEqual(params.temperature, 0.8)
