"""
eu261_compensation_calculator.py - Calculates EU261 statutory compensation eligibility in Euros based on flight distance and delay duration
"""
import sys
import json


def calculate_eu261(delay_data_json: str):
    import json
    data = json.loads(delay_data_json) if isinstance(delay_data_json, str) else delay_data_json
    delay = data.get("delay_minutes", 200)
    dist = data.get("distance_km", 2000.0)
    exempt = data.get("extraordinary_circumstance", False)
    
    if exempt or delay < 180:
        comp = 0
    elif dist <= 1500:
        comp = 250
    elif dist <= 3500:
        comp = 400
    else:
        comp = 600
    return {
        "delay_minutes": delay,
        "distance_km": dist,
        "exempt": exempt,
        "compensation_eur": comp,
        "status": f"EU261_ELIGIBLE_{comp}_EUR" if comp > 0 else "NO_COMPENSATION_DUE"
    }


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "eu261-compensation-calculator"}))
