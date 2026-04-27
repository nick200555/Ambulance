# BAS Ambulance Service Management Module

This is a comprehensive ERPNext v15 application for managing ambulance service operations, built from the ground up to mirror the BAS Ambulance Service specifications.

## 🚑 Project Overview

The **BAS Ambulance Service Management** module digitizes the end-to-end operations of an ambulance service provider—from patient call intake and dispatch, through ambulance tracking and crew management, to billing, compliance, and fleet maintenance.

## ⚙️ Versions & Dependencies
- **Frappe Framework**: v15.x
- **ERPNext**: v15.x
- **Python**: 3.11+
- **Database**: MariaDB / PostgreSQL

## ✨ Key Features

- **Fleet Management**: Track vehicle identities, equipment, and current operational status.
- **Dispatch Engine**: Real-time intake of emergency calls with triage priority and automated ambulance assignment.
- **Crew & Paramedic Management**: Detailed staff profiles, certifications tracking (BLS, ACLS, PALS), and shift allocation.
- **Operational Trip Sheets**: Lifecycle recording of trips including vitals, procedures, medications, and handover.
- **Billing & Insurance**: Seamless invoice generation linked to trips with insurer-wise claim tracking.
- **Automated Compliance Engine**: 15 pre-seeded templates for vehicle fitness, drug licenses, and training renewals.
- **Incidents & Maintenance**: Track adverse events and vehicle service cycles with automated status updates.
- **Analytics & Reporting**: SLA adherence, fleet utilization, and profitability reports.

## 🛠️ Installation

To install the app on your site:

```bash
bench get-app https://github.com/nick200555/Ambulance.git bas_ambulance
bench --site [your-site-name] install-app bas_ambulance
bench migrate
bench build
bench restart
```

## 📊 Module Architecture

### Main DocTypes
| DocType | Description |
| --- | --- |
| Ambulance Master | Central vehicle registry and equipment checklist |
| Ambulance Station | Base/depot management |
| Patient Call Record | Emergency intake and dispatch trigger |
| Ambulance Trip Sheet | Core operational run sheet |
| Crew Member | Staff profiles and certification tracker |
| Compliance Task | Auto-generated regulatory reminders |
| Insurance Claim | Reimbursement tracking |

### Workflows
- **Dispatch Workflow**: Received -> Dispatched -> En Route -> ... -> Completed
- **Trip Workflow**: Draft -> In Progress -> Pending Review -> Approved -> Billed
- **Compliance Workflow**: Open -> Assigned -> In Progress -> Completed/Overdue

## 📡 API Overview
Whitelisted APIs in `api.py`:
- `dispatch_ambulance()`: Logic for assigning assets.
- `nearest_ambulance_lookup()`: Geo-spatial search for available vehicles.
- `generate_compliance_calendar()`: Internal job for task generation.

---
*Developed as part of the Seria Internship program.*
