# Disaster Recovery Module: Stakeholder Cards

**Version:** 2.1 - Balanced & Refined Edition
**Last Updated:** October 2025

---

## Overview

**Stakeholder Cards** represent the key groups affected by a data breach. Each stakeholder has trust/satisfaction level (0-100%) that changes based on team actions. Stakeholders can escalate if not managed (causing additional Events and budget costs).

- **Total Cards:** 5 (STAKE-01 to STAKE-05)
- **Used In:** Disaster Recovery module (governance during crisis)
- **Tracking:** Each stakeholder has Trust Meter (0-100%)
- **Purpose:** Manage stakeholder relationships while responding to breach

---

## Stakeholder Cards

### STAKE-01: Customers
**Stakeholder Type:** External
**Primary Concern:** Data privacy and service availability
**Trust Meter:** Starts at 50%
**Escalation:** Trust drops 10% per turn if no communication; critical at <20%

**Description:**
The customers whose data was breached. They want to know:
- What data was accessed
- Whether it was encrypted
- What they should do (change password, watch credit)
- Whether the company is protecting them
- Whether to switch providers

**Behavior:**
- **High Trust (70%+):** Continue using service, minor PR impact
- **Medium Trust (40-70%):** Some customer loss, but company is "handling it"
- **Low Trust (<40%):** Customer exodus, lawsuits, regulatory investigation
- **Critical (<20%):** Mass churn, bankruptcy risk, acquisition/collapse

**What Affects Trust:**
- **Increases Trust:**
  - Customer Notification (ACTION-09): +15%
  - Public statement about patch/fix: +5%
  - Free credit monitoring offer: +10%
  - Quick response time: +5% per turn if investigating

- **Decreases Trust:**
  - No communication: -10% per turn
  - Media reports breach before notification: -20%
  - Delayed response: -5% per turn
  - Second breach during response: -30%
  - "No comment" from company: -15%

**Win Condition:**
- Keep customer trust above 30% to avoid game loss
- Ideally maintain above 50% for positive outcome

**Lose Condition:**
- Customer trust drops to 0% = company collapse
- Mass lawsuits filed
- Company bankruptcy/acquisition

**Crisis Actions That Help:**
- ACTION-09 (Customer Notification): +15% trust
- ACTION-11 (Media Management): +10% trust
- Any remediation action that shows progress: +2-5%

**Special Events:**
- If trust drops too low, class action lawsuit filed (see Event Cards)
- If trust stays high, customer retention and recovery possible
- Media coverage affects customer trust (see Stakeholder: Media)

---

### STAKE-02: Regulators
**Stakeholder Type:** Government/Legal
**Primary Concern:** Compliance with breach notification laws
**Trust Meter:** Starts at 60%
**Escalation:** Drops 15% if not notified within required timeframe; fines assessed

**Description:**
Government agencies that regulate data privacy:
- State attorneys general (breach notification laws)
- Federal regulators (healthcare, financial, etc.)
- International regulators (GDPR if any EU customers)
- Law enforcement (FBI, Secret Service)

**Behavior:**
- **High Confidence (70%+):** Voluntary cooperation, no penalties
- **Medium Confidence (40-70%):** Investigation, possible fines
- **Low Confidence (<40%):** Aggressive investigation, significant fines
- **Critical (<20%):** Criminal prosecution, company shut down

**What Affects Regulatory Confidence:**
- **Increases Confidence:**
  - Regulatory Notification (ACTION-10): +20%
  - Prompt customer notification: +10%
  - Third-party incident response (ACTION-04): +15%
  - Forensics evidence: +10%
  - Proactive remediation: +5%

- **Decreases Confidence:**
  - Missing notification deadline: -30%
  - No investigation: -20%
  - Hiding breach information: -50%
  - Similar breach before (poor history): -10%
  - Inadequate response: -15%

**Regulatory Requirements Vary:**
- **California CCPA:** Notification within "without unreasonable delay"
- **GDPR:** Notification within 72 hours (EU)
- **HIPAA:** Notification within 60 days (healthcare)
- **State Laws:** Usually 30-60 days, varies by state
- **Sector-Specific:** Finance, healthcare have stricter rules

**Win Condition:**
- Maintain regulatory confidence above 50%
- Comply with notification requirements
- Avoid major fines (100K-millions range)

**Lose Condition:**
- Regulatory confidence drops to 0% = company penalty
- Major fines (potentially 10-20% of company revenue)
- Criminal prosecution possible
- Company license revoked (in regulated sectors)

**Crisis Actions That Help:**
- ACTION-10 (Regulatory Notification): +20% confidence
- ACTION-04 (Third-party IR): +15% confidence
- ACTION-05, ACTION-07 (Remediation): +5-10%

**Special Events:**
- If notification deadline missed: Regulatory Penalty Event
- If confidence drops too low: Fine Assessment Event
- If properly handled: Regulatory Cooperation Event (reduced penalties)

---

### STAKE-03: Media / Public
**Stakeholder Type:** External / Communication
**Primary Concern:** Newsworthy story (bigger = bigger problem)
**Trust Meter:** Starts at 40% (media is naturally skeptical)
**Escalation:** Escalates based on company response quality

**Description:**
Media outlets, journalists, bloggers, social media. Media decides whether breach is:
- Small tech story (1 article)
- Major business news (multiple outlets, days)
- National news (major outlets, weeks)
- International scandal (global coverage)

**Behavior:**
- **Positive Coverage (70%+):** "Company handled breach well", trust maintained
- **Neutral Coverage (40-70%):** Matter-of-fact reporting, some concern
- **Negative Coverage (<40%):** "Company slow to respond", "Cover-up suspected"
- **Scandal (<20%):** Major negative coverage, "Company failed customers"

**What Affects Media Coverage:**
- **Positive Factors:**
  - Proactive media statement (ACTION-11): +20%
  - Quick notification (within 24-48 hours): +15%
  - CEO takes responsibility: +10%
  - Transparent communication: +10%
  - Third-party validation: +5%

- **Negative Factors:**
  - "No comment" response: -30%
  - Delayed notification (discovered by media): -40%
  - Executives dodge reporters: -25%
  - Defensive response: -20%
  - Multiple breaches: -30%

**Media Impact on Business:**
- Positive media → customers stay, suppliers trust company
- Negative media → customers leave, stock price drops, suppliers question
- Scandal media → business collapse possible, bankruptcy risk

**Win Condition:**
- Maintain media trust above 40%
- Frame narrative as "company handled responsibly"
- Minimize negative coverage

**Lose Condition:**
- Media presents company as negligent/criminal
- Social media amplifies negative narrative
- Stock price crashes (if public company)
- Consumer boycott possible

**Crisis Actions That Help:**
- ACTION-11 (Media Management): +20% coverage
- ACTION-09 (Customer Notification): +5% (transparency)
- ACTION-12 (Board Communication): +5% (if credible)

**Special Events:**
- If company is silent: "Media Frenzy" Event (increased coverage)
- If company responds well: "Positive Coverage" Event (mitigates damage)
- If executives hide: "Cover-up Narrative" Event (major damage)

---

### STAKE-04: Board of Directors
**Stakeholder Type:** Internal / Governance
**Primary Concern:** Company liability and fiduciary duty
**Trust Meter:** Starts at 70% (board is inherently supportive initially)
**Escalation:** Drops if response is inadequate; may fire CEO

**Description:**
Board of directors (and C-level executives if private company). Board must:
- Fulfill fiduciary duty to shareholders
- Authorize major spending (crisis response can be very expensive)
- Decide on disclosure (SEC rules if public)
- Decide on executives' future (fire/retain CEO)
- Manage shareholder relationships

**Behavior:**
- **High Confidence (70%+):** Board is supportive, authorizes spending, defends executives
- **Medium Confidence (40-70%):** Board is questioning, scrutinizes spending, considers changes
- **Low Confidence (<40%):** Board is critical, may fire CEO, considers restructuring
- **Critical (<20%):** Board votes to remove management, sell company, or file bankruptcy

**What Affects Board Confidence:**
- **Increases Confidence:**
  - Board Notification (ACTION-12): +20%
  - Professional incident response: +15%
  - Quick containment: +10%
  - Good regulatory relationship: +10%
  - Transparent communication: +5%

- **Decreases Confidence:**
  - Lack of incident response plan: -20%
  - Slow response: -10% per turn
  - Inadequate budget allocation: -15%
  - Executive hiding information: -40%
  - Multiple breaches: -30%

**Board Decision Points:**
- **Turn 3:** First board meeting (ACTION-12 happens)
  - Board decides if CEO retains confidence
  - Major spending approvals (forensics, lawyers, PR)
  - Disclosure decisions

- **Turn 5:** Mid-crisis assessment
  - Board may fire CEO (if confidence <40%)
  - Shareholder communication
  - Restructuring decisions

- **Turn 7:** End-game assessment
  - Board decides if company survives
  - Long-term damage control
  - Leadership changes finalized

**Win Condition:**
- Maintain board confidence above 50%
- Board authorizes necessary spending
- Executives retain their positions
- Company survives intact

**Lose Condition:**
- Board confidence drops to 0% = CEO fired
- Shareholder lawsuits
- Company forced to sell
- Bankruptcy filing possible

**Crisis Actions That Help:**
- ACTION-12 (Board Notification): +20% confidence
- ACTION-04 (Third-party IR): +15% (shows professional response)
- ACTION-01, ACTION-07 (Forensics/Rebuild): +5-10%

**Special Events:**
- Turn 3: Board Meeting Event (first assessment)
- If confidence drops low: "CEO Removed" Event (new CEO, game becomes harder)
- If well-managed: "Board Confidence Maintained" Event (positive modifier)

---

### STAKE-05: Executive Leadership
**Stakeholder Type:** Internal / Management
**Primary Concern:** Job security and company survival
**Trust Meter:** Starts at 80% (executives are naturally supportive initially)
**Escalation:** Drops if response is chaotic; may resign or sabotage

**Description:**
C-level executives (CEO, CTO, CFO, CISO, General Counsel) who must:
- Make critical decisions under pressure
- Coordinate crisis response
- Handle media inquiries
- Present to board
- Ensure company continues operating
- Manage their own careers/reputations

**Behavior:**
- **High Morale (70%+):** Executives are focused, coordinated, decisive
- **Medium Morale (40-70%):** Executives are stressed, some disagreements, slower decisions
- **Low Morale (<40%):** Executives may resign, infighting, poor decisions
- **Critical (<20%):** Executive exodus, chaos, no leadership

**What Affects Executive Morale:**
- **Increases Morale:**
  - Clear incident response plan: +15%
  - Professional guidance (consultants): +10%
  - Regular communication/updates: +5% per turn
  - Board support: +10%
  - Progress on containment: +5%

- **Decreases Morale:**
  - No response plan: -20%
  - Chaotic response: -10% per turn
  - Board criticism: -15%
  - Media attacks: -10%
  - Regulatory fines: -15%

**Executive Departures Risk:**
- If morale drops too low, key executives resign
- Each resignation removes their expertise from future decisions
- Replacement executives are less effective initially
- Crisis becomes harder to manage

**Win Condition:**
- Maintain executive morale above 50%
- Prevent key executive resignations
- Executives remain focused on response
- Company leadership stays intact

**Lose Condition:**
- Key executives resign (cascading departures)
- Leadership vacuum causes chaos
- Crisis response deteriorates
- Company collapses

**Crisis Actions That Help:**
- Regular communication: +5% per turn
- Professional response team: +10%
- Regulatory/customer progress: +5%
- Board confidence: +10%

**Special Events:**
- If morale drops low: "Executive Resignation" Event (key person leaves)
- If morale stays high: "Leadership United" Event (positive coordination bonus)
- Media attacks on executives: Morale drop (-10%)

---

## Stakeholder Summary

| Stakeholder | Type | Start Trust | Critical Level | Primary Actions |
|------------|------|------------|-----------------|-----------------|
| Customers | External | 50% | <20% | ACTION-09 (notify), ACTION-11 (PR) |
| Regulators | Government | 60% | <20% | ACTION-10 (notify), ACTION-01/04 (forensics) |
| Media | External | 40% | <20% | ACTION-11 (PR), ACTION-09 (transparency) |
| Board | Internal | 70% | <40% | ACTION-12 (notify), ACTION-04 (guidance) |
| Executives | Internal | 80% | <40% | Regular communication, success indicators |

---

## Gameplay Strategy

### Multi-Stakeholder Management

Teams must balance managing five competing stakeholder groups:

**Prioritization Strategy 1: External First**
- Focus on Customers and Media
- Maintain public trust
- Regulators will follow
- Risk: Internal management gets neglected

**Prioritization Strategy 2: Internal First**
- Focus on Board and Executives
- Maintain leadership confidence
- Internal team makes better decisions
- Risk: External stakeholders (customers, media) get neglected

**Prioritization Strategy 3: Balanced**
- Do some actions for each stakeholder group
- Distribute budget across all notifications
- More complex but sustainable
- Risk: Medium progress on all, complete on none

**Prioritization Strategy 4: Targeted**
- Identify critical stakeholder (maybe regulators)
- Focus budget there
- Neglect others
- Risk: Single stakeholder collapse

### Stakeholder Interactions

Stakeholders influence each other:
- **Media → Customers:** If media says "company hid breach", customers distrust (stack penalties)
- **Regulators → Customers:** If regulator fines company, customers see company as unsafe
- **Board → Executives:** If board removes CEO, executives lose confidence
- **Executives → Board:** If executives resign, board loses confidence in response
- **Customers → Stock Price:** If customer trust drops, stock price drops (affects Board decisions)

---

## Escalation Mechanics

Each stakeholder has escalation triggers:

### Customers Escalate If:
- Not notified within 48-72 hours
- Trust drops below 20%
- Learn about breach from media before company notification
- **Escalation:** Class action lawsuit filed (see Event Cards)

### Regulators Escalate If:
- Not notified within legal deadline (30-60 days)
- No investigation underway
- Company appears to be hiding information
- **Escalation:** Regulatory fine assessed, investigation launched

### Media Escalates If:
- Company is silent ("no comment")
- Executives dodge reporters
- Social media discovers negative information
- **Escalation:** Media frenzy (negative coverage spiral)

### Board Escalates If:
- Response is inadequate or chaotic
- Board confidence drops below 40%
- CEO loses control
- **Escalation:** Board votes to remove CEO

### Executives Escalate If:
- Morale drops too low
- Key executives receive personal blame
- Career prospects look bad
- **Escalation:** Executive resignations, leadership void

---

## Print Instructions

1. Print on cardstock (250 gsm minimum)
2. Color-code by stakeholder type:
   - **Blue (External):** STAKE-01 (Customers), STAKE-03 (Media)
   - **Red (Internal):** STAKE-04 (Board), STAKE-05 (Executives)
   - **Purple (Government):** STAKE-02 (Regulators)
3. Include trust meter on each card (0-100% indicator)
4. Include escalation triggers
5. Cut along dotted lines
6. Create a "Stakeholder Tracker" reference card for game management

---

*Disaster Recovery Module: Stakeholder Cards*
*Part of Incident Zero, a modular cybersecurity board game*
*v2.1 - Balanced & Refined Edition*
