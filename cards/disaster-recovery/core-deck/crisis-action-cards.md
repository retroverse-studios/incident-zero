# Disaster Recovery Module: Crisis Action Cards

**Version:** 2.1 - Balanced & Refined Edition
**Last Updated:** October 2025

---

## Overview

**Crisis Action Cards** represent the specific actions an organization can take during a breach to investigate, remediate, and respond. Teams deploy Crisis Actions each turn to advance three objectives: Investigation %, Remediation %, and Communication %.

- **Total Cards:** 12 (ACTION-01 to ACTION-12)
- **Used In:** Disaster Recovery module (primary gameplay cards)
- **Cost Range:** 5-30 Budget depending on action scope
- **Purpose:** Drive incident response forward under time/budget pressure

---

## Crisis Action Card Organization

### Action Categories

Crisis Actions are organized into three categories:

1. **Investigation Actions** (4 cards)
   - Advance understanding of breach
   - Determine scope and impact
   - Gather evidence for forensics
   - Enable faster containment

2. **Remediation Actions** (4 cards)
   - Fix vulnerability that was exploited
   - Contain compromised systems
   - Recover from backup
   - Rebuild infrastructure

3. **Communication Actions** (4 cards)
   - Notify stakeholders
   - Manage media/public relations
   - Report to regulators
   - Maintain customer trust

---

## Investigation Actions

### ACTION-01: Forensic Analysis
**Category:** Investigation
**Cost:** 12 Budget
**Investigation Advance:** +25%
**Duration:** 2 turns (multi-turn action)

**Description:**
Forensic experts analyze compromised systems to determine:
- What data was accessed
- What was exfiltrated
- How long attacker had access
- What attack techniques were used
- Evidence for legal proceedings

**Key Details:**
- Requires shutting down compromised system (removes it from operation)
- Requires forensics team (may need external consultants)
- Takes time (2 turns minimum)
- Provides detailed evidence
- Essential for legal action and regulatory compliance

**When to Use:**
- Need definitive answer about breach scope
- Legal action is likely
- Compliance investigation required
- Regulatory agency involved

**Risk if Not Done:**
- Cannot determine full extent of damage
- Cannot properly remediate (may miss persistence)
- No evidence for law enforcement
- Regulatory penalties for inadequate investigation

**Regulatory Impact:**
- Most breach notification laws require "reasonable investigation"
- Forensics evidence may be required for regulatory compliance
- Better investigation = stronger regulatory defense

**Team Trade-off:**
- Expensive (12 Budget)
- Takes time (2 turns)
- But provides high investigation %
- Provides evidence for future action

---

### ACTION-02: Threat Hunting
**Category:** Investigation
**Cost:** 8 Budget
**Investigation Advance:** +15%
**Duration:** 1 turn

**Description:**
Security team proactively searches logs and systems for:
- Other compromised systems
- Lateral movement indicators
- Persistence mechanisms
- Command & Control communication
- Evidence of data staging

**Key Details:**
- Requires SIEM with good logging (if available)
- Team searches for attack indicators
- Can discover secondary compromises
- Lower cost than forensics but less detailed
- Faster than forensics (1 turn)

**When to Use:**
- Need to know if compromise spread
- Want to find hidden persistence
- Time is critical (forensics takes 2 turns)
- Budget is constrained

**Risk if Not Done:**
- May not discover all compromised systems
- Attacker may maintain hidden access
- May lose evidence over time (logs rotate)
- Compliance investigation may be incomplete

**Regulatory Impact:**
- Shows good faith investigation effort
- Supports "reasonable investigation" standard
- Evidence of proactive security posture

**Team Trade-off:**
- Cheaper than forensics (8 Budget)
- Faster (1 turn vs. 2)
- Less detailed evidence
- Good balance of cost/time/effectiveness

---

### ACTION-03: Log Analysis
**Category:** Investigation
**Cost:** 5 Budget
**Investigation Advance:** +10%
**Duration:** 1 turn

**Description:**
Security team reviews available logs (firewall, VPN, Windows Event Log, application logs) to understand:
- When breach was discovered
- What access was gained
- What systems were accessed
- What data might have been accessed
- Timeline of attack

**Key Details:**
- Requires logs (must have been collecting logs)
- Basic analysis of existing logs
- Cheapest investigation action
- Quick (1 turn)
- Limited by log retention/quality
- Can be done internally (no external consultants)

**When to Use:**
- Budget is extremely tight
- Need quick preliminary understanding
- Good logging infrastructure in place
- Time is critical

**Risk if Not Done:**
- No understanding of what happened
- Cannot determine scope or impact
- Regulatory agencies upset about lack of investigation
- Potential for incomplete response

**Regulatory Impact:**
- Minimal investigation (may not satisfy "reasonable investigation")
- Shows attempt at investigation
- Not sufficient as sole investigation method

**Team Trade-off:**
- Cheapest investigation (5 Budget)
- Fastest (1 turn)
- Limited effectiveness
- Often insufficient alone

---

### ACTION-04: Third-Party Incident Response Engagement
**Category:** Investigation (+ Remediation)
**Cost:** 20 Budget
**Investigation Advance:** +30% (+ Remediation +20%)
**Duration:** 3 turns (ongoing engagement)

**Description:**
Bring in external incident response firm (forensics, incident handling, remediation specialists). They conduct:
- Comprehensive forensic investigation
- Breach scope determination
- Remediation recommendations
- Expert testimony for legal proceedings
- Regulatory coordination

**Key Details:**
- Very expensive (20 Budget)
- Takes significant time to mobilize
- Provides expert guidance and credibility
- Provides evidence acceptable in court
- Supports regulatory defense
- Can conduct investigation while team does other actions

**When to Use:**
- Major breach with legal implications
- Need expert investigation for court
- Regulatory agency demands expertise
- Internal team cannot handle scope
- Liability is significant

**Benefits:**
- Expert investigation (higher quality)
- Evidence for prosecution
- Regulatory/legal credibility
- Expert testimony available
- Ongoing support (3 turns)

**Risk if Not Done:**
- Without external expertise, breach response may be insufficient
- Legal case may fail (poor evidence)
- Regulatory penalties for inadequate investigation
- May miss critical evidence

**Regulatory Impact:**
- High credibility with regulators
- Better legal defense
- Shows serious investigation effort
- External experts satisfy "reasonable investigation"

**Team Trade-off:**
- Most expensive (20 Budget)
- Long commitment (3 turns)
- But provides significant investigation + remediation
- Provides external expertise and credibility
- Can run alongside other actions

---

## Remediation Actions

### ACTION-05: Patch & Harden (Affected Systems)
**Category:** Remediation
**Cost:** 10 Budget
**Remediation Advance:** +20%
**Duration:** 1 turn

**Description:**
Apply patches to the vulnerability that was exploited:
- Install OS patches (if vulnerability is OS-level)
- Update application (if vulnerability is app-level)
- Change default credentials
- Remove backdoor accounts
- Harden network configuration

**Key Details:**
- Targets the specific vulnerability that was exploited
- Must know what vulnerability was exploited (requires investigation)
- Can be done on specific systems or organization-wide
- Prevents same attack from succeeding again
- Does NOT remove attacker if already inside

**When to Use:**
- Know what vulnerability was exploited
- Want to prevent re-exploitation
- Can apply patch without affecting business
- Quick remediation needed

**Risk if Not Done:**
- Attacker can re-exploit same vulnerability
- Breach scope may grow
- Regulatory agency upset about lack of remediation
- Risk of breach happening again

**Regulatory Impact:**
- Shows timely remediation
- Prevents recurrence
- Good compliance posture
- Regulatory agencies expect patching

**Team Trade-off:**
- Moderate cost (10 Budget)
- Quick (1 turn)
- Fixes vulnerability
- But only prevents re-exploitation, doesn't remove attacker

---

### ACTION-06: Containment (Isolate Compromised Systems)
**Category:** Remediation
**Cost:** 8 Budget
**Remediation Advance:** +15%
**Duration:** 1 turn

**Description:**
Remove compromised systems from network to:
- Stop attacker from using compromised system for lateral movement
- Prevent attacker from exfiltrating more data
- Preserve compromised system for forensics
- Limit blast radius of compromise

**Key Details:**
- Disconnect compromised system from network (kill network)
- System is still available for forensics
- Stops active attacker in that system
- Does NOT affect attacker if they're in other systems
- May impact business (systems are unavailable)

**When to Use:**
- Know which systems are compromised
- Want to stop active attacker
- Can tolerate system downtime
- Attacker is still actively in system

**Risk if Not Done:**
- Attacker continues using compromised system
- Lateral movement continues
- More data exfiltration
- Attacker may install additional backdoors

**Regulatory Impact:**
- Shows swift containment action
- Demonstrates incident response
- Limits liability (stopped attacker)
- Good compliance posture

**Team Trade-off:**
- Moderate cost (8 Budget)
- Quick (1 turn)
- Stops active attacker
- But impacts business operations

---

### ACTION-07: System Rebuild/Recovery from Backup
**Category:** Remediation
**Cost:** 15 Budget
**Remediation Advance:** +25%
**Duration:** 2 turns (restore + verification)

**Description:**
Rebuild compromised systems from backup:
- Restore system from clean backup (pre-compromise)
- Apply patches to prevent re-exploitation
- Restore only clean data
- Verify system is clean before returning to production
- Monitor restored system for attacker re-entry

**Key Details:**
- Requires backup of system (must exist and be clean)
- Takes time to restore (2 turns minimum)
- Removes all attacker artifacts
- Ensures system is truly clean
- Most reliable remediation method
- Dependent on backup quality/testing

**When to Use:**
- Backup exists and is verified clean
- System compromise is extensive
- Want to ensure complete attacker removal
- Business can tolerate 2-turn rebuild

**Risk if Not Done:**
- Attacker may maintain persistence (if system not rebuilt)
- Restore from backup with attacker in it = no improvement
- Compliance may require clean rebuild

**Regulatory Impact:**
- Shows complete remediation
- Demonstrates thorough approach
- Better regulatory outcome
- Shows commitment to clean recovery

**Team Trade-off:**
- Higher cost (15 Budget)
- Takes time (2 turns)
- But provides complete remediation
- Most reliable method

---

### ACTION-08: Change Credentials & Access Controls
**Category:** Remediation
**Cost:** 6 Budget
**Remediation Advance:** +12%
**Duration:** 1 turn

**Description:**
Revoke and reset all potentially compromised credentials:
- Reset passwords for all accounts that touched compromised system
- Revoke tokens/API keys
- Reset VPN credentials
- Update database passwords
- Revoke certificates/SSH keys

**Key Details:**
- Prevents attacker from using stolen credentials
- Must do if credentials were compromised (stolen by Mimikatz, etc.)
- Can cause business disruption (users locked out)
- Quick and important
- Often overlooked but critical

**When to Use:**
- Credentials were likely compromised
- Attacker had access to credential stores
- Need to prevent attacker re-entry via stolen credentials
- Quick credential reset is possible

**Risk if Not Done:**
- Attacker can use stolen credentials to re-enter
- Lateral movement using stolen creds continues
- Breach is not truly contained
- Regulatory violation (allowing unauthorized access)

**Regulatory Impact:**
- Essential remediation step
- Shows understanding of attack chain
- Prevents credential reuse attacks
- Regulatory expectation

**Team Trade-off:**
- Low cost (6 Budget)
- Quick (1 turn)
- Important and often overlooked
- Can cause short-term business disruption

---

## Communication Actions

### ACTION-09: Customer Notification
**Category:** Communication
**Cost:** 10 Budget
**Communication Advance:** +20%
**Duration:** 1 turn (but affects later turns)

**Description:**
Notify customers that their data may have been breached:
- Determine which customers were affected
- Prepare notification message
- Send via email, mail, or phone
- Provide information about what was accessed
- Offer credit monitoring/identity protection if applicable
- Field customer questions/complaints

**Key Details:**
- Required by most breach notification laws (usually 30-60 days)
- Can be very expensive if many customers affected
- Notification can cause loss of customer trust
- Early notification shows good faith
- Delayed notification shows company doesn't care
- Impacts Customers stakeholder directly

**Regulatory Requirements:**
- Most laws require "without unreasonable delay" (usually 30-60 days)
- Some states require notification within specific timeframe
- Notification must include:
  - What information was accessed
  - Recommended actions
  - Contact information
  - Free credit monitoring (sometimes)

**When to Use:**
- Customer data was accessed in breach
- Regulatory requirement to notify
- Want to rebuild customer trust
- Transparency is important

**Risk if Not Done:**
- Regulatory violation (fines, penalties)
- Customer discovery + lawsuits
- Loss of customer trust (worse than notification)
- Reputation damage from cover-up worse than from breach

**Regulatory Impact:**
- Many states REQUIRE customer notification
- California CCPA, GDPR, state laws all require notification
- Without notification = regulatory violation + fines
- Proactive notification = better regulatory relationship

**Team Trade-off:**
- Moderate cost (10 Budget)
- Can be done quickly (1 turn)
- Required by law (usually)
- Impacts Customers stakeholder (see Stakeholder Cards)
- Must be done eventually

---

### ACTION-10: Regulatory/Law Enforcement Notification
**Category:** Communication
**Cost:** 8 Budget
**Communication Advance:** +10%
**Duration:** 1 turn (but ongoing for months)

**Description:**
Notify appropriate regulatory agencies:
- Contact FBI/Secret Service (federal crimes)
- Contact state attorney general (breach notification)
- Contact relevant sector regulator (HHS for healthcare, OCC for banking, etc.)
- Contact DHS (if critical infrastructure)
- Coordinate with law enforcement

**Key Details:**
- Required by law in many cases (healthcare, financial, etc.)
- May trigger investigation by law enforcement
- Can help recover stolen data
- Provides some legal protection
- Can delay prosecution (if they're investigating)
- Required before public disclosure in some cases

**Regulatory Requirements:**
- Healthcare (HIPAA): Must report to HHS Office for Civil Rights
- Financial (GLBA/FFIEC): Must report to banking regulators
- Payment cards (PCI-DSS): Must report to card networks
- Critical infrastructure: Must report to DHS/CISA

**When to Use:**
- Data breach triggers regulatory requirement
- Want law enforcement assistance
- Want to establish good faith investigation
- Legal team recommends it

**Risk if Not Done:**
- Regulatory violation if required
- Law enforcement cannot assist
- Company appears to be hiding breach
- Regulators may impose penalties

**Regulatory Impact:**
- Required in many cases (legal obligation)
- Shows cooperation with authorities
- May help recover stolen data
- Better regulatory relationship
- May reduce penalties (self-reporting)

**Team Trade-off:**
- Moderate cost (8 Budget)
- Ongoing (involves multiple turns of coordination)
- Required by law (usually)
- Impacts Regulators stakeholder (see Stakeholder Cards)
- Must be done in most cases

---

### ACTION-11: Media/Public Relations Management
**Category:** Communication
**Cost:** 12 Budget
**Communication Advance:** +15%
**Duration:** 1 turn (but ongoing for days/weeks)

**Description:**
Manage media coverage and public perception:
- Prepare press statement
- Contact media proactively
- Manage social media response
- Coordinate CEO/executive messaging
- Defend company reputation
- Provide accurate information to media

**Key Details:**
- Can heavily influence public perception
- Proactive messaging better than reactive
- Media coverage can amplify damage
- Poor communication = reputation disaster
- Good communication = company "handled it well"
- HR firm may be needed (crisis PR)

**When to Use:**
- Breach is significant (likely to attract media)
- Company has public reputation risk
- Customers are media-aware (B2C more than B2B)
- Proactive messaging is possible

**Risk if Not Done:**
- Media covers story with only attacker's perspective
- Reputation damage from poor response
- Stock price may drop (if public company)
- "No comment" looks like company is hiding
- Social media amplifies negative coverage

**Impact if Done Well:**
- "Company handled breach responsibly"
- Trust is maintained or recovered
- Stock price less impacted
- Reputation damage is contained
- Customer retention better

**Team Trade-off:**
- Higher cost (12 Budget)
- Ongoing (multiple turns)
- Impacts Media/Board stakeholder (see Stakeholder Cards)
- Critical for public companies
- Can significantly affect perception

---

### ACTION-12: Board & Shareholder Communication
**Category:** Communication
**Cost:** 9 Budget
**Communication Advance:** +12%
**Duration:** 1 turn (but triggers Board Meeting - see Event Cards)

**Description:**
Inform board of directors and shareholders about breach:
- Prepare incident briefing for board
- Present forensics findings
- Discuss regulatory/legal implications
- Present remediation plan and costs
- Discuss risk mitigation going forward
- Field board questions

**Key Details:**
- Board must be informed promptly
- Disclosure may be required (SEC rules if public company)
- Board has fiduciary duty to inform shareholders
- Lawsuit risk if board hides information
- Board can fire CEO if response is poor
- Must include implications for D&O insurance

**Regulatory Requirements:**
- SEC disclosure rules (if public company)
- State corporate law (fiduciary duty)
- Insurance requirements (D&O coverage)

**When to Use:**
- Board needs to understand breach
- Public company (SEC disclosure likely needed)
- Board questions will come (better to be prepared)
- Shareholder lawsuits are likely

**Risk if Not Done:**
- Board discovers breach from media = crisis of confidence
- Shareholder lawsuits for non-disclosure
- SEC investigation for disclosure violations
- CEO may be fired (looked like hiding information)
- Stock price crashes when discovered

**Impact if Done Well:**
- Board is informed and supportive
- No surprise when disclosed
- Board can defend company (if sued)
- Stock market takes news in stride
- Organized response is possible

**Team Trade-off:**
- Moderate cost (9 Budget)
- Critical for public companies
- Impacts Board stakeholder (see Stakeholder Cards)
- Required by law (usually)
- Triggers Board Meeting Event (see Event Cards)

---

## Crisis Action Card Summary

| Card | Category | Cost | Advance | Duration | Key Benefit |
|------|----------|------|---------|----------|------------|
| ACTION-01 | Investigation | 12 | +25% | 2 turns | Expert forensics |
| ACTION-02 | Investigation | 8 | +15% | 1 turn | Find hidden compromises |
| ACTION-03 | Investigation | 5 | +10% | 1 turn | Quick log analysis |
| ACTION-04 | Investigation | 20 | +30% | 3 turns | Third-party expertise |
| ACTION-05 | Remediation | 10 | +20% | 1 turn | Fix vulnerability |
| ACTION-06 | Remediation | 8 | +15% | 1 turn | Contain attacker |
| ACTION-07 | Remediation | 15 | +25% | 2 turns | Clean rebuild |
| ACTION-08 | Remediation | 6 | +12% | 1 turn | Revoke access |
| ACTION-09 | Communication | 10 | +20% | 1 turn | Notify customers |
| ACTION-10 | Communication | 8 | +10% | 1 turn | Notify regulators |
| ACTION-11 | Communication | 12 | +15% | 1 turn | Media management |
| ACTION-12 | Communication | 9 | +12% | 1 turn | Board notification |

---

## Gameplay Strategy

### Three Competing Objectives

Teams must balance three objectives (each goes 0-100%):
- **Investigation %:** Understand scope and impact
- **Remediation %:** Fix vulnerability and remove attacker
- **Communication %:** Manage stakeholders and public perception

### Investigation vs. Remediation Trade-off

**Investigation-Heavy Strategy:**
- Spend early turns investigating (ACTION-01, ACTION-02, ACTION-04)
- Then remediate with full knowledge
- Advantage: Know exactly what happened
- Disadvantage: Takes time, attacker may still be active

**Remediation-Heavy Strategy:**
- Contain and clean immediately (ACTION-06, ACTION-07, ACTION-08)
- Investigate after containment
- Advantage: Stop attacker quickly
- Disadvantage: May miss something, incomplete cleanup

**Balanced Strategy:**
- Do some investigation + some remediation each turn
- Use cheaper actions (ACTION-03, ACTION-06, ACTION-08)
- Save expensive actions for critical moments
- Advantage: Steady progress on all three objectives

### Communication Strategy

**Early Communication:**
- Notify stakeholders early (ACTION-09, ACTION-10, ACTION-12)
- Show proactive response
- Maintain trust and credibility

**Late Communication:**
- Wait until full picture is known
- Risk: Stakeholders discover from media
- Risk: Looks like hiding information

**Selective Communication:**
- Notify regulators (required by law)
- Delay customer notification (if allowed)
- Focus on internal response first

---

## Print Instructions

1. Print on cardstock (250 gsm minimum)
2. Color-code by action category:
   - **Blue (Investigation):** ACTION-01 to ACTION-04
   - **Red (Remediation):** ACTION-05 to ACTION-08
   - **Green (Communication):** ACTION-09 to ACTION-12
3. Include cost in bold on card
4. Include progress bars (Investigation %, Remediation %, Communication %)
5. Cut along dotted lines

---

*Disaster Recovery Module: Crisis Action Cards*
*Part of Incident Zero, a modular cybersecurity board game*
*v2.1 - Balanced & Refined Edition*
