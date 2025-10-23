# Incident Zero: Game Module Framework

## Core Philosophy

**Incident Zero** is a modular, flexible educational game system. Rather than a rigid "phase" structure, we offer **5 interchangeable modules** that educators can combine in any way that serves their learning objectives.

- **Educators choose** which modules to play
- **Educators sequence** the modules in any order
- **Educators combine** modules to create custom experiences
- **Each module** works standalone with generated modifiers
- **Module combinations** can enhance or modify subsequent modules

---

## The 5 Core Modules

### 1. Incident Response Module
**Duration:** 30-45 minutes (solo), 20-35 minutes (in combination)
**Focus:** Attack detection, investigation, incident response
**Best For:** Teaching cyber kill chain, investigation methodology, budget prioritization

**Standalone:** Players detect a hidden attack chain through investigation and defense deployment
**In Combination:** Outcome (win/lose) and discovered cards modify subsequent modules

---

### 2. Hardening Module
**Duration:** 30-45 minutes (solo), 20-30 minutes (in combination)
**Focus:** Defense-in-depth, security architecture, proactive hardening
**Best For:** Teaching layered security, strategic planning, cost-benefit analysis

**Standalone:** Players build comprehensive defenses against known threat vectors
**In Combination:** Discovered threats (from Incident Response) guide defense strategy; OR defenses are generated via dice/cards

---

### 3. Disaster Recovery Module
**Duration:** 30-45 minutes (solo), 25-35 minutes (in combination)
**Focus:** Crisis management, forensics, stakeholder communication
**Best For:** Teaching incident response procedures, risk management, decision-making under pressure

**Standalone:** Players manage a breach crisis with budget constraints and reputation scoring
**In Combination:** Breach scope determined by Incident Response outcome; OR generated at setup

---

### 4. Network Building Module
**Duration:** 30-45 minutes (solo), 15-25 minutes (in combination)
**Focus:** Network architecture, asset security, foundational infrastructure
**Best For:** Teaching network design, critical asset identification, infrastructure hardening

**Standalone:** Players design and secure a network from scratch
**In Combination:** Network design becomes prerequisite for all other modules; OR used as rebuild scenario after Incident Response

---

### 5. Audit & Compliance Module
**Duration:** 30-45 minutes (solo), 15-20 minutes (in combination)
**Focus:** Security compliance, audit procedures, governance
**Best For:** Teaching regulatory frameworks, security assessment, governance workflows

**Standalone:** Players conduct security audits and address findings
**In Combination:** Findings from Incident Response guide audit focus; OR used post-Hardening to validate controls

---

## Module Combinations: Framework & Examples

### Combination Philosophy

Each module can modify the **next** module in several ways:

1. **Outcome Modifiers:** Results from one module affect setup of the next
2. **Information Modifiers:** Discoveries in one module inform decisions in the next
3. **Constraint Modifiers:** Limitations in one module carry forward
4. **Generated Modifiers:** When modules aren't combined in sequence, modifiers are generated during setup (dice rolls, card draws, narrative decisions)

### Combination Types

#### Solo Modules (No Dependencies)
Play any single module standalone. All modifiers are generated during setup via:
- Dice rolls (d20 for random element)
- Card draws (threat, defense, or scenario cards)
- Educator narrative choices
- Difficulty selection (Beginner/Intermediate/Advanced)

**Examples:**
- Incident Response solo
- Hardening solo
- Disaster Recovery solo
- Network Building solo
- Audit & Compliance solo

#### Linear Sequences (Recommended Paths)

**Path A: Building → Defending**
```
Network Building → Incident Response → Hardening
```
- Network built first establishes asset context
- Incident Response tests network against known threats
- Hardening hardens defenses based on lessons learned
- **Modifiers:** Network layout → Attack chain targeting → Defense strategy

**Path B: Crisis & Response**
```
Incident Response (Loss) → Disaster Recovery → Audit
```
- Detection fails; breach occurs
- Crisis management under pressure
- Post-incident audit and compliance
- **Modifiers:** Breach scope → DR decisions → Compliance findings

**Path C: Build, Test, Fix**
```
Network Building → Audit → Hardening
```
- Network designed
- Audit identifies gaps
- Hardening addresses findings
- **Modifiers:** Network design → Audit findings → Defense priorities

**Path D: Complete Lifecycle**
```
Network Building → Incident Response → Hardening → Audit
```
- Design secure network
- Test against attack
- Harden based on findings
- Audit final posture
- **Duration:** 2+ hours (advanced, comprehensive)

#### Custom Combinations
Educators can mix modules any way they choose:
- "We want Incident Response, then straight to Audit"
- "Network Building + Hardening, no incident"
- "Just Disaster Recovery for crisis training"
- "Audit first, then rebuild with Hardening"

**For any custom sequence:**
1. Identify the **first module** → play normally with generated setup
2. For **each subsequent module** → during setup, generate any missing modifiers that would normally flow from prior modules

### Modifier Generation (For Non-Sequential Play)

When modules aren't combined sequentially, educators create modifiers at setup using:

**Scenario Deck:** Pre-written scenario cards describing:
- Network layouts (if starting mid-way)
- Threat context (if starting without Incident Response)
- Compliance requirements (if starting without Audit)
- Budget constraints (if starting mid-lifecycle)

**Dice Methods:** Randomized setup parameters:
- Roll d20 for network security level
- Roll d20 for breach scope (for Disaster Recovery solo)
- Roll d20 for compliance findings (for Audit solo)

**Educator Narrative:** Direct creation based on:
- Learning objectives
- Time available
- Difficulty desired
- Real-world inspiration

**Example:**
```
Educator wants: Network Building → Disaster Recovery (no Incident Response)

Setup for Disaster Recovery:
- Educator describes network built in prior module
- Generate breach scenario via dice or narrative:
  "Roll 2d6: (3,5) = Insider threat, moderate data loss"
  "Modifiers: Budget=60, Reputation=100, Dwell time=24 hours"
- Play Disaster Recovery with those generated modifiers
```

---

## Module Flexibility & Educator Choice

### Why Modules Over Phases?

**"Phases"** implies:
- ❌ Linear progression (1→2→3)
- ❌ Specific sequence required
- ❌ All elements must be played
- ❌ Rigid pedagogical structure

**"Modules"** enables:
- ✅ Non-linear play
- ✅ Flexible educator choice
- ✅ Partial/complete experiences
- ✅ Adapts to learning objectives
- ✅ Combines in any sequence

### Educator Decision Tree

```
START: What do you want to teach?

├─ "Incident response basics"
│  └─ Play: Incident Response module solo
│     (30-45 min, fast, focuses on detection)
│
├─ "Network security & architecture"
│  └─ Play: Network Building module solo
│     (30-45 min, strategic planning focus)
│
├─ "Defense-in-depth"
│  └─ Play: Hardening module solo
│     (30-45 min, layering & strategy)
│
├─ "Crisis management"
│  └─ Play: Disaster Recovery module solo
│     (30-45 min, pressure & decisions)
│
├─ "Compliance & governance"
│  └─ Play: Audit & Compliance module solo
│     (30-45 min, assessment & findings)
│
├─ "Complete incident lifecycle"
│  └─ Play: Incident Response → Disaster Recovery → Audit
│     (90-120 min, full arc, defeat scenario)
│
├─ "Defensive preparation"
│  └─ Play: Network Building → Hardening
│     (60-90 min, proactive focus)
│
├─ "Design, audit, defend"
│  └─ Play: Network Building → Audit → Hardening
│     (90-120 min, planning-focused)
│
├─ "Everything"
│  └─ Play: Network Building → Incident Response → Hardening → Audit
│     (2+ hours, comprehensive, advanced)
│
└─ "Custom"
   └─ Pick any combination, generate modifiers for gaps
```

---

## Module Mechanics: Consistency Across All

### Common Elements (All Modules)

Every module includes:
- **Setup (5 minutes):** Configure difficulty, generate modifiers
- **Gameplay (20-35 minutes):** Core decision-making and rolls
- **Scoring/Outcome (5 minutes):** Determine results
- **Debrief (5-15 minutes):** Reflect on decisions and learning

### Common Mechanics

**Resource Management:**
- Budget (Incident Response, Hardening, Disaster Recovery)
- Time/Turns (all modules)
- Reputation/Morale (Disaster Recovery, Audit)

**Decision Making:**
- Choose action from limited options (3-5 choices)
- Roll d20 for success/failure
- Technical justification bonuses (+2, +1)
- Accept consequences or trade-offs

**Modifiers & Penalties:**
- Uncontained Threats (Incident Response)
- Pentester Tactics (Hardening)
- Compliance Violations (Audit)
- Network Vulnerabilities (Network Building)
- Breach Scope (Disaster Recovery)

**Debrief Questions:**
- What was the decision point?
- What would you do differently?
- How does this reflect reality?
- What did you learn?

---

## Module Compatibility Matrix

Which modules work well together?

```
                 IR    Hard   DR    Net    Audit
Incident Resp.   -     ✓✓    ✓✓    ✓     ✓
Hardening        ✓✓    -     ✓     ✓✓    ✓✓
Disaster Rec.    ✓✓    ✓     -     ✓     ✓✓
Network Build.   ✓     ✓✓    ✓     -     ✓✓
Audit            ✓     ✓✓    ✓✓    ✓✓    -

Legend:
✓✓ = Highly compatible (strong modifier flow)
✓  = Compatible (weak modifier flow, mostly independent)
-  = Same module (obviously)

Example:
- Incident Response + Hardening = ✓✓ (strong flow)
- Network Building + Hardening = ✓✓ (complementary)
- Audit + Compliance = ✓ (independent, minimal flow)
```

---

## Documentation Structure

To support module flexibility:

```
docs/
├── FRAMEWORK.md                    # THIS FILE - Module philosophy & combinations
├── module-combinations.md          # Educator guide to combining modules
├── rules/
│   ├── core-rules.md              # Core mechanics (timeless)
│   ├── module-incident-response.md # Full IR rules
│   ├── module-hardening.md        # Full Hardening rules
│   ├── module-disaster-recovery.md# Full DR rules
│   ├── module-network-building.md # Full Network rules
│   └── module-audit-compliance.md # Full Audit rules
└── standalone-games/
    ├── incident-response.md       # IR solo setup & play
    ├── hardening.md               # Hardening solo setup & play
    ├── disaster-recovery.md       # DR solo setup & play
    ├── network-building.md        # Network solo setup & play
    └── audit-compliance.md        # Audit solo setup & play
```

---

## Version Notes

**Current:** v2.1 (Balanced & Refined)

**Modules based on:**
- Incident Response v2.1 with Uncontained Threats & Pentester Tactics
- Hardening as alternative Phase 2 outcome
- Disaster Recovery as alternative Phase 2 outcome
- Network Building from original design (needs v2.1 refresh)
- Audit & Compliance from original design (needs v2.1 refresh)

**Pending Refinements:**
- Network Building: Update to reflect v2.1 mechanics
- Audit & Compliance: Update to reflect v2.1 mechanics
- All modules: Explicit standalone setup procedures
- Modifier generation: Formalize dice/card procedures

---

## For Educators

**Key Takeaway:** You are not bound to a rigid structure. Incident Zero modules are tools in your pedagogical toolkit. Choose the modules that serve your learning objectives, sequence them in any order, and use the flexibility to adapt to your classroom needs.

**Examples of Flexibility:**

*"I only have 45 minutes"* → Play one module solo (Incident Response or Hardening)

*"I want to teach the complete lifecycle"* → Play all 5 modules in sequence (2+ hours)

*"My students need crisis management training"* → Play Disaster Recovery solo

*"I want to rebuild after a fictional breach"* → Network Building + Hardening (no Incident Response)

*"I need governance training"* → Audit & Compliance solo or after Hardening

---

**Bottom Line:** Incident Zero is flexible. Your classroom needs come first. Choose the modules and combinations that work for you.

