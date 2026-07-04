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

All difficulty levels run **7 turns**, one action per turn (v2.2). Difficulty scales via Pentester Tactic count.

| Difficulty | Budget | Turn Limit | Pentester Tactics | Best For |
|------------|--------|-----------|------------------|----------|
| **Beginner** | 150 | 7 turns | 2 cards | First-time, teaching defense concepts |
| **Intermediate** | 150 | 7 turns | 3 cards | Standard play, balanced challenge |
| **Advanced** | 150 | 7 turns | 4 cards | Experienced players, comprehensive test |

### 2. Set Your Scenario Context

**Option A: Hypothetical Threat (Solo)**
Threat Orchestrator describes a realistic threat scenario:

> "Imagine your team successfully detected an attack last month. The attacker started with a phishing email, moved laterally through the network via SMB, and escalated privileges using a kernel exploit. Now you have time to harden your defenses. Here's the threat profile you need to defend against..."

**Option B: Follow from Incident Response Module**
If continuing from Incident Response:
- Use the attack chain that was just played
- Players now design defenses against those specific threats
- Discovered vectors guide defense selection

**Option C: Generate Threat Vectors Randomly (v2.2 — one standard procedure)**
Roll **1d6 for each of the six threat vectors** to determine which threats you must defend against (1-2 = no notable threat, 3-4 = intermediate threat, 5-6 = advanced threat):
- Roll 1d6 for SOCIAL ENGINEERING threats
- Roll 1d6 for WEB EXPLOIT threats
- Roll 1d6 for CREDENTIAL ABUSE threats
- Roll 1d6 for MALWARE threats
- Roll 1d6 for NETWORK threats
- Roll 1d6 for DATA EXFIL threats

### 3. Blue Team Setup

- Starting Budget: **150** (represents planning time/resources)
- Draw 5 Defense Cards (random, face down)
- Place Security Score Tracker at **0**
- Place Hardening Tokens/Upgrade Counter at **0**
- Prepare to track deployed defenses on paper/board
- Optional: Place relevant Asset Cards on the table for scenario context (shared components — see `cards/network-building/core-deck/asset-cards.md`)

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

**Quick-Win Rule (v2.2):** You may deploy **up to 2 BASIC-tier defenses as a single action** (pay 10 Budget each).

**Note (v2.2):** The core deck contains one copy of each defense (D-01 to D-24), so each defense can only be deployed once per game. If you want duplicate deployments (e.g., two MFA implementations on different systems), print a second copy of the deck and house-rule it.

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
**Limit (v2.2):** Maximum **2 playbooks per game**

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
- Limited use (one-time per playbook, then discarded after use; max 2 per game)
- Forces teams to predict which threats are most dangerous
- Playbooks alone cannot win: victory requires at least 4 deployed defenses (v2.2)

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

**After turn 3 or 4**, the Threat Orchestrator draws a **Pentester Tactic Card** (PT-01 to PT-08, see `cards/hardening/core-deck/pentester-tactic-cards.md`) and launches a simulated attack.

### Pentester Attack Resolution (v2.2 — one canonical formula)

**1. TO Describes the Attack Scenario**
Example (PT-02): "Your red team delivered a payload that uses only built-in Windows tools — living-off-the-land. Can your defenses detect it?"

**2. Blue Team Chooses ONE Deployed Defense to Resolve With**
Team selects one deployed defense to defend against this attack

**3. Roll the Defense Roll**

> **Defense roll = d20 + printed defense bonus for the chosen defense (from the tactic card's bonus list) + hardening upgrades on that defense (+2 each) + relevant playbook (+3, one-time, matching vector)**
>
> **Success if the total ≥ the tactic card's printed DC** (DC 12-15 for PT-01 to PT-08).

If the chosen defense isn't on the tactic's bonus list, its printed bonus is +0 (upgrades and playbooks still apply). Multi-vector tactics: two separate rolls, one defense each.

**4. Outcome**
- **Success:** Defense holds; count as a Pentester Tactic Defended (+5 Security Score)
- **Failure:** Attack succeeds; apply the consequence printed on the tactic card; no score for this tactic

**Optional:** Play multiple pentester tactics (2-4 total) across turns 3-6.

---

## Scoring & Final Security Posture

### Security Score Calculation (v2.2 — same formula as the module rules)

```
Defenses Deployed:          Count × 5 points
Hardening Upgrades:         Count × 2 points
Playbooks Created:          Count × 10 points   [max 2 playbooks per game]
Pentester Tactics Defended: Count × 5 points
Budget Efficiency:          (Remaining Budget / Starting Budget) × 10 points

EXAMPLE (150 starting budget, 7 turns):
- 7 defenses deployed (two turns used the 2-BASIC Quick-Win):  35 points
- 1 hardening upgrade:                                          2 points
- 1 playbook created:                                          10 points
- 3 of 3 pentester tactics defended:                           15 points
- 50 budget remaining (spent 100): (50/150) × 10 ≈              3 points
────────────────────────────
TOTAL SECURITY SCORE:                                          65 points → Strong (Victory)
```

### Scoring Tiers (v2.2 — rescaled for the 7-action economy)

| Score | Level | Interpretation |
|-------|-------|-----------------|
| **75+** | Exceptional | Enterprise-grade security posture; sophisticated threat preparedness |
| **60-74** | Strong | Mid-market ready; layered, comprehensive defenses |
| **45-59** | Adequate | Startup-level protection; covers main attack vectors |
| **30-44** | Weak | Minimal protection; significant gaps remain |
| **Below 30** | Vulnerable | Inadequate defenses; likely to fail against sophisticated attacks |

---

## Winning & Losing

### Victory Condition ✓ (v2.2)

**Blue Team Wins Hardening if ALL of:**
- Final Security Score ≥ 60 (strong layered defenses)
- AND at least 4 defenses deployed (playbooks and upgrades alone cannot win)
- AND majority of Pentester Tactics were successfully defended against

### Defeat Condition ✗

**Blue Team Loses Hardening if:**
- Final Security Score < 45 (inadequate protection)
- OR Budget exhausted before defenses were deployed
- OR majority of Pentester Tactics succeeded despite defenses

Scores of 45-59 that meet the tactic/defense requirements count as a partial success.

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
- D-01: Email Authentication Setup (BASIC)
- D-02: User Security Training (BASIC)
- D-07: Multi-Factor Authentication (ADVANCED)
- D-20: Zero Trust Access Control (ELITE)

---

### Scenario 2: "Ransomware Preparedness" (Intermediate)
**Threat Vectors:** MALWARE, DATA EXFIL, NETWORK
**Budget:** 150
**Pentester Tactics:** 3

**Setup:** "A ransomware variant targeted your industry. Prepare your defenses."

**Key defenses:**
- D-08: EDR (Endpoint Detection & Response)
- D-11: Data Loss Prevention (DLP)
- D-09: Network Segmentation
- D-15: Deception Technology (Honeypots)
- D-19: Backup & Disaster Recovery
- D-23: IR Program & Runbooks

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
- Play 9 turns instead of 7 (more time)
- 4-5 Pentester Tactics (more challenges)
- Raise the playbook cap from 2 to 3

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
| **Deploy Defense** | 10/15/25 | Defense active immediately (up to 2 BASIC per action, v2.2) | None |
| **Harden Upgrade** | 5 | +2 effectiveness to defense | None |
| **Create Playbook** | 10 | +3 bonus when used once (max 2 per game, v2.2) | None |
| **Test & Drill** | 0 | Validate defenses | 11+ |

**Pentester defense roll (v2.2):** d20 + printed bonus (one chosen defense) + upgrades (+2 each) + playbook (+3) ≥ tactic DC.

*For the full list of v2.2 changes and the reasoning behind them, see the "v2.2 Playtest Edition Changes" section in [Module: Hardening](../rules/module-hardening.md).*

---

## Need Help?

- **Questions about rules?** See [Core Rules](../rules/core-rules.md)
- **Want to combine modules?** See [Module Combinations](../module-combinations.md)
- **Confused about scoring?** See [FRAMEWORK.md](../FRAMEWORK.md)

---

*Hardening Module - Standalone Play Guide*
*Part of Incident Zero, a modular cybersecurity board game*

