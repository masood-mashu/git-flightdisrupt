# GitFlightDisrupt Explainability Specification

This document provides a transparent, verifiable architectural breakdown of how **GitFlightDisrupt** operates, processes input, makes decisions, and enforces security boundaries.

---

## 1. Input Data and Data Sources Used

GitFlightDisrupt consumes flight radar schedule telemetry, airline departure and arrival timestamps, airport meteorological reports (METAR), and air traffic control (ATC) ground delay notices. These data sources include scheduled departure times, actual touchdown times, flight distance in kilometers, and passenger ticket class codes. The agent ingests these inputs in raw JSON, XML, and aviation data format and parses them into standardized passenger rights evaluation records for downstream compensation analysis. Montreal Convention baggage liability limits and passenger booking manifests are also monitored as sensitive data sources to ensure passenger rights compliance is strictly maintained.

---

## 2. How It Decides and Reasoning Process

The decision making process follows a deterministic, five-stage analytical pipeline designed to eliminate ambiguity and hallucination. When a flight delay or cancellation incident occurs, the agent first evaluates statutory compensation eligibility using the eu261-compensation-calculator tool based on arrival delay duration and flight flight distance. Next, the reasoning engine invokes the passenger-reroute-optimizer tool to select available replacement flight connections. Furthermore, delayed baggage claims are audited using the baggage-sla-tracker tool. Finally, the agent correlates all aviation metrics against predefined passenger rights regulations to issue a conclusive verdict of APPROVED, BLOCKED, or NEEDS_REVIEW alongside an automated compensation voucher package.

---

## 3. Constraints, Limitations, and Known Issues

GitFlightDisrupt operates under strict operational constraints to prevent false positives and non-deterministic behavior across different agent frameworks. GitFlightDisrupt operates under strict operational constraints to prevent regulatory fines and passenger dissatisfaction across commercial airline operations. The agent is deliberately limited to flight telemetry parsing and statutory compensation calculation and cannot author flight crew scheduling rosters or aircraft maintenance logs. Another known issue and limitation is that complex multi-leg codeshare flights with mixed international carrier legs may require secondary human review rather than autonomous blocking. Furthermore, the agent enforces a low temperature constraint of 0.1 to maintain strict predictability across all supported export frameworks.
