# Forensics Module: Rules & Mechanics

**Version:** 2.2 - Playtest Edition (rule changes marked "(v2.2)"; see [v2.2 Playtest Edition Changes](#v22-playtest-edition-changes))
**Last Updated:** July 2026

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

**Incident Response:** Teaches proactive threat detection
**Hardening (typically after an IR win):** Teaches proactive defense
**Disaster Recovery (typically after an IR loss):** Teaches crisis management
**Forensics (after IR or DR):** Teaches investigation and learning

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

#### Investigation Action Cards (12 cards)

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

*DISK-01 rush option (v2.2): pay +5 Budget (15 total) to run it at Duration 1.*

**Investigation Action Card Structure:**
- **Title:** e.g., "Disk Image & Analysis"
- **Technique:** MITRE ATT&CK reference (e.g., "Forensic Analysis")
- **Difficulty Class (DC):** Roll d20+modifiers vs. this number to succeed
- **Cost:** Budget required to perform investigation
- **Duration:** Number of turns this investigation takes
- **What It Reveals:** Type of evidence discovered (see Evidence Cards below)
- **Success Condition:** d20+forensics_skill vs. DC (11+ usually succeeds, but higher DC cards reward skilled investigators)

**Investigation Duration (v2.2):** Starting an investigation with Duration N occupies your action on the turn you start it (pay the Budget cost then). Count the turn you start it as turn 1: the results (evidence + meter advances) arrive — and the roll is made — at the START of turn N. So Duration 1 resolves immediately on the same turn; Duration 2 resolves at the start of the following turn; Duration 3 resolves two turns after starting. Only ONE multi-turn (Duration 2+) investigation may be in flight at a time, but you may take other actions (Analyze Evidence, Follow Lead, or a Duration 1 investigation) while waiting.

---

#### Evidence Cards (12 cards)

These represent specific findings from investigations. They document what was discovered and provide investigative leads.

**Categories of Evidence (core deck counts):**

**A. Malware & Persistence (4 cards: EVD-01, EVD-03, EVD-08, EVD-10)**
- Trojan samples with capabilities (spyware, RAT, backdoor)
- Persistence mechanisms (scheduled tasks, registry modifications, startup folders)
- Encryption keys recovered from malware or memory
- Malware behavior profiles from sandbox analysis

**B. Credentials & Access (1 card: EVD-04)**
- Admin account compromise timeline
- Suspicious logins from unusual times, locations, or sources

**C. Lateral Movement (1 card: EVD-05)**
- Pass-the-hash evidence
- Tools used for pivoting
- Systems accessed with each credential

**D. Exfiltration (1 card: EVD-06)**
- Volume of data exfiltrated
- File types extracted
- Destination IP addresses or domains
- Timing of exfiltration windows

**E. Attack Infrastructure (2 cards: EVD-02, EVD-07)**
- Command-and-control servers
- Malware staging servers
- Registrar information (domain registration)
- ASN and geolocation data

**F. Attack Activity (3 cards: EVD-09, EVD-11, EVD-12)**
- Attacker command history
- File staging artifacts (what was collected before exfiltration)
- Anti-forensics evidence (log deletion, timestamp manipulation)

**Evidence Card Structure:**
- **Title:** Specific finding (e.g., "Credential Dumper Malware")
- **Type:** Category (Malware, Persistence, Credentials, Movement, Exfiltration, Infrastructure, Timeline)
- **MITRE ATT&CK Technique:** Referenced technique (e.g., T1003 - OS Credential Dumping)
- **Description:** What was found and where
- **Investigation Source:** Which Investigation Action card led to this
- **Investigative Lead:** What the Blue Team can do with this information
- **Connection to Attack Chain:** Links back to specific Threat cards from IR phase (if sequential)

---

#### Findings Cards (4 cards)

These represent the conclusions of the forensic investigation and feed into recommendations.

**Finding Types:**

| Finding | Description | Feeds Into Module |
|---------|-------------|------------------|
| **FIND-01: Threat Attribution Report** | Identified attacker group, techniques, motivations | Hardening, Audit & Compliance (threat model), Incident Response |
| **FIND-02: Attack Surface Analysis** | Systems/methods exploited; entry points identified | Network Building, Hardening, Audit |
| **FIND-03: Persistence Mechanisms Discovered** | How attacker maintained access; backdoors identified | Hardening (remove persistence), Disaster Recovery, Audit |
| **FIND-04: Investigative Gaps & Recommendations** | Questions answered vs. remaining; next steps | Audit & Compliance (post-incident review), Training |

---

### Game Materials Required (Forensics-Specific)

**Physical Components:**
- Investigation Action cards (12 cards)
- Evidence cards (12 cards)
- Findings cards (4 cards)
- Turn Tracker (8-15 turns typical)
- Budget Tracker (Investigation budget: 0-100)
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
- **Budget Tracker Range (v2.2):** 0-100 (75 base + 25 optional bonus is the maximum starting value)

---

### Action System

Each turn, the Blue Team performs ONE of these actions:

#### Action A: Conduct Investigation 🔍

**Description:** The team describes a specific forensic investigation they want to perform.

**Mechanics:**
1. **Choose Investigation Card:** Select from available Investigation Action cards (Disk, Memory, Logs, Network, Malware, Timeline, or Attribution)
2. **Pay Cost:** Spend Budget equal to card cost (paid on the turn you start the investigation)
3. **Resolve Duration (v2.2):** If Duration is 2+, the roll and results wait until the START of the turn the investigation completes (see Investigation Duration rule above)
4. **Roll:** d20 + relevant skill modifier vs. Difficulty Class on card
   - **Modifiers:**
     - +2 if team has forensics background
     - +1 if prior Investigation Action revealed clues to this technique
     - +1 if team provides detailed narrative explanation of investigation approach
     - -2 if investigation is being done hastily (using extra turn pressure to rush)
5. **Check Results:**
   - **Success (roll ≥ DC):** Discover ONE Evidence card — unless the card says otherwise (v2.2: MEM-02 and NET-02 award TWO) — and apply that Evidence card's printed meter impacts (see No Double Counting, Rule 5)
   - **Partial Success (roll DC-2 to DC-1):** Discover PARTIAL Evidence (partial timeline, hints of compromise, etc.) and apply the investigation card's partial-success advance line
   - **Failure (roll < DC-2):** No Evidence discovered this turn; Budget still spent

**Progress Meter Advancement:**
Each successful Investigation Action advances one or more Progress Meters. Typical advances are **+5-35%** per meter (major breakthroughs can exceed +20%):
- **Timeline Completeness** (+5-35%): Evidence that establishes temporal sequence
- **Attack Chain Reconstruction** (+5-35%): Evidence linking attacker actions together
- **Attribution Confidence** (+5-35%): Evidence pointing to threat actor identity
- **Evidence Chain of Custody**: advances via the Chain of Custody rule (v2.2, Rule 1) and the printed impacts on some Evidence cards

**Example Investigation:**

> **Blue Team:** "We want to conduct a disk image and analysis of the compromised server."
> **Cost:** 10 Budget (paid now). DISK-01 has Duration 2, so the team's action this turn is starting the imaging; results arrive at the start of the next turn.
> **DC:** 12
> **Blue Team Roll (at the start of the next turn):** d20 + 2 (forensics background) = 15
> **Result:** Success! Discover evidence card EVD-01 "Credential Dumper Malware" and apply its printed impacts: Attack Chain +15%, Attribution +10%, Timeline +10%. The team states the binary was hashed (SHA-256) before analysis: Chain of Custody +5% (v2.2)

---

#### Action B: Analyze Existing Evidence 📊

**Description:** The team reviews evidence cards already discovered and makes connections.

**Cost (v2.2):** 5 Budget. **Each Evidence card can be Analyzed only once (v2.2)** — mark cards as Analyzed when they are included in this action.

**Mechanics:**
1. **Pay Cost:** Spend 5 Budget (v2.2)
2. **Review Evidence:** Team looks at 2-4 not-yet-Analyzed Evidence cards already discovered
3. **Make Connection:** Team describes how findings are related (temporal, technical, or attribution-based)
4. **Roll:** d20 + relevant skill vs. DC 10
   - **Modifiers:**
     - +2 if team connects 3+ evidence cards in coherent narrative
     - +1 if connection references specific MITRE ATT&CK technique
5. **Check Results:**
   - **Success (roll ≥ 10):** Gain insight; advance two Progress Meters by 5-10% each
   - **Failure (roll < 10):** No progress; action still costs a turn (represents time spent on dead-end analysis)

**Example Analysis:**

> **Blue Team:** "The malware sample found in memory matches the persistence mechanism in the scheduled task, suggesting the attacker uploaded the same tool twice. This indicates they knew what they were doing and weren't just randomly exploring."
> **Roll:** d20 + 2 (good narrative) = 16
> **Result:** Success! +10% Attribution Confidence (skilled attacker), +10% Attack Chain Reconstruction (coordinated multi-stage attack)

---

#### Action C: Follow Investigative Lead 🔗

**Description:** Based on existing evidence, the team pursues a specific investigative thread.

**Cost (v2.2):** 5 Budget (printed cost for every Follow Investigative Lead action).

**Mechanics:**
1. **Pay Cost:** Spend 5 Budget (v2.2)
2. **Choose Evidence Card:** Pick an Evidence card with an "Investigative Lead"
3. **Describe Approach:** How will the team pursue this lead? (e.g., "Track the C2 domain to registrar records to find other registered domains")
4. **Roll:** d20 + relevant skill vs. DC (varies 11-14 depending on lead)
5. **Check Results:**
   - **Success:** Discover a new Evidence card directly related to the lead and apply its printed meter impacts (v2.2: if no suitable undiscovered Evidence card exists, advance Attribution Confidence +20% instead — never both)
   - **Partial Success:** Discover related evidence but get a false lead (discover 1 Evidence + 1 Red Herring card)
   - **Failure:** Dead-end lead; use turn without discovering evidence

**Example Lead:**

> **Evidence Card:** "Command-and-Control Communications (IP: 203.0.113.45)"
> **Investigative Lead:** "Perform ASN and WHOIS lookup to find other infrastructure operated by this attacker"
> **Blue Team:** "Let's trace the IP's ASN and registrar records to find other malicious domains."
> **Cost:** 5 Budget (v2.2)
> **Roll:** d20 + 1 (good idea) = 14 vs. DC 12
> **Result:** Success! Discover EVD-07 "Attacker Infrastructure Map" and apply its printed impacts: Attribution +30%, Attack Chain +15%, Timeline +10%. Team documents WHOIS/passive-DNS exports: Chain of Custody +5% (v2.2)

---

### Victory & Failure Conditions

#### Investigation Complete (Victory)

The Blue Team achieves ONE of these:

**Victory Condition 1: "Full Attribution"**
- **Attribution Confidence ≥ 90%** AND **Timeline Completeness ≥ 80%**
- **Outcome:** "Your investigation successfully attributes this attack to [Known Threat Group]. Security intelligence briefing prepared."

**Victory Condition 2: "Solid Case"**
- **Timeline Completeness ≥ 80%** AND **Attack Chain Reconstruction ≥ 80%** AND **Evidence Chain of Custody ≥ 70%**
- **Outcome:** "Your forensic report is publishable quality and defensible in court. Law enforcement briefed."

**Victory Condition 3: "Partial Findings"**
- **Any two Progress Meters ≥ 70% at game end**
- **Outcome:** "Investigation concluded. Findings are actionable for hardening and threat intelligence."

#### Investigation Inconclusive (Failure)

- **At the turn limit, no victory condition is met.**
- **Outcome:** "Investigation stalled. Critical questions remain unanswered. Threat actor unattributed."

**Precedence (v2.2):**
- Victory conditions are always checked FIRST. The old "any meter < 40% = failure" clause is DELETED (it conflicted with Victory Condition 3): a low meter never overrides a met victory condition.
- **Budget exhaustion is NOT a loss.** The game continues to the turn limit: you may always take the cheap 5-Budget actions (Analyze Existing Evidence, Follow Investigative Lead, LOG-01, TIMELINE-01) while Budget lasts, and even at 0 Budget the team keeps playing (narrating connections, re-checking victory at game end). Victory conditions are still checked normally.

**Penalty for Inconclusive Investigation:**
- Cannot feed findings into Hardening or Network Building modules
- Audit & Compliance module must assess with incomplete information
- Reduced confidence in future threat intelligence

---

### Special Forensics Rules

#### Rule 1: Chain of Custody Tracking

Every Evidence card must be documented to maintain admissibility in legal proceedings.

**Earning Chain of Custody (v2.2):** **+5% Chain of Custody every time an Evidence card is discovered AND the team states how it was preserved (hash, imaging, log export); the TO may award +10% for exemplary handling.** This is in addition to any Chain of Custody impact printed on the Evidence card itself.

**How It Works:**
- When an Evidence card is discovered, mark how it was obtained (which Investigation Action) and state how it was preserved
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
- Example: "Evidence logs were deleted. Log Analysis (DC 11) now has DC 13."

**Overcoming Anti-Forensics:**
- Investigators can use advanced techniques (Memory Forensics, Network Traffic Analysis) that bypass deleted logs
- Alternatively, **combine multiple Investigation Actions** to corroborate timeline from different sources
- Example: "Timeline can't be built from deleted logs, but network traffic shows exfiltration at 2:15 AM, and memory analysis shows C2 connection at 2:10 AM. We can reconstruct it."

---

#### Rule 3: Attacker Dwell Time

Represents how long the attacker remained in the network before detection or expulsion.

**Mechanics (v2.2):**
- **If the scenario states the attacker dwelled undetected 3+ turns (or the preceding Incident Response module ran 10+ turns), apply +1 DC to DISK and LOG investigations (evidence degraded).**
- Longer dwell time = more data exfiltrated, more persistence mechanisms installed, harder to attribute
- But longer dwell also = more evidence: the TO may make 1-2 additional Evidence cards discoverable (more actions, more forensic artifacts)

**Example:**
> Scenario states the attacker dwelled undetected for 4 turns before the investigation began.
> DISK-01, DISK-02, LOG-01, and LOG-02 all have +1 DC (evidence degraded over time).
> But the Blue Team can discover more Evidence cards (+2 cards total) due to the attacker's extended activity.

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

#### Rule 5: No Double Counting (v2.2)

Investigation cards list meter advances AND discovered Evidence cards list their own meter impacts. Never apply both.

**How It Works:**
- **When an investigation discovers an Evidence card, apply ONLY the Evidence card's printed meter impacts.**
- The investigation card's own "Advance" line applies **only when no Evidence card is produced** — e.g., a partial success that yields fragments, or a success when no suitable undiscovered Evidence card remains.
- The +5% Chain of Custody handling bonus (Rule 1, v2.2) still applies on top of the Evidence card's printed impacts — it rewards documentation, not discovery.

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
- **-2 (v2.2):** Using hastily (team taking Forensics as last-ditch effort in final turn)
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

4. **Victory Conditions (v2.2):**
   - Identical to campaign play — use the three canonical conditions in [Victory & Failure Conditions](#victory--failure-conditions):
     - **V1 "Full Attribution":** Attribution ≥90% AND Timeline ≥80%
     - **V2 "Solid Case":** Timeline ≥80% AND Attack Chain ≥80% AND Chain of Custody ≥70%
     - **V3 "Partial Findings":** any two meters ≥70% at game end

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
- Disk Forensics → T1005 (Data from Local System), T1025 (Data from Removable Media)
- Memory Forensics → T1112 (Modify Registry), T1055 (Process Injection)
- Log Analysis → T1071 (Application Layer Protocol), T1090 (Proxy)
- Network Analysis → T1041 (Exfiltration Over C2 Channel), T1048 (Exfiltration Over Alternative Protocol)
- Malware Analysis → T1104 (Multi-Stage Channels), T1059 (Command and Scripting Interpreter)
- Timeline Reconstruction → T1074 (Data Staged), T1003 (OS Credential Dumping)
- Attribution → G#### group / S#### software identification (threat attribution)

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

- **v2.2** (Current) - Playtest Edition
  - Canonical victory conditions (V1/V2/V3), failure only at turn limit
  - Investigation Duration mechanic; No Double Counting rule; Chain of Custody earn rule
  - Costed Analyze Evidence (5) and Follow Lead (5); balance and errata fixes
  - See "v2.2 Playtest Edition Changes" at the bottom of this document
- **v2.1** - Investigation & Attribution Edition
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
**Actions:** Conduct Investigation (card cost, Duration 1-3 turns), Analyze Evidence (5 Budget, each Evidence card only once), Follow Leads (5 Budget)
**Rolls:** d20 vs. DC, with skill modifiers; partial success on DC-2 to DC-1
**Durations (v2.2):** Duration N resolves at the start of turn N, counting the starting turn as turn 1 (Duration 1 = immediate); only one multi-turn investigation in flight at a time
**Resources:** Budget (75 base, tracker 0-100), Turns (6-15), Progress Meters (4 tracked)
**Victory (v2.2):**
- **V1 "Full Attribution":** Attribution ≥90% AND Timeline ≥80%
- **V2 "Solid Case":** Timeline ≥80% AND Attack Chain ≥80% AND Chain of Custody ≥70%
- **V3 "Partial Findings":** any two meters ≥70% at game end
**Failure (v2.2):** At the turn limit, no victory condition met. Victory conditions are checked first; there is no meter-minimum failure clause and budget exhaustion is not a loss.

---

## v2.2 Playtest Edition Changes

1. **Canonical victory conditions.** Four conflicting versions of the "complete case" condition (plus a fifth standalone-only condition) are replaced by one canonical set, stated identically here, in the Quick Reference, and in the standalone guide:
   - **V1 "Full Attribution":** Attribution ≥90% AND Timeline ≥80%
   - **V2 "Solid Case":** Timeline ≥80% AND Attack Chain ≥80% AND Chain of Custody ≥70%
   - **V3 "Partial Findings":** any two meters ≥70% at game end
   - **Failure:** at the turn limit, no victory condition met
   - **Precedence:** victory conditions are checked first. The "any meter <40% = failure" clause is deleted (it conflicted with V3). Budget exhaustion is not a loss. Meter "averages" are never used anywhere.
2. **Investigation Duration is now a real rule.** Starting a Duration-N investigation occupies your action and Budget on the starting turn; results arrive at the start of turn N (counting the starting turn as turn 1) — Duration 1 resolves immediately. Only one multi-turn investigation in flight at a time. DISK-01's rush option is priced: pay +5 Budget to run it at Duration 1.
3. **Chain of Custody is earnable:** +5% every time an Evidence card is discovered AND the team states how it was preserved (hash, imaging, log export); TO may award +10% for exemplary handling.
   - **Reachability math:** printed CoC impacts on Evidence cards total +50% (EVD-08 +15, EVD-09 +10, EVD-10 +10, EVD-11 +10, EVD-12 +5). In a typical 8-10 turn game the team discovers 6-8 Evidence cards: 7 discoveries with stated preservation = +35% handling; if those include EVD-08, EVD-09, and EVD-11 that adds +35% printed, for **70% — the V2 threshold — without any exemplary awards**. Exemplary handling (+10 instead of +5) or additional CoC-bearing cards push it higher. Under v2.1's printed-only gains, the ceiling was ~60% and V2 was mathematically unreachable.
4. **Analyze Existing Evidence costs 5 Budget**, and each Evidence card can be Analyzed only once (it was a free, infinitely repeatable dominant action).
5. **Follow Investigative Lead has a printed cost: 5 Budget** (examples previously charged 10 or 0).
6. **No Double Counting (Rule 5):** when an investigation discovers an Evidence card, apply ONLY the Evidence card's printed meter impacts; the investigation card's advance line applies only when no Evidence card is produced (e.g., partial success).
7. **Partial-success band is DC-2 to DC-1** (matches all printed cards; the module previously said DC-3 to DC-1).
8. **Meter advance range widened to +5-35%** — major breakthroughs can exceed +20% (cards already went to +35).
9. **One-Evidence rule now reads "unless the card says otherwise"** (MEM-02 and NET-02 award two Evidence cards).
10. **Haste modifier is -2 everywhere** (was -1 in one list). Anti-forensics example corrected to DC 13 (11 + 2). Dwell time redefined in turns: attacker dwelled undetected 3+ turns (or IR module ran 10+ turns) → +1 DC to DISK and LOG investigations.
11. **MITRE ATT&CK corrections** across the module and card files (~12 wrong ID/name pairs fixed: T1005, T1074, T1112, T1040, T1055, T1059.001, T1556, T1027, and removal of irrelevant T1120/T1113/T1004 mappings).
12. **Credential and path errata:** DISK-01 GCIH/GCFE (was CCNA-Security), MALW-01 GREM (was fictional "CRT"), EVD-10 registry path now includes `\CurrentVersion`.
13. **Budget tracker range is 0-100** (was "maximum useful 150"). Starting budget stays 75 (+25 optional).
14. **Deck summaries recounted from the actual cards:** 12 Investigation, 12 Evidence, 4 Findings; evidence-type counts and the investigation→evidence flow map regenerated from the cards' Discovery Sources.

