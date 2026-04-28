# 📘 BAS Ambulance Service Management System — Standard Operating Procedure (SOP)
### Functional Guide for Ambulance Operations, Fleet & Emergency Response Teams

---

> **Document Version:** 1.0  
> **Application:** BAS Ambulance ERP on ERPNext v15  
> **Audience:** Dispatch Operators, Fleet Managers, Crew Supervisors, Billing Teams, Compliance Officers, Maintenance Teams, Hospital Coordinators, Operations Managers  
> **Support:** support@basambulance.com

---

## 📋 Table of Contents

1. [Getting Started — First Login](#1-getting-started--first-login)
2. [Module 1 — Ambulance Dispatch & Call Management](#2-module-1--ambulance-dispatch--call-management)
3. [Module 2 — Fleet & Ambulance Management](#3-module-2--fleet--ambulance-management)
4. [Module 3 — Crew & Shift Management](#4-module-3--crew--shift-management)
5. [Module 4 — Billing & Insurance Management](#5-module-4--billing--insurance-management)
6. [Module 5 — Compliance & Regulatory Management](#6-module-5--compliance--regulatory-management)
7. [Module 6 — Incident & Emergency Management](#7-module-6--incident--emergency-management)
8. [Module 7 — Reports & Analytics](#8-module-7--reports--analytics)
9. [Daily / Weekly / Monthly Operating Checklist](#9-daily--weekly--monthly-operating-checklist)
10. [User Roles & Who Does What](#10-user-roles--who-does-what)
11. [Frequently Asked Questions](#11-frequently-asked-questions)
12. [Support & Contact](#12-support--contact)

---

## 1. Getting Started — First Login

### 1.1 Access the Application

1. Open your browser and go to your BAS Ambulance URL:  
   `https://ambulance.yourdomain.org`
2. Login with your ERPNext credentials (provided by your administrator).
3. On the left sidebar, click the **Ambulance Service** workspace.
4. You will see the **BAS Ambulance Dashboard** with 4 quick-access shortcuts at the top:
   - 🔴 Active Emergencies
   - 🔵 Fleet Availability
   - 🟢 Active Trip Live Monitoring
   - 🟣 Compliance Score

---

### 1.2 Initial Company Setup (One-Time — Admin Only)

> **Who does this:** Operations Admin or System Administrator (first time only)

| Step | Action | Where |
|---|---|---|
| 1 | Create your Branch/Company | ERPNext → Accounting → Company |
| 2 | Add Ambulance Stations | Ambulance Service → Infrastructure → Ambulance Station |
| 3 | Seed the Initial Fleet Data | Ambulance Service → Fleet → Ambulance Master |
| 4 | Run Demo Data (optional) | `bench execute bas_ambulance.setup.demo.run` |

---

### 1.3 Assign User Roles

> **Who does this:** Administrator

Go to **ERPNext → HR → User** and assign each person their role:

| Role | Assign To |
|---|---|
| Dispatch Operator | Control Room Staff / Call Handlers |
| Fleet Manager | Fleet Operations & Garage Head |
| Crew Supervisor | Shift Lead / Paramedic In-Charge |
| Billing Executive | Finance / Insurance Desk |
| Compliance Officer | Legal and Regulatory Desk |
| Operations Admin | Operations Managers / Admins |

---

## 2. Module 1 — Ambulance Dispatch & Call Management

> **Purpose:** Never waste seconds during an emergency. Ensure fastest closest vehicle allocation, track active trip states, and coordinate hospitals.

---

### 2.1 SOP — Patient Emergency Call Registration

**Who:** Dispatch Operator  
**When:** Whenever a distress call is received on emergency line

| Step | Action |
|---|---|
| 1 | Go to **Ambulance Dispatch → Patient Call Record** |
| 2 | Click **+ New** |
| 3 | Enter **Caller Name** and **Phone Number** |
| 4 | Set **Priority Level** (Critical / High / Medium / Low) |
| 5 | Fill in **Pickup Location** and (if known) **Drop-off Hospital** |
| 6 | Select **Required Equipment** (ALS / BLS / Incubator / Oxygen) |
| 7 | Click **Save** |

✅ **Expected Result:** Call is logged and mapped immediately for nearest vehicle matching parameters.

---

### 2.2 SOP — Nearest Ambulance Allocation & Dispatch

**Who:** Dispatch Operator  
**When:** After saving a new Patient Call Record

| Step | Action |
|---|---|
| 1 | Open the **Patient Call Record** recently created |
| 2 | System will display a list of nearest available vehicles under **Nearest Stations** |
| 3 | Select an available **Ambulance Master** from the suggestions list |
| 4 | Click the **Create Trip** button |
| 5 | An **Ambulance Trip Sheet** is generated. Confirm assigned **Shift Schedule** (Crew). |
| 6 | Change Status to **Allocated** and Save. |

✅ **Expected Result:** A Trip Sheet is created. The Driver and Paramedic are notified on their mobile devices to begin the journey.

---

### 2.3 SOP — Trip Live Monitoring & Status Updates

**Who:** Dispatch Operator / Crew Supervisor  
**When:** While an ambulance is on active deployment

**The 6 Trip Workflow Stages:**

```
Dispatched ──► En Route to Patient ──► At Scene ──► En Route to Hospital ──► Hospital Reached ──►┬── Completed ✅
                                                                                                 └── Cancelled ❌
```

**How to Update Status:**

| Step | Action |
|---|---|
| 1 | Crew / Driver opens **Ambulance Trip Sheet** on their tablet |
| 2 | Clicks action buttons: `En Route`, `Arrival at Scene`, `Departure from Scene`, `Arrival at Destination` |
| 3 | Ensure to hit **Save** to stamp the timestamp |
| 4 | Operations Manager/Dispatch continues monitoring via the **Live Trip Monitoring** dashboard |

---

### 2.4 SOP — Trip Closure

**Who:** Crew Supervisor / EMT  
**When:** After patient handoff is successfully done at destination

| Step | Action |
|---|---|
| 1 | Open the active **Ambulance Trip Sheet** |
| 2 | Set status as **Completed** |
| 3 | Enter **End Odometer Reading** |
| 4 | Add closing notes or patient handoff signatures under **Notes** |
| 5 | Save to close trip |

✅ **Expected Result:** The ambulance is released back into the available fleet pool, visible on the availability dashboard.

---

## 3. Module 2 — Fleet & Ambulance Management

> **Purpose:** Maintain maximum up-time for all assets. Ensure valid MOT/inspections, correct supply of drugs, and zero un-managed downtime.

---

### 3.1 SOP — Ambulance Registration & Setup

**Who:** Fleet Manager  
**When:** Upon purchasing/leasing a new ambulance

| Step | Action |
|---|---|
| 1 | Go to **Fleet Management → Ambulance Master** |
| 2 | Click **+ New** |
| 3 | Fill in **Registration Number**, **Chassis Number**, **Engine Number** |
| 4 | Set **Ambulance Type** (e.g. ALS, BLS, Neonatal, Patient Transport) |
| 5 | Link it to the base **Ambulance Station** |
| 6 | Fill initial **Current Odometer** reading |
| 7 | Save |

✅ **Expected Result:** Ambulance is registered in ERPNext and becomes available for assigning. 

---

### 3.2 SOP — Drug & Supply Inventory Check

**Who:** Paramedic / EMT  
**When:** At the start of every shift

| Step | Action |
|---|---|
| 1 | Go to **Drug & Supply Inventory** |
| 2 | Click **+ New** |
| 3 | Select your **Ambulance Master** |
| 4 | Conduct visual check. Log the items present vs required limits (Oxygen Cylinders, AED pads, Adrenaline, IV strings) |
| 5 | Submit restock request if anything falls below threshold |
| 6 | Save |

---

### 3.3 SOP — Ambulance Maintenance & Handling Downtime

**Who:** Fleet Manager / Driver  
**When:** Routine vehicle servicing, scheduled repair, or sudden failure

| Step | Action |
|---|---|
| 1 | Go to **Fleet Management → Ambulance Maintenance Record** |
| 2 | Click **+ New** |
| 3 | Select **Ambulance Master** |
| 4 | Enter **Maintenance Reason** (Routine / Breakdown) |
| 5 | Under **Ambulance Master**, change Status to **Under Maintenance** |
| 6 | Save |
| 7 | *Once Fixed*: Open **Maintenance Record**, log the work done and costs, update status to **Completed**. |
| 8 | Re-set **Ambulance Master** back to **Available**. |

✅ **Expected Result:** During the downtime period, the ambulance will not appear as an allocatable asset in the dispatch screen, preventing mis-deployments.

---

## 4. Module 3 — Crew & Shift Management

> **Purpose:** Assign right trained people to the correct rigs, ensure no fatigue or skipped shifts, track certification expiries accurately.

---

### 4.1 SOP — Crew Onboarding & Certification Check

**Who:** Operations Admin / Crew Supervisor  
**When:** When making a new hire (Paramedic, EMT, Driver)

| Step | Action |
|---|---|
| 1 | Go to **Crew & Shift Management → Crew Member** |
| 2 | Click **+ New** |
| 3 | Enter **Name**, **Contact Number**, and **Role** (Driver / Paramedic / Doctor) |
| 4 | In the certifications table, add entries for **BLS**, **ACLS**, **Driving License** |
| 5 | Enter the exact **Expiry Dates** for each certification |
| 6 | Attach scanned copies directly on the record |
| 7 | Save |

✅ **Expected Result:** The scheduler runs daily and will issue alerts 30 days before any certification expires.

---

### 4.2 SOP — Shift Scheduling & Assignment

**Who:** Crew Supervisor  
**When:** Weekly or monthly (depending on agency policy)

| Step | Action |
|---|---|
| 1 | Go to **Shift Schedule** |
| 2 | Click **+ New** |
| 3 | Select **Shift Date Date**, **Shift Start Time** and **Shift End Time** |
| 4 | Select **Ambulance Station** and allocated **Ambulance Master** vehicle |
| 5 | Add multiple rows for assigned **Crew Members** to this specific shift/vehicle |
| 6 | Change Status to **Published** |
| 7 | Save |

✅ **Expected Result:** Crew members are assigned rigorously to specific rigs and are marked as "Active duty" when shift commences.

---

### 4.3 SOP — Emergency Replacement Assignment

**Who:** Crew Supervisor  
**When:** Call-out or unexpected sickness from a crew member

| Step | Action |
|---|---|
| 1 | Open the **Shift Schedule** for the current day |
| 2 | Re-assign the substitute by deleting the absent crew member row and adding the new **Crew Member** |
| 3 | Alert the replacement via System Note or WhatsApp integration |
| 4 | Save the change |

---

## 5. Module 4 — Billing & Insurance Management

> **Purpose:** Standardize emergency cash and corporate billing, manage insurance settlements smoothly to prevent revenue leakage.

---

### 5.1 SOP — Trip Cash/Emergency Bill Generation

**Who:** Billing Executive  
**When:** End of the trip for direct-pay cases

| Step | Action |
|---|---|
| 1 | Go to **Ambulance Bill → + New** |
| 2 | Select the completed **Ambulance Trip Sheet** |
| 3 | The system auto-fetches Start/End Odometers and distance. Base rate is calculated automatically. |
| 4 | Add any **Consumables Used** (Oxygen per hour, emergency drugs injected) |
| 5 | Check **Total Amount** |
| 6 | Save and **Submit** |
| 7 | Collect payment / generate receipt |

---

### 5.2 SOP — Insurance Claim Creation Workflow

**Who:** Billing Executive  
**When:** Patient coverage provides direct billing to their PPO or Gov Insurance

| Step | Action |
|---|---|
| 1 | Ensure the **Ambulance Bill** is created under standard rates, but left unpaid by patient. |
| 2 | Go to **Insurance Claim → + New** |
| 3 | Link the **Ambulance Bill** and **Patient Call Record** |
| 4 | Fill out **Insurance Provider**, **Policy ID**, and **Claim Amount** |
| 5 | Attach the required proofs: Run form, Patient ID, Trip Sheet PDF |
| 6 | Set status to **Claim Submitted** and enter submission date |
| 7 | Save |

---

### 5.3 SOP — Resolving an Insurance Claim Settlement

**Who:** Billing Team / Finance  
**When:** The payer sends their settlement check/wire

| Step | Action |
|---|---|
| 1 | Open the pending **Insurance Claim** |
| 2 | Change Status to **Settled** |
| 3 | Fill in the **Settlement Amount Received** |
| 4 | If the payer paid less than billed, write off the variance to allowances via linked Journal Entry |
| 5 | Mark the underlying **Ambulance Bill** as Paid |

---

## 6. Module 5 — Compliance & Regulatory Management

> **Purpose:** Ensure standard operations without regulatory disruptions by managing RTO docs, drug licenses, and safety constraints.

---

### 6.1 SOP — Setup Compliance Permits & Hydo-Testing Tracker

**Who:** Compliance Officer  
**When:** During initial vehicle onboarding or as new periodic compliance laws appear

| Step | Action |
|---|---|
| 1 | Go to **Compliance Task** |
| 2 | Click **+ New** |
| 3 | Fill **Task Name**: e.g., "O2 Cylinder Hydro Testing - AMB-001" |
| 4 | Select **Ambulance Master** linked |
| 5 | Set **Compliance Type**: Oxygen Cylinder / Fitness Certificate / RTO Permit |
| 6 | Select **Due Date** |
| 7 | Set **Status** to **Upcoming** |
| 8 | Save |

> **Automated Reminders:** Reminders are configured automatically for permits dropping under 30 days.

---

### 6.2 SOP — Mark a Compliance Action Complete

**Who:** Fleet Manager / Compliance Officer  
**When:** Once the inspection or renewal fee is paid

| Step | Action |
|---|---|
| 1 | Open the impending **Compliance Task** |
| 2 | Change Status to **Completed** |
| 3 | Enter **Completion Date** |
| 4 | Attach PDF receipt, clear test log, or newly updated license document |
| 5 | Next, set up the _next_ cycle's compliance task (System allows duplication of record and bumping the date by +1yr) |
| 6 | Save |

---

## 7. Module 6 — Incident & Emergency Management

> **Purpose:** Properly manage any accident, complaint, or delay that threatens patient safety and brand reputation.

---

### 7.1 SOP — Report an Accident / Vehicle Incident

**Who:** Ambulance Driver / Paramedic  
**When:** Vehicle is involved in a collision or unexpected hazard occurs

| Step | Action |
|---|---|
| 1 | Provide immediate patient safety handoff / dispatch alternate vehicle first. |
| 2 | Open **Incident Report** on mobile or tablet |
| 3 | Click **+ New** |
| 4 | Select **Incident Type**: Vehicle Accident |
| 5 | Select **Ambulance Master** and **Trip Sheet** linked |
| 6 | Describe the incident, upload photos of the vehicle via camera access |
| 7 | Identify if injuries occurred (Yes/No) |
| 8 | Submit |

✅ **Expected Result:** SMS/System Alert sent to Fleet Manager and Operations Admin immediately.

---

### 7.2 SOP — Investigate & Close an Incident

**Who:** Operations Manager  
**When:** Post incident debriefing

| Step | Action |
|---|---|
| 1 | Review the submitted **Incident Report** |
| 2 | Fill the **Root Cause Analysis (RCA)** field |
| 3 | Identify **Corrective Action** (e.g. Mandatory retraining or mechanical fix) |
| 4 | Once actions are taken, change Status to **Resolved** |
| 5 | Document the closure and save. |

---

## 8. Module 7 — Reports & Analytics

Examine the core components of the BAS Intelligence module:

1. **Response Time Analysis Report**: Evaluates time between Patient Call Record logging and 'En-Route' timestamp.
2. **Dashboard — Fleet Utilization Dashboard**: Real-time representation of how many of total fleet units are active, dispatched, maintenance, or idle.
3. **Revenue vs Effort Analytics**: Number of billable trips, cash vs corporate, distance normalized revenue metric.
4. **Compliance Ageing Report**: Shows the count of vehicles operating with expired or near-expiring validations.
5. **Crew Certification Expiry Dashboard**: Visual flags on paramedics out of standard BLS/ACLS compliance guidelines.

---

## 9. Daily / Weekly / Monthly Operating Checklist

### 9.1 Daily

| Task | Who | Where |
|---|---|---|
| ☐ Review oxygen / drug baseline checks for all active vehicles | Paramedic / Fleet | Drug & Supply Inventory |
| ☐ Review dispatch queue to ensure 0 open stale calls | Dispatcher | Patient Call Record |
| ☐ Check daily active trip live statuses | Operations Admin | Trip Dashboard |
| ☐ Review billing settlements from yesterday's trips | Billing | Ambulance Bill |

### 9.2 Weekly

| Task | Who | Where |
|---|---|---|
| ☐ Review Incident Reports & corrective actions | Operations Admin | Incident Report |
| ☐ Plan next week's shift schedule | Crew Supervisor | Shift Schedule |
| ☐ Perform routine multi-point mechanical review on idle assets | Fleet Manager | Ambulance Maintenance |
| ☐ Review open insurance claims outstanding | Billing | Insurance Claim |

### 9.3 Monthly

| Task | Who | Where |
|---|---|---|
| ☐ Monthly invoice cycle & corporate billing dispatch | Billing | Ambulance Bill |
| ☐ Audit all upcoming vehicle/crew compliances | Compliance | Compliance Task |
| ☐ Review overall fleet utilization metric % | Ops Admin | Reports |
| ☐ Reconcile fuel consumptions | Fleet Manager | Fleet Sub-System |

---

### 9.4 Quarterly

| Task | Who | Where |
|---|---|---|
| ☐ Advanced equipment calibration review (Defibrillators) | Fleet Manager | Ambulance Maintenance |
| ☐ Station Performance audits (Response times comparison) | Ops Admin | Reports |
| ☐ Mandatory periodic driving & safety courses (audit list) | HR/Supervisor | Crew Member |

---

### 9.5 Annual

| Task | Who | Where |
|---|---|---|
| ☐ Annual medical fitness cert renewals for crew | HR/Supervisor | Crew Member |
| ☐ Renew fleet insurance & road permits | Compliance | Compliance Task |
| ☐ Ambulance depreciation & replacement planning | Finance/Ops | Assets / Fleet Master |

---

## 10. User Roles & Who Does What

| Feature | Operations Admin | Dispatch Operator | Crew Supervisor | Fleet Manager | Billing Executive | Compliance Officer |
|---|---|---|---|---|---|---|
| Patient Call Record | 👁 Read | ✅ Full | 👁 Read | ❌ | ❌ | ❌ |
| Ambulance Trip Sheet | 👁 Read | ✅ Full | ✅ Full | 👁 Read | 👁 Read | ❌ |
| Ambulance Master | ✅ Full | 👁 Read | 👁 Read | ✅ Full | ❌ | 👁 Read |
| Maintenance Record | 👁 Read | ❌ | ❌ | ✅ Full | ❌ | 👁 Read |
| Drug & Inventory | 👁 Read | ❌ | ✅ Full | ✅ Full | ❌ | ❌ |
| Shift Schedule | 👁 Read | 👁 Read | ✅ Full | 👁 Read | ❌ | ❌ |
| Ambulance Bill/Claim | 👁 Read | ❌ | ❌ | ❌ | ✅ Full | ❌ |
| Compliance Task | 👁 Read | ❌ | ❌ | ✅ Edit | ❌ | ✅ Full |
| Incident Report | ✅ Full | 👁 Read | ✅ Full | ✅ Edit | ❌ | ✅ Edit |

---

## 11. Frequently Asked Questions

**Q1: The ambulance isn't showing up as available on the dispatch map. How do I fix this?**  
A: Go to the **Ambulance Master** document and check its status. If it is marked as 'Under Maintenance' or assigned to an active 'Allocated' trip that has not been Closed, it will not appear as available. Update statuses correctly to return it to the pool.

---

**Q2: What happens if an insurance claim is rejected?**  
A: Open the **Insurance Claim**, mark the status as 'Rejected' and assign a follow-up date for appeals, or revert the billing structure back to the originating Patient/Responsible Party with an outstanding **Ambulance Bill**.

---

**Q3: How do I escalate a patient emergency call if no fleet units are near?**  
A: Use the "Escalate" level on the Patient Call Record. This signals the system to pull off units from minor transfers or non-emergencies (low priority calls), notifying them immediately to divert. Operations are also SMS notified.

---

**Q4: A crew member's BLS certification is marked expired in the system. Can I still assign them?**  
A: A system warning will trigger. While overridden globally by Admin configuration, practically, paring scheduling protocols prevents adding to the **Shift Schedule** dynamically. Request the paramedic renew immediately.

---

**Q5: We closed an incident report but realized more damages. How do I reopen it?**  
A: Operations Admin must navigate to the **Incident Report**, hit "Reopen" via the actions dropdown, append the new damages, complete further RCA documentation, and re-Resolve.

---

**Q6: Oxygen cylinder hydrostatic testing is overdue. How does the system handle this?**  
A: The **Compliance Task** related to that cylinder batch changes to 'Red/Overdue'. Fleet Managers receive automated notifications, urging immediate cycling out of those specific tanks to the testing vendor.

---

**Q7: A cash payment for a completed trip isn't reflected on the revenue report. Why?**  
A: The **Ambulance Bill** must be marked 'Paid' via a linked recorded Payment Entry in ERPNext. Simply creating the bill leaves it as 'Unpaid / Draft'.

---

**Q8: How does system compute Dispatch Priority?**  
A: Based on standard logic tied to the Call Record input. Critical defaults to 'Alpha-tier dispatch', moving other operations down. It evaluates time distance and specific equipment requests (e.g. neonatal). 

---

**Q9: How is 'Response Time' technically calculated in the backend?**  
A: Measured universally as: _Time Logged (Patient Call Created)_ to _Time Stamped (Dispatch En-Route updated on Trip Sheet)_. Any duration extending set parameters degrades the target KPI in the Reports.

---

**Q10: How to pause automatic scheduling due to sudden mechanical downtime?**  
A: Create an **Ambulance Maintenance Record** with status "Under Breakdown". This systematically hides the vehicle from all prospective Shift Schedule mappings until "Completed".

---

**Q11: We have a no-show crew member for a 12 hour shift. How do I assign backup?**  
A: Go directly into the live **Shift Schedule**, remove the Absent member row, input the Backup **Crew Member** row, and hit save. This updates payroll and log parameters.

---

**Q12: Is there a unified way to just export ALL trip bills for end-of-month corporate hospital audits?**  
A: Yes. Navigate to Ambulance Bill list view, filter by 'Corporate' customer and Date Range, drop down the 'Menu' button top-right, and select 'Export Data' to CSV/Excel.

---

**Q13: A settled insurance check didn't cover the full claim. How to handle the variance?**  
A: Mark **Insurance Claim** as 'Settled', enter actual value received. Instruct Finance to route the remainder to 'Insurance Variance Write Off' ledgers via Journal Entry.

---

**Q14: How are compliance reminders actually delivered?**  
A: Governed by the backend scheduler via ERPNext's Notification rules. Automatically pushes emails/system alerts at limits (30 days before / Date of / Overdue). Ensure Compliance Task dates are right.

---

**Q15: How can a manager view raw data of overall utilization to demonstrate efficiency to stakeholders?**  
A: Access 'Fleet Utilization Dashboard' inside the Reports Module, presenting visual bar charts reflecting Idle, Transit, Scene, Maintenance, and Station times mapped cumulatively.

---

## 12. Support & Contact

| Channel | Details |
|---|---|
| 📧 Email | support@basambulance.com |
| 📖 Documentation | https://docs.basambulance.com |
| 🐛 Bug Reports | https://github.com/seriainternship/bas_ambulance/issues |
| 📱 Operations Hotline | +91-XXXXXXXXXX (BAS Dispatch Escalation) |

---

*© 2026 BAS Ambulance Services — Empowered Emergency Response*  
*Powered by Frappe Framework & ERPNext v15*
