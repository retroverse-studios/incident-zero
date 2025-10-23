# Disaster Recovery Module: Advanced Crisis Scenarios (Expansion)

**Version:** 2.1 - Balanced & Refined Edition
**Last Updated:** October 2025

---

## Overview

**Advanced Scenario Cards** extend the Disaster Recovery module with sophisticated, multi-faceted crisis situations that challenge experienced crisis management teams.

- **Total Cards:** 8 (SCENARIO-01 to SCENARIO-08)
- **Used In:** Disaster Recovery expansion (replaces standard core-deck events)
- **Prerequisite:** Familiarity with core Disaster Recovery mechanics
- **Complexity:** HIGH (recommended for experienced teams)

---

## Advanced Crisis Scenarios

### SCENARIO-01: Multi-Region Breach with Data Sovereignty Issues
**Complexity:** ADVANCED
**Affected Regions:** US + EU + Asia
**Primary Challenge:** Different legal requirements for different regions

**Description:**
Breach affects customer data in multiple countries with different privacy laws:
- **US (CCPA):** 30-day notification deadline, $7,500 per violation fine
- **EU (GDPR):** 72-hour notification deadline, 4% of revenue fine (up to €20M)
- **Asia (varies):** Different deadlines and requirements in each country

Data residency requirements mean:
- EU customer data cannot be transferred to US servers
- Forensics must happen in country where data is stored
- Different regulators in each country demand investigation
- Different notification laws require different messages

**Key Complications:**
- **Timeline Conflict:** EU needs notification in 72 hours, US in 30 days, Asia varies
- **Legal Conflict:** EU GDPR vs. US lawful intercept (conflicting requirements)
- **Investigation:** Must conduct forensics in multiple jurisdictions simultaneously
- **Costs:** Multi-region response = much higher costs

**Team Decision Points:**
1. Which region to prioritize (cannot satisfy all simultaneously)
2. How to conduct forensics across jurisdictions
3. How to notify customers differently per region
4. How to handle conflicting regulatory requirements

**Special Events:**
- **Turn 2:** EU 72-hour deadline reminder (must start notification)
- **Turn 4:** US 30-day deadline reminder
- **Turn 3-5:** International regulators demand investigation coordination
- **Turn 4+:** Data residency violation triggers additional fines

**Cost Implications:**
- Multi-region forensics: +20 Budget (expensive)
- Multiple legal teams: +15 Budget (lawyers in each region)
- Regulatory fines stacked: 4% + 0.75% + varying amounts = significant
- Notification costs: Translations, different templates, regulatory filings

**Team Response:**
- Must prioritize regions (satisfy EU first due to timeline)
- Must engage local lawyers in each jurisdiction
- Must conduct compliant investigation (following local laws)
- Communication % must advance faster than usual

**Difficulty Multiplier:** Investigation, Remediation, Communication all +25% harder (more moving parts)

---

### SCENARIO-02: Ransomware with Extortion Threat
**Complexity:** ADVANCED
**Attacker Demand:** $10M ransom or threaten to sell/publish data
**Primary Challenge:** Responding to extortion threats

**Description:**
Attacker not only encrypted data but also stole data and threatens public disclosure:
- "Pay $10M or we publish 50GB of customer PII on dark web"
- Attacker provides proof of data access (sample files)
- Extortion email sent to CEO and board
- Attacker sets 5-day deadline

**Key Complications:**
- **Payment Question:** Pay ransom or not?
  - Paying: Funding criminal enterprise, no guarantee of data deletion
  - Not paying: Risk of data publication (massive PR disaster)
- **Disclosure Dilemma:** Tell customers about extortion threat?
  - Yes: Customers fear data will be published
  - No: If data is published, looks like cover-up
- **Law Enforcement:** FBI recommends not paying (incentivizes more attacks)
- **Backup Reliance:** Can you recover without paying?

**Timeline Pressure:**
- Turn 1: Extortion email + 5-day deadline
- Turn 2: First partial data publication (attacker shows they have data)
- Turn 3-4: Attacker lowers price (negotiation attempt)
- Turn 5: Deadline reached (attacker publishes full dataset if unpaid)

**Financial Dilemma:**
- Ransom: $10M upfront, cannot claim insurance (illegal to pay ransoms)
- Recovery from backup: Slow (if backups exist)
- Data publication: Regulatory fines + lawsuits (potentially $50M+ liability)
- Public disclosure: Stock price crash, customer loss

**Team Decisions:**
1. Pay ransom? (Risk: Encourages future attacks, no guarantee)
2. Attempt to recover from backup? (Risk: Slow recovery, data loss)
3. Notify customers before/after data publication? (Risk: Either way is bad)
4. Notify regulators? (Required, but shows full extent of damage)

**Law Enforcement Engagement:**
- FBI may take over investigation (federal crime)
- Reduces team's control of situation
- May recommend decoy ransom negotiation (catch attacker)
- Investigation may take weeks (slow response)

**Special Events:**
- Turn 2: Partial data publication (sample data released)
- Turn 3: Media discovers extortion threat ("CEO held for ransom")
- Turn 4: Attacker releases more data (pressure increases)
- Turn 5: Deadline decision point (pay or lose everything?)

**Cost Implications:**
- Ransom: $10M (if paid)
- Investigation: +10 Budget (FBI coordination, forensics)
- Notification: +15 Budget (customers affected by extortion)
- Remediation: +20 Budget (full system rebuild if paying ransom)
- Regulatory fines: 4% revenue + penalties (if data published)

**Difficulty Multiplier:** Investigation +30%, Remediation +50% (rebuild required), Communication +40% (extortion is PR disaster)

---

### SCENARIO-03: Supply Chain Compromise (Vendor Breach Affects Customers)
**Complexity:** ADVANCED
**Vector:** Breach compromises customers' data at YOUR company's data store
**Primary Challenge:** Managing responsibility for vendor compromise

**Description:**
Investigation reveals attacker didn't target your company directly—they compromised a vendor you use:
- Your company uses cloud storage vendor (e.g., competitor to AWS)
- That vendor was breached
- Attacker gained access to YOUR customer data stored at vendor
- **Question:** Who is responsible? You? Vendor? Both?

**Key Complications:**
- **Liability Question:**
  - You're liable to customers (you selected vendor)
  - Vendor is liable (their security failure)
  - Customers might sue both
- **Vendor Response:**
  - Vendor may be uncooperative (deny liability)
  - Vendor may be bankrupt (vendor company collapse during breach)
  - Vendor may not investigate properly
- **Notification Question:**
  - Tell customers you chose bad vendor?
  - Or just notify about data breach without explaining vendor?
  - Either way looks bad
- **Investigation:**
  - Must investigate vendor (not your own systems)
  - Vendor may not cooperate
  - Limited forensic access (you don't control vendor systems)
  - Regulatory agencies may blame you anyway

**Responsibility & Liability:**
- Customer lawsuits: "You failed to vet vendor properly"
- Regulatory fines: "You failed to oversee third-party risk"
- Vendor lawsuits: "Vendor refuses to pay damages"
- Vendor bankruptcy: "Vendor can't pay, customers turn to you"

**Team Decisions:**
1. Blame vendor (legally risky, looks bad)
2. Share responsibility (legally safer, but costs more)
3. Quickly terminate vendor relationship (looks reactive)
4. Demand vendor pay for notification/remediation (vendor may refuse)

**Special Events:**
- Turn 1: Discovery that vendor was breached
- Turn 2: Vendor denies liability / claims it's your responsibility
- Turn 3: Regulatory agency demands to know vendor details
- Turn 4: First customer lawsuit against both you AND vendor
- Turn 5: Vendor declares bankruptcy (can't pay damages)

**Cost Implications:**
- Investigation into vendor: +8 Budget (forensics at vendor site)
- Legal: +20 Budget (defending against liability claims)
- Regulatory fines: Potentially full amount (you're still liable)
- Customer lawsuits: Likely regardless of vendor's role
- Vendor transition: +15 Budget (switch to new vendor, migrate data)

**Communication Challenge:**
- Customers angry at you (you chose bad vendor)
- Media: "Company failed to vet third-party security"
- Regulatory: "Poor third-party risk management"
- Board: "Why did we use this vendor?"

**Difficulty Multiplier:** Investigation +20% (limited access), Communication +35% (third-party failure is hard to explain), Remediation +25% (vendor transition)

---

### SCENARIO-04: Insider Threat Revealed Mid-Crisis
**Complexity:** ADVANCED
**Attacker:** Current employee, not external hacker
**Primary Challenge:** Organizational trauma and trust collapse

**Description:**
During investigation of external breach, forensic team discovers:
- The "external breach" had help from insider
- Employee provided attacker with access/credentials
- Employee may have also exfiltrated data
- Employee is still working at company (not yet caught)

**Key Complications:**
- **Who is involved?**
  - Single rogue employee?
  - Conspiracy (multiple employees)?
  - Which departments are involved?
- **Motive:**
  - Disgruntled employee selling data
  - Corporate espionage (hired by competitor)
  - Theft for personal gain
  - Political/ideological motivation
- **Scope:**
  - What other systems did insider compromise?
  - What data did they access/steal?
  - How long were they active?
  - Are there other insiders?
- **HR/Legal:**
  - Fire the employee immediately (risks legal action)
  - Continue employment while investigating (ethics question)
  - Involve law enforcement (police investigation)
  - Civil litigation from employee (wrongful termination claims)

**Organizational Impact:**
- Trust in employees collapses
- Morale plummets (people suspect each other)
- Staff paranoia increases
- Executive distraction (investigating insider)

**Special Events:**
- Turn 2: Forensics discovers insider involvement
- Turn 3: HR/Legal team must decide: fire or investigate?
- Turn 4: If fired, wrongful termination lawsuit likely
- Turn 4: If not fired, employee may destroy more evidence
- Turn 5: Law enforcement investigation (if reported to police)

**Team Decisions:**
1. Immediately fire employee (legal risk but stops damage)
2. Continue employment while investigating (ethical but risky)
3. Involve law enforcement (criminal investigation, slow)
4. Settle potential lawsuits preemptively (expensive)

**Investigation Complexity:**
- Cannot trust employee's explanations
- Must verify what employee had access to
- Must recover deleted data/logs
- Must interview other employees
- Investigation takes much longer (suspicious of everyone)

**Cost Implications:**
- Extended forensics: +15 Budget (investigating employee)
- Legal: +25 Budget (employment law, potential settlements)
- HR investigation: +8 Budget (interview staff, background checks)
- Remediation: +20 Budget (credential reset, system rebuild)
- Potential lawsuit: Millions if significant

**Communication Challenge:**
- Cannot publicly disclose insider involvement (defamation risk)
- Regulators and customers demand explanation
- Media: "Company had insider threat"
- Board: "Why was security so bad?"

**Difficulty Multiplier:** Investigation +40% (added complexity), Remediation +30% (reset credentials), Communication +25% (cannot disclose details)

---

### SCENARIO-05: Critical Infrastructure Breach (Safety/Lives at Risk)
**Complexity:** ADVANCED+
**Sector:** Utilities, Healthcare, Transportation, Manufacturing
**Primary Challenge:** Physical safety takes priority over cybersecurity response

**Description:**
Breach affects critical infrastructure where compromise could cause physical harm:
- **Healthcare:** Hospital network compromise during surgery (patient safety risk)
- **Utilities:** Power grid compromise during storm (people without power/heat)
- **Transportation:** Traffic system compromise (accidents possible)
- **Manufacturing:** Production system compromise (equipment failure)

**Key Complication: Safety > Security**
- Cannot shut down system for forensics if people are harmed
- Cannot remediate if it requires system downtime
- Incident response must preserve operational safety
- Balances security investigation with operational continuity

**Regulatory Escalation:**
- CISA (Cybersecurity Infrastructure Security Agency) involved immediately
- National Incident Command System (NICS) may take over
- Government mandates response (not optional)
- Military/intelligence agencies may be involved
- Cannot investigate without government approval

**Special Considerations:**
- Lives are at stake (not just data)
- Response priorities are: Safety → Containment → Investigation
- Traditional forensics may be impossible (system must stay operational)
- Attacker knows system is critical (leverage for negotiation)

**Special Events:**
- Turn 1: CISA declaration of critical infrastructure incident
- Turn 2: Government takes partial control of response (may override company decisions)
- Turn 3-4: Attacker threatens system shutdown (extortion using safety risk)
- Turn 5: Coordinated media/government briefings (national security implications)

**Team Decisions:**
1. Continue operations (risk of safety incident) or shut down (risk to people without service)?
2. Engage with government agencies (lose control of response)
3. Negotiate with attacker (funding terrorism, illegal)
4. Accept potential service interruption (for safety)

**Cost Implications:**
- Immediate government response: +50 Budget (federal agencies)
- Operational impact: Unknown (depends on what breaks)
- Remediation: Cannot shut down system (very limited options)
- Investigation: Deferred (safety is priority)
- National security classification: Investigation may be classified (cannot discuss publicly)

**Communication Challenge:**
- Cannot disclose security details (national security)
- Cannot disclose full scope (might encourage copycat attacks)
- Public panic risk (if people know infrastructure is vulnerable)
- Media cannot report full details (government requests)

**Difficulty Multiplier:** Investigation +50% (cannot interrupt operations), Remediation +100% (limited options), Communication +75% (national security restrictions, cannot disclose)

---

### SCENARIO-06: Stock Price Crash (Public Company Panic)
**Complexity:** ADVANCED
**Trigger:** Negative media coverage + analyst downgrades
**Primary Challenge:** Managing financial crisis alongside security crisis

**Description:**
Public company stock price crashes following breach announcement:
- News of breach announced
- Stock drops 10-20% in first day
- Short-sellers amplify negative sentiment
- Analysts downgrade stock rating
- Institutional investors sell (panic selling)
- Stock drops 30-50% or more

**Key Complications:**
- **Financial Crisis:**
  - Company loses market value ($1B+ in some cases)
  - Credit rating downgrade possible
  - Difficulty accessing credit markets
  - Acquisition at depressed price possible
- **Board/Shareholder Panic:**
  - Shareholders demand CEO removal
  - Board may fire executives immediately
  - Board may accept lowball acquisition offer
  - Media coverage of internal turmoil
- **Business Disruption:**
  - Employee morale crashes (stock is part of compensation)
  - Key employees leave (seeking more stable companies)
  - Customer confidence drops
  - Supplier payment delays (credit rating issue)
  - Business slows due to loss of employee focus

**Investor Psychology:**
- Fear-driven selling (stock is "falling knife")
- Rumors spread (company is bankruptcy risk)
- Technical traders amplify selling (algorithmic trading)
- Recovery takes months/years even if breach is minor

**Special Events:**
- Turn 1: Stock drops 20% (breach announcement)
- Turn 2: Analyst downgrades (stock drops another 15%)
- Turn 3: Media "Death Spiral" narrative ("Company Doomed")
- Turn 4: Short-seller report (negative narrative amplified)
- Turn 5: Activist investor demands board change
- Turn 6: Acquisition offer from vulture investor (lowball)
- Turn 7: Board may accept acquisition (loses independence)

**Team Decisions:**
1. Focus on crisis response (stock takes care of itself)
2. Spend effort on investor relations (PR effort)
3. Respond to activist pressure (appeasement or defiance?)
4. Accept acquisition offer or fight it?

**Indirect Crisis Complications:**
- Cannot spend freely on response (stock-based credit)
- May need to cut crisis response budget (unexpected)
- Board becomes distracted (shareholder meetings, hostile negotiations)
- Executives leave (job market is competitive)
- Crisis response effectiveness drops

**Cost Implications:**
- Investor relations campaign: +10 Budget
- Board/shareholder meetings: Distraction (-10 effectiveness)
- Potential acquisition: Loss of independence
- Employee departures: Loss of key expertise
- Credit access: May be restricted (raises costs)

**Communication Challenge:**
- Must manage investor narrative (balance hope + realism)
- Must appear competent (or stock collapses more)
- Media attention is intense (every statement scrutinized)
- Cannot show weakness (stock market punishes)

**Difficulty Multiplier:** Communication +50% (investor relations critical), Remediation -20% (budget may be cut), Board confidence +50% risk (board pressure is constant)

---

### SCENARIO-07: Ransomware + Data Breach + Business Email Compromise
**Complexity:** ADVANCED+
**Multiple Simultaneous Compromises:** Systems encrypted + data stolen + email account compromised
**Primary Challenge:** Responding to multiple attack objectives simultaneously

**Description:**
Not a single attack but multiple overlapping compromises:
1. **Ransomware:** File servers encrypted (production stops, cannot access files)
2. **Data Breach:** Database stolen (customer data exfiltrated)
3. **Email Compromise:** CEO's email account compromised (attacker can send as CEO)

**Key Complications:**
- **Attacker has multiple leverage points:**
  - "Pay ransom or systems stay encrypted" (operational pressure)
  - "Pay to prevent data publication" (financial/reputational pressure)
  - "Stop responding or we'll send fake CEO email" (social engineering pressure)
- **Investigation difficulty:**
  - Multiple attack vectors to investigate
  - May be different attackers or coordinated campaign
  - Each compromise has different timeline
  - Cannot determine if attacks are related or independent
- **Remediation priorities clash:**
  - Decrypt systems immediately (get operations back)
  - Recover stolen data (prevent publication)
  - Secure CEO email account (prevent further compromise)
  - Cannot do all three at once (budget/time constraints)

**Special Complications:**
- **Fake CEO Email Risk:**
  - Attacker sends email as CEO
  - "Approves" emergency spending
  - "Authorizes" data transfers
  - "Orders" employee actions
  - Teams cannot tell if email is real
- **Timeline Acceleration:**
  - Email compromise creates urgency
  - Attacker can impersonate executives
  - Must immediately notify all employees
  - Breach of trust (employees distrust CEO emails)

**Special Events:**
- Turn 1: Discovery of ransomware + data breach
- Turn 2: Discovery of CEO email compromise
- Turn 3: Fake CEO email sends "emergency transfer" (employees confused)
- Turn 4: Attacker threatens to send more fake emails (escalation)
- Turn 5: Ransom deadline, data publication deadline, email account deadline (all converging)

**Investigation Complexity:**
- Three separate forensics investigations (expensive)
- Each compromise requires different approach
- Timelines may overlap (more complexity)
- May be related (same attacker) or unrelated (unlucky)

**Cost Implications:**
- Triple forensics: +20 Budget (investigating all three)
- Triple ransom/extortion demands: $10M+ total
- Remediation: +25 Budget (rebuild files, backup, email security)
- Communication: +15 Budget (notifying employees about fake emails)
- Regulatory fines: Stacked (multiple breach types)

**Team Decisions:**
1. Which compromise to prioritize? (Cannot fix all simultaneously)
2. Pay multiple ransoms or negotiate single amount?
3. How to prevent fake CEO emails during investigation?
4. How to rebuild trust after email compromise?

**Communication Challenge:**
- Must warn employees about fake emails (careful wording)
- Cannot fully disclose CEO email compromise (executive embarrassment)
- Must appear to have control (or stock crashes)
- Media narrative: "Multiple breaches mean security is very bad"

**Difficulty Multiplier:** Investigation +50%, Remediation +75%, Communication +60% (complexity multiplied by multiple simultaneous crises)

---

### SCENARIO-08: Breach During Merger/Acquisition (Regulatory + Deal Complications)
**Complexity:** ADVANCED+
**Context:** Breach happens while company is being acquired or merging
**Primary Challenge:** Managing breach while deal dynamics change

**Description:**
Breach is discovered during critical phase of M&A transaction:
- Company announced acquisition/merger
- Deal close in 30-45 days
- Due diligence is underway (acquirer evaluating company)
- **Breach discovered mid-deal**
- Acquirer may walk away (reduces deal value or terminates)
- Regulators may block deal (antitrust, security concerns)

**Key Complications:**
- **Deal Dynamics:**
  - Acquirer discovers breach during due diligence
  - Acquirer may lower offer price (leverage)
  - Acquirer may demand warranty/escrow (financial penalty)
  - Deal may fail entirely (destroys shareholder value)
- **Information Control:**
  - Acquirer has limited information (still under NDA)
  - Seller has incentive to minimize breach
  - Acquirer has incentive to maximize perceived severity
  - Buyer/seller information asymmetry complicates response
- **Regulatory Issues:**
  - Merger may be blocked for security concerns
  - FTC may demand security improvements (delay deal)
  - State regulators may oppose merger (security risk)
  - Deal timing already tight (additional scrutiny delays close)
- **Board Pressure:**
  - Board wants to preserve deal value
  - May demand minimal response (to not disclose full scope)
  - May pressure executives to downplay breach
  - Creates pressure for inadequate response

**Timeline Pressure:**
- Deal must close in 30-45 days
- Breach response takes time
- Regulatory review adds time
- Conflicting priorities: Deal vs. Response

**Special Events:**
- Turn 1: Breach discovered, acquirer learns in due diligence
- Turn 2: Acquirer threatens to walk away (leverage)
- Turn 3: Price renegotiation (acquirer lowers offer 10-20%)
- Turn 4: Regulatory delay (FTC requests documents)
- Turn 5: Deal extension negotiations (need more time for breach response)
- Turn 6: Shareholder lawsuit (shareholders allege breach was hidden)

**Team Decisions:**
1. Full disclosure to acquirer (cooperation but deal value drops)
2. Minimal disclosure (preserve deal but fraud risk)
3. Separate negotiation: breach response vs. acquisition terms
4. Push for deal delay (to respond properly to breach)

**Complex Incentives:**
- **Company wants:**
  - Deal to close at good price
  - Breach to be minimized
  - Acquirer to handle breach remediation
- **Acquirer wants:**
  - Full disclosure of breach
  - Lower price to account for risk
  - Warranties that seller covers breach costs
- **Regulators want:**
  - Full investigation
  - Breach remediation
  - Assurance of future security
  - May block if combined entity is too powerful

**Cost Implications:**
- Breach response: Standard costs (+20-30 Budget)
- Deal renegotiation: Millions in lost value
- Regulatory review: Delays (may block deal)
- Shareholder lawsuit: If breach was hidden, liability
- Escrow/warranty: Seller may have to hold money as security

**Communication Challenge:**
- Cannot disclose full breach details (acquirer has leverage)
- Cannot hide breach (fraud risk)
- Must negotiate simultaneously with acquirer + regulators + investigators
- Media discovery complicates (stock price pressure)

**Difficulty Multiplier:** Communication +70% (multiple audiences with conflicting interests), Negotiation complexity extreme, Board pressure to under-respond

---

## Advanced Scenarios Summary

| Scenario | Challenge | Difficulty | Key Pressure |
|----------|-----------|-----------|--------------|
| SCENARIO-01 | Multi-Region Legal | HIGH | 3 different regulatory timelines |
| SCENARIO-02 | Ransomware Extortion | HIGH | $10M decision + data publication threat |
| SCENARIO-03 | Supply Chain Liability | HIGH | Vendor failure, customer trust |
| SCENARIO-04 | Insider Threat | HIGH | Organizational trust collapse |
| SCENARIO-05 | Critical Infrastructure | EXTREME | Lives at risk, government control |
| SCENARIO-06 | Stock Crash | HIGH | Financial crisis + board pressure |
| SCENARIO-07 | Triple Compromise | EXTREME | 3 simultaneous attacks, multiple ransoms |
| SCENARIO-08 | M&A Complications | EXTREME | Deal value + regulatory blocks |

---

## Gameplay Recommendations

### When to Use Advanced Scenarios

**Use if:**
- Playing with experienced crisis management teams
- Want sophisticated, realistic scenarios
- Have time for complex decision-making (add 20-30 min per scenario)
- Want to teach cascading effects of bad decisions

**Skip if:**
- Playing with beginners (too complex)
- Want simpler, faster gameplay
- Limited time available
- Focus is on learning basics

### Scenario Selection Strategy

**Start with easier scenarios:**
1. SCENARIO-01 (Multi-Region): Complex but straightforward
2. SCENARIO-02 (Ransomware): Familiar from news, clear choices
3. SCENARIO-04 (Insider): Interesting organizational dynamics

**Progress to harder scenarios:**
4. SCENARIO-03 (Supply Chain): Adds liability complexity
5. SCENARIO-06 (Stock Crash): Financial crisis layer

**Reserve for expert play:**
6. SCENARIO-05 (Critical Infrastructure): Government involvement changes everything
7. SCENARIO-07 (Triple Compromise): Multiple simultaneous crises
8. SCENARIO-08 (M&A): Extreme complexity, conflicts of interest

---

## Print Instructions

1. Print on cardstock (250 gsm minimum)
2. Use distinct coloring by complexity level:
   - **Orange (Advanced):** SCENARIO-01 to SCENARIO-04
   - **Red (Advanced+):** SCENARIO-05, SCENARIO-06
   - **Dark Red (Extreme):** SCENARIO-07, SCENARIO-08
3. Include warning icons (exclamation mark for extreme scenarios)
4. Include difficulty rating on card
5. Cut along dotted lines
6. Create a "Scenario Difficulty Guide" for selecting appropriate scenarios

---

## Possible Future Advanced Scenarios

- SCENARIO-09: Nation-State Attack (APT involvement, geopolitical implications)
- SCENARIO-10: Pandemic/Natural Disaster (breach during crisis)
- SCENARIO-11: Data in Wrong Hands (journalist/competitor leaked)
- SCENARIO-12: Cryptocurrency Ransom Laundering (financial forensics required)
- SCENARIO-13: International Incident (cross-border attack, diplomatic implications)

---

*Disaster Recovery Module: Advanced Crisis Scenarios (Expansion)*
*Part of Incident Zero, a modular cybersecurity board game*
*v2.1 - Balanced & Refined Edition*
