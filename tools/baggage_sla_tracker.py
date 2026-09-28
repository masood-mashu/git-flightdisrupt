"""
baggage_sla_tracker.py - Tracks delayed baggage transit days against Montreal Convention compensation threshold
"""
import sys
import json


def track_baggage_sla(delayed_days: int, declaration_loss_days: int = 21):
    is_lost = delayed_days >= declaration_loss_days
    return {
        "delayed_days": delayed_days,
        "declared_lost": is_lost,
        "status": "BAGGAGE_DECLARED_LOST_COMPENSATE" if is_lost else "BAGGAGE_IN_TRANSIT_LOCATE"
    }


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "baggage-sla-tracker"}))
