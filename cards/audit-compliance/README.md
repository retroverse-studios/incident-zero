# Audit & Compliance Module: Card Decks

This folder contains all card materials for the **Audit & Compliance Module** - where teams assess security controls using compliance frameworks.

---

## Module Overview

**Audit & Compliance** is a module where:
- 1 Auditor assesses security controls across the organization
- 1+ Team(s) either prepare for audit or respond to findings
- Teams win by achieving adequate compliance scores
- Can be played standalone or as lead-in to other modules
- Duration: 10-45 minutes (depending on usage)

---

## Card Decks

### Core Deck
**File:** `core-deck/audit-domain-cards.md`

**Audit Domain Assessment Cards (6 cards):**
1. **Network Segmentation & Isolation** - Evaluates network architecture
2. **Access Control & Identity Management** - Assesses authentication and authorization
3. **Threat Detection & Incident Response** - Reviews monitoring and response capabilities
4. **Backup & Disaster Recovery** - Examines backup/restore processes
5. **Third-Party Risk & Cloud Security** - Evaluates supply chain and cloud risks
6. **Security Operations & Monitoring** - Reviews security team and tools

Each domain card includes:
- Assessment criteria (what's being checked)
- Finding types (what could go wrong)
- Severity levels (minor, major, critical)
- Remediation requirements

**Total:** 6 cards

**Best for:** Standalone quick assessment (~10 minutes) or comprehensive audit (~30 minutes)

---

### Expansion Deck
**File:** `expansion-deck/compliance-frameworks.md` (framework variant cards AND the remediation action cards — see its remediation section)

Extends core deck with compliance-specific assessments:

**Compliance Framework Variant Cards (11):**
- **NIST Cybersecurity Framework (CSF)** - 5 cards (Identify, Protect, Detect, Respond, Recover)
- **CIS Controls** - 3 cards (18 controls, CIS v8, organized by priority)
- **PCI-DSS** - 3 cards (12 major requirements)

**Remediation Action Cards (8):**
- Specific fixes for common findings
- Resource requirements and timelines
- Budget costs for remediation (this is where the Audit module's Budget of 100 is spent — the assessment itself costs nothing)
- Testing/validation requirements

**Planned (not yet in the deck):** HIPAA and SOC 2 framework cards.

**Total:** 19 additional cards (11 framework + 8 remediation)

**Best for:** Comprehensive compliance assessment with framework-specific rules

---

## How Cards Are Used

### Audit Domain Cards
1. **Assessed One Per Turn** - Team is evaluated on each domain
2. **Create Findings** - Based on existing controls and architecture
3. **Generate Modifiers** - Findings create modifiers that affect IR/DR modules
4. **Require Remediation** - Teams must fix critical findings

### Compliance Framework Cards
1. **Provide Alternative Structure** - Different framework perspective on same controls
2. **Add Detail** - Break down broad domains into specific requirements
3. **Create Compliance Score** - Track overall compliance %
4. **Drive Prioritization** - Frameworks help teams prioritize fixes

### Remediation Action Cards
1. **Fix Findings** - Teams choose remediation for failed audits
2. **Cost Budget** - Each remediation has implementation cost
3. **Take Time** - Some remediations happen immediately, others over time
4. **Create Cascading Benefits** - Fixing one finding often helps others

---

## Modifier Generation (generated from the canonical table in `docs/rules/module-audit-compliance.md`, v2.2)

**Each FAILED audit domain (1-2★; 3★+ = PASS, PARTIAL = FAIL) creates exactly one modifier:**

| Failed Domain | IR Modifier | DR Budget Penalty |
|---------------|-------------|-------------------|
| Segmentation | -1 to NETWORK defenses | -10 |
| Identity/Access Control | -1 to CREDENTIAL_ABUSE defenses | -15 |
| Detection | -1 to Investigation rolls | -10 |
| Backup | None | -25 |
| Third-Party/Cloud | -1 to WEB_EXPLOIT defenses | -20 |
| Security Ops | -1 to Investigation rolls | -5 |

**Cap (v2.2):** the total gap penalty applied to a subsequent module's budget is capped at **-30**.

Example: if a team fails 3 audit domains, IR carries three -1 modifiers and DR loses up to 30 starting Budget.

---

## Integration with Other Modules

### Audit → Incident Response
- Failed audits create modifiers that make IR harder
- Teams understand why certain threats went undetected
- Reinforces importance of preventive controls

### Audit → Disaster Recovery
- Failed audits subtract from the DR starting budget (capped at -30 total)
- No backup capability = much slower recovery
- Poor ops = slower forensics

### Audit → Hardening
- Findings guide hardening priorities
- Teams fix vulnerabilities identified in audit
- Creates continuity between assessment and action

### Audit → Network Building
- Helps teams understand architecture requirements
- Guides choice of security devices
- Justifies costs for defensive infrastructure

---

## Usage Patterns

### Standalone Assessment (10 minutes)
- Quick evaluation of current security posture
- Identify top 3-5 findings
- Recommend quick wins for remediation

### Comprehensive Audit (30 minutes)
- Full assessment across all domains
- Generate detailed findings report
- Map to compliance framework
- Create remediation roadmap

### Audit as Module Lead-In
- Play audit first to establish baseline
- Findings become modifiers in subsequent modules
- Creates narrative continuity

---

## Documentation Links

For rules on how to use these cards:
- **Module Rules:** `../../docs/rules/module-audit-compliance.md`
- **Standalone Guide:** `../../docs/standalone-games/audit-compliance.md`
- **Card Reference:** `../CARD_REFERENCE.md` (comprehensive index)
- **Module Combinations:** `../../docs/module-combinations.md` (how to use audit with other modules)

---

*Audit & Compliance Module: Card Decks*
*Part of Incident Zero, a modular cybersecurity board game*
*v2.2 - Playtest Edition*
