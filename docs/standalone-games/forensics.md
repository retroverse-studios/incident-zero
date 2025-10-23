# Forensics Module: Standalone Game Guide

**Version:** 2.1 - Investigation & Attribution Edition
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
- **Budget Tracker** (tracks spending from 0-150)
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
2. **Budget Tracker:** Current budget = 75 (or 100), Max = 150
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
- Declare the Budget cost (shown on card)
- Example: "We'll do a full disk image of the compromised database server and look for persistence mechanisms, rootkits, and artifact evidence. Cost 10 Budget."

**Option B: Analyze Existing Evidence**
- Review 2-4 Evidence cards already discovered
- Describe connections between findings (temporal sequence, technical relationships, or attribution links)
- Example: "The malware sample matches the persistence mechanism we found in scheduled tasks, suggesting the attacker knew exactly what they were doing. Plus, the C2 domain was registered by the same person who registered two other domains we found in old breach reports."

**Option C: Follow Investigative Lead**
- Pick an Evidence card with an "Investigative Lead" noted
- Describe how you'll pursue this lead
- Example: "This C2 domain resolves to a Russian ASN. Let's do a WHOIS lookup and see what other domains are hosted on this infrastructure."

---

#### Step 2: TO Rolls & Resolves (2-3 minutes)

**For Conduct Investigation or Follow Investigative Lead:**

1. **Verify Cost:** Check if Blue Team has sufficient Budget
   - If insufficient Budget, investigation cannot proceed (suggest alternative action)

2. **Set Difficulty Class (DC):** TO checks Investigation Action card for DC
   - Example: Disk Forensics has DC 12
   - Modify DC if anti-forensics present: +2 DC
   - Modify DC if attacker was sophisticated: +1-2 DC

3. **Determine Modifiers:** Apply skill modifiers to the roll
   - +2 if investigator has forensics certification
   - +1 if basic IT security background
   - +2 if team provides detailed technical narrative
   - +1 if previous investigation discovered clues to this action
   - -1 if attempting hastily (rushed, final turn desperation)

4. **Roll:** Investigator (or TO on their behalf) rolls d20

5. **Compare Results:**
   - **Success (roll ≥ DC):** Discover ONE Evidence card + advance relevant Progress Meters by 10-20%
   - **Partial Success (roll DC-3 to DC-1):** Discover partial or incomplete evidence + advance Progress Meter by 5-10%
   - **Failure (roll < DC-3):** No evidence discovered; Budget still spent; take a turn

**For Analyze Existing Evidence:**

1. **Describe Connection:** Blue Team explains how findings are related
2. **Roll:** d20 + investigator skill modifier vs. DC 10
3. **Results:**
   - **Success (≥10):** Gain insight; advance two Progress Meters by 5-10% each
   - **Failure (<10):** No progress; use a turn

---

#### Step 3: Record & Update Tracking (1-2 minutes)

1. **Deduct Budget:** Subtract investigation cost from Budget Tracker
2. **Advance Turn:** Increment Turn counter by 1
3. **Update Progress Meters:** Record any progress from successful investigation
4. **Note Evidence:** If Evidence card discovered, add to Evidence Log with source and chain of custody status
5. **Check Victory Condition:** Did Blue Team achieve any victory condition? (see Victory Conditions section)

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

---

## Victory & Failure Conditions

### Investigation Complete (VICTORY)

Blue Team wins if they achieve ONE of these before running out of turns or budget:

**Victory Condition 1: Attribution Success**
- **Attribution Confidence ≥ 90%** (identified threat actor, techniques, motivations)
- PLUS **Attack Chain Reconstruction ≥ 75%** (understand attack progression)
- **Result:** "You have successfully attributed this attack to [Threat Group]. Intelligence briefing prepared for leadership."

**Victory Condition 2: Complete Timeline & Evidence**
- **Timeline Completeness ≥ 80%** (clear chronological sequence of all major events)
- PLUS **Attack Chain Reconstruction ≥ 80%** (complete understanding of how attacker progressed)
- PLUS **Evidence Chain of Custody ≥ 70%** (evidence is documented and admissible)
- **Result:** "Your forensic investigation is publishable quality and legally defensible. Law enforcement briefed."

**Victory Condition 3: Actionable Findings**
- Budget exhausted (or turn limit reached) early
- BUT achieved **any two Progress Meters ≥ 70%** with clear findings
- **Result:** "Investigation concluded with sufficient findings for remediation. Hardening team can now implement controls."

---

### Investigation Inconclusive (FAILURE)

Blue Team fails if they reach the turn limit with:

- **Any single Progress Meter < 40%** (critical gap in understanding), PLUS
- No coherent findings to act on

**Result:** "Investigation stalled. Too many unanswered questions. Threat actor remains unidentified. Forensic team recommends additional investigation by external firm."

**Consequence of Failure:**
- Investigation results are incomplete and cannot feed into Hardening or Network Building modules
- Audit & Compliance module must assess security posture with incomplete information
- Organization loses confidence in threat intelligence

---

## Example Investigation (Complete Turn)

### Scenario Setup (TO Secret)
> TIER 2 attack: Credential-based lateral movement with persistence
> Turn limit: 10 turns
> Attacker profile: Eastern European cybercriminal group
> Key technique: Password spray → Privilege escalation → Scheduled task persistence → Data exfiltration

### Turn 1

**Blue Team:** "We'll start with event log analysis of the compromised database server. We want to see the login history and identify unusual access patterns."

**Investigator Skill:** IT Security background (+1)

**TO Facilitator:**
1. **Check Cost:** LOG-01 costs 5 Budget. Current budget 75. ✓ OK
2. **Set DC:** LOG-01 has DC 11. No anti-forensics. DC = 11
3. **Apply Modifiers:** +1 (IT security background) + 0 (no prior clues) = +1 total
4. **Roll:** Investigator rolls d20+1. Result: 14
5. **Success!** (14 ≥ 11) → Discover Evidence card "Suspicious Admin Logins (Timeline)"

**Update Tracking:**
- Budget: 75 - 5 = 70 remaining
- Turn: 1 → 2
- Timeline Completeness: 0% → 15% (login timeline discovered)
- Evidence Log: "Suspicious Admin Logins - discovered via Event Log Analysis - Chain of Custody: intact"

**Blue Team Deduction:** "Looks like an admin account was accessed from unusual locations. Might be credential theft."

---

### Turn 2

**Blue Team:** "Let's analyze that malware sample. We want to understand what it does and where it connects to."

**Investigator Skill:** Forensic certification background (+2)

**TO Facilitator:**
1. **Check Cost:** MALW-01 costs 15 Budget. Current budget 70. ✓ OK
2. **Set DC:** MALW-01 has DC 12. Attacker was moderately sophisticated. DC = 13
3. **Apply Modifiers:** +2 (forensic cert) + 0 = +2 total
4. **Roll:** Investigator rolls d20+2. Result: 16
5. **Success!** (16 ≥ 13) → Discover Evidence card "Command-and-Control Callback Domain"

**Update Tracking:**
- Budget: 70 - 15 = 55 remaining
- Turn: 2 → 3
- Attack Chain Reconstruction: 0% → 20% (malware functionality understood)
- Evidence Log: "C2 Domain - discovered via Malware Analysis - Chain of Custody: intact"

**Blue Team Deduction:** "The malware communicates with an external server. That's how the attacker stays in control."

---

### Turn 3-5 (Abbreviated)

**Turn 3:** Network Traffic Analysis (DC 12, roll 15) → Discover "Data Exfiltration Evidence" (evidence of 100+ GB transferred)

**Turn 4:** Timeline Reconstruction (DC 13, roll 10) → Partial success: "Incomplete Timeline" card (some gaps remain)

**Turn 5:** Threat Attribution Analysis (DC 15, roll 17) → Discover "Attacker Infrastructure Map" (multiple C2 domains)

**Progress So Far:**
- Timeline: 30%, Attack Chain: 50%, Attribution: 20%, Chain of Custody: 60%
- Budget: 25 remaining, Turn: 6 of 10

---

### Turn 6 (Critical Decision)

**Blue Team:** "This is expensive, but let's do Memory Forensics Deep Dive on the admin workstation. If the attacker has malware in memory, we might find encryption keys or recent commands that show their intent."

**Investigator Skill:** Forensic analyst (+2)

**TO Facilitator:**
1. **Check Cost:** MEM-02 costs 20 Budget. Current budget 25. ✓ OK (barely)
2. **Set DC:** MEM-02 has DC 15. Advanced investigation. DC = 15
3. **Apply Modifiers:** +2 (forensic analyst) + 1 (prior investigations revealed attacker is sophisticated) = +3
4. **Roll:** Investigator rolls d20+3. Result: 19
5. **Success!** (19 ≥ 15) → Discover "Attacker Command History" + "Encryption Keys"

**Update Tracking:**
- Budget: 25 - 20 = 5 remaining (nearly exhausted)
- Turn: 6 → 7
- Attribution: 20% → 50% (command history shows attacker intent and tools)
- Chain of Custody: 60% → 85% (all evidence now properly documented)
- **CRITICAL CHECK:** Two meters now ≥ 70%! But still need higher for victory...

**Blue Team Deduction:** "We see evidence of Russian-language malware and cryptocurrency mining commands. Eastern European group confirmed!"

---

### Turn 7 (Final Push)

**Blue Team:** "We have 5 Budget left and 3 turns. Let's do a quick THREAT-01: Threat Attribution Analysis. We have enough evidence to make a determination."

**Investigator Skill:** Security analyst (+1)

**TO Facilitator:**
1. **Check Cost:** THREAT-01 costs 20 Budget. Current budget 5. ✗ NOT ENOUGH
2. **Alternative:** "You don't have enough budget for THREAT-01. You could do LOG-02 (Deep Log Correlation) for 10 Budget instead, but you'd need to use this turn and next turn might be your last."

**Blue Team Pivots:** "OK, we'll use our follow investigative lead action instead. That C2 domain we found—let's do WHOIS and ASN lookup to find related attacker infrastructure."

**TO Facilitator:**
1. **Set DC:** Follow Lead is DC 12
2. **Apply Modifiers:** +2 (good idea, references prior evidence) = +2
3. **Roll:** d20+2 = 18
4. **Success!** → Discover "Attacker Infrastructure Network" evidence

**Update Tracking:**
- Budget: 5 remaining (effectively exhausted)
- Turn: 7 → 8 of 10
- Attribution: 50% → 75% (infrastructure linked to known threat group)

**Blue Team Assessment:** "We have 75% attribution and solid evidence. Let's see if we meet victory condition..."

---

### Victory Determination (After Turn 8)

**Check Victory Conditions:**

**Condition 1: Attribution ≥ 90%?** No (75%)
**Condition 2: Timeline + Chain of Custody ≥ 80% combined?** Timeline 30%, Chain of Custody 85% = 60% average. No.
**Condition 3: Two meters ≥ 70% with budget exhausted?**
- Attribution: 75% ✓
- Chain of Custody: 85% ✓
- Budget: Nearly exhausted (5 remaining) ✓
- **YES! VICTORY CONDITION 3 MET!**

**Game Ends with VICTORY**

> **Investigation Result:** "Your forensic investigation successfully identified the attacker as a member of the [Eastern European Cybercriminal Group]. Key findings:
> - Attack vector: Credential theft via password spray
> - Persistence: Scheduled task malware
> - Exfiltration: 100+ GB customer database records
> - Timeline: 3-week dwell time before discovery
> - Attribution: 75% confidence linked to known group; 85% evidence admissibility
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

- **If game is ending early** (Victory Condition 3 before turn 6): Let it happen. Means they played smart.
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
1. **Choose action:** Conduct Investigation, Analyze Evidence, or Follow Lead
2. **Pay cost:** Deduct Budget
3. **Roll d20:** Add skill modifier, compare to DC
4. **Resolve:** Discover evidence, advance Progress Meters, or fail
5. **Update:** Budget, Turn counter, Progress Meters

**Resources:**
- Budget: 75 (represents forensic lab time)
- Turns: 6-15 (depends on tier + d4 roll)
- Progress Meters: Timeline, Attack Chain, Attribution, Chain of Custody (each 0-100%)

**Victory:**
- Attribution ≥ 90% + Attack Chain ≥ 75%, OR
- Timeline ≥ 80% + Chain of Custody ≥ 70%, OR
- Any two meters ≥ 70% + Budget exhausted/nearly exhausted

**Failure:** Any meter < 40% at turn limit = Inconclusive investigation

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
  - [ ] Malware & Persistence (3 cards)
  - [ ] Credentials & Access (2 cards)
  - [ ] Lateral Movement (2 cards)
  - [ ] Exfiltration (2 cards)
  - [ ] Infrastructure (2 cards)
  - [ ] Timeline (1 card)

- [ ] 4 Findings Cards
  - [ ] Threat Attribution
  - [ ] Attack Surface
  - [ ] Persistence Analysis
  - [ ] Control Gaps

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
A: That's a realistic outcome! You must work with what you've discovered. Did you achieve Victory Condition 3 (two meters ≥70%)? If so, you win with incomplete findings (like real-world investigations). If not, investigation is inconclusive.

**Q: Can we retry a failed investigation?**
A: You can attempt the same investigation again next turn (costs full budget again), but you still don't know if you'll succeed. You're essentially re-investigating the same evidence looking for something you missed.

---

## Printable Components

All printable cards and tracking sheets are available in:
- [cards/forensics/core-deck/investigation-cards.md](../../cards/forensics/core-deck/investigation-cards.md)
- [cards/forensics/core-deck/evidence-cards.md](../../cards/forensics/core-deck/evidence-cards.md)
- [cards/forensics/core-deck/findings-cards.md](../../cards/forensics/core-deck/findings-cards.md)
- [Forensics Progress Meter Tracker (Excel/Google Sheets template)](../../assets/forensics-tracker-template.xlsx)

---

**Ready to investigate?** Print your cards, gather 1-4 forensic analysts, and begin your investigation. Good luck!

