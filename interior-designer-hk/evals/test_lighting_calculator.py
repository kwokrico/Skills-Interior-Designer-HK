"""Regression checks for overall-factor lighting estimates through the dispatcher."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from dispatcher import InteriorDesignerDispatcher


class LightingCalculationTests(unittest.TestCase):
    def calculate(self, **overrides):
        data = {"target_lux": 500, "maintenance_factor": 0.8}
        data.update(overrides)
        return InteriorDesignerDispatcher().run_interior_calculator("lux_targeting", data)

    def test_overall_factor_applied_once(self):
        result = self.calculate()
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["result"]["initial_design_lux"], 625.0)

    def test_no_depreciation_boundary(self):
        self.assertEqual(self.calculate(maintenance_factor=1)["result"]["initial_design_lux"], 500)

    def test_overlapping_legacy_factor_rejected(self):
        self.assertEqual(self.calculate(llf=0.9)["status"], "error")

    def test_missing_inputs_not_defaulted(self):
        for data in ({}, {"target_lux": 500}, {"maintenance_factor": 0.8}):
            with self.subTest(data=data):
                self.assertEqual(InteriorDesignerDispatcher().run_interior_calculator("lux_targeting", data)["status"], "error")

    def test_invalid_factors_rejected(self):
        for value in (0, -0.2, 1.1, float("nan"), float("inf"), None, True, "unknown"):
            with self.subTest(value=value):
                self.assertEqual(self.calculate(maintenance_factor=value)["status"], "error")

    def test_invalid_targets_rejected(self):
        for value in (0, -500, float("nan"), float("inf"), None, False):
            with self.subTest(value=value):
                self.assertEqual(self.calculate(target_lux=value)["status"], "error")

    def test_fixture_count_rounds_up_with_explicit_utilization(self):
        result = self.calculate(room_area_m2=20, lumens_per_fixture=2000, utilization_factor=0.5)
        self.assertEqual(result["result"]["estimated_fixture_count"], 13)

    def test_partial_fixture_inputs_rejected(self):
        self.assertEqual(self.calculate(room_area_m2=20, lumens_per_fixture=2000)["status"], "error")

    def test_invalid_fixture_inputs_rejected(self):
        for key, value in (("room_area_m2", -1), ("lumens_per_fixture", 0), ("utilization_factor", 0), ("utilization_factor", 1.1)):
            with self.subTest(key=key, value=value):
                data = dict(room_area_m2=20, lumens_per_fixture=2000, utilization_factor=0.5)
                data[key] = value
                self.assertEqual(self.calculate(**data)["status"], "error")


if __name__ == "__main__":
    unittest.main()
