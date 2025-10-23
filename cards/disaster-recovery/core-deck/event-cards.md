# Disaster Recovery Module: Event Timeline Cards

**Version:** 2.1 - Balanced & Refined Edition
**Last Updated:** October 2025

---

## Overview

**Event Cards** represent external events that occur during the crisis—some predictable deadlines, some unexpected escalations. Events are drawn each turn to create time pressure and complicate the response.

- **Total Cards:** 12 (EVENT-01 to EVENT-12)
- **Used In:** Disaster Recovery module (each turn draws an Event)
- **Timing:** Draw one Event per turn (turn sequence)
- **Purpose:** Create time pressure and complicate decision-making

---

## Event Timeline Cards

### EVENT-01: First Media Coverage
**Turn:** Usually Turn 1-2
**Type:** Discovery
**Impact:** Media becomes aware of breach (if not publicly disclosed yet)

**Description:**
A news outlet publishes story about the breach:
- "Company Suffers Data Breach" headline
- Unnamed source gives details
- Story spreads on social media
- Phone starts ringing with reporter calls

**Triggers:**
- Automatically drawn if not yet publicly announced
- Can be triggered by leaked information
- Cannot be prevented (media finds out)

**Consequences:**
- Media stakeholder awareness increases
- Customers learn about breach (if not notified)
- Stock price may drop (if public company)
- Regulatory agencies become aware

**Team Response:**
- If prepared: ACTION-11 (Media Management) + 5% effectiveness
- If unprepared: Media coverage becomes more negative
- Every turn of delay worsens media perception

**Duration:** Ongoing (media coverage continues)

---

### EVENT-02: Regulatory Notification Deadline (30 days)
**Turn:** Turn 3-4 (usually, depending on rule)
**Type:** Deadline
**Impact:** Legal requirement to notify regulators

**Description:**
Calendar reminder that you've reached the regulatory notification deadline:
- "30-day notification deadline for California CCPA"
- Must notify regulators by end of this turn
- Failure to notify = regulatory violation

**Triggers:**
- Automatically on turn corresponding to deadline
- Varies by jurisdiction (30-60 days typical)
- Different for different regulators

**Consequences:**
- If notified (ACTION-10): Regulatory confidence stabilizes
- If NOT notified: Regulatory penalty Event triggered
  - -30% regulatory confidence
- Must allocate 8 Budget to ACTION-10

**Team Decision:**
- Must choose between ACTION-10 (notify regulators) vs. other actions
- If budget is low, difficult choice
- Failure is not an option (deadline is legal requirement)

**Duration:** Single turn decision point

---

### EVENT-03: Customer Notification Deadline (60 days)
**Turn:** Turn 6-7 (usually)
**Type:** Deadline
**Impact:** Legal requirement to notify customers

**Description:**
Calendar reminder that you've reached the customer notification deadline:
- "60-day notification deadline for customers"
- Must notify customers by end of this turn
- Notification law requires it (varies by state)

**Triggers:**
- Automatically on turn corresponding to deadline
- Usually 60 days, varies by state
- Some states require "without unreasonable delay" (30 days)

**Consequences:**
- If notified (ACTION-09): Customer trust stabilizes
- If NOT notified: Legal violation
  - -30% customer trust
  - Class action lawsuit triggered (see EVENT-07)
- Must allocate 10 Budget to ACTION-09

**Team Decision:**
- Must choose between ACTION-09 vs. other actions
- Late-game deadline adds pressure
- Failure triggers lawsuits

**Duration:** Single turn decision point

---

### EVENT-04: Board Meeting
**Turn:** Turn 3 (automatically)
**Type:** Governance
**Impact:** Board meets to assess breach response

**Description:**
Board of directors holds emergency meeting to review:
- Breach scope and impact
- Investigation progress
- Remediation plan
- Budget and timeline
- Executive performance
- Shareholder communication

**Triggers:**
- Automatically on Turn 3
- Can also be triggered if board confidence drops very low
- Should have ACTION-12 (Board Notification) completed

**Consequences:**
- If prepared: Board confidence increases (+10%)
- If unprepared: Board confidence decreases (-20%)
- Board authorizes budget for crisis response
- Board may fire CEO (if confidence is low)

**Team Preparation:**
- Should have forensics/investigation underway
- Should have preliminary findings
- Should have communication plan
- CEO should be briefed

**Duration:** Single turn, but affects future turns

---

### EVENT-05: Customer Class Action Lawsuit
**Turn:** Variable (Turn 3-5 if customers are angry)
**Type:** Legal
**Impact:** Customers file lawsuit against company

**Description:**
Law firm recruits customers and files class action lawsuit:
- "Jane Doe et al. vs. [Company Name]"
- Claims company failed to protect data
- Claims company failed to notify timely
- Seeks damages + attorney fees
- Demands court proceedings

**Triggers:**
- If customer notification deadline missed
- If customer trust drops below 20%
- If customers learn about breach from media first

**Consequences:**
- -15% Customer Trust (additional damage)
- -10% Board Confidence (liability risk)
- Additional legal costs (attorney fees)
- Long-term liability (discovery, depositions, trial)
- Settlement possible (can cost millions)

**Team Response:**
- Action: Use crisis budget for legal defense
- Action: Settle lawsuit (mitigate long-term cost)
- Cannot prevent, only mitigate damage

**Duration:** Ongoing (discovery phase lasts months)

---

### EVENT-06: Regulatory Fine
**Turn:** Variable (Turn 4-6 if regulatory requirements missed)
**Type:** Regulatory
**Impact:** Regulatory agency assesses financial penalty

**Description:**
Regulatory agency (FTC, state AG, HHS, etc.) announces fine:
- "Company fined $500K for data breach"
- Fine amount depends on breach severity and response
- Justification: inadequate security, late notification, etc.
- Payment due within 30 days

**Triggers:**
- If regulatory notification deadline missed
- If regulatory confidence drops very low
- If investigation shows inadequate security

**Consequences:**
- Immediate budget impact (-$500K to -$5M)
- -20% Regulatory Confidence (temporary)
- Stock price impact (if public company)
- -10% Board Confidence (financial impact)
- Ongoing compliance requirements (can be expensive)

**Amount:**
- Small fine: $100K-$500K (if good faith response)
- Medium fine: $500K-$5M (if inadequate response)
- Large fine: $5M-$100M+ (if egregious violations like HIPAA/GDPR)
- FTC can fine up to 10% of revenue (severe)

**Team Response:**
- Pay fine (required, no choice)
- Use crisis budget to cover
- May need to cut other response actions
- Appeal possible but risky

**Duration:** Single event, but financial impact lasts

---

### EVENT-07: Media Frenzy
**Turn:** Variable (Turn 2-4 if company is silent)
**Type:** Communication
**Impact:** Major media escalation and negative coverage

**Description:**
Major media outlets pick up story:
- National news covers breach
- "Major Company Suffers Massive Data Breach" headlines
- Multiple outlets running story for days
- Social media amplifies negative narrative
- Stock price crashes (if public)

**Triggers:**
- If company says "no comment"
- If executives dodge reporters
- If company is seen as unresponsive
- If breach is very large (millions of records)

**Consequences:**
- -30% Media/Public Trust (large negative swing)
- -20% Customer Trust (customers see negative coverage)
- -15% Stock price (if public company)
- -10% Board Confidence (market impact)
- Ongoing media scrutiny (every action becomes news)

**Team Response:**
- Use ACTION-11 (Media Management) immediately
- Issue proactive statement
- CEO visible and responsive
- Transparency is key

**Duration:** Continues for several turns (media doesn't quickly forget)

---

### EVENT-08: Second Breach Discovered
**Turn:** Variable (Turn 4-6 if first breach wasn't fully contained)
**Type:** Escalation
**Impact:** Another breach is discovered while still responding to first

**Description:**
While responding to first breach, investigators discover:
- Another data store was compromised
- Different attacker or same attacker spreading
- More customer data exposed
- Response scope suddenly doubles

**Triggers:**
- If containment was inadequate
- If remediation didn't fully clean systems
- If attacker established hidden persistence
- Probability increases if not using ACTION-07 (Rebuild)

**Consequences:**
- Investigation % resets to 0% (new breach to investigate)
- Customer Trust: -30% (customers feel betrayed)
- Regulatory Confidence: -25% (regulatory agencies upset)
- Budget: +20 additional Budget needed (double response)
- Media: -20% Media Trust (looks like cover-up)
- Board: -30% Board Confidence (shows inadequate response)

**Prevention:**
- Use ACTION-07 (System Rebuild/Recovery): Prevents second breaches
- Use ACTION-04 (Third-party IR): Comprehensive investigation finds all breaches
- Use ACTION-01 (Forensic Analysis): Deep investigation prevents surprises

**Duration:** Triggers additional 7-turn cycle for second breach

---

### EVENT-09: Shareholder Pressure
**Turn:** Turn 4-5 (if public company)
**Type:** Governance
**Impact:** Shareholders demand action and accountability

**Description:**
Shareholder activists contact board:
- Demand CEO removal
- Demand explanation of failures
- Threaten proxy fight
- Organize shareholder vote
- Media coverage of shareholder anger

**Triggers:**
- Automatic for public companies (Turn 4-5)
- Triggered if stock price drops >20%
- Triggered if second breach occurs
- Triggered if large fine is announced

**Consequences:**
- -15% Board Confidence
- May trigger CEO removal (if confidence is low)
- Proxy vote must be held
- Distraction from crisis response
- Public spectacle of internal fighting

**Team Response:**
- Maintain board confidence (prevents removal)
- Board communicates well with shareholders
- Show financial impact is temporary
- Demonstrate strong response plan

**Duration:** Proxy season (typically 1-2 months)

---

### EVENT-10: Competitor Advantage
**Turn:** Turn 5-6 (if company hasn't recovered)
**Type:** Business
**Impact:** Competitor capitalizes on breach for market advantage

**Description:**
Competitor launches marketing campaign:
- "Trust us, we take security seriously"
- Advertises better security practices
- Recruits customers away from breached company
- Emphasizes competitor's investment in security

**Triggers:**
- If customer trust drops below 40%
- If media coverage is heavily negative
- If company's response appears weak
- Automatic if second breach occurs

**Consequences:**
- Customer churn: -20% Customer Trust (additional)
- Revenue impact: Budget decreases by 15 (representing lost sales)
- Market share loss: Difficult to recover
- Stock price: Further decline

**Team Response:**
- Focus on customer communication
- Demonstrate strong security improvements
- Win-back marketing campaign
- Time = recovery (trust can rebuild)

**Duration:** Ongoing (competitors keep advantage)

---

### EVENT-11: Key Executive Resignation
**Turn:** Variable (Turn 4-6 if morale is low)
**Type:** Internal
**Impact:** Important executive quits during crisis

**Description:**
Key executive resigns, citing:
- Personal/family reasons
- "Not aligned with company direction"
- Better opportunity elsewhere
- Really: "I don't trust the response"

**Triggers:**
- If executive morale drops below 30%
- If executives are publicly blamed
- If they disagree with response strategy
- If board removes CEO

**Consequences:**
- -20% Executive Morale (cascading resignations likely)
- -15% Board Confidence (key person gone)
- Loss of expertise (executive's role must be filled)
- Replacement executive is less effective
- Media coverage: "Executives flee sinking ship"

**Common Executives:**
- CISO (security expert needed)
- CTO (technical expertise needed)
- General Counsel (legal guidance needed)
- CFO (financial decisions needed)

**Prevention:**
- Maintain executive morale (regular communication)
- Show progress on response
- Don't blame executives publicly
- Board support is critical

**Duration:** Replacement takes 1-2 turns (interim less effective)

---

### EVENT-12: Government Subpoena
**Turn:** Turn 5-7 (if significant breach)
**Type:** Legal
**Impact:** Government agency demands evidence and witnesses

**Description:**
Subpoena arrives from:
- FBI (federal crime investigation)
- State attorney general (state investigation)
- Congress (hearings on security failures)
- Law enforcement (criminal case)

**Demands:**
- Turn over all evidence from investigation
- Executive depositions/testimony
- Expert witness testimony
- Compliance with investigation

**Triggers:**
- Automatic if breach involves federal crimes
- Automatic if breach affects critical infrastructure
- Likely if breach is large (millions of records)
- Can be triggered by media coverage

**Consequences:**
- Executive distraction (testimony, depositions)
- -10% Executive Morale (executives in spotlight)
- Legal costs: +15 Budget (attorney fees)
- Evidence gathering: Can accelerate investigation
- Public trial = media coverage (good or bad)

**Opportunity:**
- Can use as credibility boost (independent investigation validates response)
- Law enforcement may help recover evidence
- Investigation may result in criminal prosecution of attacker

**Duration:** Investigation phase (months), trial (years)

---

## Event Timeline Deck Summary

| Event | Turn | Type | Impact | Prevention |
|-------|------|------|--------|-----------|
| EVENT-01 | 1-2 | Discovery | Media aware | ACTION-11 (PR) |
| EVENT-02 | 3-4 | Deadline | Notify regulators | ACTION-10 (notify) |
| EVENT-03 | 6-7 | Deadline | Notify customers | ACTION-09 (notify) |
| EVENT-04 | 3 | Governance | Board meeting | Prepare briefing |
| EVENT-05 | 3-5 | Legal | Lawsuit filed | Good response, customer trust |
| EVENT-06 | 4-6 | Regulatory | Fine assessed | Regulatory compliance |
| EVENT-07 | 2-4 | Communication | Media frenzy | ACTION-11 (PR) response |
| EVENT-08 | 4-6 | Escalation | Second breach | ACTION-07 (rebuild) |
| EVENT-09 | 4-5 | Governance | Shareholder pressure | Board confidence |
| EVENT-10 | 5-6 | Business | Competitor gains | Customer communication |
| EVENT-11 | 4-6 | Internal | Executive quits | Executive morale |
| EVENT-12 | 5-7 | Legal | Government subpoena | Legal costs |

---

## Event Mechanics

### Drawing Events

Each turn:
1. Resolve current turn's Crisis Actions
2. Draw next turn's Event Card
3. Read Event description
4. Apply Event consequences
5. Teams prepare response for next turn

### Event Escalation

Some events have escalation conditions:
- If not addressed, they get worse
- Example: First Media Coverage → Media Frenzy
- Example: First breach → Second Breach
- Prevention = addressing root cause quickly

### Event Combinations

Multiple events can occur:
- Turn 3: Board Meeting + First Regulatory Deadline (double pressure)
- Turn 4: Regulatory Fine + Customer Lawsuit (financial + legal)
- Turn 5: Second Breach + Executive Resignation (compounding crisis)

### Event Chaining

Events can trigger other events:
- Media Frenzy → Shareholder Pressure (media coverage makes shareholders angry)
- Second Breach → Competitor Advantage (another failure = lose more customers)
- Executive Resignation → Second Breach (less supervision = attacker spreads)

---

## Turn Sequence with Events

**Standard 7-Turn Disaster Recovery Game:**

| Turn | Expected Events | Crisis Actions | Objectives |
|-----|-----------------|-----------------|-----------|
| 1 | First Media Coverage | Contain + Investigate | 0% Investigation, 0% Remediation, 0% Communication |
| 2 | Second Major Outlet | More investigations | ~20-30% on each |
| 3 | Board Meeting + Regulatory Deadline | Notify regulators | ~40-50% on each |
| 4 | Regulatory Fine or Lawsuit | Remediation + Communication | ~50-60% on each |
| 5 | Shareholder Pressure or Competitor | Finish remediation | ~70-80% on each |
| 6 | Customer Notification Deadline | Final communications | ~80-90% on each |
| 7 | Final Assessment | Wrap up | 85-100% on objectives |

---

## Gameplay Strategy

### Early Game (Turns 1-3)
- Focus on Investigation (need facts before remediation)
- Prepare for Board Meeting (Turn 3)
- Notify regulators (deadline Turn 3-4)
- Manage media (prevent Frenzy)

### Mid Game (Turns 4-5)
- Shift to Remediation (clean systems)
- Prepare for regulatory fine (likely)
- Manage shareholder pressure
- Prevent second breach

### Late Game (Turns 6-7)
- Notify customers (deadline Turn 6-7)
- Finish remediation
- Focus on recovery
- Support executive stability

---

## Print Instructions

1. Print on cardstock (250 gsm minimum)
2. Color-code by event type:
   - **Blue (Deadlines):** EVENT-02, EVENT-03
   - **Red (Legal):** EVENT-05, EVENT-06, EVENT-12
   - **Yellow (Communication):** EVENT-01, EVENT-07
   - **Purple (Internal):** EVENT-04, EVENT-09, EVENT-11
   - **Orange (Escalation):** EVENT-08, EVENT-10
3. Include turn number on card
4. Include consequences clearly
5. Cut along dotted lines
6. Create "Event Tracker" to mark which events have occurred

---

*Disaster Recovery Module: Event Timeline Cards*
*Part of Incident Zero, a modular cybersecurity board game*
*v2.1 - Balanced & Refined Edition*
