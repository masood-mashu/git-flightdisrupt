"""
eval_predictability.py - Checkpoint 02 Benchmark Suite for GitFlightDisrupt.
"""
import os, sys, unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tools.eu261_compensation_calculator import *
from tools.passenger_reroute_optimizer import *
from tools.baggage_sla_tracker import *

class TestGitFlightDisruptPredictability(unittest.TestCase):

    def test_eu261_compensation_calculator(self):
        res = calculate_eu261('{"delay_minutes": 240, "distance_km": 2500, "extraordinary_circumstance": false}')
        self.assertEqual(res["compensation_eur"], 400)
        self.assertEqual(res["status"], "EU261_ELIGIBLE_400_EUR")

    def test_passenger_reroute_optimizer(self):
        res = optimize_reroute('{"candidate_departure_offset_hours": 3.5}')
        self.assertTrue(res["acceptable"])
        self.assertEqual(res["status"], "REBOOKING_OPTION_APPROVED")

    def test_baggage_sla_tracker(self):
        res = track_baggage_sla(5)
        self.assertFalse(res["declared_lost"])
        self.assertEqual(res["status"], "BAGGAGE_IN_TRANSIT_LOCATE")


if __name__ == "__main__":
    unittest.main()
