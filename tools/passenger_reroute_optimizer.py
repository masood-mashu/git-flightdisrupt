"""
passenger_reroute_optimizer.py - Evaluates candidate rebooking flights to ensure departure within 12 hours of canceled flight
"""
import sys
import json


def optimize_reroute(rebooking_data_json: str, max_offset_hours: float = 12.0):
    import json
    data = json.loads(rebooking_data_json) if isinstance(rebooking_data_json, str) else rebooking_data_json
    offset = data.get("candidate_departure_offset_hours", 4.0)
    acceptable = offset <= max_offset_hours
    return {
        "offset_hours": offset,
        "acceptable": acceptable,
        "status": "REBOOKING_OPTION_APPROVED" if acceptable else "EXCESSIVE_REBOOKING_DELAY"
    }


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "passenger-reroute-optimizer"}))
