# Card Layout Template & Contribution Guide

**Version:** 1.0
**Last Updated:** October 2025

---

## Overview

This document provides consistent card layout templates and guidelines for creating new cards for Incident Zero. Whether you're designing Threat cards, Defense cards, Event cards, or any other card type, these templates ensure visual consistency and clarity.

---

## Card Design Principles

1. **Consistency:** All cards of the same type follow the same structure
2. **Clarity:** Information hierarchy makes cards easy to scan
3. **Usability:** Cards work well both printed and digital
4. **Accessibility:** Clear text, simple language, no color-dependency for meaning
5. **Space:** Room for future artwork, but cards work without images

---

# Card Type 1: THREAT CARDS (Incident Response Module)

**Purpose:** Represent attacker actions in the kill chain
**Used In:** Incident Response module
**Total Cards:** 12 core + 8 expansion

## ASCII Layout

```
╔═════════════════════════════════════════════╗
║  THREAT CARD                    ⚔️  T-01   ║
╠═════════════════════════════════════════════╣
║                                             ║
║  PHISHING CAMPAIGN                          ║
║                                             ║
╠═════════════════════════════════════════════╣
║  Step:   INITIAL COMPROMISE                 ║
║  Vector: SOCIAL_ENGINEERING                 ║
║  Difficulty: DC 12                          ║
╠═════════════════════════════════════════════╣
║  FLAVOUR TEXT (Threat Orchestrator clue):   ║
║  "Your security team reports that several   ║
║  employees have received emails claiming    ║
║  to be from your IT department requesting   ║
║  password resets..."                        ║
╠═════════════════════════════════════════════╣
║  [OPTIONAL IMAGE SPACE - 2" x 2"]           ║
║                                             ║
╠═════════════════════════════════════════════╣
║  RULES TEXT (Why this works):                ║
║  Phishing exploits human psychology rather  ║
║  than technical vulnerabilities. Attackers  ║
║  use social engineering to create urgency   ║
║  and bypass technical controls. With email  ║
║  authentication (DMARC/SPF) and training,   ║
║  this attack is highly preventable.         ║
╠═════════════════════════════════════════════╣
║  COUNTERS:                                  ║
║  ✓ D-01 (Email Authentication) +2           ║
║  ✓ D-02 (User Security Training) +3         ║
║  ✓ D-03 (Email Gateway) +2                  ║
╠═════════════════════════════════════════════╣
║  KEYWORDS: Phishing | Email | Credential    ║
║  harvesting | Social engineering            ║
╚═════════════════════════════════════════════╝
```

## Content Fields

| Field | Description | Example |
|-------|-------------|---------|
| **Card Type** | Always "THREAT CARD" | THREAT CARD |
| **Icon & Card ID** | Sword symbol + ID (T-01, T-09) | ⚔️ T-01 |
| **Title** | Attack name (1-3 words) | PHISHING CAMPAIGN |
| **Kill Chain Step** | Where in attack progression | INITIAL COMPROMISE, PIVOT & ESCALATE, etc. |
| **Attack Vector** | Category of attack method | SOCIAL_ENGINEERING, WEB_EXPLOIT, CREDENTIAL_ABUSE, MALWARE, NETWORK, DATA_EXFIL |
| **Difficulty** | DC (Difficulty Class) for d20 roll | DC 10-15 |
| **Flavour Text** | Scenario/clue for Threat Orchestrator | Italicized, narrative description of what's happening |
| **Rules Text** | Why this attack works, teaching point | Explanation of attack mechanics and defenses |
| **Counters** | Which Defense cards defeat this | List with bonuses (✓ Card Name +X) |
| **Keywords** | Searchable tags | Comma-separated list |
| **Image Space** | Optional artwork (marked as optional) | Suggested: 2" × 2" at 300 dpi |

---

# Card Type 2: DEFENSE CARDS (Incident Response & Hardening)

**Purpose:** Tools and procedures to counter attacks
**Used In:** Incident Response, Hardening modules
**Total Cards:** 24 core (shared deck) + 19 expansion

## ASCII Layout

```
╔═════════════════════════════════════════════╗
║  DEFENSE CARD                   🛡️  D-01   ║
╠═════════════════════════════════════════════╣
║                                             ║
║  EMAIL AUTHENTICATION SETUP                 ║
║                                             ║
╠═════════════════════════════════════════════╣
║  Tier:   BASIC                              ║
║  Cost:   10 Budget                          ║
║  Vector: SOCIAL_ENGINEERING                 ║
║  Efficiency: ★★★★☆ (4/5)                    ║
╠═════════════════════════════════════════════╣
║  FLAVOUR TEXT (What is this control?):      ║
║  Deploy SPF, DKIM, and DMARC protocols      ║
║  to prevent email spoofing and improve      ║
║  email authentication...                    ║
╠═════════════════════════════════════════════╣
║  [OPTIONAL IMAGE SPACE - 2" x 2"]           ║
║                                             ║
╠═════════════════════════════════════════════╣
║  EFFECT (What does it do?):                 ║
║  Blocks phishing emails claiming to be      ║
║  from your domain. Requires attackers to    ║
║  find alternative vectors.                  ║
╠═════════════════════════════════════════════╣
║  THREATS DEFENDED:                          ║
║  ✓ T-01 (Phishing Campaign)                 ║
║  ✓ T-11 (Email Spoofing)                    ║
║                                             ║
║  SYNERGIES (works well with):               ║
║  ✓ D-02 (User Training) - combined 80%      ║
║  ✓ D-03 (Email Gateway) - defense-in-depth ║
╠═════════════════════════════════════════════╣
║  IMPLEMENTATION:                            ║
║  Timeline: 1-2 weeks                        ║
║  Difficulty: Low (DNS config)               ║
║  Resources: IT/Network team                 ║
╠═════════════════════════════════════════════╣
║  KEYWORDS: Email | Authentication | Phishing║
║  | SPF | DKIM | DMARC                       ║
╚═════════════════════════════════════════════╝
```

## Content Fields

| Field | Description | Example |
|-------|-------------|---------|
| **Card Type** | Always "DEFENSE CARD" | DEFENSE CARD |
| **Icon & Card ID** | Shield symbol + ID (D-01, D-25) | 🛡️ D-01 |
| **Title** | Defense name | EMAIL AUTHENTICATION SETUP |
| **Tier** | Cost category | BASIC (10), ADVANCED (15), ELITE (25) |
| **Budget Cost** | Resource cost | 10 Budget |
| **Attack Vector** | What type of attack it defends | SOCIAL_ENGINEERING, WEB_EXPLOIT, etc. |
| **Efficiency Rating** | Visual effectiveness (★★★☆☆) | 1-5 stars |
| **Flavour Text** | What is this control? | Brief description of the technology/procedure |
| **Effect** | What happens when deployed | Specific impact on threats |
| **Threats Defended** | Which Threat cards this counters | ✓ Card Name (applies bonus to rolls) |
| **Synergies** | Works well with other defenses | Other Defense cards that complement this |
| **Implementation** | Practical deployment info | Timeline, difficulty, required resources |
| **Keywords** | Searchable tags | Comma-separated list |
| **Image Space** | Optional artwork | Suggested: 2" × 2" at 300 dpi |

---

# Card Type 3: PENTESTER TACTIC CARDS (Hardening Module)

**Purpose:** Red team attacks that test deployed defenses
**Used In:** Hardening module
**Total Cards:** 8 core + 8 expansion

## ASCII Layout

```
╔═════════════════════════════════════════════╗
║  PENTESTER TACTIC                  ⚔️ PT-01║
╠═════════════════════════════════════════════╣
║                                             ║
║  SOCIAL ENGINEERING - PRETEXTING             ║
║                                             ║
╠═════════════════════════════════════════════╣
║  Type:       Initial Access                 ║
║  Vectors:    SOCIAL_ENGINEERING,            ║
║              CREDENTIAL_ABUSE               ║
║  Difficulty: BASIC (DC 12)                  ║
║  Threat Level: ▓▓░░░ (2/5)                  ║
╠═════════════════════════════════════════════╣
║  SCENARIO (Threat Orchestrator describes):  ║
║  "A pentester calls your IT helpdesk        ║
║  impersonating a VIP executive. They claim  ║
║  to be traveling without their laptop and   ║
║  need emergency access to critical systems. ║
║  They pressure with urgency and authority.  ║
║  Can they bypass your security procedures?" ║
╠═════════════════════════════════════════════╣
║  [OPTIONAL IMAGE SPACE - 2" x 2"]           ║
║                                             ║
╠═════════════════════════════════════════════╣
║  ATTACK MECHANICS:                          ║
║  Targets: User security training gaps,      ║
║           process enforcement               ║
║  Success if: Blue Team rolls < 12 on d20    ║
║  Consequence: Attacker gains credentials or ║
║               system access                 ║
╠═════════════════════════════════════════════╣
║  DEFENDING DEFENSES (Applicable Bonuses):   ║
║  ✓ D-02 (User Security Training) +2         ║
║  ✓ D-07 (MFA) +1 (second factor needed)     ║
║  ✓ D-23 (IR Playbooks) +2 (escalation)      ║
║  ✓ D-24 (Crisis Plan) +1 (procedures)       ║
╠═════════════════════════════════════════════╣
║  OUTCOME:                                   ║
║  SUCCESS (11+):  Helpdesk follows proper    ║
║                  verification, attacker     ║
║                  denied, morale +5          ║
║  FAILURE (≤10):  Attacker gains access,     ║
║                  must deploy additional     ║
║                  defenses, morale -10       ║
╠═════════════════════════════════════════════╣
║  TEACHING POINT:                            ║
║  Social engineering exploits human          ║
║  psychology and organizational process      ║
║  gaps. Technology alone cannot defend       ║
║  against this; training and procedures      ║
║  are essential. Regular security drills      ║
║  improve outcomes.                          ║
╠═════════════════════════════════════════════╣
║  KEYWORDS: Social engineering | Pretexting  ║
║  | Helpdesk | Credential compromise | Call  ║
║  | Phone-based attack                       ║
╚═════════════════════════════════════════════╝
```

## Content Fields

| Field | Description | Example |
|-------|-------------|---------|
| **Card Type** | Always "PENTESTER TACTIC" | PENTESTER TACTIC |
| **Icon & Card ID** | Sword symbol + ID (PT-01, PT-09) | ⚔️ PT-01 |
| **Title** | Tactic name with category | SOCIAL ENGINEERING - PRETEXTING |
| **Attack Type** | Tactic category | Initial Access, Persistence, Privilege Escalation, etc. |
| **Target Vectors** | What it exploits | SOCIAL_ENGINEERING, CREDENTIAL_ABUSE, etc. |
| **Difficulty** | DC for d20 roll | BASIC (DC 12), INTERMEDIATE (DC 13), ADVANCED (DC 14), EXPERT (DC 15+) |
| **Threat Level** | Visual threat indicator (▓▓░░░) | 1-5 blocks filled |
| **Scenario** | Narrative description | What the pentester does |
| **Attack Mechanics** | How the attack works | Targets, success conditions |
| **Defending Defenses** | Which Defense cards apply | ✓ Card Name +X bonus |
| **Outcome** | SUCCESS and FAILURE paths | What happens with each result |
| **Teaching Point** | Learning objective | What players should understand |
| **Keywords** | Searchable tags | Comma-separated list |
| **Image Space** | Optional artwork | Suggested: 2" × 2" at 300 dpi |

---

# Card Type 4: CRISIS ACTION CARDS (Disaster Recovery Module)

**Purpose:** Actions taken during a breach to respond
**Used In:** Disaster Recovery module
**Total Cards:** 13 core

## ASCII Layout

```
╔═════════════════════════════════════════════╗
║  CRISIS ACTION                    🛠️ A-01   ║
╠═════════════════════════════════════════════╣
║                                             ║
║  FORENSIC ANALYSIS                          ║
║                                             ║
╠═════════════════════════════════════════════╣
║  Category: Investigation                    ║
║  Cost:     12 Budget                        ║
║  Duration: 2 turns (multi-turn)             ║
║  Advance:  +25% Investigation               ║
╠═════════════════════════════════════════════╣
║  DESCRIPTION (What does this action do?):   ║
║  Forensic experts analyze compromised       ║
║  systems to determine scope of breach,      ║
║  what data was accessed, and how long       ║
║  attacker had access...                     ║
╠═════════════════════════════════════════════╣
║  [OPTIONAL IMAGE SPACE - 2" x 2"]           ║
║                                             ║
╠═════════════════════════════════════════════╣
║  KEY DETAILS:                               ║
║  ⚠️ Requires shutting down compromised      ║
║     system (removes from operation)         ║
║  ⚠️ Requires forensics team (external cost) ║
║  ✓ Provides evidence for legal action       ║
║  ✓ Essential for regulatory compliance      ║
╠═════════════════════════════════════════════╣
║  WHEN TO USE:                               ║
║  • Need definitive answer about scope       ║
║  • Legal action is likely                   ║
║  • Compliance investigation required        ║
║  • Regulatory agency involved               ║
║                                             ║
║  RISK IF NOT DONE:                          ║
║  ⚠️ Cannot determine full extent of damage  ║
║  ⚠️ Cannot properly remediate                ║
║  ⚠️ No evidence for law enforcement         ║
║  ⚠️ Regulatory penalties                    ║
╠═════════════════════════════════════════════╣
║  IMPACT ON STAKEHOLDERS:                    ║
║  Customer Trust:    -5% (system offline)    ║
║  Regulatory Trust:  +10% (shows diligence)  ║
║  Board Confidence:  +5% (legal protection)  ║
║  Media Perception:  Neutral (shows thorough ║
║                     investigation)          ║
╠═════════════════════════════════════════════╣
║  SYNERGIES (Works well with):               ║
║  ✓ ACTION-04 (Third-Party IR) - coordinates ║
║  ✓ ACTION-05 (Patch & Harden) - confirms    ║
║    what needs fixing                        ║
╠═════════════════════════════════════════════╣
║  KEYWORDS: Forensics | Investigation |      ║
║  Evidence | Digital forensics | Analysis    ║
╚═════════════════════════════════════════════╝
```

## Content Fields

| Field | Description | Example |
|-------|-------------|---------|
| **Card Type** | Always "CRISIS ACTION" | CRISIS ACTION |
| **Icon & Card ID** | Wrench symbol + ID (A-01 to A-12) | 🛠️ A-01 |
| **Title** | Action name | FORENSIC ANALYSIS |
| **Category** | Type of action | Investigation, Remediation, Communication |
| **Budget Cost** | Resource cost to deploy | 12 Budget |
| **Duration** | How many turns it takes | 1 turn, 2 turns, etc. |
| **Advancement** | Progress toward objective | +25% Investigation (or other metric) |
| **Description** | What happens | Narrative description of action |
| **Key Details** | Important conditions | Prerequisites, consequences (⚠️ and ✓) |
| **When to Use** | Strategic guidance | When is this action most valuable |
| **Risk if Not Done** | Consequences of not using | What goes wrong without this |
| **Stakeholder Impact** | Effect on trust meters | Customer, Regulatory, Board, Media effects |
| **Synergies** | Works well with other actions | Other Crisis Actions that complement |
| **Keywords** | Searchable tags | Comma-separated list |
| **Image Space** | Optional artwork | Suggested: 2" × 2" at 300 dpi |

---

# Card Type 5: EVENT CARDS (Disaster Recovery Module)

**Purpose:** Time pressure and escalation events
**Used In:** Disaster Recovery module
**Total Cards:** 12 core (6 Scheduled + 6 Triggered); the DR expansion adds 8 Scenario cards instead of extra events

## ASCII Layout

```
╔═════════════════════════════════════════════╗
║  EVENT CARD                       📅 E-01   ║
╠═════════════════════════════════════════════╣
║                                             ║
║  FIRST MEDIA COVERAGE                       ║
║                                             ║
╠═════════════════════════════════════════════╣
║  Type:    Discovery / Escalation            ║
║  Turn:    Usually Turn 1-2                  ║
║  Trigger: Automatic (media finds out)       ║
║  Severity: ▓▓░░░ (2/5)                      ║
╠═════════════════════════════════════════════╣
║  EVENT DESCRIPTION:                         ║
║  A news outlet publishes story about the    ║
║  breach. Unnamed source gives details.      ║
║  Story spreads on social media. Phone       ║
║  starts ringing with reporter calls.        ║
╠═════════════════════════════════════════════╣
║  [OPTIONAL IMAGE SPACE - 2" x 2"]           ║
║                                             ║
╠═════════════════════════════════════════════╣
║  IMMEDIATE EFFECTS:                         ║
║  ⚠️ Media becomes aware of breach           ║
║  ⚠️ Customers learn about breach (if not    ║
║     already notified)                       ║
║  ⚠️ Stock price may drop (public company)   ║
║  ⚠️ Regulatory agencies become aware        ║
║                                             ║
║  IMPACT ON TRUST METERS:                    ║
║  Customer Trust:    -10% to -20%            ║
║  Media/Public:      -15%                    ║
║  Regulatory:        -5%                     ║
║  Board:             -5%                     ║
╠═════════════════════════════════════════════╣
║  CAN THIS BE PREVENTED?                     ║
║  ✓ Not entirely (media always finds out)    ║
║  ✓ Can be mitigated with ACTION-11          ║
║    (Media Management) to control narrative  ║
║  ✓ Preparation is key                       ║
╠═════════════════════════════════════════════╣
║  TEAM RESPONSE OPTIONS:                     ║
║  IF PREPARED:                               ║
║  • Use ACTION-11 (Media Management) +5%     ║
║  • Proactive media statement reduces damage ║
║  • Control narrative becomes critical       ║
║                                             ║
║  IF UNPREPARED:                             ║
║  • Media coverage becomes more negative     ║
║  • Every turn of delay worsens perception   ║
║  • Risk of escalation to Media Frenzy       ║
║    (EVENT-07)                               ║
╠═════════════════════════════════════════════╣
║  ESCALATION PATH:                           ║
║  If company is silent or evasive:           ║
║  EVENT-01 → EVENT-07 (Media Frenzy)         ║
║  Media Frenzy has much worse effects        ║
║  (-30% Media, -20% Customer Trust)          ║
╠═════════════════════════════════════════════╣
║  DURATION:                                  ║
║  Ongoing (media coverage continues)         ║
║  Lasts until company demonstrates response  ║
║  and trust begins to rebuild                ║
╠═════════════════════════════════════════════╣
║  KEYWORDS: Media | Public relations | News  ║
║  | Publicity | Press | Social media | PR    ║
╚═════════════════════════════════════════════╝
```

## Content Fields

| Field | Description | Example |
|-------|-------------|---------|
| **Card Type** | Always "EVENT CARD" | EVENT CARD |
| **Icon & Card ID** | Calendar symbol + ID (E-01 to E-12) | 📅 E-01 |
| **Title** | Event name | FIRST MEDIA COVERAGE |
| **Type** | Category of event | Discovery, Deadline, Escalation, Legal, etc. |
| **Turn** | When typically occurs | Usually Turn 1-2 |
| **Trigger** | How event is triggered | Automatic, conditional, if X condition met |
| **Severity** | Visual severity (▓▓░░░) | 1-5 blocks filled |
| **Event Description** | What happens | Narrative description of event |
| **Immediate Effects** | Consequences | What occurs (⚠️ warnings, ✓ positives) |
| **Impact on Trust** | Effect on stakeholder meters | % changes to Customer, Media, Regulatory, Board |
| **Can This Be Prevented?** | Mitigation options | Can it be stopped? Mitigated? How? |
| **Team Response** | What Blue Team can do | Actions available, bonuses, timing |
| **Escalation Path** | If not handled, what happens next | How this event leads to worse ones |
| **Duration** | How long effect lasts | Ongoing, single turn, multiple turns |
| **Keywords** | Searchable tags | Comma-separated list |
| **Image Space** | Optional artwork | Suggested: 2" × 2" at 300 dpi |

---

# Card Type 6: NETWORK BUILDING CARDS

**Purpose:** Components for designing network infrastructure
**Used In:** Network Building module

## Server Card ASCII Layout

```
╔═════════════════════════════════════════════╗
║  SERVER CARD                      💾 SRV-01║
╠═════════════════════════════════════════════╣
║                                             ║
║  EMAIL SERVER                               ║
║                                             ║
╠═════════════════════════════════════════════╣
║  Type:              Business Critical       ║
║  Cost:              8 Budget                ║
║  Complexity:        ▓▓░░ (2/4)              ║
║  Availability Req:  99.9% uptime            ║
║  Criticality:       ★★★★★ (5/5)            ║
╠═════════════════════════════════════════════╣
║  DESCRIPTION (What is this system?):        ║
║  Central email system (Exchange, Postfix,   ║
║  or cloud-based like Office 365). Handles   ║
║  all organizational communication. Commonly ║
║  targeted by phishing and credential        ║
║  attacks...                                 ║
╠═════════════════════════════════════════════╣
║  [OPTIONAL IMAGE SPACE - 2" x 2"]           ║
║                                             ║
╠═════════════════════════════════════════════╣
║  KEY CONCERNS:                              ║
║  ⚠️ Email spoofing and phishing             ║
║  ⚠️ Credential compromise (email = reset)   ║
║  ⚠️ Data exfiltration via attachments       ║
║  ⚠️ High user impact if unavailable         ║
╠═════════════════════════════════════════════╣
║  REQUIRED DEFENSES:                         ║
║  ✓ Email Authentication (DMARC/SPF/DKIM)   ║
║  ✓ DLP for sensitive attachments            ║
║  ✓ Gateway filtering (phishing/malware)     ║
║  ✓ MFA for admin access                     ║
╠═════════════════════════════════════════════╣
║  NETWORK PLACEMENT:                         ║
║  DMZ or protected segment                   ║
║  (external access required, isolated)       ║
╠═════════════════════════════════════════════╣
║  INTERACTIONS & REFERENCES:                 ║
║  ✓ Used with Asset Card "Email"             ║
║  ✓ IR Scenarios: T-01 (Phishing),           ║
║    T-11 (Browser Extension)                 ║
║  ✓ DR "Critical Services" list              ║
║  ✓ Audit Domain: DOMAIN-02 (Identity)       ║
╠═════════════════════════════════════════════╣
║  KEYWORDS: Email | Communication |          ║
║  Exchange | Postfix | Office 365 | Phishing ║
╚═════════════════════════════════════════════╝
```

## Security Device Card ASCII Layout

```
╔═════════════════════════════════════════════╗
║  SECURITY DEVICE                  🔒 SEC-01║
╠═════════════════════════════════════════════╣
║                                             ║
║  FIREWALL                                   ║
║                                             ║
╠═════════════════════════════════════════════╣
║  Type:              Network Security        ║
║  Cost:              8 Budget                ║
║  Complexity:        ▓▓▓░ (3/4)              ║
║  Coverage:          Perimeter / Border      ║
║  Effectiveness:     ★★★★☆ (4/5)            ║
╠═════════════════════════════════════════════╣
║  DESCRIPTION (What does this do?):          ║
║  Perimeter firewall (pfSense, Palo Alto,    ║
║  Fortinet, Cisco ASA). Controls ingress/    ║
║  egress traffic. Blocks unauthorized        ║
║  protocols and connections...               ║
╠═════════════════════════════════════════════╣
║  [OPTIONAL IMAGE SPACE - 2" x 2"]           ║
║                                             ║
╠═════════════════════════════════════════════╣
║  WHAT IT PROTECTS AGAINST:                  ║
║  ✓ Unauthenticated inbound traffic          ║
║  ✓ Malware C2 beaconing (outbound)          ║
║  ✓ DDoS attacks (rate limiting)             ║
║  ✓ Lateral movement (with segmentation)     ║
╠═════════════════════════════════════════════╣
║  LIMITATIONS:                               ║
║  ⚠️ Only effective for N/W traffic           ║
║  ⚠️ Cannot detect application-layer attacks ║
║  ⚠️ Requires proper configuration           ║
║  ⚠️ Becomes single point of failure         ║
╠═════════════════════════════════════════════╣
║  WORKS WITH:                                ║
║  ✓ ARCH-02/03 (Network Segmentation)        ║
║  ✓ SEC-02 (IDS) - detection layer           ║
║  ✓ SEC-03 (IPS) - inline protection         ║
║  ✓ Defense D-04 (Firewall Rules)            ║
╠═════════════════════════════════════════════╣
║  PLACEMENT IN ARCHITECTURE:                 ║
║  Perimeter / DMZ boundary                   ║
║  Between external network and internal      ║
║  network segments                           ║
╠═════════════════════════════════════════════╣
║  KEYWORDS: Firewall | Network | Perimeter  ║
║  | Traffic control | Stateful inspection    ║
╚═════════════════════════════════════════════╝
```

---

# Card Type 7: AUDIT & COMPLIANCE CARDS

**Purpose:** Assessment criteria and compliance frameworks
**Used In:** Audit & Compliance module

## Audit Domain Card ASCII Layout

```
╔═════════════════════════════════════════════╗
║  AUDIT DOMAIN                    📋 DOM-01  ║
╠═════════════════════════════════════════════╣
║                                             ║
║  NETWORK SEGMENTATION & ISOLATION            ║
║                                             ║
╠═════════════════════════════════════════════╣
║  Assessment: How well is network divided    ║
║  into protected segments?                   ║
║  Finding Impact: ★★★★★ (5/5 - Critical)    ║
║  Audit Difficulty: ▓▓▓░░ (3/5)              ║
╠═════════════════════════════════════════════╣
║  1-STAR FINDING (⭐):                        ║
║  • No network segmentation                  ║
║  • Flat network (all systems equal access)  ║
║  • Lateral movement trivial for attacker    ║
║  • One compromise = full network breach     ║
║                                             ║
║  3-STAR FINDING (⭐⭐⭐):                     ║
║  • Basic 2-3 zone segmentation              ║
║  • DMZ / Internal / Admin zones              ║
║  • Firewalls between zones                  ║
║  • Some traffic restrictions                ║
║                                             ║
║  5-STAR FINDING (⭐⭐⭐⭐⭐):                  ║
║  • Full zero-trust network                  ║
║  • Microsegmentation by service             ║
║  • End-to-end encryption                    ║
║  • Dynamic access policies                  ║
╠═════════════════════════════════════════════╣
║  [OPTIONAL IMAGE SPACE - 2" x 2"]           ║
║                                             ║
╠═════════════════════════════════════════════╣
║  ASSESSMENT CRITERIA:                       ║
║  □ Are network zones documented?            ║
║  □ Are firewalls between zones?             ║
║  □ Are access rules documented?             ║
║  □ Is VLANs used for isolation?             ║
║  □ Are crown jewels in protected zone?      ║
║  □ Is monitoring between zones?             ║
╠═════════════════════════════════════════════╣
║  TYPICAL FINDINGS:                          ║
║  ⚠️ Flat network design                     ║
║  ⚠️ No documented network zones             ║
║  ⚠️ Overly permissive firewall rules        ║
║  ⚠️ No VLAN isolation                       ║
╠═════════════════════════════════════════════╣
║  IMPACT ON OTHER MODULES:                   ║
║  Incident Response: -3 to -5 modifier       ║
║  (lateral movement easier)                  ║
║  Network Building: Cost +5 Budget to fix    ║
║  Disaster Recovery: +15 Budget crisis cost  ║
╠═════════════════════════════════════════════╣
║  REMEDIATION OPTIONS:                       ║
║  • REMEDIATION-03 (Network Segmentation)    ║
║    Cost: 12 Budget | Timeline: 4-6 weeks    ║
║  • REMEDIATION-01 (MFA)                     ║
║    Cost: 5 Budget | Timeline: 2-4 weeks     ║
╠═════════════════════════════════════════════╣
║  KEYWORDS: Network | Segmentation | Zones  ║
║  | Firewall | VLAN | Isolation | Lateral   ║
║  | Movement | Zero-trust                    ║
╚═════════════════════════════════════════════╝
```

## Compliance Framework Card ASCII Layout

```
╔═════════════════════════════════════════════╗
║  COMPLIANCE FRAMEWORK           🏛️ NIST-01  ║
╠═════════════════════════════════════════════╣
║                                             ║
║  NIST CSF: IDENTIFY FUNCTION                ║
║                                             ║
╠═════════════════════════════════════════════╣
║  Framework: NIST Cybersecurity Framework    ║
║  Standard:  5 Core Functions                ║
║  Relevance: US Federal, Critical Infra,     ║
║             Government Contractors          ║
║  Maturity:  ★★★★☆ (4/5 - Mature)           ║
╠═════════════════════════════════════════════╣
║  ASSESSMENT FOCUS:                          ║
║  Knowing what systems/data you have and     ║
║  what risks they face.                      ║
║                                             ║
║  Key Questions:                             ║
║  • Asset inventory: What systems exist?     ║
║  • Data classification: What's sensitive?   ║
║  • Risk assessment: What could go wrong?    ║
║  • Threat intelligence: Realistic threats?  ║
╠═════════════════════════════════════════════╣
║  [OPTIONAL IMAGE SPACE - 2" x 2"]           ║
║                                             ║
╠═════════════════════════════════════════════╣
║  MATURITY LEVELS:                           ║
║  ⭐ (1): No asset inventory, no risk        ║
║          assessment                         ║
║  ⭐⭐ (2): Partial inventory, informal       ║
║           risk assessment                   ║
║  ⭐⭐⭐ (3): Complete inventory, documented  ║
║            risk assessment                  ║
║  ⭐⭐⭐⭐ (4): Regularly updated, annual      ║
║              reviews                        ║
║  ⭐⭐⭐⭐⭐ (5): Real-time visibility,        ║
║               continuous assessment        ║
╠═════════════════════════════════════════════╣
║  TYPICAL FINDINGS:                          ║
║  ⚠️ Unknown systems (shadow IT)             ║
║  ⚠️ Unclassified data                       ║
║  ⚠️ Missing risk assessment                 ║
║  ⚠️ Risk assessment not updated             ║
║  ⚠️ No threat modeling                      ║
╠═════════════════════════════════════════════╣
║  REMEDIATION STEPS:                         ║
║  1. Deploy discovery tools (find systems)   ║
║  2. Create data classification policy       ║
║  3. Conduct annual risk assessment          ║
║  4. Implement asset management system       ║
║  5. Integrate threat intelligence           ║
╠═════════════════════════════════════════════╣
║  RELATED FRAMEWORKS:                        ║
║  • CIS Controls (general security)          ║
║  • ISO 27001 (international standard)       ║
║  • HIPAA (healthcare)                       ║
║  • PCI-DSS (payment cards)                  ║
╠═════════════════════════════════════════════╣
║  KEYWORDS: NIST | Identify | Asset          ║
║  | Inventory | Risk | Data classification   ║
╚═════════════════════════════════════════════╝
```

---

# Universal Card Elements

## Icons Used Across All Cards

| Icon | Meaning | Used In |
|------|---------|---------|
| ⚔️ | Attack/Threat | Threat Cards, Pentester Tactics |
| 🛡️ | Defense/Protection | Defense Cards |
| 🛠️ | Action/Tool | Crisis Action Cards |
| 📅 | Event/Timeline | Event Cards |
| 💾 | Server/System | Server Cards |
| 🔒 | Security | Security Device Cards |
| 📋 | Assessment/Audit | Audit Domain Cards |
| 🏛️ | Framework/Standard | Compliance Framework Cards |
| ★★★☆☆ | Rating/Effectiveness | Any card with scoring |
| ▓▓░░░ | Visual bar indicator | Difficulty, Severity, Complexity |
| ✓ | Positive/Supported | Synergies, defenses |
| ⚠️ | Warning/Risk | Consequences, limitations |

## Text Formatting Standards

```
**BOLD TITLES**     = Card names and section headers
_Italic Text_      = Flavor text, narrative descriptions
UPPERCASE          = Keywords, field names
`Code blocks`      = Technical terms, configuration names
► Bullet points    = Lists of items
[BRACKETS]         = Optional elements
```

## Field Organization

All cards should follow this general structure:
1. Card type & identifier (top)
2. Title (prominent)
3. Metadata (type, cost, difficulty, etc.)
4. Flavor/descriptive text (narrative)
5. [Optional image space]
6. Rules/mechanics text
7. Interactions (what this card works with)
8. Outcomes or implementation
9. Keywords (bottom)

---

# Creating New Cards: Step-by-Step

## 1. Choose Your Card Type
Determine which type of card you're creating (Threat, Defense, Event, etc.)

## 2. Select Template
Copy the appropriate ASCII template from this document

## 3. Fill in Core Fields
- **Title:** 1-3 words, clear and memorable
- **Identifier:** Use next sequential ID (T-09, D-25, etc.)
- **Metadata:** Cost, difficulty, type, vectors
- **Flavor Text:** Write as if describing to players
- **Rules Text:** Explain mechanics clearly

## 4. Define Interactions
- What does this card synergize with?
- What does it counter?
- What counters it?
- Cross-reference other cards

## 5. Test Clarity
- Can someone unfamiliar with the card understand it?
- Is the teaching point clear?
- Is the balance appropriate?
- Does it fit with existing cards?

## 6. Proofread & Format
- Check spelling and grammar
- Ensure consistent formatting
- Verify all cross-references
- Test ASCII art alignment

## 7. Submit for Feedback
- Share with module designers
- Get playtester feedback
- Iterate based on testing
- Balance with existing cards

---

# Card Printing Guidelines

## Paper Specifications
- **Cardstock Weight:** 250 gsm (minimum)
- **Finish:** Matte or satin (reduces glare)
- **Size:** Standard poker card (2.5" × 3.5")
- **Margins:** 0.125" on all sides

## Color Coding by Card Type

```
Threat Cards       = Red border (#8B0000)
Defense Cards      = Blue border (#004080)
Pentester Tactics  = Red with black accent
Events            = Orange/Yellow border (#FF6B35)
Crisis Actions    = Green/Teal border (#008080)
Network Cards     = Purple border (#663399)
Audit Cards       = Gray/Brown border (#4A4A4A)
```

## Image Specifications (Optional)

If including artwork:
- **Resolution:** 300 DPI minimum
- **Size:** 2" × 2" recommended
- **Format:** PNG or JPG with transparent background
- **Color Space:** RGB (for printing: convert to CMYK)
- **Suggested Elements:**
  - Icon/symbol representing card concept
  - Subtle background (doesn't interfere with text)
  - Cybersecurity theme (locks, networks, etc.)

---

# Contributing New Cards

## Submission Checklist

- [ ] Card follows template structure
- [ ] All required fields filled in
- [ ] Cross-references verified
- [ ] Balanced with existing cards
- [ ] Teaching point is clear
- [ ] Keywords are relevant
- [ ] ASCII art is properly aligned
- [ ] Flavor text is engaging
- [ ] Interactions are documented
- [ ] Module compatibility confirmed

## Submission Format

Submit as markdown file with:
1. Card type header
2. Complete card content
3. Any balance notes
4. Playtesting results
5. Cross-references to other cards

## Questions?

See [CONTRIBUTING.md](../../CONTRIBUTING.md) for full contribution guidelines.

---

# Appendix: Quick Reference

## Card Type Summary

| Type | Count | Cost | Difficulty | Module |
|------|-------|------|------------|--------|
| Threat Cards | 12 core + 8 exp | — | DC 10-15 | IR |
| Defense Cards | 24 core (shared) + 19 exp | 10/15/25 | — | IR, Hardening |
| Pentester Tactics | 8 core + 8 exp | — | DC 12-16 | Hardening |
| Crisis Actions | 13 | 0-20 | — | DR |
| Event Cards | 12 core (6 Scheduled + 6 Triggered) | — | — | DR |
| Stakeholder Cards | 5 | — | — | DR |
| Crisis Scenarios | 8 exp | — | — | DR |
| Server Cards | 10 core + 8 exp (legacy + cloud) | 3-15 | — | NB |
| Security Devices | 10 core | 6-15 | — | NB |
| Architecture Cards | 5 | 0-12 | — | NB |
| Asset Cards | 8 | — | — | NB |
| Business Requirements | 20 (standalone) | — | — | NB |
| Operational Events | 16 (standalone) | — | — | NB |
| Investigation Cards | 12 | 5-20 | DC 11-15 | Forensics |
| Evidence Cards | 12 | — | — | Forensics |
| Findings Cards | 4 | — | — | Forensics |
| Audit Domains | 6 | — | — | A&C |
| Frameworks | 11 exp (5 NIST + 3 CIS + 3 PCI) | — | — | A&C |
| Remediation Actions | 8 exp | 3-15 | — | A&C |

---

*Last Updated: October 2025*
*Version: 1.0*
*For contributions, see: CONTRIBUTING.md*
