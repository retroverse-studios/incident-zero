# Incident Zero: Disaster Recovery Phase
## Post-Breach Crisis Management & Aftermath

---

## Overview: When Phase 1 Fails

When a Blue Team **fails to reveal all cards before losing budget or reaching turn 10**, they enter **Phase 2: Disaster Recovery (DR)** instead of the optional Hardening phase.

This is not a "second chance" to solve the attack chain. Instead, it simulates the real-world consequences of a successful breach:
- **Crisis management** under pressure
- **Stakeholder communication** (board, customers, regulators)
- **Forensic investigation** with limited budget
- **Public disclosure** and legal requirements
- **Incident containment** and damage assessment
- **Financial impact** and recovery costs

### Educational Purpose

**Phase 1 (Incident Response):** Teaches proactive threat detection and investigation  
**Phase 2 - Hardening (Win):** Teaches proactive defense and resilience  
**Phase 2 - Disaster Recovery (Lose):** Teaches crisis management, consequences, and recovery

---

## Phase 2: Disaster Recovery Phase Setup

### Prerequisites for DR Phase

**Trigger:** Team failed Phase 1 by either:
- Reaching Turn 10 with unrevealed cards remaining, OR
- Running out of Budget (reaching 0)

**Outcome:** The attack chain proceeded undetected. The threat actor succeeded.

### Discovery & Revelation

The Threat Orchestrator **reveals the entire unrevealed attack chain** to the Blue Team:
- All hidden Threat cards are shown
- The complete attack progression is explained
- The attacker's objectives are stated

**Example Revelation:**
"Your security team was unable to detect the attack in time. The attacker successfully:
1. Sent a phishing email (SOCIAL ENGINEERING)
2. Harvested credentials (CREDENTIAL ABUSE)
3. Moved laterally across your network (NETWORK)
4. Dumped admin credentials (CREDENTIAL ABUSE)
5. Exfiltrated your entire customer database (DATA EXFIL)

The attacker is now threatening to publish the data unless you pay $500,000. You have 48 hours to respond."

---

### DR Phase Setup Steps

1. **Reveal Total Damage:**
   - Calculate data breach impact: Record count × Sensitivity level = **Initial Breach Cost**
   - Estimate business interruption if applicable
   - Document timeline of attack progression

2. **Establish DR Budget:**
   - Starting DR Budget = **50** (flat allocation for crisis response)
   - This is **separate from Phase 1 budget** (represents insurance, emergency funds, etc.)
   - Blue Team also has any remaining Phase 1 budget available (represents operational reserves)
   - **Total Available Budget for DR = (Phase 1 Remaining + 50)**

3. **Create Crisis Situation Card:**
   - Document the attack details, customer impact, and attacker demands
   - Set timelines (48-72 hours for disclosure decisions, negotiations, etc.)
   - List stakeholders requiring notification

4. **Initialize Tracking Sheets:**
   - **Damage Assessment Tracker** (what was compromised)
   - **Stakeholder Communication Log** (who needs to know, when, what)
   - **Forensic Investigation Tracker** (evidence collection, analysis)
   - **Financial Impact Sheet** (investigation costs, notifications, PR, legal)
   - **Reputation/Trust Score** (starts at 100, decreases based on response quality)

5. **Set Up Disclosure Timeline:**
   - **6-hour mark:** Internal discovery (already happened)
   - **12-hour mark:** Regulatory notification deadline (if applicable)
   - **24-hour mark:** Customer notification deadline (varies by regulation)
   - **48-hour mark:** Public disclosure and media response
   - **72-hour mark:** Investigation completion and reporting

---

## Phase 2 Disaster Recovery Mechanics

### Action Types in DR Phase

Instead of Investigation/Deploy Defense, teams make **Crisis Response Actions**:

---

#### **Action A: Forensic Investigation 🔍**

**Cost:** 5-15 Budget (depending on depth)

**Action:** The team describes a specific forensic investigation to determine:
- Extent of data compromise
- Timeline of attack
- What systems were affected
- Whether attacker still has access

**Investigation Options & Costs:**

| Investigation | Cost | Duration | Result |
|--------------|------|----------|--------|
| Quick log review | 5 | Immediate | General timeline |
| Forensic image (1 system) | 10 | 2-4 hours | Detailed evidence |
| Full network forensics | 15 | 6-8 hours | Complete picture |
| Threat hunting for backdoors | 15 | Ongoing | Persistence detection |
| Attacker infrastructure analysis | 10 | 4-6 hours | Attribution hints |

**Outcomes:**
- **Success (roll 11+):** Gain critical information for stakeholder communication and remediation
- **Partial Success (roll 8-10):** Get some useful data but miss important details
- **Failure (roll < 8):** Investigation inconclusive, creates liability and requires more investigation later

**Educational Purpose:** Teaches that thorough forensics take time and money, but are critical for:
- Legal/regulatory compliance
- Attribution and threat intelligence
- Prevention of future attacks
- Customer confidence

---

#### **Action B: Stakeholder Communication & Notification 📢**

**Cost:** 0-10 Budget (depending on scope)

**Action:** The team chooses WHO to notify and WHEN:

**Stakeholder Groups & Notification Requirements:**

| Stakeholder | Regulatory | Cost | Timing | Impact on Reputation |
|------------|-----------|------|--------|-------------------|
| **Internal Leadership** | Required | 0 | Immediately | N/A (internal) |
| **Legal Team** | Required | 5 | Within 2 hours | N/A |
| **Affected Customers** | Required* | 10 | 24-72 hours** | -10 per day late |
| **Regulatory Bodies** | Required* | 5 | 24-72 hours** | -5 if late |
| **Insurance Company** | Recommended | 0 | Within 24h | -2 if missed |
| **Credit Monitoring (if PII)** | Required* | 15 | Within 48h | -15 if missed |
| **Public Media Statement** | Optional | 0 (or 20 for PR firm) | 48-72h | Variable |

*Varies by regulation (GDPR, CCPA, HIPAA, PCI-DSS, state breach notification laws)

**Notification Quality:** 
- **Pro (Full transparency):** +3 Reputation - "We're investigating and will share details"
- **Standard (Required info only):** No change - "Here's what happened, here's what we're doing"
- **Defensive (Minimize info):** -2 Reputation - "We're handling it internally" (looks like cover-up)

**Notification Timing:**
- **Early (within timeline):** No reputation penalty
- **On-time (at deadline):** No penalty
- **Late (after deadline):** -10 Reputation per day late (regulatory violation)

**Example Communication Action:**
"We're issuing a transparent customer notification admitting the breach extent, offering 2 years of credit monitoring, and outlining our investigation findings. Cost 10 Budget, Professional approach."
→ **Result:** +3 Reputation, stakeholder trust maintained

---

#### **Action C: Evidence & Data Preservation 🔒**

**Cost:** 5-20 Budget (depending on scope)

**Action:** Preserve forensic evidence, isolate breached systems, secure backups

**Preservation Options & Costs:**

| Action | Cost | Effect |
|--------|------|--------|
| Isolate breached systems (network air-gap) | 5 | Prevents further attacker access; may impact business |
| Preserve logs & evidence (chain of custody) | 10 | Critical for investigation and legal proceedings |
| Backup customer data (offline copy) | 15 | Enables recovery; prevents double-extortion loss |
| Memory forensics on infected systems | 10 | Finds attacker tools still in RAM |
| Threat intelligence collection | 5 | Helps with attribution, IOCs |

**Outcomes:**
- **Success:** Evidence preserved properly, admissible in court, supports investigation
- **Failure:** Evidence contaminated, chain of custody broken, reduces legal standing

**Educational Purpose:** Teaches that forensic procedures must follow legal standards or evidence becomes inadmissible.

---

#### **Action D: Remediation & System Hardening 🛡️**

**Cost:** 10-25 Budget (depending on scope)

**Action:** Remove attacker access and harden systems to prevent re-compromise

**Remediation Options & Costs:**

| Action | Cost | Effect |
|--------|------|--------|
| Change all compromised credentials | 5 | Essential but basic |
| Patch vulnerability used in initial access | 10 | Prevents same attack vector |
| Rebuild compromised systems (fresh OS) | 15 | Most thorough but time-consuming |
| Deploy additional monitoring/detection | 10 | Prevents future undetected access |
| Implement firewall rules to block attacker IP/domains | 5 | Reactive; attacker may use new infrastructure |
| Full security infrastructure upgrade | 25 | Comprehensive but expensive |

**Outcomes:**
- **Success:** System hardened, attacker access removed, risk of re-breach reduced
- **Partial Success:** Some vulnerabilities remain, re-breach risk moderate
- **Failure:** Remediation incomplete, attacker may maintain persistence

**Educational Purpose:** Teaches that proper incident remediation is expensive, time-consuming, and critical to prevent repeat attacks.

---

#### **Action E: Attacker Negotiation & Ransom Decision 💰** *(if applicable)*

**Cost:** Variable (negotiation) or Ransom Amount (payment)

**Action:** If the attacker is demanding payment (ransomware, extortion), the team must decide:

**Option 1: Pay the Ransom**
- **Cost:** Amount attacker demands (usually 10-30% of revenue, represented as a percentage of budget)
- **Effect:** Potential decryption key, but no guarantee
- **Reputation:** -15 (seen as capitulating to criminals; funds future attacks)
- **Legal risk:** May violate sanctions laws; doesn't guarantee data deletion

**Option 2: Refuse & Negotiate**
- **Cost:** 5-10 Budget (negotiator/lawyer fees)
- **Roll:** Negotiate (roll 10+ to convince attacker to lower demands)
- **Success:** Attacker may reduce demands or agree not to publish
- **Failure:** Attacker publishes/encrypts anyway
- **Reputation:** +5 (seen as standing against extortion)

**Option 3: Negotiate with Law Enforcement**
- **Cost:** 0 (law enforcement typically free, but limited resources)
- **Roll:** Law Enforcement Investigation (roll 12+ to identify attacker; very hard)
- **Success:** Attacker arrested or infrastructure seized (data may still be leaked, but criminal prosecuted)
- **Failure:** Investigation ongoing, no immediate resolution
- **Timeline:** Takes months/years

**Decision Framework for Teams:**
- **Small company, limited budget:** Often pays (can't afford extended downtime)
- **Large company, security-conscious:** Often refuses (sets precedent, funds crime)
- **Critical infrastructure:** May negotiate with government assistance
- **Regulated industry:** May be prohibited from paying certain threat actors

**Educational Purpose:** Teaches the ethical and practical considerations of ransom decisions; no "right" answer, depends on risk tolerance.

---

### DR Phase Turns & Timeline

**Each "Turn" in DR Phase = 6 hours of real time**

| Turn | Real Time | Key Deadline | Actions Available |
|------|-----------|--------------|-------------------|
| Turn 1 | Hour 0-6 | Internal discovery & legal notification | Investigation, Evidence Preservation, Legal prep |
| Turn 2 | Hour 6-12 | Regulatory bodies notification (12h) | Investigation, Customer notification prep |
| Turn 3 | Hour 12-18 | Customer notifications begin (24h window) | Investigation, Remediation begins, Stakeholder communication |
| Turn 4 | Hour 18-24 | Customer notifications complete (48h) | Remediation, Negotiation if applicable |
| Turn 5 | Hour 24-30 | Media & public disclosure | Public statement, Reputation management |
| Turn 6 | Hour 30-36 | Investigation completion pressure | Final forensics, Final remediation |
| Turn 7 | Hour 36-48 | Crisis period ends | Post-incident analysis |

**Maximum Turns:** 7 turns (48 hours of crisis management)

Each turn, the Blue Team chooses **ONE** action.

---

### Financial Impact Tracking

As teams take actions, the cost accumulates beyond their Budget:

**Immediate Costs (paid from DR Budget):**
- Forensic investigation
- Stakeholder notification
- Evidence preservation
- Remediation efforts

**Deferred/Ongoing Costs (tracked separately, affect final score):**
- Credit monitoring (if PII breached): 2-5% of revenue
- Legal costs: 1-3% of revenue
- Regulatory fines: 2-10% of revenue (GDPR fines up to 4% of global revenue)
- PR & reputation recovery: 1-5% of revenue
- Customer churn & loss of trust: 5-20% of revenue (variable)

**Ransom Paid (if applicable):**
- 10-30% of annual revenue

**Cost Summary Example:**
```
Phase 1 Failed with: 15 Budget remaining

DR Setup:
- DR Budget: 50
- Total Available: 65

DR Phase Spending:
- Forensic Investigation (full): 15
- Customer Notification (transparent): 10
- Evidence Preservation: 10
- Remediation & Patch: 15
- PR Firm & Media Response: 10
Total DR Spending: 60 (remaining: 5)

Deferred Costs (not from budget, but tracked):
- Credit Monitoring: 50,000 (2% of revenue estimate)
- Legal Costs: 30,000 (1% of revenue)
- Regulatory Fine: 40,000 (GDPR violation = up to 4%)
- Customer Churn: 120,000 (estimated 10% revenue loss)
- Total Deferred: 240,000

Final Financial Impact:
DR Budget Spent: 60 out of 65 (92% utilized)
Deferred Costs: 240,000+ (ongoing)
Total Incident Cost: ~300,000+ (varies by size of company)
```

---

### Reputation/Trust Score System

**Starting Reputation:** 100 (fully trusted)

**Reputation Modifiers During DR:**

| Action | Reputation Change |
|--------|------------------|
| Transparent customer notification (early) | +5 |
| On-time regulatory notification | +2 |
| Successful forensic investigation (no delays) | +3 |
| Quick remediation & system hardening | +3 |
| Public accountability & lessons learned | +3 |
| **Late customer notification** | -10 per day |
| **Inadequate forensics or evidence loss** | -5 |
| **Failed remediation (re-compromise)** | -15 |
| **Attempting to cover up/mislead** | -20 |
| **Regulatory fine for negligence** | -10 |
| **Ransomware payment** | -15 |
| **Customer churn/class action lawsuit** | -10 |

**Final Reputation Tiers:**
- **90-100:** Crisis well-managed; customer trust recovered; industry sees as responsible
- **75-89:** Adequate response; some customer concern; regulatory scrutiny
- **60-74:** Poor response; significant customer loss; regulatory investigation likely
- **40-59:** Very poor response; major reputational damage; industry loses trust
- **Below 40:** Catastrophic; company may not survive; CEO likely replaced

---

## DR Phase Outcomes & Debrief

### Phase 2 DR Completion (after 7 turns or team finishes actions)

**Final Scoring:**

```
Forensic Investigation Quality (0-25 points)
- Thorough investigation: 25 points
- Adequate investigation: 15 points
- Poor investigation: 5 points
- No investigation: 0 points

Stakeholder Communication (0-20 points)
- All stakeholders notified on-time & transparently: 20
- Most stakeholders notified timely: 15
- Late or incomplete notifications: 5
- Failed to notify required parties: 0 (regulatory violation)

Incident Containment (0-20 points)
- Attacker access fully removed, hardened: 20
- Partially contained, some vulnerabilities remain: 10
- Poorly contained, re-breach risk high: 5
- Inadequate containment: 0

Financial Management (0-15 points)
- Minimized costs, efficient response: 15
- Moderate spending: 10
- Excessive spending or ransom paid: 5
- Uncontrolled costs: 0

Reputation Management (0-20 points)
- Final Reputation Score (90-100): 20 points
- Final Reputation Score (75-89): 15 points
- Final Reputation Score (60-74): 10 points
- Final Reputation Score (40-59): 5 points
- Final Reputation Score (Below 40): 0 points

TOTAL DR PHASE SCORE: 0-100 points
```

### DR "Win" vs "Lose" Outcomes

**DR Phase WIN (60+ points):**
"Your team's swift and thorough response minimized damage. Though the breach occurred, your transparent communication, proper forensics, and effective remediation preserved customer trust. The organization will recover, though the incident cost significant resources. Key learning: Next time, detect earlier."

**DR Phase ACCEPTABLE (40-59 points):**
"Your response was adequate but not optimal. Customers are concerned but mostly stayed. Regulatory bodies are investigating. The organization will recover, but reputation damage is longer-term. Key learning: Response procedures need improvement."

**DR Phase POOR (Below 40 points):**
"Your response was inadequate. Major customer loss, regulatory fines, and significant reputational damage. This incident may impact leadership changes and requires extensive recovery. Key learning: Breach response procedures must be pre-planned and tested."

---

## Mandatory Lessons Learned Debrief (20 minutes)

After DR Phase completion, run a structured debrief:

### Part 1: Attack Analysis (5 minutes)
1. **What was the initial compromise vector?** Why did defenses fail?
2. **How far did the attacker progress?** What could have stopped them?
3. **What was the attacker's objective?** (Data theft? Ransomware? Persistence?)

### Part 2: Detection Failures (5 minutes)
1. **Why wasn't this detected in Phase 1?** What signs did we miss?
2. **What defense would have caught this attack?**
3. **What monitoring/logging was inadequate?**

### Part 3: Response Evaluation (5 minutes)
1. **Was the forensic investigation adequate?** What gaps remained?
2. **Did we communicate effectively with stakeholders?** What went wrong?
3. **Was remediation thorough enough to prevent re-breach?**

### Part 4: Prevention for Next Time (5 minutes)
1. **What one thing would you deploy first if you replayed?**
2. **How would you prioritize defenses differently?**
3. **What process improvements would help next time?**

---

## Comparison: Phase 2 Hardening vs. Phase 2 Disaster Recovery

### Win Phase 1 → Phase 2 Hardening
- **Focus:** Proactive security improvements
- **Mindset:** "We won, now how do we make sure this never happens again?"
- **Timeline:** Leisurely (30 minutes); planning for future
- **Budget:** Focus on investment
- **Outcome:** Security Score (70-100 scale)
- **Key Mechanic:** Deploying layers of defense, hardening with playbooks
- **Educational Value:** Defense-in-depth, layered security, cost-benefit analysis
- **Realism:** How Fortune 500 companies think about security

### Lose Phase 1 → Phase 2 Disaster Recovery
- **Focus:** Crisis management and damage control
- **Mindset:** "We failed to detect; now manage the fallout"
- **Timeline:** Urgent (48 hours); crisis response
- **Budget:** Limited emergency funds; costly but necessary
- **Outcome:** Reputation/Financial Impact (0-100 scale)
- **Key Mechanic:** Forensics, communication, remediation under pressure
- **Educational Value:** Incident response procedures, stakeholder management, consequences
- **Realism:** Real-world breach management; what actually happens when detection fails

---

## Sample Disaster Recovery Scenarios

### Scenario: "The Ransomware Nightmare" (4-card chain failure)

**Attack Chain (revealed at start of DR):**
1. Phishing Email with Malicious Attachment
2. Lateral Movement via SMB
3. Scheduled Task Persistence
4. Ransomware Deployment

**Breach Impact:**
- All customer data encrypted (500,000 records)
- Ransom demand: 50 Bitcoin (~$2M)
- Business systems down 36 hours (ongoing)
- Public media coverage beginning

**Initial Situation:**
- DR Budget: 50
- Remaining Phase 1 Budget: 5
- Total: 55 Budget
- Reputation: 100 (starts high; decreases with poor decisions)

**Timeline Pressure:**
- Turn 1 (6h): Internal discovery
- Turn 2 (12h): Regulatory notification deadline
- Turn 3 (18h): Customer notification begins (24h window starts)
- Turn 4 (24h): Media coverage intensifies
- Turn 5 (30h): Ransom deadline (attacker threatens to publish data)
- Turn 6 (36h): Business impact critical (systems still down)
- Turn 7 (42h): First customer lawsuits filed

**Recommended Action Sequence:**
1. **Turn 1:** Forensic Investigation (10 Budget) - Determine scope of encryption
2. **Turn 2:** Evidence Preservation (10 Budget) - Secure backups before further encryption
3. **Turn 3:** Customer Notification (10 Budget) - Transparent communication about ransom demand
4. **Turn 4:** Negotiation Decision (0 Budget or Ransom) - Pay, negotiate, or refuse?
5. **Turn 5:** Remediation (10 Budget) - Deploy patches, reset credentials
6. **Turn 6:** Backup Recovery (5-10 Budget) - Begin system restoration from backups
7. **Turn 7:** Final Communication (0 Budget) - Update stakeholders on recovery timeline

**Deferred Costs:**
- Ransom (if paid): 50 Bitcoin (~$2M)
- Regulatory fine (GDPR violation): 2-4% of revenue
- Customer notification & credit monitoring: 2% of revenue
- Business interruption & customer churn: 5-10% of revenue
- Legal costs: 1% of revenue

**Total Incident Cost:** $3M+ (industry average for ransomware)

**Likely Outcome:** 45-60 Reputation points (depending on response quality)

---

### Scenario: "The Insider Data Theft" (4-card chain failure)

**Attack Chain (revealed at start of DR):**
1. Disgruntled Employee Sabotage
2. Lateral Movement via SMB
3. Mimikatz Credential Dumping
4. Malicious Insider Data Theft

**Breach Impact:**
- Customer database (500,000 records) exfiltrated
- Competitor intelligence and source code also stolen
- Employee went to competitor/foreign entity
- Data already for sale on dark web

**Initial Situation:**
- DR Budget: 50
- Remaining Phase 1 Budget: 10
- Total: 60 Budget
- Reputation: 100

**Complexity Factors:**
- HR involvement required (personnel issue)
- Legal complexity (employee likely sued for breach of contract)
- Criminal referral (FBI may investigate)
- Forensic complexity (need to prove insider's involvement)

**Recommended Action Sequence:**
1. **Turn 1:** Evidence Preservation (10 Budget) - Preserve employee's digital footprint before deletion
2. **Turn 2:** Internal Investigation + Legal (5 Budget) - HR & legal review of insider's activities
3. **Turn 3:** Forensic Investigation (10 Budget) - Detailed analysis of data access patterns
4. **Turn 4:** Law Enforcement Notification (0 Budget) - FBI referral for criminal investigation
5. **Turn 5:** Customer Notification (10 Budget) - Transparent disclosure of breach
6. **Turn 6:** Remediation (10 Budget) - Credential reset, access review for other privileged employees
7. **Turn 7:** Insider Threat Program (5 Budget) - Deploy behavioral monitoring to prevent future insider threats

**Deferred Costs:**
- Regulatory fine: 2-4% of revenue
- Customer notification: 2% of revenue
- Customer churn: 5-15% of revenue (higher for insider threat)
- Legal costs (employee lawsuit, criminal prosecution): 2% of revenue
- Insider Threat Program deployment: 1% of revenue

**Total Incident Cost:** $2M-$4M (depends on customer base size)

**Reputation Challenges:** Insider threats are particularly damaging to trust; reputation recovery slower

**Likely Outcome:** 40-55 Reputation points (insider threats harder to recover from)

---

### Scenario: "The Supply Chain Compromise" (5-card chain failure)

**Attack Chain (revealed at start of DR):**
1. Compromised Software Vendor Update
2. Lateral Movement via SMB
3. Cloud API Token Theft
4. DNS Tunneling Data Exfiltration
5. Beaconing to C2 Server (persistence established)

**Breach Impact:**
- Attacker has persistent backdoor in your infrastructure
- Customer data partially exfiltrated (investigating full scope)
- Attack affects 100+ other organizations (industry-wide supply chain compromise)
- Regulatory & media attention is severe
- Attacker likely nation-state (high-complexity attack)

**Initial Situation:**
- DR Budget: 50
- Remaining Phase 1 Budget: 0 (spent everything investigating but didn't find it)
- Total: 50 Budget
- Reputation: 100

**Complexity Factors:**
- Multiple organizations affected (industry-wide response coordination)
- Vendor communications required (shared victim status)
- Government/CISA involvement (critical infrastructure if applicable)
- Extremely complex forensics (supply chain tracing)
- Extended investigation timeline (months, not hours)

**Recommended Action Sequence:**
1. **Turn 1:** Forensic Investigation (15 Budget) - Identify compromised vendor and scope
2. **Turn 2:** Vendor Coordination (0 Budget) - Work with vendor and other organizations
3. **Turn 3:** Evidence Preservation (10 Budget) - Chain of custody for attribution
4. **Turn 4:** Regulatory Notification (5 Budget) - CISA & industry regulators
5. **Turn 5:** Customer Notification (10 Budget) - Transparent about supply chain compromise
6. **Turn 6:** Threat Intelligence (5 Budget) - IOC analysis for attribution/tracking
7. **Turn 7:** Remediation (Not possible in 7 turns - mark as ongoing)

**Critical Decision Point:**
Teams quickly realize they **cannot fully remediate in 48 hours** due to complexity. Instead, they must:
- Isolate the compromised software
- Begin long-term forensic investigation
- Coordinate with vendor, government, and other organizations
- Accept that this is a months-long incident response

**Deferred Costs:**
- Regulatory fine: 2-4% of revenue
- Customer notification: 2% of revenue
- Incident investigation team (extended): 3-5% of revenue
- System rebuilds and re-platforming: 2-3% of revenue
- Customer churn: 5-10% of revenue
- Reputational damage: Long-term (recovery takes 12+ months)

**Total Incident Cost:** $5M+ (supply chain incidents are very expensive)

**Learning:** Some incidents are too complex to "solve" in phase 2; they transition to ongoing incident response

**Likely Outcome:** 30-45 Reputation points (complex incidents naturally have lower scores due to timeline)

---

## Advanced DR Rules: Second-Phase Escalation

### If DR Phase Goes Poorly (Reputation <40)

**Optional Rule:** Teams can request **Executive Intervention**

- **Cost:** 10 Budget (bringing in outside crisis management firm)
- **Effect:** Get ONE additional turn (turn 8)
- **Limited Help:** Can redo ONE previous action with better outcome
- **Realistic Model:** Companies often bring in outside forensic firms or crisis PR agencies when internal response fails

**Example:** "We botched customer notification. Cost 10 Budget to hire PR firm to re-communicate and salvage relationship."

---

### If Attacker Has Persistence (Some attacks establish ongoing access)

**Optional Rule:** Post-Incident Follow-Up (Turn 8+)

After 48-hour crisis period, if the Threat Orchestrator reveals "The attacker maintains persistence," the team can:
- Spend additional turns (1 per turn) to conduct "Threat Hunting"
- Attempt to find and remove backdoors
- Cost: 10 Budget per threat hunting turn
- Success: Roll 12+ to find and remove persistence

**Realistic Model:** Some breaches aren't fully "cleaned up" in 48 hours; threats are discovered weeks/months later

---

## Integration with Base Game: Full Game Flow

### Option 1: Standalone Play (Single Path)
- **Setup:** 10 min
- **Choose Path:** 2 min (based on flip coin or predetermined)
- **Play Phase 1 OR DR Phase:** 30-40 min
- **Debrief:** 10-15 min
- **Total:** 60-75 minutes

### Option 2: Full Campaign (Both Paths)
- **Setup:** 10 min
- **Play Phase 1:** 30-40 min
- **Checkpoint:** 2 min (determine if win or lose)
- **Play Phase 2 (Hardening or DR):** 20-30 min
- **Debrief:** 15 min
- **Total:** 90-120 minutes

### Option 3: Tournament Mode (Multiple Teams, Both Paths)
- **Setup:** 10 min
- **All teams play Phase 1 simultaneously:** 40 min
- **Teams split by outcome:**
  - Winners → Phase 2 Hardening (30 min)
  - Losers → Phase 2 Disaster Recovery (30 min)
- **Final Scoring & Awards:** 15 min
- **Debrief:** 10 min
- **Total:** 2-2.5 hours

---

## Disaster Recovery Phase Materials (Required)

### New Tracking Sheets Needed

1. **Crisis Situation Card** - Breach details, timeline, attacker demands
2. **Damage Assessment Sheet** - What was compromised, scope, sensitivity
3. **Forensic Investigation Tracker** - Evidence collected, timeline, findings
4. **Stakeholder Communication Log** - Who was notified, when, what was said, response
5. **Financial Impact Sheet** - Budget spent, deferred costs, total incident cost
6. **Reputation Tracking Chart** - Reputation score over time, modifiers applied
7. **Remediation Checklist** - Systems hardened, credentials reset, vulnerabilities patched
8. **Debrief Worksheet** - Lessons learned, prevention strategies, process improvements

### Optional: DR-Specific Cards (Alternative to Freeform)

Instead of open-ended actions, you can create specific **Crisis Action Cards** for teams to draw from:
- "Forensic Lab Activated" - Forensic investigation action
- "Legal Team Briefing" - Stakeholder communication
- "Incident Command Center" - Coordination across teams
- "Evidence Chain of Custody" - Preservation procedures
- "Customer Crisis Hotline" - Customer communication
- "Remediation Squad Deployed" - System hardening
- "Negotiation Team" - Ransom decision
- "CEO Press Conference" - Public communication

---

## Teaching Notes for DR Phase

### Key Learning Objectives

**Incident Response Skills:**
- Prioritize crisis response actions under pressure
- Coordinate across teams and stakeholders
- Make decisions with incomplete information
- Understand forensic investigation requirements

**Business Impact Understanding:**
- Recognize financial costs of breaches (not just immediate costs)
- Understand regulatory & legal consequences
- Learn about reputational damage and customer churn
- Recognize insurance and recovery programs

**Stakeholder Management:**
- Communicate effectively with diverse audiences (customers, regulators, media)
- Balance transparency with liability reduction
- Manage expectations during crisis
- Follow regulatory notification requirements

**Long-term Recovery:**
- Incident doesn't end when systems are "fixed"
- Organizational recovery takes months/years
- Prevention is far cheaper than response
- Importance of pre-incident preparation

### Discussion Questions After DR Phase

**For Teams That Had Better Detection (Lost Phase 1 by Turn 9-10):**
- "If you'd detected the attack one turn earlier, what would have changed?"
- "What one additional control would have triggered detection?"
- "How does dwell time (time from compromise to detection) affect these costs?"

**For Teams That Lost Quickly (Out of budget by Turn 5-6):**
- "Why did your investigation fail so quickly?"
- "Which budget-saving action actually cost you more in the long run?"
- "What would aggressive early investigation have prevented?"

**For All Teams:**
- "How much did this incident actually cost (total financial + reputational)?"
- "If Phase 1 detection saves 80% of these costs, what should you invest in detection?"
- "How would a pre-prepared incident response plan have helped?"
- "What's the value of having a Disaster Recovery plan before you need it?"

### Real-World Context for DR Phase

**Average Breach Costs (2023 data):**
- **Detection Time (Dwell Time):** 206 days average
- **Cost per Compromised Record:** $4.50 (varies by industry)
- **Total Average Cost:** $4.5M (for 1M records)
- **Cost Breakdown:**
  - Detection & Analysis: 25%
  - Containment & Eradication: 20%
  - Recovery & Restoration: 20%
  - Legal & Regulatory: 15%
  - PR & Communications: 10%
  - Customer Notifications: 10%

**Common Mistakes in Real Incidents:**
- Poor forensic planning → Extended investigation costs
- Late customer notification → Regulatory fines + brand damage
- Inadequate remediation → Re-compromise (adds cost)
- Ransom payment → Funds future attacks; doesn't guarantee data deletion
- No incident plan → Chaos and poor decisions

**Success Factors in Real Incidents:**
- Pre-incident planning and training
- Clear communication protocols
- Rapid forensic investigation
- Transparent customer communication
- Thorough remediation
- Post-incident review and improvements

---

## Comparison Matrix: Phase 2 Outcomes

### Win Phase 1 → Hardening Phase

| Aspect | Outcome |
|--------|---------|
| **Time** | 30+ minutes (leisurely planning) |
| **Budget** | Remains high; focuses on investment |
| **Pressure** | Low; strategic decisions |
| **Focus** | "How do we prevent this next time?" |
| **Controls Deployed** | Multiple layers (defense-in-depth) |
| **Score Range** | 70-100 (Security Score) |
| **Key Metric** | Defense capabilities |
| **Emotional Tone** | Achievement-focused; optimistic |
| **Real-World Equivalent** | Fortune 500 post-acquisition security planning |

### Lose Phase 1 → Disaster Recovery Phase

| Aspect | Outcome |
|--------|---------|
| **Time** | 48 hours (crisis mode) |
| **Budget** | Limited emergency funds; every decision has cost |
| **Pressure** | High; time-sensitive with external deadlines |
| **Focus** | "How do we manage this disaster?" |
| **Actions Taken** | Forensics, communication, containment (reactive) |
| **Score Range** | 0-100 (Reputation/Financial Impact) |
| **Key Metric** | Response quality and cost management |
| **Emotional Tone** | Crisis-focused; pressurized |
| **Real-World Equivalent** | Actual breach response; Target, Yahoo, Equifax situations |

---

## Recommended Play Sequence

### Classroom Session: First Exposure (90 minutes)

1. **Setup (10 min):** Explain both Phase 2 paths
2. **Play Phase 1 (35 min):** Standard 3-4 card chain, beginner difficulty
3. **Outcome Determined (2 min):** Did they win or lose?
4. **Play Phase 2 (25 min):** Either Hardening or DR based on outcome
5. **Debrief (15 min):** Lessons learned from the path they took
6. **Optional: Brief Against Path (3 min):** "If you'd won/lost instead, here's what would have happened"

### Advanced Session: Comparative Play (2.5 hours)

1. **Setup (10 min)**
2. **Split Teams (2-3 teams per group):**
   - Half play Scenario A (designed to be winnable)
   - Half play Scenario B (designed to be challenging)
3. **Phase 1 (40 min):** All play simultaneously
4. **Phase 2a - Winners (30 min):** Play Hardening
5. **Phase 2b - Losers (30 min):** Play DR
6. **Compare & Contrast (20 min):** 
   - Show both paths side-by-side
   - Discuss cost differences
   - Analyze decision quality
7. **Debrief (10 min)**

### Tournament Mode (Tournament organizer sees both paths)

Each team experiences one path (win or lose) and sees the results. Organizer can optionally:
- Show "what if" scenarios for losing teams
- Discuss how different choices in Phase 1 led to Phase 2 path
- Emphasize detection importance

---

## Variants & Extensions

### Variant: "Instant Replay" Recovery

**Optional Rule (for motivated teams):**

If a team does **exceptionally well** in Disaster Recovery phase (Reputation 85+):

After Crisis Period ends, they can attempt:
- **Recovery Analysis:** Spend 5 Budget for deep forensic review
- **Root Cause Analysis:** Identify systemic failure that allowed Phase 1 loss
- **Prevention Investment:** Spend remaining budget to deploy detection that would have caught this

This models the concept of "turning crisis into opportunity" - some organizations emerge stronger after breaches.

**Example:** "Our forensic analysis revealed we had no SIEM. Cost 5 Budget for analysis, 15 Budget to deploy SIEM. If we replay, we'd detect this attack."

### Variant: "Ongoing Breach" (Extended Campaign)

For advanced play, Phase 2 DR doesn't necessarily end the incident:

- **Week 2 Post-Breach:** Threat hunting discovers backdoor still active
- **Week 4:** Attacker attempts lateral movement again
- **Week 8:** New variant of attack appears

Teams make decisions across extended timeline, learning that some breaches have long tails.

### Variant: "Insurance & Legal" Module

Add Negotiation Mechanics:
- **Insurance Negotiation:** Do they cover this incident? (Cost: 5 Budget to negotiate; Outcome: 0-50% coverage)
- **Litigation Preparedness:** How much forensic evidence prepared for lawsuits? (Affects future legal costs)
- **Regulatory Settlement:** Can you negotiate with regulators? (Cost: 5 Budget; Outcome: 0-75% fine reduction)

---

## Final Thought: Why This Matters

**Phase 1 (Incident Response)** teaches: "Catch attacks early"
**Phase 2 - Hardening (Win)** teaches: "Prevent future attacks"
**Phase 2 - Disaster Recovery (Lose)** teaches: **"Plan for what you'll miss"**

Together, they create a complete incident response curriculum:
1. **Detection & Investigation** (Phase 1)
2. **Hardening & Prevention** (Phase 2 - Win path)
3. **Crisis Management & Recovery** (Phase 2 - Disaster Recovery path)

Students learn that **even with perfect security, breaches can happen**. The question isn't "Will we be attacked?" but "When we're attacked, will we respond effectively?"

---

*Disaster Recovery Phase for Incident Zero*  
*For teams that experience the cost of failed detection*  
*Emphasizing that response quality matters as much as prevention*