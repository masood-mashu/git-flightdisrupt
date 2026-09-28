# Segregation of Duties (SOD) Policy: GitFlightDisrupt

This document establishes the role boundaries and segregation of duties for the GitFlightDisrupt agent.

## Role Separation

### 1. Maker
The Maker role is responsible for authoring passenger disruption handling workflows, configuring compensation rule matrices, and preparing automated voucher diffs.
This role cannot approve or merge its own changes into protected flight operations branches.

### 2. Checker
The Checker role is responsible for reviewing, auditing, and validating incoming flight delay records, EU261 claims, and reroute options.
This role operates as an impartial auditor to verify compliance with aviation regulatory and passenger rights benchmarks.

### 3. Approver
The Approver role is strictly reserved for human Airline Operations Directors and Passenger Rights Compliance Officers.
Human approval is required for all mass cancellation compensation releases and extraordinary circumstance exemption overrides.
