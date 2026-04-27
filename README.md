# BAS Ambulance Service Management Module

This is a comprehensive ERPNext v15 application for managing ambulance service operations.

## Key Features

- **Fleet Management**: Track ambulances, availability, and maintenance.
- **Dispatch Engine**: Intake emergency calls, triage, and dispatch ambulances.
- **Crew Management**: Manage paramedic profiles, certifications, and shifts.
- **Trip Sheets**: Record trip details, patient vitals, and procedures.
- **Billing & Claims**: Automated billing and insurance claim tracking.
- **Compliance Engine**: Automated tracking of vehicle fitness, drug licenses, and staff certifications.
- **Reports & Dashboards**: Analytics for response time, fleet utilization, and revenue.

## Installation

1. Clone this repository into your bench's `apps` folder.
2. Install the app to your site:
   ```bash
   bench get-app https://github.com/your-repo/bas_ambulance
   bench install-app bas_ambulance
   bench migrate
   bench build
   bench restart
   ```

## DocTypes

- Ambulance Master
- Ambulance Station
- Patient Call Record
- Ambulance Trip Sheet
- Crew Member
- Ambulance Maintenance Record
- Ambulance Bill
- Insurance Claim
- Compliance Task
- Incident Report
- Drug & Supply Inventory
- Shift Schedule

## Workflows

1. Dispatch Workflow
2. Trip Workflow
3. Maintenance Workflow
4. Billing Workflow
5. Insurance Claim Workflow
6. Incident Investigation Workflow
7. Compliance Workflow
