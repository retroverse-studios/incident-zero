# Card Consistency Model & Field Structure

**Version:** 1.0
**Purpose:** Document which card fields are universal, which are module-specific, and which are unique to card types

---

## Overview

Incident Zero uses a **hierarchical consistency model** with three levels:

1. **Universal Core Fields** - Appear on ALL cards across ALL modules
2. **Module-Specific Fields** - Appear only in certain modules (but consistent within that module)
3. **Card Type Unique Fields** - Appear only on specific card types

This document maps every field to its consistency level.

---

# Part 1: Universal Core Fields

These fields appear on **EVERY card** in **EVERY module**:

| Field | Description | Location | Example |
|-------|-------------|----------|---------|
| **Card ID** | Unique identifier | Top right badge | T-01, D-24, PT-09, A-01, E-12, SRV-03, DOM-02 |
| **Card Type** | Type of card | Top left | THREAT CARD, DEFENSE CARD, EVENT CARD, etc. |
| **Title** | Card name | Prominent | PHISHING CAMPAIGN, EMAIL AUTHENTICATION SETUP |
| **Description/Narrative** | What is this? | Center | Scenario, explanation, or narrative text |
| **Optional Image Space** | 2"×2" artwork area | Center/middle | [PICTURE HERE] |
| **Keywords/Tags** | Searchable terms | Bottom | phishing \| email \| credential harvesting |

---

# Part 2: Module-Specific Field Sets

## Module A: INCIDENT RESPONSE

### Threat Cards (T-01 to T-20)

**Consistent Fields Within IR Module:**
- `Step` - Kill chain position (INITIAL COMPROMISE, PIVOT & ESCALATE, PERSISTENCE, C2 & EXFIL)
- `Vector` - Attack vector (SOCIAL_ENGINEERING, WEB_EXPLOIT, CREDENTIAL_ABUSE, MALWARE, NETWORK, DATA_EXFIL)
- `Difficulty` - DC rating (DC 10-15)
- `Clue for Threat Orchestrator` - Narrative scenario
- `Why This Works` - Rules explanation
- `Counters` - List of defending defense cards with bonuses

**Example Card:**
```
T-01: PHISHING CAMPAIGN
├─ Step: INITIAL COMPROMISE
├─ Vector: SOCIAL_ENGINEERING
├─ Difficulty: DC 12
├─ Clue: "Your security team reports..."
├─ Why This Works: "Phishing exploits human psychology..."
├─ Counters: D-01 (+2), D-02 (+3), D-03 (+2)
└─ Keywords: phishing | email | social engineering
```

### Defense Cards (D-01 to D-43)

**Consistent Fields Within IR Module:**
- `Tier` - Cost category (BASIC, ADVANCED, ELITE)
- `Cost` - Budget (10, 15, or 25)
- `Vector` - What it defends against (SOCIAL_ENGINEERING, WEB_EXPLOIT, etc.)
- `Effect` - What this defense does
- `Used Against` - List of threat cards it counters
- `Synergies` - Other defenses it works well with

**Example Card:**
```
D-01: EMAIL AUTHENTICATION SETUP
├─ Tier: BASIC
├─ Cost: 10 Budget
├─ Vector: SOCIAL_ENGINEERING
├─ Effect: "Blocks phishing emails claiming to be from your domain..."
├─ Used Against: T-01, T-11
├─ Synergies: D-02, D-03
└─ Keywords: email | authentication | SPF | DKIM | DMARC
```

---

## Module B: HARDENING

### Defense Cards (Same as IR - D-01 to D-24)

**Important Note:** Defense cards are REUSED from Incident Response module. Same fields, same structure.

### Pentester Tactic Cards (PT-01 to PT-16)

**Unique Fields for Hardening Module:**
- `Tactic Type` - Category (Initial Access, Persistence, Privilege Escalation, etc.)
- `Target Vectors` - What it exploits (same vector system)
- `Difficulty` - DC rating (BASIC DC 12, INTERMEDIATE DC 13, ADVANCED DC 14, EXPERT DC 15+)
- `Threat Level` - Visual bar (▓▓░░░)
- `Scenario` - Narrative of what pentester does
- `Attack Details` - How the attack works
- `Defending Defenses` - Which defense cards apply with bonuses
- `Outcome` - SUCCESS and FAILURE paths with consequences
- `Teaching Point` - Learning objective

**Example Card:**
```
PT-01: SOCIAL ENGINEERING - PRETEXTING
├─ Tactic Type: Initial Access / Social Engineering
├─ Target Vectors: SOCIAL_ENGINEERING, CREDENTIAL_ABUSE
├─ Difficulty: BASIC (DC 12)
├─ Threat Level: ▓▓░░░
├─ Scenario: "A pentester calls your IT helpdesk..."
├─ Attack Details: "Targets: User training gaps, process enforcement"
├─ Defending Defenses: D-02 (+2), D-07 (+1), D-23 (+2)
├─ Outcome: SUCCESS (11+) vs FAILURE (≤10)
├─ Teaching Point: "Social engineering exploits psychology..."
└─ Keywords: social engineering | pretexting | helpdesk
```

---

## Module C: DISASTER RECOVERY

### Crisis Action Cards (ACTION-01 to ACTION-13)

**Unique Fields for Disaster Recovery Module:**
- `Category` - Type of action (Investigation, Remediation, Communication)
- `Cost` - Budget (5-30)
- `Duration` - Turns required (1 turn, 2 turns, etc.)
- `Advancement` - Progress metric (+25% Investigation, +20% Remediation, +15% Communication, etc.)
- `Description` - What does this action do?
- `Key Details` - Important conditions (⚠️ warnings, ✓ requirements)
- `When to Use` - Strategic guidance
- `Risk if Not Done` - Consequences of skipping
- `Stakeholder Impact` - Effect on trust meters (Customer, Regulatory, Board, Media)
- `Synergies` - Works well with other actions

**Example Card:**
```
ACTION-01: FORENSIC ANALYSIS
├─ Category: Investigation
├─ Cost: 12 Budget
├─ Duration: 2 turns
├─ Advancement: +25% Investigation
├─ Description: "Forensic experts analyze compromised systems..."
├─ Key Details: [⚠️ system offline] [✓ legal protection]
├─ When to Use: "Need definitive answer about scope..."
├─ Risk if Not Done: "Cannot determine full extent of damage..."
├─ Stakeholder Impact: Customer -5%, Regulatory +10%, Board +5%
├─ Synergies: ACTION-04, ACTION-05
└─ Keywords: forensics | investigation | evidence
```

### Stakeholder Cards (STAKE-01 to STAKE-05)

**Unique Fields for Disaster Recovery Module:**
- `Type` - Stakeholder category (Customers, Regulators, Media, Board, Executive)
- `Starting Trust` - Initial meter value (%)
- `Critical Threshold` - Below this = escalation
- `Trust Meter Effects` - What increases/decreases trust
- `Escalation Trigger` - What happens if trust drops too low

**Example Structure:**
```
STAKE-01: CUSTOMERS
├─ Starting Trust: 50%
├─ Critical Threshold: <20%
├─ Trust Increases: +10% for ACTION-09 (Customer Notification)
├─ Trust Decreases: -20% for missed notification deadline
├─ Escalation: Class action lawsuit (EVENT-05)
└─ Keywords: customers | trust | reputation
```

### Event Cards (EVENT-01 to EVENT-12)

**Unique Fields for Disaster Recovery Module:**
- `Type` - Event category (Discovery, Deadline, Escalation, Legal, Regulatory, etc.)
- `Turn` - When typically occurs ("Usually Turn 3-4")
- `Trigger` - How event happens (Automatic, Conditional, etc.)
- `Severity` - Visual threat (▓▓░░░)
- `Immediate Effects` - What happens (⚠️ negative, ✓ positive)
- `Impact on Trust` - % changes to stakeholders
- `Can This Be Prevented?` - Mitigation options
- `Team Response Options` - What Blue Team can do
- `Escalation Path` - If not handled, chains to worse event
- `Duration` - How long effect lasts

**Example Card:**
```
EVENT-01: FIRST MEDIA COVERAGE
├─ Type: Discovery
├─ Turn: Usually Turn 1-2
├─ Trigger: Automatic (media finds out)
├─ Severity: ▓▓░░░
├─ Immediate Effects: [⚠️ Media aware] [⚠️ Customers learn]
├─ Impact on Trust: Customer -10%, Media -15%, Board -5%
├─ Prevention: Cannot prevent, only mitigate with ACTION-11
├─ Team Response: Use ACTION-11 (Media Management)
├─ Escalation: EVENT-01 → EVENT-07 (Media Frenzy) if unprepared
├─ Duration: Ongoing
└─ Keywords: media | public relations | news
```

---

## Module D: NETWORK BUILDING

### Server Cards (SRV-01 to SRV-10)

**Unique Fields for Network Building Module:**
- `Type` - Server category (Business Critical, Development, Legacy, etc.)
- `Cost` - Budget (3-25)
- `Complexity` - Scale (1/4 to 4/4)
- `Availability Requirement` - Uptime SLA (99.9%, 95%, etc.)
- `Criticality` - Importance (★★★☆☆ to ★★★★★)
- `Key Concerns` - What attacks target this
- `Defense Considerations` - Required/recommended defenses
- `Network Placement` - Where in architecture (DMZ, Internal, Admin zone)
- `Interactions` - References to IR threats, DR scenarios, Audit domains

**Example Card:**
```
SRV-01: EMAIL SERVER
├─ Type: Business Critical
├─ Cost: 8 Budget
├─ Complexity: ▓▓░░ (2/4)
├─ Availability Req: 99.9% uptime
├─ Criticality: ★★★★★
├─ Key Concerns: [⚠️ phishing] [⚠️ credential compromise] [⚠️ exfiltration]
├─ Defense Considerations: Email Auth, DLP, Gateway Filter, MFA
├─ Network Placement: DMZ or protected segment
├─ Interactions: T-01 (Phishing), DOMAIN-02 (Identity)
└─ Keywords: email | communication | critical
```

### Security Device Cards (SEC-01 to SEC-10)

**Unique Fields for Network Building Module:**
- `Type` - Device category (Network Security, Detection, Monitoring, etc.)
- `Cost` - Budget (4-15)
- `Complexity` - Scale (2/4 to 4/4)
- `Coverage` - Where deployed (Perimeter, Internal, Endpoint, etc.)
- `Effectiveness` - Rating (★★★★☆)
- `What It Protects Against` - List of threats
- `Limitations` - What it doesn't do
- `Works With` - Other security components
- `Placement in Architecture` - Network location

**Example Card:**
```
SEC-01: FIREWALL
├─ Type: Network Security
├─ Cost: 8 Budget
├─ Complexity: ▓▓▓░ (3/4)
├─ Coverage: Perimeter / Border
├─ Effectiveness: ★★★★☆
├─ Protects Against: [✓ unauthenticated traffic] [✓ malware C2] [✓ DDoS]
├─ Limitations: [⚠️ N/W only] [⚠️ not app-layer] [⚠️ single point of failure]
├─ Works With: ARCH-02/03, SEC-02, SEC-03, D-04
├─ Placement: Perimeter / DMZ boundary
└─ Keywords: firewall | network | perimeter
```

### Architecture Cards (ARCH-01 to ARCH-05)

**Unique Fields for Network Building Module:**
- `Type` - Architecture category (Flat, Segmented, Cloud, Hybrid, etc.)
- `Cost` - Budget (0-15)
- `Complexity` - Scale (1/4 to 4/4)
- `Security Posture` - How well protected (Low, Medium, High, Very High)
- `Performance Impact` - Latency/throughput (None, Low, Medium, High)
- `Maintenance Overhead` - Operational burden
- `Suitable For` - Company sizes, threat levels
- `Scaling Properties` - How it grows
- `Interactions` - Which servers/devices work with this

**Example Card:**
```
ARCH-02: 3-ZONE SEGMENTED NETWORK
├─ Type: Segmented
├─ Cost: 5 Budget (beyond base)
├─ Complexity: ▓▓▓░ (3/4)
├─ Security Posture: Medium to High
├─ Performance Impact: Low
├─ Maintenance: Medium (3 zones to manage)
├─ Suitable For: Small to Medium businesses
├─ Scaling: Can add more zones (4-zone, 5-zone)
├─ Interactions: Works with SEC-01, D-04, DOMAIN-01
└─ Keywords: segmentation | zones | DMZ | defense-in-depth
```

### Asset Cards (ASSET-01 to ASSET-08)

**Unique Fields for Network Building Module:**
- `Type` - Asset category (Data store, Service, User access, etc.)
- `Criticality` - Importance (★★★☆☆ to ★★★★★)
- `Data Sensitivity` - Classification (Public, Internal, Confidential, Restricted)
- `Users/Scope` - Who uses it / how broad
- `Required Infrastructure` - Servers/devices needed
- `Protection Requirements` - Mandatory defenses
- `Backup/Recovery` - RTO/RPO needs
- `Compliance` - Regulatory requirements

**Example Card:**
```
ASSET-03: DATABASE (Customer Data)
├─ Type: Data store / Critical system
├─ Criticality: ★★★★★ (5/5)
├─ Data Sensitivity: Confidential (PII)
├─ Users/Scope: All customers (millions of records)
├─ Required Infrastructure: SRV-03 (Database Server), Backup
├─ Protection Requirements: Encryption, Access Control, Backup, Audit
├─ Backup/Recovery: RTO 4 hours, RPO 1 hour
├─ Compliance: GDPR, PCI-DSS, CCPA
└─ Keywords: database | customer data | PII | critical
```

---

## Module E: AUDIT & COMPLIANCE

### Audit Domain Cards (DOMAIN-01 to DOMAIN-06)

**Unique Fields for Audit & Compliance Module:**
- `Focus` - Assessment question
- `Critical For` - Why it matters
- `Regulatory References` - Which frameworks require this
- `What's Assessed` - Checklist of evaluation points
- `Maturity Levels` - Scoring from 1⭐ to 5⭐
  - Each level includes specific findings
- `Typical Findings` - Common issues (⚠️)
- `Impact on Other Modules` - Modifiers to IR/DR/NB
- `Remediation Options` - Which REMEDIATION cards apply

**Example Card:**
```
DOMAIN-01: NETWORK SEGMENTATION & ISOLATION
├─ Focus: How well is network divided into segments?
├─ Critical For: Preventing lateral movement
├─ Regulatory Refs: PCI-DSS, NIST, ISO 27001
├─ What's Assessed: [□ zones documented?] [□ firewalls?] [□ VLANs?]
├─
│ MATURITY:
│ ⭐ No segmentation (flat network)
│ ⭐⭐ Basic 2-3 zones
│ ⭐⭐⭐ Documented zones, firewalls between
│ ⭐⭐⭐⭐ Regularly updated, monitored
│ ⭐⭐⭐⭐⭐ Zero-trust, microsegmentation
│
├─ Typical Findings: [⚠️ flat network] [⚠️ no firewall rules] [⚠️ no VLANs]
├─ Impact on Modules: IR -3 modifier, DR +15 Budget cost
├─ Remediation: REMEDIATION-03 (12 Budget, 4-6 weeks)
└─ Keywords: network | segmentation | zones | firewall
```

### Compliance Framework Cards (FRAMEWORK-* to REMEDIATION-*)

**Unique Fields for Audit & Compliance Module:**
- `Framework` - Standard name (NIST CSF, CIS, PCI-DSS, etc.)
- `Standard/Function` - Specific standard element
- `Relevance` - Who needs this (US Federal, Healthcare, Payment, etc.)
- `Key Standard` - Reference document
- `Assessment Criteria` - Evaluation checklist
- `Scoring` - Maturity or pass/fail
- `Typical Findings` - Common issues
- `Remediation` - Which REMEDIATION cards apply
- `Related Frameworks` - Other standards

**Example Card:**
```
FRAMEWORK-NIST-01: IDENTIFY FUNCTION
├─ Framework: NIST Cybersecurity Framework
├─ Function: Identify (Asset Management, Risk Management)
├─ Relevance: US Federal, Critical Infrastructure
├─ Standard: NIST CSF 5 Functions
├─
│ ASSESSMENT:
│ ├─ Asset inventory (what systems?)
│ ├─ Data classification (what's sensitive?)
│ ├─ Risk assessment (what could go wrong?)
│ └─ Threat intelligence (realistic threats?)
│
├─ Scoring: ⭐ to ⭐⭐⭐⭐⭐ (maturity levels)
├─ Typical Findings: [⚠️ unknown systems] [⚠️ no risk assessment]
├─ Remediation: Asset management system setup
└─ Related: CIS-01, ISO 27001, HIPAA
```

### Remediation Action Cards (REMEDIATION-01 to REMEDIATION-08)

**Unique Fields for Audit & Compliance Module:**
- `Type` - What's being remediated (MFA, SIEM, Segmentation, etc.)
- `Cost` - Budget (3-15)
- `Timeline` - Duration (1-2 weeks, 4-6 weeks, etc.)
- `Difficulty` - Implementation complexity (Low, Medium, High)
- `What It Does` - Specific actions
- `Prerequisites` - Requirements before deployment
- `Impact` - What improves (which DOMAIN findings, which other modules)
- `Implementation Notes` - Practical guidance

**Example Card:**
```
REMEDIATION-01: IMPLEMENT MFA
├─ Type: Access Control
├─ Cost: 5 Budget
├─ Timeline: 2-4 weeks
├─ Difficulty: Low-Medium
├─ What It Does: [✓ Deploy MFA for all access] [✓ Email, VPN, Admin]
├─ Prerequisites: Identity system, User devices, App support
├─ Impact: Reduces DOMAIN-02 findings, makes T-03/T-06 harder
├─ Implementation: Select method (app, hardware token, SMS)
└─ Keywords: MFA | authentication | access control
```

---

## Module F: FORENSICS

The Forensics module uses three card types: **INVESTIGATION**, **EVIDENCE**, and **FINDINGS**.

### Investigation Action Cards (DISK-01/02, MEM-01/02, LOG-01/02, NET-01/02, MALW-01/02, TIMELINE-01, THREAT-01)

**Unique Fields for Forensics Module:**
- `MITRE ATT&CK` - Referenced technique(s) this investigation detects
- `Difficulty Class (DC)` - d20 roll target (DC 11-15)
- `Cost` - Budget (5-20)
- `Duration` - Turns the investigation takes (1-3)
- `Success Conditions` - Success / partial success / failure outcomes
- `Chain of Custody Notes` - Admissibility and documentation concerns

### Evidence Cards (EVD-01 to EVD-12)

**Unique Fields for Forensics Module:**
- `Type` - Evidence category (Malware & Persistence, Attack Infrastructure, Credentials & Access, Lateral Movement, Exfiltration, Attack Activity)
- `Discovery Source` - Which Investigation cards find this evidence
- `Chain of Custody` - Admissibility rating (Strong/Moderate/Weak)
- `Investigative Lead` - What the team can do next
- `Impact on Progress Meters` - Attack Chain / Attribution / Timeline advances
- `Feeds Into Modules` - Cross-module recommendations

### Findings Cards (FIND-01 to FIND-04)

**Unique Fields for Forensics Module:**
- `Triggered When` - Meter threshold or completion condition that produces the finding
- `Finding` - Synthesis conclusion drawn from evidence
- `Recommendations` - Actions arising from the finding
- `Feeds Into Modules` - Which modules consume the finding (Hardening, Network Building, Audit, IR)

---

# Part 3: Consistency Summary Table

## Universal Fields (Every Card)

| Field | Always Present? | Notes |
|-------|-----------------|-------|
| Card ID | ✅ Yes | Unique per card (T-01, D-24, etc.) |
| Card Type | ✅ Yes | THREAT, DEFENSE, EVENT, etc. |
| Title | ✅ Yes | Card name (1-3 words) |
| Description | ✅ Yes | Narrative or rules text |
| [Image Space] | ✅ Yes | Optional 2"×2" area |
| Keywords | ✅ Yes | Searchable tags |

## Module-Specific Fields

| Field | Modules | Appears On |
|-------|---------|-----------|
| **Kill Chain Step** | IR only | Threat Cards |
| **Attack Vector** | IR, Hardening | Threats, Defenses, Tactics |
| **Difficulty (DC)** | IR, Hardening | Threats, Pentester Tactics |
| **Tier/Cost** | IR, Hardening, NB, A&C | Defense, Server, Device, Remediation cards |
| **Synergies** | IR, Hardening, DR | Defense, Tactic, Action cards |
| **Stakeholder Impact** | DR only | Event, Action cards |
| **Trust Meters** | DR only | Event, Stakeholder cards |
| **Maturity Levels** | A&C only | Audit Domain, Framework cards |
| **Availability/Criticality** | NB only | Server, Asset cards |
| **Network Placement** | NB, A&C | Server, Device, Architecture cards |
| **Chain of Custody** | Forensics only | Investigation, Evidence cards |
| **Progress Meter Impact** | Forensics only | Evidence cards |

## Card Types with Multiple Unique Elements

| Card Type | Unique Elements Count | Examples |
|-----------|----------------------|----------|
| Threat Cards | 4 unique fields | Step, Vector, DC, Clue |
| Defense Cards | 4 unique fields | Tier, Cost, Effect, Used Against |
| Pentester Tactics | **6 unique fields** | Tactic Type, Threat Level, Attack Details, Defending Defenses, Outcome, Teaching Point |
| Crisis Actions | **5 unique fields** | Category, Cost, Duration, Advancement, Stakeholder Impact |
| Event Cards | **6 unique fields** | Type, Turn, Trigger, Severity, Escalation Path, Duration |
| Server Cards | **5 unique fields** | Type, Cost, Complexity, Availability, Criticality |
| Security Devices | **4 unique fields** | Type, Cost, Coverage, Effectiveness |
| Audit Domains | **5 unique fields** | Focus, Critical For, Maturity Levels, Impact on Modules |
| Frameworks | **4 unique fields** | Framework, Standard, Scoring, Related Frameworks |
| Remediation | **4 unique fields** | Type, Cost, Timeline, Difficulty |
| Investigation Cards | **5 unique fields** | MITRE ATT&CK, DC, Duration, Success Conditions, Chain of Custody Notes |
| Evidence Cards | **5 unique fields** | Type, Discovery Source, Chain of Custody, Investigative Lead, Meter Impact |
| Findings Cards | **4 unique fields** | Triggered When, Finding, Recommendations, Feeds Into Modules |

---

# Part 4: Consistency in Practice

## Example: How Fields Progress Across Modules

Let's track **Email Security** across all modules to show field consistency:

### Network Building (Design Phase)
```
SRV-01: EMAIL SERVER
├─ Cost: 8 Budget (when designing)
├─ Complexity: 2/4
├─ Availability: 99.9%
├─ Criticality: ★★★★★
└─ Required Defenses: Email Auth, Gateway, MFA
```

### Incident Response (Attack Phase)
```
T-01: PHISHING CAMPAIGN
├─ Vector: SOCIAL_ENGINEERING (targets email users)
├─ DC: 12 (difficulty to detect)
├─ Counters: D-01 (Email Auth), D-02 (Training), D-03 (Gateway)
```

### Hardening (Testing Phase)
```
PT-01: SOCIAL ENGINEERING - PRETEXTING
├─ Targets: Email helpdesk processes
├─ DC: 12 (defeat)
├─ Defending: D-02 (+2), D-07 (+1) — same defenses reused
```

### Disaster Recovery (Crisis Phase)
```
EVENT-01: FIRST MEDIA COVERAGE
└─ Mitigated by: ACTION-11 (Media Management)

ACTION-01: FORENSIC ANALYSIS
├─ May discover: Email compromise, credential theft
└─ Duration: 2 turns (to analyze email logs)
```

### Audit & Compliance (Assessment Phase)
```
DOMAIN-02: ACCESS CONTROL & IDENTITY
├─ Assesses: Email MFA, credential policies
├─ Finding: "No MFA on email access"
└─ Remediation: REMEDIATION-01 (MFA deployment)
```

**Note:** Same email server appears across all modules, with different fields relevant to each module's purpose, but with consistent references.

---

# Part 5: Design Principles for Consistency

## ✅ DO: Maintain Field Consistency

1. **Universal Fields:** Always include Card ID, Type, Title, Description, Keywords
2. **Vector System:** Use same attack vectors across IR and Hardening
3. **Cost/Difficulty:** Use consistent scales (Budget 10/15/25, DC 12-16)
4. **Cross-References:** Link cards between modules (T-01 references D-01, SRV-01 references T-01)
5. **Maturity Scales:** 1-5 stars for assessments, difficulty tiers for challenges

## ❌ DON'T: Break the Pattern

1. ❌ Create fields that only appear on one card
2. ❌ Use different cost scales in different modules (except where intentional)
3. ❌ Fail to cross-reference related cards
4. ❌ Introduce new field names for existing concepts
5. ❌ Use different vector names for same attacks

## 🎯 Best Practice: Extend Not Replace

When adding module-specific fields:
- **Keep universal fields intact**
- **Add new fields after core fields**
- **Follow existing naming conventions**
- **Document the new field** in this consistency model
- **Ensure cross-module references** work

---

# Part 6: Field Naming Conventions

Use these standard field names across all cards:

### Metadata Fields
- `Card Type` - THREAT CARD, DEFENSE CARD, etc.
- `Card ID` - T-01, D-24, etc.
- `Title` - Card name

### Common Assessment Fields
- `Cost` - Budget requirement
- `Difficulty` / `DC` - Challenge rating
- `Vector` / `Vectors` - Attack/Defense category
- `Type` - Category within module
- `Tier` - Tier level
- `Duration` - Time required
- `Complexity` - Difficulty of implementation

### Common Effect Fields
- `Effect` - What this card does
- `Impact` - Consequences or changes
- `Advancement` - Progress metric
- `Scoring` / `Rating` - Effectiveness (⭐)

### Common Relationship Fields
- `Synergies` - Works well with
- `Used Against` / `Defends Against` - Counters
- `Interactions` - Cross-module references
- `Related Cards` / `Cross-References` - Other relevant cards

### Common Outcome Fields
- `Outcome` / `Outcomes` - SUCCESS/FAILURE
- `Escalation` / `Escalation Path` - What happens next
- `Remediation` - How to fix

---

# Part 7: Creating New Cards with Consistency

## Checklist for New Card Fields

When creating a new card:

- [ ] **Use existing universal fields** (ID, Type, Title, Description, Keywords)
- [ ] **Check module field patterns** - Follow existing cards in that module
- [ ] **Don't invent new fields** - Use existing field names
- [ ] **Cross-reference other cards** - Link to related cards in same/other modules
- [ ] **Document exceptions** - If you must add a truly unique field, explain why
- [ ] **Test consistency** - Does this card feel like it belongs with existing cards?
- [ ] **Verify naming** - Are field names consistent with existing cards?
- [ ] **Check references** - Do cross-references work both ways?

---

# Part 8: Summary: Core + Module + Unique Model

```
┌─────────────────────────────────────────────────────────┐
│  UNIVERSAL CORE FIELDS (All Cards)                      │
│  ├─ Card ID                                             │
│  ├─ Card Type                                           │
│  ├─ Title                                               │
│  ├─ Description                                         │
│  ├─ [Image Space]                                       │
│  └─ Keywords                                            │
└─────────────────────────────────────────────────────────┘
         │
         ├──> Module IR
         │    ├─ + Step, Vector, DC (Threat)
         │    ├─ + Tier, Cost, Effect (Defense)
         │    └─ + Counters, Synergies
         │
         ├──> Module Hardening
         │    ├─ + Tactic Type, Threat Level (Pentester)
         │    ├─ + Attack Details, Defending Defenses
         │    └─ + Outcome, Teaching Point
         │
         ├──> Module Disaster Recovery
         │    ├─ + Category, Duration, Advancement (Action)
         │    ├─ + Type, Turn, Trigger (Event)
         │    └─ + Stakeholder Impact, Escalation
         │
         ├──> Module Network Building
         │    ├─ + Type, Complexity, Availability (Server)
         │    ├─ + Coverage, Effectiveness (Device)
         │    ├─ + Cost, Security Posture (Architecture)
         │    └─ + Criticality, Data Sensitivity (Asset)
         │
         ├──> Module Forensics
         │    ├─ + MITRE ATT&CK, DC, Duration (Investigation)
         │    ├─ + Type, Discovery Source, Chain of Custody (Evidence)
         │    └─ + Triggered When, Recommendations (Findings)
         │
         └──> Module Audit & Compliance
              ├─ + Focus, Critical For, Maturity Levels (Domain)
              ├─ + Framework, Standard, Scoring
              └─ + Timeline, Difficulty (Remediation)
```

---

## Answer to Your Question

**Are cards consistent?**

**YES**, with a three-tier hierarchy:

1. **Universal Core** (6 fields on every card)
   - Card ID, Type, Title, Description, Image Space, Keywords

2. **Module-Specific** (consistent within each module)
   - Incident Response: Vector, DC, Tier, Cost system
   - Hardening: Tactic Type, Threat Level, Teaching Point
   - Disaster Recovery: Category, Duration, Stakeholder Impact
   - Network Building: Type, Complexity, Availability, Criticality
   - Forensics: DC, Duration, Chain of Custody, Meter Impact
   - Audit & Compliance: Focus, Maturity Levels, Remediation

3. **Card Type Unique** (specific to card type, not module)
   - Some card types have 4-6 unique fields
   - Example: Event Cards have Escalation Paths (unique to events)
   - Example: Crisis Actions have Stakeholder Impact (unique to DR actions)

**There is NOT a single "Unique Element" field that updates per module.** Instead, **different card types have different numbers of unique fields**, and **modules are defined by which card types they use** + **those card types' unique fields.**

For example:
- **Threat Cards have 4 unique fields** (Step, Vector, DC, Counters)
- **Event Cards have 6 unique fields** (Type, Turn, Trigger, Severity, Escalation, Duration)
- **Pentester Tactics have 6 unique fields** (Tactic Type, Threat Level, Attack Details, Defending Defenses, Outcome, Teaching Point)

This is more flexible than a single "Unique" field because different card types genuinely need different information.

---

*Last Updated: October 2025*
*Version: 1.0*
