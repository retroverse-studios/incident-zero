# Disaster Recovery Module: Standalone Play Guide

**Duration:** 30-45 minutes
**Players:** 1 Threat Orchestrator + 2-4 Blue Team members
**Best For:** Crisis management training, incident response procedures, stakeholder communication

---

## Module Overview

The **Disaster Recovery Module** teaches players how to **manage a real breach**—investigation, forensics, stakeholder communication, and recovery decisions under extreme pressure.

Players must balance investigation thoroughness, stakeholder notification timing, evidence preservation, and critical decisions (ransom, negotiation) while their reputation score ticks down.

---

## Setup (5 minutes)

### 1. Set the Crisis Scenario

**The Breach Has Already Succeeded**

Threat Orchestrator reveals the full attack chain that succeeded:

> "Your organization has experienced a significant data breach. Here's what happened:
>
> **Attack Chain:**
> 1. Phishing Campaign → Employee clicked malicious link
> 2. Credential Harvesting → Login credentials captured
> 3. VPN Access → Attacker gained network access
> 4. Lateral Movement → Access to production servers
> 5. Database Exfiltration → 500,000+ customer records stolen
>
> **Current Status:**
> - Breach discovered 24 hours ago (dwell time = 24 hours)
> - Attacker demanding $1M ransom
> - Media starting to ask questions
> - You have 7 "turns" (48 hours) to respond
>
> **Your Challenge:**
> Investigate the breach, communicate with stakeholders, preserve evidence, and recover systems—all while managing reputation and costs."

### 2. Choose Breach Scope

| Scope | Records Affected | Dwell Time | Starting Reputation | Difficulty |
|-------|------------------|-----------|-------------------|------------|
| **Small** | 50,000 | 12 hours | 100 | Beginner |
| **Medium** | 500,000 | 24 hours | 90 | Intermediate |
| **Large** | 5M+ | 48 hours | 80 | Advanced |

### 3. Blue Team Setup

- **Starting Budget:** 50 (emergency crisis fund)
- **Starting Reputation:** 100 (or modified based on scope)
- **Turn Limit:** 7 turns (represents 6-hour intervals)
- **Turn 1 = 6 hours after discovery**
- **Turn 7 = 48 hours after discovery**

Initialize tracking sheets:
- Reputation Tracker (starts at 100)
- Financial Impact Sheet (track all costs)
- Stakeholder Log (who was notified and when)
- Turn Counter

### 4. Crisis Timeline (Place on Table)

| Turn | Time | Event | Deadline |
|-----|------|-------|----------|
| 1 | 6h | Internal discovery & legal | — |
| 2 | 12h | **Regulatory notification required by end of turn** | End of Turn 2 |
| 3 | 18h | Customer notification begins | — |
| 4 | 24h | Media discovers breach (external pressure) | — |
| 5 | 30h | **Ransom deadline (attacker threat)** | Turn 5 |
| 6 | 36h | First lawsuits filed | — |
| 7 | 48h | **Crisis period ends** | — |

---

## Gameplay Loop (25-35 minutes)

### Turn Structure

Each turn represents 6 hours of crisis response time.

**TURN SEQUENCE:**

**1. START OF TURN**
- Read turn number and time elapsed ("Turn 3: 18 hours after discovery...")
- Check deadlines (regulatory notification, ransom deadline, lawsuits, etc.)
- Apply any automatic reputation changes
- Announce remaining budget and reputation

**2. BLUE TEAM'S TURN (2-3 minutes discussion)**
- Discuss crisis response strategy
- Decide on ONE action to take this turn
- Consider: Do we investigate, communicate, preserve evidence, remediate, or decide on ransom?

**3. ACTION EXECUTION**
- Perform chosen action (see five options below)
- Roll if investigation/negotiation required
- Apply outcome

**4. END OF TURN**
- Advance Turn Counter by 1
- Check for deadline events
- Resolve mandatory notifications

---

### Five Crisis Response Actions

#### Action 1: Forensic Investigation 🔬

**Cost:** 5-15 Budget (by scope)
**Roll Required:** 11+ on d20

**How it works:**
1. Team describes what they're investigating: "System logs? Database access patterns? File modification timestamps?"
2. Scope of investigation (5 Budget = focused, 15 Budget = comprehensive)
3. Roll 1d20

**Outcomes:**
- **Success (11+):** Gain important breach information
  - Identify scope and timeline
  - Understand attack methodology
  - Discover if attacker has secondary access
  - Determine if backup systems were compromised

- **Failure:** Budget spent, limited information gained
  - Forensics take longer than expected
  - Evidence is partially corrupted

**Strategic Value:**
- Comprehensive investigation (15 Budget) provides better information for recovery
- Rushed investigation (5 Budget) is cheaper but leaves gaps
- Information can guide remediation decisions

---

#### Action 2: Stakeholder Communication 📢

**Cost:** 0-10 Budget (by scope)
**Roll Required:** None (but strategy matters)

**How it works:**
1. Choose stakeholder to notify: Customers, Regulators, Media, Insurance, Legal
2. Decide communication quality: Transparent, Adequate, or Poor
3. Budget determines response quality (0 = brief/delayed, 10 = comprehensive/immediate)

**Reputation Changes:**
- **Transparent Communication:** +5 Reputation (honest, proactive)
- **Adequate Communication:** 0 Reputation (meets legal requirements)
- **Poor Communication:** -10 to -20 Reputation (delayed, inadequate, evasive)

**Mandatory Deadlines:**
- **Turn 2 (12h):** Must notify regulators (late = -20 reputation per turn)
- **Turn 3 (18h):** Must begin customer notification (late = -10 reputation per day)
- **Turn 4 (24h):** Media discovers breach (automatic reputation hit = -15)

**Strategic Decisions:**
- **Customers first?** Builds trust but costs 10 Budget
- **Regulators only?** Meets legal minimum (0 Budget) but damages reputation
- **Transparent about ransom demand?** Risky but honest
- **Keep ransom secret from public?** Saves reputation but unethical if discovered

---

#### Action 3: Evidence Preservation 🔐

**Cost:** 5-20 Budget (by extent)
**Roll Required:** None

**How it works:**
1. Team describes evidence preservation strategy: "Secure isolated systems? Backup forensic images? Establish chain of custody?"
2. Budget spent determines preservation quality
3. Evidence is crucial for legal proceedings and investigation

**Outcomes:**
- **Minimal (5 Budget):** Evidence documented but not fully secured
- **Standard (10 Budget):** Professional forensic imaging and chain of custody
- **Comprehensive (20 Budget):** Full forensic preservation + legal documentation + third-party verification

**Strategic Value:**
- Good evidence preservation helps lawsuits (cost later vs. settlement earlier)
- Poor preservation damages legal case (increases settlement costs)
- Some budget for evidence preservation is mandatory to satisfy legal requirements

---

#### Action 4: Remediation & Hardening 🔨

**Cost:** 10-25 Budget (by scope)
**Roll Required:** None (but timing matters)

**How it works:**
1. Team describes remediation: "Revoke compromised credentials? Patch vulnerable systems? Install EDR?"
2. Budget spent determines remediation scope
3. Early remediation (turns 1-3) prevents secondary compromises
4. Late remediation (turns 5+) is less effective

**Outcomes:**
- **Minimal (10 Budget):** Remove attacker access (phishing accounts, stolen credentials)
- **Standard (15 Budget):** Remove access + patch critical vulnerabilities
- **Comprehensive (25 Budget):** Full system remediation + hardening improvements

**Strategic Value:**
- Early remediation prevents re-compromise during crisis
- Fast remediation prevents PR disasters ("attacker still in system")
- Delayed remediation compounds reputational damage

---

#### Action 5: Ransom Decision 💰

**Cost:** Varies (or $0 if refusing)
**Roll Required:** 10+ for negotiation

**How it works:**

**Option A: Pay the Ransom**
- Cost: 10-30 Budget (depending on negotiated amount)
- Reputation: -15 (paying criminals is unpopular)
- No guarantee attacker deletes data
- But: Faster recovery, stops public timer

**Option B: Negotiate**
- Cost: 5 Budget
- Roll: 10+ on d20
- Success: Reduce ransom demand by 50%
- Failure: Attacker increases demand or deadline
- Outcome: Still damages reputation -10, but cheaper

**Option C: Refuse & Fight**
- Cost: 0 Budget
- Reputation: +5 (standing up to criminals)
- Outcome: Attacker publishes data (external PR hit -20)
- Allows focus on investigation/remediation without ransom pressure

**Decision Framework:**
- **Small breach (50K records)?** Refusing is reasonable; public impact containable
- **Medium breach (500K)?** Negotiation prudent; publishing damages reputation significantly
- **Large breach (5M)?** Paying might be cost-effective (lawsuits exceed ransom)

**Attacker Context:** Was the attacker nation-state (no negotiation), criminal gang (may negotiate), or opportunistic (likely to delete if paid)?

---

## Deadline Management

### Critical Moments (Built into Timeline)

**Turn 2 (12 hours): Regulatory Notification Deadline**
- **Required:** Notify regulators of breach
- **If late:** -20 reputation per turn delayed
- **Cost:** 5-10 Budget (quality of notification matters)

**Turn 3 (18 hours): Customer Notification Deadline**
- **Required:** Begin customer notification
- **If late:** -10 reputation per day delayed
- **Cost:** 5-10 Budget (quality matters)
- **Note:** Notification method affects reputation (email vs. phone call vs. media conference)

**Turn 4 (24 hours): Media Discovery**
- **Automatic:** Media discovers and publishes breach
- **Impact:** -15 reputation (automatic, unavoidable)
- **Mitigation:** Proactive transparency before this turn can reduce damage

**Turn 5 (30 hours): Ransom Deadline**
- **Decision required:** Pay, negotiate, or refuse
- **If no decision:** Attacker starts publishing data (-20 reputation)

**Turn 7 (48 hours): Crisis Period Ends**
- **Accounting:** Final reputation, costs, litigation exposure calculated
- **End:** Transition to recovery phase (if continuing to other modules)

---

## Scoring & Final Reputation

### Reputation Score Calculation

```
Starting Reputation:            (80-100 based on scope)
Forensic Investigation:         +3 per quality investigation
Stakeholder Communication:       +5 (transparent), 0 (adequate), -10 to -20 (poor)
Evidence Preservation:          +5 for good preservation
Remediation Effectiveness:      +5 for comprehensive, 0 for minimal
Regulatory Compliance:          +10 for on-time notification, -20 per day late
Customer Notification:          +5 for transparent, 0 for adequate, -10 for poor
Ransom Decision:               -15 (pay), -10 (negotiate), +5 (refuse & fight)
Media Management:              -15 (automatic), mitigated by proactive transparency
Legal Compliance:              ±varies

EXAMPLE:
Starting: 90
Forensic: +3
Communication: +5 (transparent with customers)
Evidence: +5
Remediation: +5
Regulatory: +10
Customer: +5
Ransom: -10 (negotiated)
Media: -15 (but mitigated by early transparency = -10 net)
────────────────────────
FINAL REPUTATION: 83
```

### Outcome Tiers

| Reputation | Outcome | Interpretation |
|-----------|---------|-----------------|
| **85-100** | Success | Crisis well-managed; stakeholder trust maintained; recovery likely |
| **70-84** | Adequate | Adequate response; some damage; recovery possible |
| **55-69** | Poor | Poor management; significant damage; recovery uncertain |
| **40-54** | Crisis | Major mismanagement; severe reputational/financial damage |
| **Below 40** | Disaster | Company survival in question; likely bankruptcy/shutdown |

---

## Debrief & Reflection (5-10 minutes)

**PART 1: INVESTIGATION QUALITY (2 min)**
1. "Did you investigate adequately? What's the total impact?"
2. "What important information did you miss?"
3. "Would better forensics have changed your decisions?"

**PART 2: COMMUNICATION STRATEGY (2 min)**
1. "How did you prioritize stakeholder notifications?"
2. "What would you communicate differently?"
3. "Did transparency help or hurt your reputation?"

**PART 3: FINANCIAL DECISIONS (2 min)**
1. "Did you pay the ransom? Why or why not?"
2. "What was your total incident cost?"
3. "Would different decisions have saved money?"

**PART 4: RESPONSE QUALITY (2 min)**
1. "If you replayed, what would you do first?"
2. "Which stakeholder relationship was hardest to preserve?"
3. "What was your biggest crisis decision?"

**PART 5: REAL-WORLD CONNECTION (2 min)**
1. "Compare your spending to actual breaches (Target, Equifax, etc.)"
2. "What's harder: prevention or response?"
3. "Why is it so expensive to manage a real breach?"

---

## Tips for Threat Orchestrators

### Breach Scenario Variations

**Small Breach (Beginner)**
- 50,000 records (customers only)
- 12-hour dwell time
- No media involvement yet
- Attacker less sophisticated
- Total loss: ~$1-5M

**Medium Breach (Intermediate)**
- 500,000 records (customers + employees)
- 24-hour dwell time
- Media discovering it
- Attacker demanding payment
- Total loss: ~$5-50M

**Large Breach (Advanced)**
- 5M+ records (public database)
- 48-hour dwell time
- International implications
- Multiple stakeholder pressure
- Total loss: ~$50M+ (regulatory fines, lawsuits, brand damage)

### Pressure Escalation

- **Turns 1-2:** Initial discovery, legal/compliance focus
- **Turn 3-4:** Stakeholder pressure increases, media involvement
- **Turns 5-6:** Ransom deadline, lawsuit threats, operational impact
- **Turn 7:** Final reckoning, long-term consequences

### Decision Consequences

**Transparent vs. Evasive:**
- Early transparency: Reputation protected, stakeholder trust
- Late communication: Major reputation hits, legal consequences

**Thorough vs. Quick:**
- Investigation: Costs budget but provides critical info
- Speed: Saves budget but leaves gaps, compounds damage

**Negotiation vs. Paying:**
- Negotiate: Cheaper but attacker may refuse, publish data
- Pay: Costs more, no guarantee, reputation damage

---

## Sample Scenarios to Try

### Scenario 1: "Credential Breach" (Small, Beginner)

**Scope:** 50,000 customer passwords exposed
**Dwell Time:** 12 hours (attacker discovered quickly)
**Attacker:** Opportunistic (likely to accept negotiation)
**Budget:** 50

**Focus:** How to communicate bad news without panic
**Lesson:** Even small breaches require careful stakeholder management

---

### Scenario 2: "Supply Chain Breach" (Medium, Intermediate)

**Scope:** 500,000 records (vendors + customers)
**Dwell Time:** 24 hours
**Attacker:** Ransom-seeking criminal group
**Budget:** 50 + any remaining from prior modules

**Focus:** Multi-stakeholder communication, supply chain implications
**Lesson:** Vendor relationships complicate crisis response

---

### Scenario 3: "Nation-State Attack" (Large, Advanced)

**Scope:** 5M+ records (everything)
**Dwell Time:** 48 hours (sophisticated attacker)
**Attacker:** Nation-state (unlikely to negotiate, likely to publish)
**Budget:** Limited (already spent on detection/response)

**Focus:** Accept reputation damage, focus on recovery and legal action
**Lesson:** Some breaches are unwinnable; damage control is the goal

---

## Extensions & Variations

### Extended Crisis Mode (60 minutes)

- 10 turns instead of 7 (more response time)
- Budget: 100 (more resources)
- Multiple Pentester Tactics occur during recovery (attacker stages secondary attacks)
- More complex stakeholder negotiations

### Litigation Track

- Add Legal track to track lawsuit exposure
- Different remediation choices affect litigation outcomes
- Final score includes legal settlement costs
- Encourages strategic thinking about liability

### Competitive Breach Response

- Multiple teams responding to same breach
- Highest final reputation wins
- Teams compete for media narrative, regulatory favor

---

## Next Steps After This Module

**If you performed well (reputation 70+):**
- Continue to **Audit & Compliance Module** → Validate response procedures post-breach
- Transition to **Hardening Module** → Prevent similar breaches

**If you performed poorly (reputation <70):**
- Discuss what went wrong
- Replay scenario with different decisions
- Study real breach case studies (Target, Equifax, SolarWinds)

**Standalone:** Play again with different breach types or attacker profiles

---

## Quick Reference: Action Costs & Reputations

| Action | Cost | Effect |
|--------|------|--------|
| **Forensic Investigation** | 5-15 | +3 Reputation if quality |
| **Stakeholder Communication** | 0-10 | +5 (transparent), 0 (adequate), -10 to -20 (poor) |
| **Evidence Preservation** | 5-20 | +5 for good, helps legal case |
| **Remediation** | 10-25 | +5 for comprehensive |
| **Ransom Payment** | 10-30 | -15 Reputation |
| **Ransom Negotiation** | 5 | -10 Reputation (if successful) |
| **Ransom Refusal** | 0 | +5 Reputation (but -20 if data published) |

---

## Need Help?

- **Questions about rules?** See [Core Rules](../rules/core-rules.md)
- **Want to combine modules?** See [Module Combinations](../module-combinations.md)
- **Understanding timing?** See [FRAMEWORK.md](../FRAMEWORK.md)

---

*Disaster Recovery Module - Standalone Play Guide*
*Part of Incident Zero, a modular cybersecurity board game*

