# Forensics Module: Standalone Game Guide

**Version:** 2.2 - Playtest Edition (rule changes marked "(v2.2)" — see the module rules doc for the full change list)
**Duration:** 45-90 minutes
**Player Count:** 1 Threat Orchestrator + 1-4 Investigators
**Complexity:** Intermediate to Advanced

---

## Overview

This guide explains how to play the **Forensics Module** as a standalone game, without needing to have played Incident Response, Hardening, or Disaster Recovery first.

In standalone Forensics, you are a team of incident investigators called in to analyze a data breach. Your goal is to reconstruct the attack, discover the attacker's techniques, and if possible, attribute the breach to a known threat actor. This is a "detective" game focused on piecing together evidence rather than detecting or preventing attacks.

---

## What You'll Learn

- **Digital forensics methodology:** How to collect and analyze evidence from compromised systems
- **Attack chain reconstruction:** Understanding the complete progression of an attacker's actions
- **Threat intelligence:** Identifying attacker techniques, tools, and likely motivations
- **Evidence analysis:** How small clues combine to reveal the complete attack story
- **Attribution challenges:** Why identifying attackers is difficult and what evidence matters most
- **Real-world processes:** How actual incident response teams approach investigations

---

## Game Components

### Required Components

- **12 Investigation Action Cards** (from cards/forensics/core-deck/)
- **12 Evidence Cards** (from cards/forensics/core-deck/)
- **4 Findings Cards** (from cards/forensics/core-deck/)
- **One d20 (20-sided die)**
- **Turn Tracker** (paper or board showing current turn)
- **Budget Tracker** (tracks spending from 0-100)
- **Progress Meters:**
  - Timeline Completeness (0-100%)
  - Attack Chain Reconstruction (0-100%)
  - Attribution Confidence (0-100%)
  - Evidence Chain of Custody (0-100%)

### Optional Enhancements

- MITRE ATT&CK technique reference sheet
- Investigation flowchart poster
- Evidence correlation whiteboard
- Printed evidence cards displayed on table

---

## Setup Instructions

### Step 1: Choose Difficulty Tier

The **Threat Orchestrator** (game facilitator) selects an attack complexity tier. Do NOT tell the Blue Team the tier—it's secret.

| Tier | Turn Count | Attack Type | Example |
|------|-----------|-------------|---------|
| **TIER 1 (Beginner)** | 6-8 | Script kiddie, basic malware | Casual cybercriminal, obvious techniques |
| **TIER 2 (Intermediate)** | 8-10 | Organized attacker, some sophistication | Credential theft ring, lateral movement |
| **TIER 3 (Advanced)** | 11-13 | Skilled APT, heavy obfuscation | Sophisticated threat group with operational security |
| **TIER 4 (Expert)** | 14-15 | Nation-state, elite techniques | State-sponsored APT with counter-forensics |

**Turn Count Randomization:**
- Select your chosen tier's baseline (6-8, 8-10, 11-13, or 14-15)
- Roll d4: -1, 0, 0, or +1
- Add result to baseline to get final turn count
- **Example:** TIER 2 (8-10) + d4 result of +1 = final turn count of 9-11 turns

### Step 2: Prepare Threat Scenario

**Secret TO Preparation:**

1. **Select Attack Chain:** Choose 3-5 Threat cards from Incident Response core deck or expansion deck
   - Arrange in logical progression (initial access → lateral movement → exfiltration)
   - Consider realistic attack flow: not every attack needs all phases

2. **Map Investigations:** For each threat card, note which Investigation Actions would discover it
   - Example: Malware persistence → Disk Forensics, Malware Analysis
   - Example: C2 communications → Network Traffic Analysis
   - Example: Credential abuse → Event Log Analysis

3. **Plan Evidence Discovery:** Prepare which Evidence cards will be revealed as each Investigation Action succeeds
   - Not all investigations succeed (some are dead-ends)
   - Some evidence cards might be discovered by multiple investigation paths

4. **Set Attacker Profile:** In your notes, decide:
   - Attacker motivation (cybercrime, espionage, hacktivism, nation-state)
   - Sophistication level (matches the tier)
   - Likely techniques (reference MITRE ATT&CK framework)
   - Tools used (commercial, custom, open-source)

**Example Secret Setup (TIER 2):**
> **Threat Cards Selected:** Phishing → Credential Harvesting → Lateral Movement → Persistence → Exfiltration
> **Turn Count:** 8-10 (TIER 2, no roll modifier used)
> **Attacker Profile:** Eastern European cybercriminal group focused on financial data theft
> **Key Evidence:** Phishing email headers, malware samples, persistence mechanisms, C2 communications
> **Attribution Clues:** Russian language in malware, specific tool signature, Bitcoin payment addresses
> **Investigation Challenge:** Attacker deleted logs; Blue Team must reconstruct from network traffic and memory forensics

### Step 3: Brief the Blue Team

Read the **Incident Briefing** to all investigators:

> **INCIDENT BRIEFING**
>
> "You've been called by [Company Name] to investigate a data breach discovered during routine system maintenance. Here's what we know so far:
>
> **Timeline of Discovery:**
> - System administrator noticed unusual network traffic on [Date]
> - Forensic examination discovered evidence of system compromise dating back approximately [2-3 weeks / 1 month]
> - Data breach notification team estimates millions of records may have been accessed
>
> **What Was Affected:**
> - Database servers containing customer information
> - Admin accounts showing unauthorized access
> - Backup systems with potential exfiltration evidence
>
> **Your Mission:**
> - Reconstruct the complete attack chain (how did they get in? what did they do? how did they get out?)
> - Identify what data was compromised (scope and sensitivity)
> - Attribute the attack to a known threat group or attacker profile if possible
> - Produce findings for the company's security hardening and incident prevention
>
> **Resources Available:**
> - Forensic laboratory time: 75 Budget units
> - [Optional: +25 if company has cyber insurance or threat intelligence subscription]
> - Investigation period: [TURN COUNT] turns (represents [1-3 weeks] of forensic work)
>
> **Regulatory Context:**
> - Time-sensitive: Investigation results feed into breach notification requirements
> - Chain of custody critical: Findings must be admissible if this goes to law enforcement
>
> You have [TURN COUNT] turns. Begin your investigation."

### Step 4: Initialize Tracking

On a shared board or spreadsheet, create:

1. **Turn Tracker:** Current turn = 1, Max turns = [TURN COUNT]
2. **Budget Tracker:** Current budget = 75 (or 100), tracker range 0-100
3. **Progress Meters:**
   - Timeline Completeness: 0%
   - Attack Chain Reconstruction: 0%
   - Attribution Confidence: 0%
   - Evidence Chain of Custody: 0%
4. **Evidence Log:** Space to list discovered Evidence cards and their sources
5. **Investigation Record:** Track which Investigation Actions have been attempted (successful and failed)

---

## Turn Sequence

### Each Turn Has 3 Steps

#### Step 1: Blue Team Describes Action (5 minutes)

One investigator (or the whole team collectively) describes what forensic investigation they want to perform.

**Options:**

**Option A: Conduct Investigation**
- Choose an Investigation Action card (Disk Forensics, Memory Analysis, Log Analysis, Network Traffic, Malware Analysis, Timeline Reconstruction, or Threat Attribution)
- Describe HOW they'll conduct the investigation (methodology, tools, expected findings)
- Declare the Budget cost (shown on card) — paid on the turn you start
- Note the card's **Duration (v2.2):** starting the investigation is your action this turn; counting this turn as turn 1, the roll and results arrive at the START of turn N (Duration 1 = same turn, Duration 2 = start of next turn, Duration 3 = two turns later). Only ONE multi-turn investigation may be in flight at a time; you may take other actions while waiting.
- Example: "We'll do a full disk image of the compromised database server and look for persistence mechanisms, rootkits, and artifact evidence. Cost 10 Budget, Duration 2 — results at the start of next turn."

**Option B: Analyze Existing Evidence** — Cost: 5 Budget (v2.2)
- Review 2-4 Evidence cards already discovered — **each Evidence card can be Analyzed only once (v2.2)**; mark cards as Analyzed
- Describe connections between findings (temporal sequence, technical relationships, or attribution links)
- Example: "The malware sample matches the persistence mechanism we found in scheduled tasks, suggesting the attacker knew exactly what they were doing. Plus, the C2 domain was registered by the same person who registered two other domains we found in old breach reports."

**Option C: Follow Investigative Lead** — Cost: 5 Budget (v2.2)
- Pick an Evidence card with an "Investigative Lead" noted
- Describe how you'll pursue this lead
- Example: "This C2 domain resolves to a Russian ASN. Let's do a WHOIS lookup and see what other domains are hosted on this infrastructure."

---

#### Step 2: TO Rolls & Resolves (2-3 minutes)

**For Conduct Investigation or Follow Investigative Lead:**

1. **Verify Cost:** Check if Blue Team has sufficient Budget (Follow Lead costs 5 — v2.2)
   - If insufficient Budget, investigation cannot proceed (suggest alternative action)

2. **Apply Duration (v2.2):** For a Duration 2-3 investigation, the cost and action are spent now, but steps 3-5 happen at the START of the turn the investigation completes (Duration 1 resolves immediately)

3. **Set Difficulty Class (DC):** TO checks Investigation Action card for DC
   - Example: Disk Forensics has DC 12
   - Modify DC if anti-forensics present: +2 DC
   - Modify DC if attacker was sophisticated: +1-2 DC

4. **Determine Modifiers:** Apply skill modifiers to the roll
   - +2 if investigator has forensics certification
   - +1 if basic IT security background
   - +2 if team provides detailed technical narrative
   - +1 if previous investigation discovered clues to this action
   - -2 if attempting hastily (rushed, final turn desperation) (v2.2)

5. **Roll:** Investigator (or TO on their behalf) rolls d20

6. **Compare Results:**
   - **Success (roll ≥ DC):** Discover ONE Evidence card (unless the card says otherwise — MEM-02 and NET-02 award TWO) and apply ONLY that Evidence card's printed meter impacts (typically +5-35% per meter; major breakthroughs can exceed +20%). The investigation card's own advance line applies only if no Evidence card is produced (v2.2: No Double Counting)
   - **Partial Success (roll DC-2 to DC-1):** Discover partial or incomplete evidence + apply the investigation card's partial advance line (typically +5-15%)
   - **Failure (roll < DC-2):** No evidence discovered; Budget still spent; take a turn

**For Analyze Existing Evidence:**

1. **Pay Cost:** 5 Budget (v2.2); the 2-4 Evidence cards reviewed must not have been Analyzed before
2. **Describe Connection:** Blue Team explains how findings are related
3. **Roll:** d20 + investigator skill modifier vs. DC 10
4. **Results:**
   - **Success (≥10):** Gain insight; advance two Progress Meters by 5-10% each
   - **Failure (<10):** No progress; use a turn (Budget still spent)

---

#### Step 3: Record & Update Tracking (1-2 minutes)

1. **Deduct Budget:** Subtract action cost from Budget Tracker
2. **Advance Turn:** Increment Turn counter by 1
3. **Update Progress Meters:** Record any progress from resolved investigations
4. **Note Evidence:** If Evidence card discovered, add to Evidence Log with source and chain of custody status
5. **Chain of Custody (v2.2):** +5% Chain of Custody for each Evidence card discovered this turn IF the team stated how it was preserved (hash, imaging, log export); TO may award +10% for exemplary handling
6. **Check Victory Condition:** Did Blue Team achieve any victory condition? (see Victory Conditions section)

---

## Investigation Actions & Evidence

### Investigation Action Cards (Quick Reference)

| Card | DC | Cost | Duration | What It Reveals |
|------|----|----|----------|-----------------|
| DISK-01: Disk Image & Analysis | 12 | 10 | 2 turns | Deleted files, malware samples, persistence mechanisms |
| DISK-02: File System Carving | 14 | 15 | 3 turns | Deep file recovery, hidden artifacts, encrypted data |
| MEM-01: Memory Dump & Analysis | 13 | 15 | 2 turns | Volatile processes, injected code, C2 connections |
| MEM-02: Memory Forensics Deep Dive | 15 | 20 | 3 turns | Malware behavior analysis, encryption keys, exploits |
| LOG-01: Event Log Analysis | 11 | 5 | 1 turn | User login timeline, privilege escalation, admin actions |
| LOG-02: Deep Log Correlation | 13 | 10 | 2 turns | Cross-system timeline, attack sequence, lateral movement |
| NET-01: Network Traffic Analysis | 12 | 10 | 2 turns | Exfiltration evidence, C2 communications, data flows |
| NET-02: Packet Capture Deep Analysis | 14 | 15 | 3 turns | Protocol forensics, attacker tools, communication patterns |
| MALW-01: Malware Analysis (Dynamic) | 12 | 15 | 2 turns | Behavior analysis, IOCs, capabilities |
| MALW-02: Malware Analysis (Static) | 14 | 10 | 2 turns | Code reverse engineering, attacker signatures, techniques |
| TIMELINE-01: Timeline Reconstruction | 13 | 5 | 1 turn | Chronological attack sequence, entry and exit points |
| THREAT-01: Threat Attribution Analysis | 15 | 20 | 3 turns | Link to known threat groups, TTPs, motivation |

*DISK-01 rush option (v2.2): pay +5 Budget (15 total) to run it at Duration 1. Duration rule: results arrive at the start of the turn the Duration completes — see Turn Sequence.*

---

## Victory & Failure Conditions

### Investigation Complete (VICTORY)

Blue Team wins if they achieve ONE of these (canonical v2.2 conditions — identical to the module rules):

**Victory Condition 1: "Full Attribution"**
- **Attribution Confidence ≥ 90%** AND **Timeline Completeness ≥ 80%**
- **Result:** "You have successfully attributed this attack to [Threat Group]. Intelligence briefing prepared for leadership."

**Victory Condition 2: "Solid Case"**
- **Timeline Completeness ≥ 80%** AND **Attack Chain Reconstruction ≥ 80%** AND **Evidence Chain of Custody ≥ 70%**
- **Result:** "Your forensic investigation is publishable quality and legally defensible. Law enforcement briefed."

**Victory Condition 3: "Partial Findings"**
- **Any two Progress Meters ≥ 70% at game end**
- **Result:** "Investigation concluded with sufficient findings for remediation. Hardening team can now implement controls."

---

### Investigation Inconclusive (FAILURE)

Blue Team fails if, **at the turn limit, no victory condition is met**.

**Precedence (v2.2):** Victory conditions are always checked FIRST. There is no "any meter < 40% = failure" clause (deleted — it conflicted with Victory Condition 3), and **budget exhaustion is not a loss**: you may always fall back on the cheap 5-Budget actions while Budget lasts, and the game simply plays out to the turn limit.

**Result of failure:** "Investigation stalled. Too many unanswered questions. Threat actor remains unidentified. Forensic team recommends additional investigation by external firm."

**Consequence of Failure:**
- Investigation results are incomplete and cannot feed into Hardening or Network Building modules
- Audit & Compliance module must assess security posture with incomplete information
- Organization loses confidence in threat intelligence

---

## Example Investigation (Complete Turn)

### Scenario Setup (TO Secret)
> TIER 2 attack: Credential-based lateral movement with persistence
> Turn limit: 8 turns (TIER 2 baseline 9, d4 roll of -1)
> Attacker profile: Eastern European cybercriminal group
> Key technique: Password spray → Privilege escalation → Scheduled task persistence → Data exfiltration
> Bonus: The sysadmin's initial triage captured a suspicious binary, so a malware sample is available from turn 1

### Turn 1

**Blue Team:** "We'll start with event log analysis of the compromised database server. We want to see the login history and identify unusual access patterns. We'll export the logs with their digital signatures and hash the export."

**Investigator Skill:** IT Security background (+1)

**TO Facilitator:**
1. **Check Cost:** LOG-01 costs 5 Budget. Current budget 75. ✓ OK
2. **Check Duration:** LOG-01 is Duration 1 — resolves this turn
3. **Set DC:** LOG-01 has DC 11. No anti-forensics. DC = 11
4. **Apply Modifiers:** +1 (IT security background) + 0 (no prior clues) = +1 total
5. **Roll:** Investigator rolls d20+1. d20 = 13, total 14
6. **Success!** (14 ≥ 11) → Discover Evidence card **EVD-04 "Suspicious Admin Login (Timeline)"** — apply ONLY its printed impacts (v2.2 No Double Counting)

**Update Tracking:**
- Budget: 75 - 5 = 70 remaining
- Turn: 1 → 2
- EVD-04 printed impacts: Timeline 0% → 25%, Attack Chain 0% → 20%, Attribution 0% → 10%
- Chain of Custody: 0% → 5% (v2.2: preservation stated — signed log export, hashed)
- Evidence Log: "EVD-04 - discovered via LOG-01 - preserved via signed/hashed export - Chain of Custody: intact"

**Blue Team Deduction:** "Looks like an admin account was accessed from unusual locations. Might be credential theft."

---

### Turn 2

**Blue Team:** "Let's analyze that malware sample from triage. We want to understand what it does and where it connects to."

**Investigator Skill:** Forensic certification background (+2)

**TO Facilitator:**
1. **Check Cost:** MALW-01 costs 15 Budget. Current budget 70. ✓ OK
2. **Check Duration (v2.2):** MALW-01 is Duration 2. Starting the sandbox run is this turn's action; the roll and results arrive at the START of turn 3. MALW-01 is now the one multi-turn investigation in flight.

**Update Tracking:**
- Budget: 70 - 15 = 55 remaining
- Turn: 2 → 3
- Meters: unchanged (results pending) — Timeline 25%, Attack Chain 20%, Attribution 10%, Chain of Custody 5%

---

### Turn 3

**Start of turn — MALW-01 resolves (v2.2 Duration):**
1. **Set DC:** MALW-01 has DC 12. Attacker was moderately sophisticated: +1. DC = 13
2. **Apply Modifiers:** +2 (forensic cert)
3. **Roll:** d20 = 14, total 16
4. **Success!** (16 ≥ 13) → Discover **EVD-02 "Command-and-Control Callback Domain"**
   - EVD-02 printed impacts: Attack Chain 20% → 35%, Attribution 10% → 35%, Timeline 25% → 30%
   - Chain of Custody: 5% → 10% (v2.2: sample hashed, sandbox logs archived)

**Turn 3 action — Blue Team:** "Now let's look at network flow records for that C2 domain. Start NET-01."

**TO Facilitator:** NET-01 costs 10 (budget 55 → 45 ✓), Duration 2 — resolves at the start of turn 4. (Allowed: MALW-01 finished this turn, so only one investigation is in flight.)

**Update Tracking:**
- Budget: 45 remaining
- Turn: 3 → 4
- Meters: Timeline 30%, Attack Chain 35%, Attribution 35%, Chain of Custody 10%

**Blue Team Deduction:** "The malware communicates with an external server. That's how the attacker stays in control."

---

### Turn 4

**Start of turn — NET-01 resolves (v2.2 Duration):**
1. **Set DC:** NET-01 has DC 12
2. **Apply Modifiers:** +1 (IT security background)
3. **Roll:** d20 = 9, total 10
4. **Partial Success** (10 is in the DC-2 to DC-1 band, 10-11) → Suspicious outbound traffic found, but the destination is unclear. No Evidence card produced, so apply NET-01's partial advance line: Attack Chain 35% → 45%, Attribution 35% → 40%. No Chain of Custody handling bonus (no Evidence card discovered).

**Turn 4 action — Blue Team:** "Let's try to reconstruct the timeline from what we have. TIMELINE-01."

**TO Facilitator:** TIMELINE-01 costs 5 (budget 45 → 40 ✓), Duration 1 — resolves now. DC 13, +2 (DFIR training). Roll: d20 = 8, total 10. **Failure** (10 < 11, below the DC-2 partial band). Too many timestamp gaps. Budget still spent.

**Update Tracking:**
- Budget: 40 remaining
- Turn: 4 → 5
- Meters: Timeline 30%, Attack Chain 45%, Attribution 40%, Chain of Custody 10%

---

### Turn 5 (Critical Decision)

**Blue Team:** "This is expensive, but let's start the Memory Forensics Deep Dive on the admin workstation. If the attacker has malware in memory, we might find encryption keys or recent commands that show their intent."

**TO Facilitator:**
1. **Check Cost:** MEM-02 costs 20 Budget. Current budget 40. ✓ OK
2. **Check Duration (v2.2):** MEM-02 is Duration 3 — started this turn (turn 1 of 3), it resolves at the START of turn 7. It is now the one multi-turn investigation in flight.

**Update Tracking:**
- Budget: 40 - 20 = 20 remaining
- Turn: 5 → 6
- Meters: unchanged (results pending)

---

### Turn 6 (Working While Waiting)

**Blue Team:** "While the memory analysis runs, let's Analyze our existing evidence. The suspicious admin login (EVD-04, T1078 Valid Accounts) lines up with the C2 callbacks (EVD-02, T1071 Application Layer Protocol): the login happened 20 minutes before the first beacon. This was credential theft followed by remote control."

**TO Facilitator:**
1. **Check Cost:** Analyze Existing Evidence costs 5 (v2.2). Budget 20 → 15 ✓. (Allowed while MEM-02 is in flight — Analyze is not an investigation.)
2. **Check cards:** EVD-04 and EVD-02 have not been Analyzed before ✓ — mark both as Analyzed (v2.2: each Evidence card only once)
3. **Modifiers:** +1 (references specific MITRE ATT&CK techniques) + 1 (IT security background) = +2
4. **Roll:** d20 = 12, total 14 vs. DC 10. **Success!** → Advance two meters by 10% each: Timeline 30% → 40%, Attribution 40% → 50%

**Update Tracking:**
- Budget: 15 remaining
- Turn: 6 → 7
- Meters: Timeline 40%, Attack Chain 45%, Attribution 50%, Chain of Custody 10%

**Blue Team Deduction:** "Credential theft, then hands-on-keyboard control. Now we need the memory results."

---

### Turn 7 (Breakthrough)

**Start of turn — MEM-02 resolves (v2.2 Duration, started turn 5):**
1. **Set DC:** MEM-02 has DC 15
2. **Apply Modifiers:** +2 (forensic analyst) + 1 (MALW-01 already completed) = +3
3. **Roll:** d20 = 11, total 14
4. **Partial Success** (14 is in the DC-2 to DC-1 band, 13-14) → Discover ONE complete Evidence card, **EVD-09 "Attacker Command History"**, plus an INCOMPLETE second finding (fragments of an RC4 key — marked INCOMPLETE, no meter impact until completed or interpreted)
   - EVD-09 printed impacts: Timeline 40% → 65%, Attack Chain 45% → 70%, Attribution 50% → 65%, Chain of Custody 10% → 20%
   - Chain of Custody: 20% → 25% (v2.2: memory image hashed, extraction methodology documented)

**Turn 7 action — Blue Team:** "Follow the investigative lead on EVD-02: WHOIS and ASN lookup on the C2 domain to map related attacker infrastructure."

**TO Facilitator:**
1. **Check Cost:** Follow Investigative Lead costs 5 (v2.2). Budget 15 → 10 ✓
2. **Set DC:** 12
3. **Apply Modifiers:** +2 (detailed approach referencing prior evidence)
4. **Roll:** d20 = 14, total 16. **Success!** → Discover **EVD-07 "Attacker Infrastructure Map"** — apply its printed impacts (v2.2: no separate +20% Attribution bonus — No Double Counting)
   - EVD-07 printed impacts: Attribution 65% → 95%, Attack Chain 70% → 85%, Timeline 65% → 75%
   - Chain of Custody: 25% → 30% (v2.2: WHOIS records and passive-DNS exports archived)

**Update Tracking:**
- Budget: 10 remaining
- Turn: 7 → 8 of 8 (final turn)
- Meters: Timeline 75%, Attack Chain 85%, Attribution 95%, Chain of Custody 30%

**Victory check:** Condition 1 needs Attribution ≥ 90% ✓ (95%) AND Timeline ≥ 80% ✗ (75%). Not yet. Condition 2 needs Timeline ≥ 80% ✗. Play on.

---

### Turn 8 (Final Turn)

**Blue Team:** "One more push on the timeline. We retry TIMELINE-01, now synthesizing the login timeline (EVD-04), the C2 beacons (EVD-02), and the attacker's command history (EVD-09)."

**TO Facilitator:**
1. **Check Cost:** TIMELINE-01 costs 5. Budget 10 → 5 ✓. Duration 1 — resolves now.
2. **Set DC:** 13
3. **Apply Modifiers:** +2 (DFIR training) + 1 (prior investigations provide clues) = +3
4. **Roll:** d20 = 15, total 18. **Success!** All timeline-type evidence has already been discovered, so no new Evidence card is produced — apply TIMELINE-01's own advance line instead (v2.2 No Double Counting): Timeline 75% → 100%, Attack Chain 85% → 100%

**Update Tracking:**
- Budget: 5 remaining
- Turn: 8 of 8 — game end
- Final meters: Timeline 100%, Attack Chain 100%, Attribution 95%, Chain of Custody 30%

---

### Victory Determination (Game End, After Turn 8)

**Check Victory Conditions (v2.2 — victory is checked first, never overridden by a low meter):**

**Condition 1 "Full Attribution": Attribution ≥ 90% AND Timeline ≥ 80%?**
- Attribution: 95% ✓
- Timeline: 100% ✓
- **YES! VICTORY CONDITION 1 MET!**

(For completeness: Condition 2 "Solid Case" fails on Chain of Custody 30% < 70%; Condition 3 "Partial Findings" would also be met with three meters ≥ 70% at game end. Note the v2.2 precedence rule: Chain of Custody sitting at 30% does NOT cause a failure — the old "any meter < 40%" clause is deleted. Meter averages are never used.)

**Game Ends with VICTORY**

> **Investigation Result:** "Your forensic investigation successfully identified the attacker as a member of the [Eastern European Cybercriminal Group]. Key findings:
> - Attack vector: Credential theft via password spray
> - Control: C2 beaconing from checkupdate-style domains, hands-on-keyboard commands recovered from memory
> - Timeline: fully reconstructed from signed logs, beacon timing, and command history
> - Attribution: 95% confidence linked to known group via infrastructure map
> - Caveat: evidence admissibility is weak (Chain of Custody 30%) — fine for hardening, not for court
>
> Recommendations:
> 1. Implement multi-factor authentication on admin accounts
> 2. Deploy EDR solution to detect persistence mechanisms
> 3. Implement network segmentation to limit lateral movement
> 4. Increase logging and monitoring of admin activities
>
> This investigation will inform the Hardening, Network Building, and Audit modules going forward."

---

## Tips for Investigators

### Investigation Strategy

**Early Game (Turns 1-3):**
- Start with cheaper, lower DC investigations (Log Analysis, Timeline Reconstruction)
- Build foundation of knowledge before attempting expensive techniques
- Goal: 50%+ progress on any meter by turn 3

**Mid Game (Turns 4-7):**
- Use findings from early investigations to guide more expensive deep dives
- Follow Investigative Leads to get "bang for your budget"
- Aim for 75%+ on at least two meters by turn 6

**Late Game (Turns 8+):**
- If you have momentum, push for one complete meter (≥90%)
- If budget is tight, focus on two meters reaching ≥70% (Condition 3)
- Make bold investigations; you have less to lose

### Narrative Details Matter

**To Gain Bonuses:**
- Explain not just WHAT you'll investigate, but HOW and WHY
- Reference specific evidence already discovered
- Mention MITRE ATT&CK techniques you're looking for
- **Example (gains +2):** "We found a persistence mechanism in the scheduled tasks. This matches T1053 (Scheduled Task/Job). Let's do Memory Forensics to find if the malware is still resident in RAM and tracking recent C2 communications."

### Evidence Correlation

**Create Connections:**
- Note which investigations led to which evidence cards
- Look for patterns: "All malware samples have Russian-language strings"
- Timeline building: "Login at 2:15, C2 connection at 2:10, exfiltration at 2:25"
- **These connections trigger Analyze Evidence action and drive attribution forward**

---

## Tips for the Threat Orchestrator

### Maintaining Suspense

- **Don't reveal the tier.** Let investigators speculate ("This is pretty sophisticated" vs. "This is basic stuff")
- **Surprise with difficulty:** If investigators are breezing through (rolling high), reveal anti-forensics measures ("+2 DC because logs were deleted")
- **Give hints through evidence:** Realism cues (Russian malware → Eastern European group; sophisticated encryption → nation-state threat)

### Pacing the Game

- **Turn 1-3:** Should be mostly successes. Investigators build confidence and progress.
- **Turn 4-7:** Mix of successes and failures. Some investigations hit dead-ends. Tension rises.
- **Turn 8+:** Each turn matters. Budget running low. Critical decisions.

- **If game is ending early** (Victory Condition 1 or 2 before turn 6): Let it happen. Means they played smart. (Condition 3 is only checked at game end.)
- **If game is dragging** (still <50% progress by turn 6): Hint that they should use Follow Investigative Lead (cheaper, guided path)

### Challenge Scaling

**For Beginner Investigators:**
- Use TIER 1 attacks (6-8 turns, low DC, no anti-forensics)
- Provide hints during briefing ("We recovered a memory dump")
- Allow retries on failed Investigation Actions

**For Experienced Investigators:**
- Use TIER 3-4 attacks (11-15 turns, high DC, sophisticated anti-forensics)
- Limit Budget more strictly
- Add False Evidence cards (partial investigation leads to wrong conclusion)

---

## Debrief & Learning Outcomes

### Post-Game Discussion (10-15 minutes)

After game concludes, facilitate discussion:

**On Investigation Process:**
1. Which investigation technique was most valuable? Why?
2. What would you do differently with more budget?
3. What evidence was hardest to interpret?
4. How did you decide which investigation to do next?

**On Attack Reconstruction:**
1. Walk through the attack chain step-by-step. What happened first? Last?
2. How did the attacker maintain access without being detected immediately?
3. What's one technique that could have prevented this entire attack?

**On Attribution:**
1. What evidence pointed to the attacker's identity?
2. How confident are you in the attribution? (At 75%? 90%?)
3. What additional evidence would make you 95%+ confident?

**On Real-World Forensics:**
1. How does this compare to actual forensic investigations you've studied?
2. What tools mentioned in the game (memory forensics, malware analysis) are used in real incident response?
3. Why does attribution matter? (Law enforcement, threat intelligence sharing, policy response)

**On Lessons Learned:**
1. What control from Hardening module could have detected this attack early?
2. How would Network Building architecture limit lateral movement?
3. What Audit & Compliance questions need to be answered?

---

## Standalone Forensics Variants

### Variant 1: Time-Pressure Mode

**Modified Rules:** Reduce turn count by 3 (so 3-7 turns instead of 6-10)

**Effect:** Creates higher stakes; investigators must make faster decisions; less time for methodical analysis

**When to Use:** Advanced investigators who want more challenge; time-limited classroom sessions

---

### Variant 2: False Evidence Mode

**Modified Rules:** TO secretly includes 1-2 "False Evidence" cards that appear legitimate but are actually red herrings

**Effect:** Attribution becomes harder; investigators must corroborate findings; critical thinking required

**Example:** Malware sample analysis reveals Russian-language strings → seems like Eastern European group. But it was actually planted by another threat group to frame competitors.

**When to Use:** Teaching about false positives and need for corroboration

---

### Variant 3: Cold Case Mode

**Modified Rules:** Start with 40% progress already on one or two meters (from prior investigation by another team)

**Effect:** Investigators build on existing findings rather than starting from scratch

**When to Use:** Teaching how investigations are handed off; continuing previous work

---

### Variant 4: Competitive Mode

**Modified Rules:** Two teams of investigators compete to achieve highest progress on most meters

**Scoring:** +3 points per meter ≥ 90%, +2 points per meter 70-89%, +1 per meter 40-69%

**When to Use:** Competitive classroom tournament; multiple teams investigating same breach simultaneously

---

## Recommended Module Sequences with Forensics

**30-minute Warm-up:** Forensics solo (TIER 1, 6-turn simplified scenario)

**90-minute Session:** Incident Response (45 min) + Forensics (45 min)
- Phase 1: IR team detects attack chain
- Phase 2: Forensics team investigates findings

**120-minute Session:** Incident Response → Disaster Recovery mini → Forensics
- Phase 1: IR failure (breach not contained)
- Phase 2: DR (crisis management, brief)
- Phase 3: Forensics (investigation & attribution)

**180+ minute Session:** Complete lifecycle with Forensics
- Network Building (45 min) → Hardening (45 min) → Incident Response (45 min) → Forensics (30 min)

---

## Quick Reference Card for Investigators

**Setup:** Choose TIER (1-4), Roll d4, Announce turn count and starting budget (75)

**Each Turn:**
1. **Resolve arrivals (v2.2):** Any Duration 2-3 investigation completing this turn rolls and resolves at the start of the turn
2. **Choose action:** Conduct Investigation (card cost, Duration 1-3), Analyze Evidence (5 Budget, each Evidence card only once), or Follow Lead (5 Budget)
3. **Pay cost:** Deduct Budget
4. **Roll d20:** Add skill modifier, compare to DC (partial success on DC-2 to DC-1); Duration 2-3 investigations roll when they complete
5. **Resolve:** Discover evidence (apply the Evidence card's printed impacts — never also the investigation card's advance line), or fail
6. **Update:** Budget, Turn counter, Progress Meters (+5% Chain of Custody per Evidence discovery with stated preservation)

**Resources:**
- Budget: 75 (represents forensic lab time; tracker range 0-100)
- Turns: 6-15 (depends on tier + d4 roll)
- Progress Meters: Timeline, Attack Chain, Attribution, Chain of Custody (each 0-100%)

**Victory (v2.2):**
- **V1 "Full Attribution":** Attribution ≥90% AND Timeline ≥80%
- **V2 "Solid Case":** Timeline ≥80% AND Attack Chain ≥80% AND Chain of Custody ≥70%
- **V3 "Partial Findings":** any two meters ≥70% at game end

**Failure (v2.2):** At the turn limit, no victory condition met. Victory is checked first — there is no meter-minimum failure clause, and budget exhaustion is not a loss. investigation

---

## Forensics Card Deck Checklist

Before playing, ensure you have:

- [ ] 12 Investigation Action Cards (printable from cards/forensics/core-deck/)
  - [ ] Disk Forensics (2 cards)
  - [ ] Memory Forensics (2 cards)
  - [ ] Log Analysis (2 cards)
  - [ ] Network Traffic (2 cards)
  - [ ] Malware Analysis (2 cards)
  - [ ] Timeline & Attribution (2 cards)

- [ ] 12 Evidence Cards (printable from cards/forensics/core-deck/)
  - [ ] Malware & Persistence (4 cards: EVD-01, EVD-03, EVD-08, EVD-10)
  - [ ] Credentials & Access (1 card: EVD-04)
  - [ ] Lateral Movement (1 card: EVD-05)
  - [ ] Exfiltration (1 card: EVD-06)
  - [ ] Attack Infrastructure (2 cards: EVD-02, EVD-07)
  - [ ] Attack Activity (3 cards: EVD-09, EVD-11, EVD-12)

- [ ] 4 Findings Cards
  - [ ] FIND-01: Threat Attribution Report
  - [ ] FIND-02: Attack Surface Analysis
  - [ ] FIND-03: Persistence Mechanisms Discovered
  - [ ] FIND-04: Investigative Gaps & Recommendations

- [ ] 1d20 die
- [ ] Turn tracker (paper or board)
- [ ] Budget tracker (paper or board)
- [ ] Progress meter tracking sheet
- [ ] Optional: MITRE ATT&CK reference sheet

---

## Frequently Asked Questions

**Q: Can I play Forensics if I've never played Incident Response?**
A: Yes! Forensics standalone is completely self-contained. You don't need to have played IR, Hardening, or any other module first.

**Q: How long does Forensics take?**
A: Typically 45-90 minutes depending on group experience level and decision speed. Experienced investigators finish faster.

**Q: Can I play Forensics with a large group?**
A: Yes! 4-8 investigators is ideal. With more, split into two teams (each team has its own TO). You can even do competitive mode where both teams investigate the same breach.

**Q: What if investigators want to know the tier?**
A: Don't tell them. Part of the game is discovering how sophisticated the attacker is through evidence analysis. Let them discover it.

**Q: What if we run out of budget before solving the case?**
A: That's a realistic outcome, and it is NOT an automatic loss (v2.2). Keep playing to the turn limit — the cheap 5-Budget actions (Analyze Evidence, Follow Lead, LOG-01, TIMELINE-01) stretch a thin budget, and at game end you check victory normally. If any two meters are ≥70% at game end, you win via Condition 3 (like real-world investigations with incomplete findings). If no condition is met at the turn limit, the investigation is inconclusive.

**Q: Can we retry a failed investigation?**
A: You can attempt the same investigation again next turn (costs full budget again), but you still don't know if you'll succeed. You're essentially re-investigating the same evidence looking for something you missed.

---

## Printable Components

All printable cards are available in:
- [cards/forensics/core-deck/investigation-cards.md](../../cards/forensics/core-deck/investigation-cards.md) — 12 Investigation Action cards
- [cards/forensics/core-deck/evidence-cards.md](../../cards/forensics/core-deck/evidence-cards.md) — 12 Evidence cards + 4 Findings cards (Findings section)

Progress Meter Tracker: print templates coming in the print pack. Until then, draw a simple 4-meter tracker on paper: four rows labeled Timeline Completeness, Attack Chain Reconstruction, Attribution Confidence, and Evidence Chain of Custody, each marked 0-100% in 5% steps, plus a Turn row and a Budget row (0-100).

---

**Ready to investigate?** Print your cards, gather 1-4 forensic analysts, and begin your investigation. Good luck!

