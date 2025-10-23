# Forensics Module: Rules & Mechanics

**Version:** 2.1 - Investigation & Attribution Edition
**Last Updated:** October 2025

---

## Module Overview

The **Forensics Module** teaches incident investigation, digital forensics, and attack attribution. This module is typically entered after Incident Response or Disaster Recovery (representing the investigation phase of response) but can also be played standalone to teach forensic analysis concepts.

Rather than detecting the attack or managing the crisis, Forensics focuses on the crucial post-breach investigation phase:
- **Evidence collection** and preservation
- **Timeline reconstruction** of attacker actions
- **Attack chain analysis** linking findings to MITRE ATT&CK techniques
- **Attribution and threat intelligence** (who did this and how?)
- **Attack surface analysis** (how did they get in?)
- **Lessons learned** for future hardening and network building

### Educational Purpose

**Phase 1 (Incident Response):** Teaches proactive threat detection
**Phase 2 - Hardening (Win):** Teaches proactive defense
**Phase 2 - Disaster Recovery (Lose):** Teaches crisis management
**Phase 3 - Forensics (Sequential):** Teaches investigation and learning

Forensics can also be played **standalone** to teach forensic methodology without the preceding modules.

---

## Module Purpose & Integration

### When Forensics Occurs

**In Campaign Play:**
1. After **Incident Response** failure (undetected breach) → Forensics Phase
2. After **Disaster Recovery** (crisis management) → Forensics Phase
3. After **Hardening** success (discovered attack) → Optional Forensics for deeper learning

**In Standalone Play:**
- Forensics module can be played independently as a 45-90 minute investigation scenario

### Forensics Feeds Into Other Modules

**Outputs from Forensics:**
- **Attack Chain Reconstruction:** Detailed understanding of how attacker progressed
- **Vulnerability Discovery:** Systems and methods exploited
- **Threat Intelligence:** IOCs (Indicators of Compromise), malware samples, attacker infrastructure
- **Timeline Evidence:** When each compromise occurred

**Used In:**
- **Hardening Module:** "Build defenses against the techniques discovered in forensics"
- **Network Building Module:** "Redesign network architecture knowing how attacker pivoted"
- **Audit & Compliance Module:** "Assess coverage of controls that should have detected forensic findings"

---

## Forensics Module Setup

### Prerequisites for Forensics Phase

**Trigger Options:**

1. **Sequential (After IR/DR):** Team completed Incident Response or Disaster Recovery
   - Card descriptions reveal attack chain that was discovered or undetected
   - Blue Team now investigates for attribution and deeper understanding

2. **Standalone Setup:** Team starts fresh investigation (no prior IR/DR)
   - Threat Orchestrator secretly selects 1-2 complete attack chains
   - Blue Team investigates to discover and reconstruct the attack

### Discovery & Revelation (Sequential Play)

When entering Forensics after IR or DR, the **Threat Orchestrator reveals the attack context:**

**Example (After IR Success):**
"Your security team detected and contained an attack chain:
1. Phishing email (SOCIAL ENGINEERING)
2. Credential harvesting malware (MALWARE)
3. Lateral movement to admin account (CREDENTIAL ABUSE)

Now you investigate to understand: How deep did they get? Are there other persistence mechanisms? Can we attribute this to a known threat group?"

**Example (After DR/IR Failure):**
"Forensic examination of compromised systems reveals:
1. Initial access via credential stuffing (CREDENTIAL ABUSE)
2. Privilege escalation via unpatched service (WEB EXPLOIT)
3. Persistence through scheduled task modification (MALWARE)
4. Data exfiltration via DNS tunneling (DATA EXFIL)

Now you reconstruct the complete timeline and attribute the attack."

---

## Forensics Module Components

### Card Types Specific to Forensics

#### Investigation Action Cards (6-8 cards)

These represent forensic investigation techniques and evidence collection methods.

**Standard Investigation Actions:**

| Card | Technique | DC | Cost | Time | Result |
|------|-----------|----|----|------|--------|
| **DISK-01** | Disk Image & Analysis | 12 | 10 | 2 turns | Recover deleted files, malware samples |
| **DISK-02** | File System Carving | 14 | 15 | 3 turns | Deep file recovery, hidden artifacts |
| **MEM-01** | Memory Dump & Analysis | 13 | 15 | 2 turns | Volatile process info, injected code |
| **MEM-02** | Memory Forensics Deep Dive | 15 | 20 | 3 turns | Malware behavior, command-and-control |
| **LOG-01** | Event Log Analysis | 11 | 5 | 1 turn | Timeline of user actions, logins |
| **LOG-02** | Deep Log Correlation | 13 | 10 | 2 turns | Cross-system timeline, attack sequence |
| **NET-01** | Network Traffic Analysis | 12 | 10 | 2 turns | Exfiltration evidence, C2 communications |
| **NET-02** | Packet Capture Deep Analysis | 14 | 15 | 3 turns | Protocol-level forensics, attacker tools |
| **MALW-01** | Malware Analysis (Dynamic) | 12 | 15 | 2 turns | Behavior analysis, IOCs |
| **MALW-02** | Malware Analysis (Static) | 14 | 10 | 2 turns | Code reverse engineering, capabilities |
| **TIMELINE-01** | Timeline Reconstruction | 13 | 5 | 1 turn | Chronological attack sequence |
| **THREAT-01** | Threat Attribution Analysis | 15 | 20 | 3 turns | Link to known groups, TTPs |

**Investigation Action Card Structure:**
- **Title:** e.g., "Disk Image & Analysis"
- **Technique:** MITRE ATT&CK reference (e.g., "Forensic Analysis")
- **Difficulty Class (DC):** Roll d20+modifiers vs. this number to succeed
- **Cost:** Budget required to perform investigation
- **Duration:** Number of turns this investigation takes
- **What It Reveals:** Type of evidence discovered (see Evidence Cards below)
- **Success Condition:** d20+forensics_skill vs. DC (11+ usually succeeds, but higher DC cards reward skilled investigators)

---

#### Evidence Cards (8-12 cards)

These represent specific findings from investigations. They document what was discovered and provide investigative leads.

**Categories of Evidence:**

**A. Malware & Persistence**
- Trojan samples with capabilities (spyware, RAT, backdoor)
- Persistence mechanisms (scheduled tasks, registry modifications, startup folders)
- Rootkits or bootkits
- Memory-resident malware signatures

**B. Compromised Credentials**
- Admin account compromise timeline
- Service account abuse
- API token theft
- SSH key exposure

**C. Lateral Movement Artifacts**
- Pass-the-hash evidence
- Kerberos ticket forgery evidence
- Tools used for pivoting
- Systems accessed with each credential

**D. Exfiltration Evidence**
- Volume of data exfiltrated
- File types extracted
- Destination IP addresses or domains
- Timing of exfiltration windows

**E. Attack Infrastructure**
- Command-and-control servers
- Malware staging servers
- Attacker email addresses or usernames
- Registrar information (domain registration)
- ASN and geolocation data

**F. Timeline Markers**
- First suspicious activity timestamp
- Lateral movement progression
- Exfiltration start/stop times
- Attacker "dwell time" in network
- Containment points

**Evidence Card Structure:**
- **Title:** Specific finding (e.g., "Credential Dumper Malware")
- **Type:** Category (Malware, Persistence, Credentials, Movement, Exfiltration, Infrastructure, Timeline)
- **MITRE ATT&CK Technique:** Referenced technique (e.g., T1003 - OS Credential Dumping)
- **Description:** What was found and where
- **Investigation Source:** Which Investigation Action card led to this
- **Investigative Lead:** What the Blue Team can do with this information
- **Connection to Attack Chain:** Links back to specific Threat cards from IR phase (if sequential)

---

#### Findings Cards (3-4 cards)

These represent the conclusions of the forensic investigation and feed into recommendations.

**Finding Types:**

| Finding | Description | Feeds Into Module |
|---------|-------------|------------------|
| **THREAT-ATTRIBUTION** | Identified attacker group, techniques, motivations | Audit & Compliance (threat model) |
| **ATTACK-SURFACE** | Systems/methods exploited; entry points identified | Network Building, Hardening |
| **PERSISTENCE-ANALYSIS** | How attacker maintained access; backdoors identified | Hardening (remove persistence) |
| **DATA-IMPACT** | Exact scope of data compromise; exposure risk | Disaster Recovery (notification scope) |
| **CONTROL-GAPS** | Which security controls failed to detect/prevent | Audit & Compliance (control improvement) |

---

### Game Materials Required (Forensics-Specific)

**Physical Components:**
- Investigation Action cards (12 cards)
- Evidence cards (12 cards)
- Findings cards (4 cards)
- Turn Tracker (8-15 turns typical)
- Budget Tracker (Investigation budget: 0-150)
- Progress Meters (see below):
  - Timeline Completeness (0-100%)
  - Attack Chain Reconstruction (0-100%)
  - Attribution Confidence (0-100%)
  - Evidence Chain of Custody (0-100%)

**Optional:**
- Investigation Flow Chart (showing how actions lead to evidence discovery)
- MITRE ATT&CK Technique reference sheet
- Evidence correlation board (physical board or spreadsheet linking evidence)

---

## Forensics Module Mechanics

### Game Length & Difficulty

**Turn Structure:**
- **Easy (TIER 1):** 6-8 turns | Simple attack, few pivot points, obvious artifacts
- **Medium (TIER 2):** 8-10 turns | Standard breach with some obfuscation
- **Hard (TIER 3):** 11-13 turns | Complex attack, sophisticated attacker, limited logging
- **Expert (TIER 4):** 14-15 turns | APT-level sophistication, anti-forensics measures, encrypted communications

**Turn Length Determination:**
Using the **Variable Turn Length System** (see Core Rules):
1. Threat Orchestrator selects attack complexity tier
2. Roll d4 for variation (-1, 0, 0, +1)
3. Announce final turn count to Blue Team

**Investigation Budget:**
- **Starting Budget:** 75 (represents forensic lab time, tools, personnel)
- **Optional Bonus:** +25 if company has cyber insurance or threat intelligence subscription
- **Maximum Useful Budget:** 150 (after which budget constraint is not limiting factor)

---

### Action System

Each turn, the Blue Team performs ONE of these actions:

#### Action A: Conduct Investigation 🔍

**Description:** The team describes a specific forensic investigation they want to perform.

**Mechanics:**
1. **Choose Investigation Card:** Select from available Investigation Action cards (Disk, Memory, Logs, Network, Malware, Timeline, or Attribution)
2. **Pay Cost:** Spend Budget equal to card cost
3. **Roll:** d20 + relevant skill modifier vs. Difficulty Class on card
   - **Modifiers:**
     - +2 if team has forensics background
     - +1 if prior Investigation Action revealed clues to this technique
     - +1 if team provides detailed narrative explanation of investigation approach
     - -2 if investigation is being done hastily (using extra turn pressure to rush)
4. **Check Results:**
   - **Success (roll ≥ DC):** Discover ONE Evidence card + advance Progress Meters
   - **Partial Success (roll DC-3 to DC-1):** Discover PARTIAL Evidence (partial timeline, hints of compromise, etc.)
   - **Failure (roll < DC-3):** No Evidence discovered this turn; Budget still spent

**Progress Meter Advancement:**
Each successful Investigation Action advances one or more Progress Meters:
- **Timeline Completeness** (+10-20%): Evidence that establishes temporal sequence
- **Attack Chain Reconstruction** (+10-20%): Evidence linking attacker actions together
- **Attribution Confidence** (+10-20%): Evidence pointing to threat actor identity
- **Evidence Chain of Custody** (+5-10%): Each evidence card documented properly

**Example Investigation:**

> **Blue Team:** "We want to conduct a disk image and analysis of the compromised server."
> **Cost:** 10 Budget
> **DC:** 12
> **Blue Team Roll:** d20 + 2 (forensics background) = 15
> **Result:** Success! Discover evidence card "Credential Dumper Malware" + 15% Timeline Completeness

---

#### Action B: Analyze Existing Evidence 📊

**Description:** The team reviews evidence cards already discovered and makes connections.

**Mechanics:**
1. **Review Evidence:** Team looks at 2-4 Evidence cards already discovered
2. **Make Connection:** Team describes how findings are related (temporal, technical, or attribution-based)
3. **Roll:** d20 + relevant skill vs. DC 10
   - **Modifiers:**
     - +2 if team connects 3+ evidence cards in coherent narrative
     - +1 if connection references specific MITRE ATT&CK technique
4. **Check Results:**
   - **Success (roll ≥ 10):** Gain insight; advance two Progress Meters by 5-10% each
   - **Failure (roll < 10):** No progress; action still costs a turn (represents time spent on dead-end analysis)

**Example Analysis:**

> **Blue Team:** "The malware sample found in memory matches the persistence mechanism in the scheduled task, suggesting the attacker uploaded the same tool twice. This indicates they knew what they were doing and weren't just randomly exploring."
> **Roll:** d20 + 2 (good narrative) = 16
> **Result:** Success! +10% Attribution Confidence (skilled attacker), +10% Attack Chain Reconstruction (coordinated multi-stage attack)

---

#### Action C: Follow Investigative Lead 🔗

**Description:** Based on existing evidence, the team pursues a specific investigative thread.

**Mechanics:**
1. **Choose Evidence Card:** Pick an Evidence card with an "Investigative Lead"
2. **Describe Approach:** How will the team pursue this lead? (e.g., "Track the C2 domain to registrar records to find other registered domains")
3. **Roll:** d20 + relevant skill vs. DC (varies 11-14 depending on lead)
4. **Check Results:**
   - **Success:** Discover a new Evidence card directly related to the lead + advance Attribution Confidence 20%
   - **Partial Success:** Discover related evidence but get a false lead (discover 1 Evidence + 1 Red Herring card)
   - **Failure:** Dead-end lead; use turn without discovering evidence

**Example Lead:**

> **Evidence Card:** "Command-and-Control Communications (IP: 203.0.113.45)"
> **Investigative Lead:** "Perform ASN and WHOIS lookup to find other infrastructure operated by this attacker"
> **Blue Team:** "Let's trace the IP's ASN and registrar records to find other malicious domains."
> **Cost:** 10 Budget
> **Roll:** d20 + 1 (good idea) = 14 vs. DC 12
> **Result:** Success! Discover "Attacker Infrastructure Map" evidence card + 20% Attribution Confidence

---

### Victory & Failure Conditions

#### Investigation Complete (Victory)

The Blue Team achieves one of these:

**Condition 1: High Attribution Confidence**
- **Attribution Confidence ≥ 90%** (identified threat actor, techniques, likely motivations)
- Plus **Attack Chain Reconstruction ≥ 75%** (understand progression of attack)
- **Outcome:** "Your investigation successfully attributes this attack to [Known Threat Group]. Security intelligence briefing prepared."

**Condition 2: Complete Timeline & Evidence**
- **Timeline Completeness ≥ 80%** (clear chronological sequence)
- Plus **Attack Chain Reconstruction ≥ 80%** (all major compromise points identified)
- Plus **Evidence Chain of Custody ≥ 70%** (documented, admissible evidence)
- **Outcome:** "Your forensic report is publishable quality and defensible in court. Law enforcement briefed."

**Condition 3: Budget Exhausted but Sufficient Progress**
- Ran out of Budget before Turn limit expired
- BUT achieved **any two Progress Meters ≥ 70%**
- **Outcome:** "Investigation concluded. Findings are actionable for hardening and threat intelligence."

#### Investigation Inconclusive (Failure)

The Blue Team fails if they reach Turn limit with:
- **Any Progress Meter < 40%** (incomplete investigation)
- Plus no coherent findings to act on
- **Outcome:** "Investigation stalled. Critical questions remain unanswered. Threat actor unattributed."

**Penalty for Inconclusive Investigation:**
- Cannot feed findings into Hardening or Network Building modules
- Audit & Compliance module must assess with incomplete information
- Reduced confidence in future threat intelligence

---

### Special Forensics Rules

#### Rule 1: Chain of Custody Tracking

Every Evidence card must be documented to maintain admissibility in legal proceedings.

**How It Works:**
- When an Evidence card is discovered, mark how it was obtained (which Investigation Action)
- If chain of custody is broken (evidence obtained illegally or improperly), it becomes inadmissible
- Inadmissible evidence **cannot** be used for Attribution or Timeline building
- **Cost to fix broken chain:** 5 Budget + 1 turn to re-document evidence

**Example:**
> Evidence "Admin Credentials Exfiltrated" discovered via "Memory Dump Analysis" (legal). Chain of custody: intact. Can be used in court.
> But if same evidence discovered via "Unauthorized System Access" by Blue Team (illegal), chain is broken and evidence is inadmissible.

---

#### Rule 2: Anti-Forensics Techniques

More sophisticated attacks may include **anti-forensics** measures that complicate investigation.

**Anti-Forensics Examples:**
- Log deletion or manipulation
- Encrypted communication channels
- Malware that overwrites disk sectors
- Timeline obfuscation (backdated files, timezone manipulation)

**How It Works:**
- Threat Orchestrator can note that certain Investigation Actions are **harder** due to anti-forensics
- Affected Investigation Cards gain **+2 DC penalty** if anti-forensics present
- Example: "Evidence logs were deleted. Log Analysis now has DC 15 instead of 11."

**Overcoming Anti-Forensics:**
- Investigators can use advanced techniques (Memory Forensics, Network Traffic Analysis) that bypass deleted logs
- Alternatively, **combine multiple Investigation Actions** to corroborate timeline from different sources
- Example: "Timeline can't be built from deleted logs, but network traffic shows exfiltration at 2:15 AM, and memory analysis shows C2 connection at 2:10 AM. We can reconstruct it."

---

#### Rule 3: Attacker Dwell Time

Represents how long the attacker remained in the network before detection or expulsion.

**Mechanics:**
- **Dwell Time = Turn count - Detection Turn** (calculated at end of game)
- Longer dwell time = more data exfiltrated, more persistence mechanisms installed, harder to attribute
- **Impact on Evidence Discovery:**
  - Each week of dwell time in network = +1 DC to Investigation Actions (more time to cover tracks)
  - But also = more evidence (more actions, more forensic artifacts)

**Example:**
> Attack detected on Turn 3 → Investigation begins Turn 4
> Dwell Time = 3 turns (represents ~1 week based on timeline)
> Investigation Actions have +1 DC modifier
> But Blue Team discovers more Evidence cards (+2 cards total) due to attacker's extended activity

---

#### Rule 4: Incomplete Evidence

Some investigations may yield **partial or fragmentary evidence** that requires interpretation.

**How It Works:**
- Partial success on Investigation roll = discover Evidence card marked "INCOMPLETE"
- INCOMPLETE Evidence provides +1 Progress Meter advance but is NOT admissible alone for conclusions
- Team can **retry investigation** next turn to complete the evidence (costs full Budget again)
- Or team can **interpret incomplete evidence** by rolling d20+investigator skill vs. DC 12
  - Success: Use incomplete evidence as-is (risky but saves Budget)
  - Failure: Incomplete evidence leads to false conclusion (Red Herring card added)

---

### Forensics Skill Modifiers

**Base Skill Modifiers (apply to all Investigation rolls):**

| Background | Modifier | Example |
|-----------|----------|---------|
| Forensic Analyst or Incident Responder | +2 | Person with formal training |
| IT Security or System Administrator | +1 | Technical background but not formal IR training |
| General IT | +0 | Basic tech knowledge |
| Non-Technical | -2 | No technical background |
| Forensics Researcher (GIAC GCFE, etc.) | +3 | Expert-level investigator |

**Situational Modifiers:**
- **+1:** Detailed narrative explanation of investigation methodology
- **+2:** Team describes investigation approach that references MITRE ATT&CK framework
- **+1:** Prior Investigation Action discovered clues to current investigation
- **-1:** Using hastily (team taking Forensics as last-ditch effort in final turn)
- **-2:** Investigation approach is technically unsound or unrealistic

---

## Forensics Module Standalone Setup

When playing Forensics as a standalone game (without prior IR/DR):

### Setup Steps

1. **Threat Orchestrator Preparation (Secret):**
   - Select attack scenario complexity (TIER 1-4)
   - Roll d4 for turn variation (-1, 0, 0, +1)
   - Secretly choose 3-5 Threat cards from core deck or expansions
   - Arrange threat cards in logical attack progression
   - Note which investigation techniques would discover each threat

2. **Blue Team Briefing:**
   > "You've been called to investigate a data breach discovered during routine system maintenance. Initial assessment:
   > - Critical database server accessed 2 weeks ago
   > - 5 million customer records potentially compromised
   > - Attacker origin and motivations unknown
   > - You have [TURN COUNT] turns to reconstruct the attack and find attribution clues.
   > - Starting Budget: 75 (or 100 for well-funded incident response team)"

3. **Available Actions:**
   - Conduct Investigation (as normal)
   - Analyze Existing Evidence
   - Follow Investigative Leads

4. **Victory Condition:**
   - Achievement of any one complete Progress Meter (≥90%) + one partial meter (≥70%)
   - Or completion of investigation with actionable findings before turn limit

---

## Module Combinations with Forensics

### Recommended Sequences

**Sequence 1: Detect & Investigate (90 minutes)**
- Incident Response (45 min) - Detect attack chain
- Forensics (45 min) - Investigate and attribute

**Sequence 2: Failure & Investigation (120 minutes)**
- Incident Response (45 min) - Fail to detect all threats
- Disaster Recovery (45 min) - Manage breach crisis
- Forensics (30 min) - Investigate for lessons learned

**Sequence 3: Complete Lifecycle (180+ minutes)**
- Network Building (45 min) - Design initial network
- Hardening (45 min) - Build defenses
- Incident Response (45 min) - Test defenses
- Disaster Recovery (45 min) - Handle failure
- Forensics (30 min) - Investigate findings
- Audit & Compliance (30 min) - Assess overall security posture

---

## Debrief & Learning Outcomes

### Post-Game Discussion Questions

After Forensics concludes, facilitate discussion around these questions:

**Investigation Process:**
1. What investigation techniques were most revealing? Why?
2. What evidence was most critical to understanding the attack?
3. What was the attacker's most sophisticated technique? What made it hard to detect forensically?
4. How would the investigation have been different with better logging? Better endpoint tools?

**Attribution & Intelligence:**
1. What threat actor profile emerged? What's their likely motivation?
2. What geographic or geopolitical clues do you see in the evidence?
3. How would you share this intelligence with law enforcement or information sharing communities?

**Hardening & Prevention:**
1. Based on forensic findings, what specific defenses would prevent this attack?
2. How would you network design need to change to limit lateral movement?
3. What logging and monitoring would have caught this earlier?

**Real-World Connection:**
1. How does this scenario compare to actual breaches you've studied? (VERIZON DBIR, Microsoft Security Incidents, etc.)
2. What's the typical cost of forensic investigation in real incidents?
3. How does attribution accuracy impact threat intelligence and policy response?

---

## Technical Details & Implementation Notes

### MITRE ATT&CK Integration

Each Investigation Action card and Evidence card should reference specific MITRE ATT&CK techniques/procedures:

**Investigation Actions → Techniques Discovered:**
- Disk Forensics → T1005 (Data Staged), T1025 (Data from Removable Media)
- Memory Forensics → T1112 (Modify System Image), T1187 (Forced Authentication)
- Log Analysis → T1071 (Application Layer Protocol), T1090 (Proxy)
- Network Analysis → T1041 (Exfiltration Over C2), T1048 (Exfiltration Over Alternative Protocol)
- Malware Analysis → T1104 (Multi-Stage Channels), T1059 (Command and Scripting Interpreter)
- Timeline Reconstruction → T1005 (Data Staged), T1003 (OS Credential Dumping)
- Attribution → S0xxx group identification (Software attribution)

### Forensics Difficulty Scaling

**TIER 1 (6-8 turns):** Unsophisticated attacker, plenty of artifacts, obvious malware
- Low DC (10-12) Investigation Actions
- Evidence cards plentiful and obvious
- Chain of custody intact
- No anti-forensics measures
- **Example:** Script kiddie using public exploits, little cleanup

**TIER 2 (8-10 turns):** Standard attacker, some cleanup, moderate sophistication
- Medium DC (12-14) Investigation Actions
- Evidence cards present but require analysis
- Some chain of custody concerns
- Basic anti-forensics (log deletion)
- **Example:** Credential theft ring, lateral movement, data exfil

**TIER 3 (11-13 turns):** Sophisticated attacker, significant obfuscation
- High DC (13-15) Investigation Actions
- Evidence requires correlation across multiple sources
- Chain of custody significant challenge
- Advanced anti-forensics (encryption, timeline spoofing)
- **Example:** APT group with operational security discipline

**TIER 4 (14-15 turns):** Nation-state or elite attackers, expert anti-forensics
- Very high DC (14-16+) Investigation Actions
- Evidence heavily fragmented and incomplete
- Chain of custody nearly impossible to prove
- Sophisticated anti-forensics and counter-attribution
- **Example:** State-sponsored APT with deep technical expertise

---

## Printable Card Templates

See [cards/forensics/core-deck/investigation-cards.md](../../cards/forensics/core-deck/investigation-cards.md) for printable Investigation Action cards.

See [cards/forensics/core-deck/evidence-cards.md](../../cards/forensics/core-deck/evidence-cards.md) for printable Evidence and Findings cards.

---

## Version History

- **v2.1** (Current) - Investigation & Attribution Edition
  - Introduced Forensics as 6th module
  - Added Investigation Action cards with skill checks
  - Integrated MITRE ATT&CK technique mapping
  - Added Progress Meter system (Timeline, Attribution, Reconstruction, Chain of Custody)
  - Included Chain of Custody rules for legal admissibility
  - Added anti-forensics rule for difficulty scaling
  - Standalone and sequential play modes

---

## Quick Reference

**Setup:** Select complexity tier, roll d4, announce turn count
**Actions:** Conduct Investigation, Analyze Evidence, Follow Leads
**Rolls:** d20 vs. DC, with skill modifiers
**Resources:** Budget (75 base), Turns (6-15), Progress Meters (4 tracked)
**Victory:** Attribution ≥90% OR Timeline + Chain of Custody ≥80% combined
**Failure:** Any meter <40% at turn limit = Inconclusive

