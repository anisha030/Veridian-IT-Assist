# 🖥️ Veridian IT Assist — Internal IT Support Agent

**Assignment 2 | Internal Service Agent (IT Support)**

**Name:** Anisha Boken  
**Roll No.:** 23CSU030  
**Company:** Veridian Corp  
**Assignment Week:** 21–25 September 2026

---

## 📖 Overview

**Veridian IT Assist** is a policy-grounded internal IT support agent developed for **Veridian Corp**. The system helps employees get consistent responses to common IT-related requests by analyzing their request and matching it against the supplied **Knowledge Base (KB)** and **Asset Management Policy (AMP)**.

The agent classifies requests into four possible outcomes:

- 🟢 **Resolve** — The request can be handled directly using the available policy.
- 🔵 **Clarify** — More information is required before making a safe decision.
- 🟠 **Route** — The request needs to be handled by IT or another responsible team.
- 🔴 **Escalate** — The request requires immediate or specialized human intervention.

The system also determines whether a **ticket is required**, preventing unnecessary tickets for requests that can be resolved directly or need clarification first.

> **Design Principle:**  
> **Resolve what is safe. Route what requires authority. Escalate what is risky. Ask when information is missing.**

---

## ✨ Features

- 🤖 Policy-based employee request analysis
- 🔍 Automatic request classification
- 🟢 Resolve / 🔵 Clarify / 🟠 Route / 🔴 Escalate decisions
- 📚 Displays the policy source used for each decision
- 🎫 Creates tickets only when human/IT action is required
- 💬 Handles incomplete and ambiguous requests
- 🔐 Escalates security incidents to the Security team
- 📋 Includes a Ticket Queue
- 📖 Includes a Knowledge Base section
- 📝 Includes an Audit Trail
- ⚡ Runs as a standalone web application
- 🧪 Includes Python-based validation tests

---

## 🛠️ Technologies Used

- HTML5
- CSS3
- JavaScript
- Python
- JSON
- Microsoft Edge / Google Chrome / other modern browsers

### Development Tools

- ChatGPT — development assistance, debugging, logic review and documentation
- Python — decision-rule validation and testing
- Browser Developer Tools — HTML/JavaScript testing and debugging

> The final web prototype does **not require an external AI API or LLM** to run.  
> The runtime decision engine uses deterministic, policy-grounded rules.

---

## 📚 Knowledge Base & Sources

The system uses **only the information supplied in the Assignment 2 data pack**.

### Knowledge Base Policies

| Policy | Area |
|---|---|
| **KB-01** | Password Reset |
| **KB-02** | VPN Access |
| **KB-03** | Laptop Replacement |
| **KB-04** | Software Installation |
| **KB-05** | Printer Troubleshooting |
| **KB-06** | Email Mailbox Quota |
| **KB-07** | Guest Wi-Fi Access |
| **KB-08** | Expense Software Access |
| **KB-09** | Security Incident Reporting |
| **KB-10** | Work-From-Home Equipment |
| **AMP** | Asset Management Policy |

### Other Input Data

- **REQ-01 to REQ-15** — Supplied employee requests
- **TK-1042 to TK-1051** — Existing ticket history

> Historical tickets are used as **context and precedent only**. They are not treated as new policies.

---

## 🧠 How It Works

The system follows a simple decision process:

```text
Employee Request
       │
       ▼
Request Analyzer
       │
       ▼
Policy / Decision Engine
       │
       ▼
┌────────────┬────────────┬──────────────┐
│            │            │              │
Resolve    Clarify      Route        Escalate
│            │            │              │
▼            ▼            ▼              ▼
Direct     Ask for      Human/IT       Specialist
Help       Information   Action         Action
                         │              │
                         └──────┬───────┘
                                ▼
                           Create Ticket
                                │
                                ▼
                           Audit Trail
