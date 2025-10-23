# Hardening Module: Standalone Play Guide

**Duration:** 30-45 minutes
**Players:** 1 Threat Orchestrator + 2-4 Blue Team members
**Best For:** Defense architecture training, security design, proactive hardening practice

---

## Module Overview

The **Hardening Module** teaches players how to build **defense-in-depth**—layered security controls that work together to protect critical systems. Players deploy defenses strategically, harden existing controls, and defend against pentester challenges.

This module focuses on **proactive security** rather than reactive incident response.

---

## Setup (5 minutes)

### 1. Choose Difficulty Level

| Difficulty | Budget | Pentester Tactics | Best For |
|------------|--------|------------------|----------|
| **Beginner** | 150 | 2 cards | First-time, teaching defense concepts |
| **Intermediate** | 150 | 3 cards | Standard play, balanced challenge |
| **Advanced** | 150 | 4 cards | Experienced players, comprehensive test |

### 2. Set Your Scenario Context

**Option A: Hypothetical Threat (Solo)**
Threat Orchestrator describes a realistic threat scenario:

> "Imagine your team successfully detected an attack last month. The attacker started with a phishing email, moved laterally through the network via SMB, and escalated privileges using a kernel exploit. Now you have time to harden your defenses. Here's the threat profile you need to defend against..."

**Option B: Follow from Incident Response Module**
If continuing from Incident Response:
- Use the attack chain that was just played
- Players now design defenses against those specific threats
- Discovered vectors guide defense selection

**Option C: Generate Threat Vectors Randomly**
Roll 1d6 for each threat vector to determine which threats you must defend against:
- Roll 1d6 for SOCIAL ENGINEERING threats (1-2=beginner, 3-4=intermediate, 5-6=advanced)
- Roll 1d6 for WEB EXPLOIT threats
- Roll 1d6 for CREDENTIAL ABUSE threats
- Roll 1d6 for MALWARE threats
- Roll 1d6 for NETWORK threats

### 3. Blue Team Setup

- Starting Budget: **150** (represents planning time/resources)
- Draw 5 Defense Cards (random, face down)
- Place Security Score Tracker at **0**
- Place Hardening Tokens/Upgrade Counter at **0**
- Prepare to track deployed defenses on paper/board

### 4. Prepare Pentester Tactic Cards

- Shuffle the Pentester Tactic Card deck
- Set aside **2-4 cards** based on difficulty (don't reveal yet)
- These will be drawn mid-game to test the team's defenses

---

## Gameplay Loop (25-35 minutes)

### Round Structure

Each turn represents time allocated to hardening (15-30 minutes of planning work per turn).

**TURN SEQUENCE:**

**1. START OF TURN**
- Read turn number aloud ("Hardening Turn 1...")
- Remaining budget announced

**2. BLUE TEAM'S TURN (2-3 minutes discussion)**
- Discuss which hardening action to take
- Decide strategy (deploy new defense, upgrade existing, create playbook)

**3. ACTION EXECUTION**
- Perform chosen action
- No roll needed for deployment (see below for when rolls occur)
- Update trackers

**4. END OF TURN**
- Advance Turn Tracker by 1
- Draw 1 new Defense Card
- Check if mid-game Pentester Challenge should occur

### Four Available Actions

#### Action 1: Deploy a New Defense 🛡️

**Cost:** 10/15/25 Budget (by tier)
**Roll Required:** None—automatic success

**How it works:**
1. Choose a Defense Card from your hand
2. Announce which Asset or threat vector it defends
3. Explain strategy (optional but encouraged): "Why are we deploying this defense?"
4. Card is placed on the table (face up)

**Outcome:**
- Defense is immediately active
- No roll needed
- All deployed defenses contribute to final Security Score

**Note:** You can deploy the same defense multiple times (e.g., two MFA implementations on different systems) if you have duplicate cards.

---

#### Action 2: Harden an Existing Defense ⬆️

**Cost:** 5 Budget per upgrade
**Roll Required:** None

**How it works:**
1. Choose a Defense Card already deployed (from this turn or previous)
2. Pay 5 Budget
3. Mark defense with **+2 effectiveness bonus** (track on paper next to the card)
4. Optionally explain: "We're improving this defense by..."

**Examples of hardening:**
- "Hardening our EDR deployment by tuning behavioral analytics and adding threat intel integration" → EDR now has +2 bonus
- "Hardening our MFA implementation by enabling hardware token requirements" → MFA now has +2 bonus
- "Hardening Network Segmentation by adding microsegmentation within critical zones" → Network Seg now has +2 bonus

**Strategic Value:**
- Each upgrade adds +2 to the defense's effectiveness
- Upgrades can stack (e.g., MFA with +2, +2, +2 = +6 total)
- Upgraded defenses are more likely to survive Pentester Tactics

---

#### Action 3: Create an Incident Response Playbook 📋

**Cost:** 10 Budget per playbook
**Roll Required:** None

**How it works:**
1. Choose a specific threat vector you want to prepare for
2. Write a 1-2 sentence playbook describing your response: (e.g., "Ransomware Outbreak Response: Immediate backup isolation, network segmentation, and access revocation")
3. Place playbook card on the table
4. When a Pentester uses a matching vector later, you get **+3 bonus** to your defense roll

**Example Playbooks:**
- "Credential Compromise Incident: Forced MFA re-authentication and access token revocation"
- "Supply Chain Attack Detection: Monitor unusual DNS and C2 beaconing patterns"
- "Insider Threat Response: Behavioral analytics review and privileged access audit"
- "Ransomware Response: Immediate backup isolation and network segmentation"

**Strategic Value:**
- Playbooks cost more (10 Budget) but provide larger bonus (+3)
- Limited use (one-time per playbook, then discarded after use)
- Forces teams to predict which threats are most dangerous

---

#### Action 4: Test & Drill Defenses 🎯

**Cost:** 0 Budget (represents time, not money)
**Roll Required:** 11+ on d20

**How it works:**
1. Announce you're conducting a drill/test of deployed defenses
2. Choose one or more deployed defenses to test
3. Roll 1d20 for each defense
4. Each defense with roll of 11+ succeeds; 10 or less fails

**Outcome:**
- Success: Defense works properly; mark it as "tested" (contributes extra points at end)
- Failure: Defense has implementation issues; no penalty, but doesn't count toward testing bonus

**Strategic Value:**
- Free way to validate defenses
- Successful tests add confidence (and points) but don't guarantee success against real attacks
- Encourages thinking about deployment validation (realistic practice)

---

## Mid-Game: Pentester Challenge

**After turn 3 or 4**, the Threat Orchestrator draws a **Pentester Tactic Card** and launches a simulated attack.

### Pentester Attack Resolution

**1. TO Describes the Attack Scenario**
Example: "Your red team just attempted to use a detection evasion technique to bypass your SIEM and EDR monitoring. Can your team detect it?"

**2. Tactic Card Effects Apply**
Read special effects (e.g., "Bypass Basic Defenses" disables all 10-Budget defense cards)

**3. Blue Team Chooses a Defense to Counter**
Team selects one deployed defense to defend against this attack

**4. Roll with Modifiers**
- **Base:** Roll 11+ on d20
- **Apply Pentester penalties** (from tactic card)
- **Apply Hardening bonuses** (from upgrades: +2 per upgrade)
- **Apply Playbook bonuses** (if applicable: +3 if matching vector)

**5. Outcome**
- **Success:** No reputation loss, defense holds
- **Failure:** -10 Reputation (represents a successful intrusion during the drill)

**Optional:** Play multiple pentester tactics (2-4 total) across turns 3-6.

---

## Scoring & Final Security Posture

### Security Score Calculation

```
Defenses Deployed:        Count × 5 points
Hardening Upgrades:       Count × 2 points
Playbooks Created:        Count × 10 points
Pentester Tactics Won:    Count × 3 points
Budget Efficiency:        (Remaining Budget / Starting Budget) × 10 points

EXAMPLE (150 starting budget):
- 6 defenses deployed:    30 points
- 5 hardening upgrades:   10 points
- 2 playbooks created:    20 points
- 3 of 4 pentester wins:  9 points
- 25 budget remaining:    1.7 points
────────────────────────────
TOTAL SECURITY SCORE:     70.7 points
```

### Scoring Tiers

| Score | Level | Interpretation |
|-------|-------|-----------------|
| **85-100** | Exceptional | Enterprise-grade security posture; sophisticated threat preparedness |
| **70-84** | Strong | Mid-market ready; layered, comprehensive defenses |
| **55-69** | Adequate | Startup-level protection; covers main attack vectors |
| **40-54** | Basic | Minimal protection; significant gaps remain |
| **Below 40** | Vulnerable | Inadequate defenses; likely to fail against sophisticated attacks |

---

## Winning & Losing

### Victory Condition ✓

**Blue Team Wins Hardening if:**
- Final Security Score ≥ 70 (strong layered defenses)
- AND Budget remaining ≥ 10 (resourceful allocation)
- AND most Pentester Tactics were successfully defended against

### Defeat Condition ✗

**Blue Team Loses Hardening if:**
- Final Security Score < 40 (inadequate protection)
- OR Budget exhausted before defenses were deployed
- OR majority of Pentester Tactics succeeded despite defenses

---

## Debrief & Reflection (5-10 minutes)

**PART 1: DEFENSE STRATEGY (3 min)**
1. "How did you prioritize which defenses to deploy first?"
2. "What layers of defense work best together?"
3. "Did the Pentester Tactics reveal gaps? Which ones?"

**PART 2: RESOURCE MANAGEMENT (2 min)**
1. "Did you run out of budget? Would more budget have helped?"
2. "Which defenses provided the best value (cost vs. effectiveness)?"
3. "Would you have allocated budget differently?"

**PART 3: PENTESTER RESULTS (2-3 min)**
1. "Which Pentester Tactic was most surprising?"
2. "Which defense was most valuable against attacks?"
3. "How would you harden further given unlimited budget?"

**PART 4: REAL-WORLD APPLICATION (2 min)**
1. "If you were hardening your actual organization, what would you deploy first?"
2. "Why is defense-in-depth difficult in practice?"
3. "What's the hardest part of maintaining layered security?"

---

## Tips for Threat Orchestrators

### Balancing Defense Deployment

**Too Easy:**
- Teams deploy 8+ defenses with budget to spare
- All Pentester Tactics fail
- No difficult decisions required

**Too Hard:**
- Teams can only afford 3-4 defenses
- Most Pentester Tactics succeed
- Team feels overwhelmed

**Just Right:**
- Teams deploy 5-7 defenses with some budget left
- 50-70% of Pentester Tactics fail
- Teams debate defense priorities

**Adjust by:**
- Starting budget (120, 150, or 180)
- Number of Pentester Tactics (2, 3, or 4)
- Defense card availability (more common defense draws)

### Pentester Tactic Timing

- **Turn 1-2:** Let teams deploy initial defenses (no pentester challenge)
- **Turn 3-4:** First Pentester Challenge
- **Turn 5-6:** Second Pentester Challenge (if time allows)

**Narrative framing:** "Your red team has tested your defenses..."

### Running as Competitive Tournament

If multiple teams are hardening simultaneously:
- All teams get same starting threat vectors
- All teams draw from same card deck (or equivalent decks)
- Highest Security Score wins
- Tiebreaker: Most Budget remaining

---

## Sample Scenarios to Try

### Scenario 1: "Post-Phishing Hardening" (Beginner)
**Threat Vector:** SOCIAL ENGINEERING
**Budget:** 150
**Pentester Tactics:** 2

**Setup:** "Your team detected a phishing attack. Now harden against social engineering threats."

**Suggested defenses:**
- Email Authentication Setup (BASIC)
- User Security Training (BASIC)
- Multi-Factor Authentication (ADVANCED)
- User & Entity Behavior Analytics (ELITE)

---

### Scenario 2: "Ransomware Preparedness" (Intermediate)
**Threat Vectors:** MALWARE, DATA EXFIL, NETWORK
**Budget:** 150
**Pentester Tactics:** 3

**Setup:** "A ransomware variant targeted your industry. Prepare your defenses."

**Key defenses:**
- EDR (Endpoint Detection & Response)
- Data Loss Prevention (DLP)
- Network Segmentation
- Deception Technology (Honeypots)
- Incident Response Playbooks

---

### Scenario 3: "Enterprise Hardening" (Advanced)
**Threat Vectors:** All 6 (SOCIAL ENGINEERING, WEB EXPLOIT, CREDENTIAL ABUSE, MALWARE, NETWORK, DATA EXFIL)
**Budget:** 150
**Pentester Tactics:** 4

**Setup:** "Your enterprise faces threats across all vectors. Build comprehensive defense-in-depth."

**Challenge:** Defend against all six vectors with limited budget

---

## Extensions & Variations

### Hardening Plus (Extended Play)

**Duration:** 45-60 minutes
- Start with Budget: 200 (more resources)
- Play 5-7 turns (more time)
- 4-5 Pentester Tactics (more challenges)
- Create 4-5 playbooks instead of 2-3

### Defense-in-Depth Deep Dive

**Focus on layering:**
- Each turn, discuss *why* defenses work together
- Create explicit layer descriptions: "Layer 1 (Prevention), Layer 2 (Detection), Layer 3 (Response)"
- Score based on how well defenses complement each other

### Compliance Integration

**Add compliance requirement:**
- Teams must defend against threat vectors while meeting compliance requirements (PCI-DSS, GDPR, HIPAA)
- Some defenses satisfy both security and compliance
- Creates strategic depth

---

## Next Steps After This Module

**If you won:**
- Continue to **Incident Response Module** (as follow-up) → Test your defenses against attacks
- Continue to **Audit & Compliance Module** → Validate your security posture

**If you lost:**
- Replay with higher budget
- Try a less complex scenario
- Play Incident Response to understand what defenses are actually needed

**Standalone:** Play again with different threat vectors and Pentester Tactics

---

## Quick Reference: Action Costs & Effects

| Action | Cost | Effect | Roll |
|--------|------|--------|------|
| **Deploy Defense** | 10/15/25 | Defense active immediately | None |
| **Harden Upgrade** | 5 | +2 effectiveness to defense | None |
| **Create Playbook** | 10 | +3 bonus when used once | None |
| **Test & Drill** | 0 | Validate defenses | 11+ |

---

## Need Help?

- **Questions about rules?** See [Core Rules](../rules/core-rules.md)
- **Want to combine modules?** See [Module Combinations](../module-combinations.md)
- **Confused about scoring?** See [FRAMEWORK.md](../FRAMEWORK.md)

---

*Hardening Module - Standalone Play Guide*
*Part of Incident Zero, a modular cybersecurity board game*

