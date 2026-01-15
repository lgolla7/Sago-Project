# Sago Smart Follow-Up Agent 

## Overview
This repository contains a prototype for the Sago Smart Follow-Up Agent, designed to automate the re-engagement process for private market investors.

It addresses a common workflow gap: investors often meet founders who are "too early," want to follow up later, but miss the timing. This agent actively monitors startup signals and drafts personalized outreach emails when meaningful milestones (e.g., Series A, Product Launch) occur.

## Design Principles
This project strictly adheres to Sago's core design philosophy:
1. **Seamless Integration:** Works via existing email workflows. The investor simply BCCs `track@sago-agent.com` on their rejection email to trigger monitoring.
2. **Hyper-Personalization:** Outreach is tailored to the specific reason the investor originally passed (e.g., revenue traction vs. product readiness).
3. **True Agency:** The system autonomously drafts the email in the user's "Drafts" folder rather than just notifying them.

## 🚀 Features
- **Email Parsing:** Extracts company name, founder details, and "pass reasons" from rejection emails.
- **Signal Monitoring:** (Simulated) Scans external sources for funding rounds and product launches.
- **Relevance Filtering:** Intelligently decides if a news event addresses the investor's specific concerns.
- **Draft Generation:** Writes warm, context-aware re-engagement emails.

## 🛠️ Setup & Installation

### Prerequisites
- Python 3.8+

### Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/lgolla7/Sago-Project](https://github.com/lgolla7/Sago-Project)
   cd sago-agent