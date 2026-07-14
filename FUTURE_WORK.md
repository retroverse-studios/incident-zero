# Incident Zero: Future Work & Development Roadmap

**Version:** 2.1 - Post-MVP Planning Document
**Last Updated:** October 2025
**Status:** Planning Phase (Not Yet Prioritized)

---

## Overview

This document captures ideas, improvements, and refinements that emerged during v2.1 development but were deferred for future work. Items range from technical infrastructure (database conversion) to game balance (playtesting validation) to design consistency (rule harmonization).

**Note:** Items here are NOT commitments—they're candidates for future versions based on playtesting feedback and development bandwidth.

---

## High-Priority: Playtest & Balance Validation

### 1. Comprehensive Playtesting Program

**Current Status:** Game designed but NOT playtested with real players

**Scope:**
- [ ] 5+ playtests with beginner groups (learning the system)
- [ ] 5+ playtests with intermediate groups (understanding mechanics)
- [ ] 5+ playtests with advanced groups (exploring advanced rules)
- [ ] Cross-module playtests (sequences of 2+ modules)
- [ ] Diverse group types:
  - [ ] Classroom settings (students new to cybersecurity)
  - [ ] Professional training (security practitioners)
  - [ ] Casual gaming groups (no security background)
  - [ ] Experienced gamers (familiar with complex mechanics)

**Success Metrics to Track:**
- Actual session duration vs. expected (30-45 min per module)
- Turn counts vs. formula predictions (does (Cards × 2) + 1 feel right?)
- Variable game length system adoption (Default Formula vs. Tier + d4)
- Critical Rule effectiveness (Rule 1-3 preventing metagaming?)
- Rules clarity (what needs clearer explanation?)
- Card balance (are any cards overpowered or useless?)
- Player engagement (fun factor, tension, learning outcomes)

**Feedback Collection:**
- Post-game survey template (5-10 questions)
- Session notes form (timing, rule confusion, house rules used)
- Card balance feedback (which cards felt too strong/weak)
- Rules clarity survey (which sections confused players)

**Expected Outcomes:**
- Identify broken/overpowered cards
- Validate or adjust turn length formulas
- Clarify confusing rules
- Discover unintended interactions
- Understand real session durations

---

### 2. Card Balance & Power Analysis

**Current Status:** Cards designed theoretically; no balance validation

**Scope:**
- [ ] **Cost vs. Effectiveness Analysis**
  - Are 10-budget cards worth it? 15? 25?
  - Compare across modules (IR defenses vs. Hardening upgrades)
  - Identify obvious power creep
  - Check if budget limitations are meaningful

- [ ] **Difficulty Class Distribution**
  - Are DC values consistent within modules?
  - DC 11 vs DC 15 difficulty curves
  - Success rate expectations (should be ~50% raw roll?)
  - Modifier economy (do +2 bonuses swing outcomes too much?)

- [ ] **Card Overlap & Redundancy**
  - Do multiple cards do essentially the same thing?
  - Are there obvious gaps in card coverage?
  - Does redundancy serve a purpose or dilute choices?

- [ ] **Dominance Analysis**
  - Are some cards clearly better than alternatives?
  - "Always pick this card" syndrome (bad design)
  - "Never pick this card" syndrome (bad design)
  - Situational vs. universal power levels

- [ ] **Cross-Module Consistency**
  - Do cards have similar power budgets across modules?
  - Example: IR Defense Cards vs. Hardening Cards—comparable power?
  - Forensics Investigation Actions vs. IR Investigation actions?

**Tools/Methods:**
- Spreadsheet analysis of cost:benefit ratio
- Win/loss statistics by card usage (from playtests)
- Frequency analysis (which cards get picked, which ignored?)
- Designer review workshop (compare across modules)

**Expected Outcomes:**
- Identify overpowered cards (nerf candidates)
- Identify underpowered cards (buff candidates)
- Clarify card purposes and power budgets
- Establish design guidelines for future cards

---

### 3. Victory Condition & Win Rate Validation

**Current Status:** Victory conditions designed; no real-world testing

**Scope:**
- [ ] **Win Rate Monitoring**
  - Track win/loss/partial outcomes across playtests
  - Expected: ~40-60% win rate (balanced challenge)
  - Too high (>70%): Game too easy, reduce resources or tighten timelines
  - Too low (<30%): Game too hard, increase resources or loosen timelines
  - Module-by-module tracking (each may have different difficulty)

- [ ] **Victory Path Validation**
  - Which victory conditions are achievable? (all three, or only some?)
  - Do players reach Victory Condition 1 (maximum/perfect win)?
  - Do players reach Victory Condition 2 (partial/good win)?
  - Do players reach Victory Condition 3 (bare minimum win)?
  - Expected distribution: ~20% max, ~30% good, ~50% partial/loss

- [ ] **Time Pressure Feedback**
  - Do turn limits feel rushed, comfortable, or slack?
  - Variable Game Length System: Does (Cards × 2) + 1 pace well?
  - Do players often run out of budget before turns?
  - Do players often run out of turns before budget?
  - Module variations: Do different modules have different difficulty curves?

**Expected Outcomes:**
- Validate/adjust victory condition thresholds
- Calibrate turn count formulas
- Ensure challenge is balanced (not too easy or hard)
- Optimize pacing across all modules

---

## Medium-Priority: Technical Infrastructure

### 4. Card Database System (SQLite)

**Current Status:** Cards defined in Markdown (investigation-cards.md, evidence-cards.md, etc.)

**Rationale for Change:**
- Easier querying (find all cards with DC > 14)
- Programmatic card generation (PDFs, printed decks)
- Balance analysis (calculate cost:benefit, win rates by card)
- Cross-module comparison (are Defense Cards comparable to Investigation Actions?)
- Future tooling (mobile app, online version)

**Proposed Structure:**

```sql
-- Core tables
cards (id, card_id, title, type, module, cost, difficulty_class, duration)
card_details (card_id, description, mitre_technique, chain_of_custody, discovery_source)
card_balance (card_id, power_level, playtests, avg_win_rate_when_used, notes)

-- Relationships
card_combinations (card_id_1, card_id_2, synergy_note, conflict_note)
card_frequencies (card_id, playtest_id, times_selected, times_succeeded)

-- Analytics
playtest_sessions (session_id, module, date, players, duration, outcome)
playtest_results (session_id, card_id, used, success, feedback)
```

**Scope:**
- [ ] Design database schema
- [ ] Migrate Markdown card data to SQLite
- [ ] Create queries for balance analysis
- [ ] Build card PDF generator
- [ ] Create web interface for card management
- [ ] Integration with GitHub (sync from markdown as backup)

**Benefits:**
- Balance analysis becomes automated
- PDF printing just a query away
- Easy to find card interactions
- Scale to hundreds of cards
- Support future digital versions

**Effort:** Medium-High (2-3 weeks for database design + migration)
**Dependencies:** Playtest data (need sample games to validate design)

---

### 5. Automated Card Documentation Generator

**Current Status:** Cards documented manually in Markdown (repetitive structure)

**Rationale for Change:**
- Cards follow strict format (title, type, description, DC, cost, etc.)
- Manually writing 192 cards is error-prone
- If database exists, can auto-generate documentation

**Proposed Workflow:**

```
SQLite Database (source of truth)
  ↓
  ├→ PDF Generator (print-ready decks)
  ├→ Markdown Generator (game documentation)
  ├→ JSON Generator (future digital tools)
  └→ YAML Generator (web interface)
```

**Scope:**
- [ ] Build template-based documentation generator
- [ ] Create printable PDF layouts (card templates)
- [ ] Validate generated documents match format guidelines
- [ ] Test with existing cards (audit coverage)

**Benefits:**
- Consistency across all cards
- Easier to add/modify cards
- Documentation always in sync with database
- Scale to expansion decks easily

**Effort:** Medium (1-2 weeks once database exists)

---

## Medium-Priority: Design Consistency & Harmonization

### 6. Rule Consistency Audit Across Modules

**Current Status:** 6 modules with similar but not identical rule structures

**Scope:**

#### 6a. Action System Harmonization
- [ ] **Incident Response:** Investigation, Deploy Defense, Emergency Response
- [ ] **Hardening:** Build Defense, Create Playbook, Advanced Tactic Response
- [ ] **Disaster Recovery:** Forensic Investigation, Stakeholder Communication, Remediation
- [ ] **Network Building:** Design Network, Review Architecture, Implement Component
- [ ] **Forensics:** Conduct Investigation, Analyze Evidence, Follow Lead
- [ ] **Audit & Compliance:** Assess Domain, Review Control, Remediate Finding

**Questions to Answer:**
- Are action costs consistent? (5-25 budget range, or do some modules break pattern?)
- Are success target numbers consistent? (DC 11+ is baseline, but exceptions?)
- Do all modules use d20 + modifiers? (yes, but do modifier bonuses vary?)
- Do all modules have "turn limits"? (yes, but are they hard/soft/suggestions?)
- Are failure consequences consistent? (lose budget only, or other penalties?)

**Expected Outcomes:**
- Establish consistent action framework
- Create "Action Template" for future modules
- Document exceptions with justifications
- Clarify why modules differ (if intentional)

---

#### 6b. Budget System Consistency
- [ ] **Verify Budget Starting Values:**
  - IR: 100 (documented)
  - Hardening: 150 (documented)
  - DR: 50 (documented, emergency only)
  - Network Building: 150 (need to verify)
  - Forensics: 75 (documented)
  - Audit: 100 (need to verify)

- [ ] **Check Budget Spending:**
  - Basic action: 5 budget (universal?)
  - Complex action: 10-25 budget (consistent ratios?)
  - High-cost action: 25+ budget (when/why?)
  - Budget = 0 → Lose (universal?)

- [ ] **Document Budget Economy:**
  - Expected budget burn rate per turn
  - Budget lifespan (how many actions before depleted?)
  - Is budget primary limiter or are turns?

**Expected Outcomes:**
- Consistent budget economy across modules
- Clear guidelines for costing new cards/actions
- Understanding of resource pressure in each module

---

#### 6c. Difficulty Class (DC) Standardization
- [ ] **Audit DC Values Across Modules:**
  - Range check: 11-15 is typical, but outliers?
  - Mean/median DC per module (should be similar)
  - Distribution: Are DCs spread or clustered?
  - Success rates: ~50% on base roll is intended?

- [ ] **Establish DC Guidelines:**
  - DC 11-12: Routine/basic (beginner-friendly)
  - DC 13: Standard (core difficulty)
  - DC 14-15: Advanced (specialist territory)
  - DC 16+: Expert only (rare, special cases)

- [ ] **Cross-Module DC Comparison:**
  - Is IR Investigation DC similar to Forensics Investigation?
  - Should they be? (are they same skill, different context?)
  - Or intentionally different? (document why)

**Expected Outcomes:**
- Consistent difficulty framework
- Clear design guidelines for future cards
- Understanding of relative card difficulty

---

#### 6d. Turn Limit Consistency
- [ ] **Audit Turn Limits:**
  - Fixed vs. variable (which modules use which?)
  - Default Formula (Cards × 2 + 1) applies to all modules?
  - Tier System applies to all modules?
  - Module-specific variations needed?

- [ ] **Variable Game Length Across Modules:**
  - Should Forensics use same formula as IR? (probably yes)
  - Should Network Building use same formula? (maybe not—design-focused)
  - Should Audit use same formula? (maybe not—review-focused)
  - Document where formula applies and where it doesn't

**Expected Outcomes:**
- Clear turn limit system per module
- Understand why some modules differ
- Consistent variable game length approach

---

#### 6e. Victory Condition Framework
- [ ] **Map Victory Conditions Across Modules:**

| Module | Victory Type | Condition 1 | Condition 2 | Condition 3 |
|--------|--------------|------------|------------|------------|
| **IR** | Perfect | All detected | 3/4 detected | 2/4 detected |
| **Hardening** | Perfect | All defended | ? | ? |
| **DR** | Mitigation | Crisis managed | Reputation > X | Damage < Y |
| **Network** | Design | All requirements | ? | ? |
| **Forensics** | Investigation | Attribution 90% | Timeline 80% | Two meters 70% |
| **Audit** | Assessment | ? | ? | ? |

- [ ] **Standardize Victory Framework:**
  - Do all modules need 3 victory conditions? (or 1-2?)
  - Should victory be binary (win/lose) or spectrum (partial wins)?
  - Are partial/conditional victories educationally valuable?

**Expected Outcomes:**
- Consistent victory condition framework
- Clear design pattern for future modules
- Understanding of success metrics

---

### 7. Card Layout Consistency & Variation Strategy

**Current Status:** Cards have varying layouts (some compact, some detailed)

**Scope:**

#### 7a. Layout Audit
- [ ] **Classify Current Card Layouts:**
  - How many distinct layouts exist? (estimate 5-8)
  - Which layouts appear in which modules?
  - Are variations intentional or organic?
  - Do all cards of same type have same layout?

- [ ] **Measure Layout Consistency:**
  - Field count per card type (do all Defense Cards have same fields?)
  - Text length variation (some cards verbose, some terse?)
  - Visual density (spacing, font sizes, readability?)

#### 7b. Three Options for Future

**Option A: Standardize All (High Effort, Maximum Consistency)**
- One layout per card type across all modules
- Pros: Clean, professional, easy to learn
- Cons: High effort to redesign 192 cards
- Recommendation: Worth it IF printing professionally

**Option B: Modular Framework (Medium Effort, Flexible)**
- Create "card template system" with components
- Example: [Universal Fields] + [Module-Specific Fields] + [Type-Unique Fields]
- Pros: Consistent structure, allows variation
- Cons: More complex documentation
- Recommendation: Best balance (aligns with CARD_CONSISTENCY_MODEL.md)

**Option C: Embrace Variation (No Effort, Organic Feel)**
- Keep current variation as-is
- Pros: Already done, adds visual interest, organic feel
- Cons: Harder to learn patterns, less professional
- Recommendation: Fine for initial release, revisit post-playtesting

**Decision Point:** After playtesting, choose based on:
- Are players confused by layout variation? → Choose A or B
- Do players find variation adds character? → Choose C
- Printing constraints (professional vs. DIY)? → Influences choice

---

#### 7c. Proposed Resolution

**Immediate (v2.1):** Document OPTION C choice explicitly
- [ ] Write design decision document explaining variation
- [ ] Create "Card Layout Guide" showing all layouts
- [ ] Add layout rationale to CARD_DESIGN/CARD_LAYOUT_TEMPLATE.md

**Post-Playtesting (v2.2):** Collect feedback
- [ ] Survey: "Were card layouts confusing or helpful?"
- [ ] Track: Do players struggle finding info on cards?
- [ ] Decide: Standardize (A/B) or keep variation (C)?

**If Standardize (v2.3+):**
- [ ] Redesign all 192 cards to single framework
- [ ] Test with professional printer (if going that route)
- [ ] Update PDF generation to use new template

---

## Medium-Priority: Game Design Exploration

### 8. Card Repetition & Recycling Rules

**Current Status:** Unclear if cards can appear in multiple attack chains or be played multiple times

**Scope:**

#### 8a. Decision Framework

**Question 1: Can same threat card appear in multiple attack chains?**

**Option A: No (Unique per Chain)**
- Once a threat card is revealed, never again in that game
- Pros: Variety, unpredictability
- Cons: Depletes deck quickly (only 12 core + 8 expansion)
- Recommendation: Works for single-scenario games

**Option B: Yes (Card Deck Recycling)**
- Cards go back to deck after chain completes
- Pros: Supports extended campaigns
- Cons: Less surprising (players recognize patterns)
- Recommendation: Better for multi-module campaigns

**Option C: Smart Recycling**
- Basic cards (Phishing, Malware) can repeat
- Advanced cards (Zero-day, Supply Chain) appear once per campaign
- Pros: Balances variety and realism
- Cons: Adds complexity
- Recommendation: Most realistic, requires design discipline

**Decision Point:** Depends on campaign vs. scenario play
- Single 45-min game: Option A (no repeat)
- Multi-module campaign: Option B (recycle)
- Teaching real incidents: Option C (smart recycling)

#### 8b. Documented Decision

**Immediate (v2.1):** Document the current assumption
- [ ] Write rule clarification: "Can threat cards repeat?"
- [ ] Provide examples for each module
- [ ] Note differences between campaign and scenario play

**Post-Playtesting (v2.2):** Validate with experience
- [ ] Track: Do players encounter card repetition?
- [ ] Feedback: Did repetition help or hurt?
- [ ] Decide: Keep current approach or adjust?

---

### 9. Card Expansion Strategy & Categories

**Current Status:** 6 modules with core + expansion decks

**Scope:**

#### 9a. Expansion Deck Analysis
- [ ] **Map Current Expansions:**
  - Which modules have expansion decks?
  - What's the expansion strategy for each?
  - Are expansions "more of same" or "different mechanics"?

- [ ] **Planned Future Expansions:**
  - Thematic expansions (Cloud, IoT, Supply Chain)
  - Difficulty expansions (harder cards for expert games)
  - Real-world incidents (Stuxnet, SolarWinds, etc.)
  - Geographic/cultural variations

#### 9b. Expansion Design Framework
- [ ] **Define Expansion Categories:**
  - "More of Same" (additional cards, same mechanics)
  - "Difficulty Scaling" (harder/easier variants)
  - "Thematic" (new attack vectors, e.g., cloud-specific)
  - "Scenario" (specific incidents, countries, industries)

- [ ] **Balance Expansion with Core:**
  - Should core deck be playable standalone? (yes)
  - Should expansion break core? (no)
  - Should expansion be 1.5× or 2× core size?
  - Clear versioning/compatibility

**Expected Outcomes:**
- Clear expansion design guidelines
- Strategy for scaling to multiple expansions
- Community contribution framework

---

## Low-Priority: Long-term Improvements

### 10. Accessibility & Inclusive Design

**Scope:**
- [ ] **Colorblind Accessibility**
  - Current cards use color coding (red=threat, blue=defense)
  - Add icon/pattern differentiation
  - Test with colorblind players

- [ ] **Dyslexia-Friendly Formatting**
  - Font choices (some fonts better for dyslexics)
  - Text sizing and contrast
  - Simple language options

- [ ] **Neurodivergence Considerations**
  - Rule complexity (can be overwhelming)
  - Sensory considerations (dice rolling noise, table crowding)
  - Pacing flexibility (some groups need slower play)

- [ ] **Language Accessibility**
  - Translate to other languages (Spanish, German, Mandarin?)
  - Simplify language for ESL players
  - Cultural adaptation for different regions

---

### 11. Digital Tools & Companion Apps

**Scope:**
- [ ] **Mobile App Concept**
  - Card lookup (searchable database)
  - Turn tracker (digital instead of paper)
  - Rules reference (searchable rules)
  - Score/budget calculator

- [ ] **Web-Based Version**
  - Play via web browser (no physical cards)
  - Online multiplayer (remote groups)
  - Automated rule enforcement
  - Integration with learning management systems (LMS)

- [ ] **Discord/Slack Bot**
  - Rules reference bot (!rule "turn system")
  - Card lookup bot (!card "phishing")
  - Automated turn tracking
  - Session timer/notifications

---

### 12. Educational Integration & Curriculum Support

**Scope:**
- [ ] **Lesson Plan Templates**
  - Beginner curriculum (weeks 1-4)
  - Intermediate curriculum (weeks 5-8)
  - Advanced curriculum (weeks 9-12)
  - One-shot scenario planning

- [ ] **Assessment Tools**
  - Pre/post-game quizzes
  - Learning outcome rubrics
  - Rubric for "technical justification" quality
  - Case study connection documents

- [ ] **Instructor Resources**
  - Facilitation tips for each module
  - Common mistakes and how to address
  - Adaptation for different class sizes
  - Time management guides

- [ ] **Real-World Incident Integration**
  - Stuxnet scenario (nation-state engineering)
  - SolarWinds scenario (supply chain)
  - Equifax scenario (data breach response)
  - Colonial Pipeline scenario (ransomware response)

---

### 13. Community & Moderation Systems

**Scope:**
- [ ] **Community Card Design**
  - Process for community to design new cards
  - Playtesting/validation pipeline
  - Integration into official decks
  - Attribution/credit system

- [ ] **Scenario Sharing Platform**
  - Repository for user-created scenarios
  - Difficulty ratings and reviews
  - Integration with main docs
  - Version control (track updates)

- [ ] **House Rules Registry**
  - Collect common house rules from community
  - Evaluate for potential official adoption
  - Document trade-offs of each house rule
  - Community voting on favorites

---

## Low-Priority: Analysis & Research

### 14. Comparative Game Design Research

**Scope:**
- [ ] **Analyze Comparable Games**
  - How do other educational games handle difficulty?
  - How do other board games handle variable length?
  - How do other war games handle balance?

- [ ] **Playtesting Data Analysis**
  - Publish anonymized playtest data
  - Statistical analysis of win rates, card usage
  - Comparison across different player types
  - Educational outcome measurement

- [ ] **Academic Integration**
  - Research partnerships with universities
  - Publish game design case study
  - Measure learning outcomes formally
  - Contribute to game design community

---

### 15. Incident Response Realism Audit

**Scope:**
- [ ] **Cross-Reference with Real Incidents**
  - Map game mechanics to real breaches
  - Validate turn counts with actual incident timelines
  - Check attack vectors against VERIZON DBIR
  - Verify defense effectiveness with breach data

- [ ] **Interview Security Professionals**
  - Incident responders: Do turn limits feel realistic?
  - Forensic analysts: Are investigation mechanics accurate?
  - Blue teamers: Is defense deployment reasonable?
  - CISOs: Do overall strategies match real decisions?

- [ ] **Continuous Improvement**
  - Feedback loop from security practitioners
  - Annual realism audit against new threat landscape
  - Update scenarios with new attack types
  - Keep educational content current

---

### 16. Facilitation Aids (High Value, Near-Term — do before/during playtesting)

**Rationale:** The biggest remaining facilitation burden is that every Threat Orchestrator must invent clue delivery and adjudication from raw card text. These aids lower TO skill requirements and improve playtest consistency.

- [ ] **Pre-built Scenario Packs** — 3-5 ready-to-run attack chains per difficulty with *scripted clue text* (ideally fake log excerpts/artifacts as handouts, not just prose). Biggest single authenticity + facilitation win; cheap to write.
- [ ] **TO Screen** — one page per module: turn sequence, costs, DCs, penalty triggers. Rules are now consistent (v2.2), so this is mechanical condensation. Companion to `cards/print-templates/tracker-sheets.md`.
- [ ] **True-Solo Tabletop Rules** — a flowchart/dice-table "automated TO" so one person can play IR or Forensics unassisted. Doubles as the design spec for the digital/IF TO logic below.
- [ ] **Playtest Issue Template** — GitHub issue template mirroring `docs/playtesting/feedback-form.md` so reports arrive structured.
- [ ] **Role Cards (anti-quarterbacking)** — optional Blue Team roles (e.g., Lead Analyst, Comms Lead, Budget Owner) that give each player final say over one decision type. Standard co-op fix for one player dominating table talk; playtest first to confirm quarterbacking is actually a problem.
- [ ] **Graduated Justification Rubric ("Expert Mode")** — at higher difficulty the TO awards +2 only for justifications naming specific ATT&CK technique IDs, artifacts, or detection logic. Raises the challenge ceiling for practitioner groups without touching card math.

---

### 17. Interactive Fiction Edition (Ink) — Solo Campaign Mode

**Concept:** A browser-playable IF version where scripted narrative replaces the human TO — either standalone episodes or one epic "whole-of-life" saga (one fictional company played through all 6 modules, state carried between episodes exactly like the existing modifier-flow system).

**Why it fits:** The module/modifier-flow design is already an episodic save-state structure; the TO requirement is the game's biggest solo-play blocker; and the justification mechanic translates well to multiple-choice reasoning (wrong-but-plausible options become teachable moments).

**Architecture decision:** Ink + inkjs embedded in a web page (consistent with the PWA pattern). **Mechanics live in JavaScript** (d20, budget, meters — via inkjs external functions); **narrative lives in Ink**. This split avoids combinatorial explosion in Ink and lets the Ink layer become the scenario/content layer of the Phase B web app (shared mechanics engine with the AI-TO version).

**Sequencing (important):**
1. Playtest tabletop v2.2 first — IF prose hard-codes rule numbers; don't write against unvalidated numbers
2. Prototype ONE episode: a 3-card beginner IR chain as a self-contained "case file" (~30-45 min play) — proves the Ink/JS split, doubles as a try-before-you-print onboarding artifact
3. Full 6-episode saga is v3.0-scale (each episode ≈ novella of branching prose); decide after the prototype lands, ideally after the Phase A retro rebrand so it ships with the visual identity
4. Real-incident scenarios (#12: SolarWinds, Colonial Pipeline) make excellent IF episodes

**Relationship to RetroVerse Digital Edition:** the IF edition is a stepping stone to (not a replacement for) Phase B — Phase B's AI TO can reuse the same mechanics engine and scenario format.

---

## Implementation Priority Matrix

Use this matrix to decide what to work on next:

```
          High Impact
             │
High Effort  │ 4: Playtesting (START HERE)
             │ 2: Rule Consistency Audit
             │ 3: Card Balance Analysis
───────────┼────────────────────── Low Effort
             │ 5: Database System (FUTURE)
             │ 6: Documentation Generator
             │ 7: Layout Strategy
             │ 9: Digital Tools (LONG-TERM)
          Low Impact
```

**Recommended Next Steps (In Order):**

1. **IMMEDIATE:** Comprehensive Playtesting Program (#1)
   - Essential for validating all design decisions
   - Drives feedback for all other work items
   - Can't optimize without data

2. **AFTER PLAYTEST:** Rule Consistency Audit (#6)
   - Medium effort, high impact
   - Can be done in parallel with more playtesting
   - Establishes design patterns

3. **AFTER PLAYTEST:** Card Balance Validation (#2)
   - Directly improves game quality
   - Database would help (#4), but can analyze from playtests
   - Identifies broken/overpowered mechanics

4. **MEDIUM-TERM:** Card Database System (#4)
   - Enables automation of analysis/generation
   - Required for scaling to digital versions
   - Reduces manual card management burden

5. **LONG-TERM:** Digital Tools (#11)
   - Based on database system
   - Extends reach beyond tabletop
   - Supports remote and classroom play

---

## Decision Framework for Contributors

**Before Starting Future Work, Answer:**

1. **Is this validated by playtesting?**
   - If no → Do playtesting first
   - If yes → Can proceed with confidence

2. **Does this affect core rules?**
   - If yes → Need community feedback before implementing
   - If no → Can proceed independently

3. **Is this a breaking change?**
   - If yes → Should be in major version (v3.0)
   - If no → Can be in minor version (v2.2, v2.3)

4. **Does this need new card/rule content?**
   - If yes → Must design and playtest first
   - If no → Can proceed with infrastructure work

5. **Can this be backwards-compatible?**
   - If no → Document migration path
   - If yes → Old content still works

---

## Appendix: Suggested Playtesting Rubric

```
SESSION EVALUATION FORM
─────────────────────────

Scenario: [ ] IR [ ] Hardening [ ] DR [ ] Network [ ] Forensics [ ] Audit
Player Count: ___ | Group Type: [ ] Beginner [ ] Intermediate [ ] Advanced
Date: ___ | Duration: ___ min | Expected: ___ min

PACING
  Turn count felt: [ ] Rushed [ ] Comfortable [ ] Dragging
  Budget felt: [ ] Depleted too fast [ ] Balanced [ ] Never constrained
  Comments: _____________________________________________________

RULES CLARITY
  Rules I had to clarify: _________________________________________
  Rules that were confusing: ______________________________________
  Rules that worked great: ________________________________________

CARD BALANCE
  Cards that felt overpowered: ____________________________________
  Cards that felt useless: ________________________________________
  Cards that felt perfect: ________________________________________

ENGAGEMENT
  Fun factor (1-10): ___
  Tension/stress (1-10): ___
  Learning outcome (1-10): ___
  Would play again: [ ] Yes [ ] Maybe [ ] No

VARIABLE GAME LENGTH
  System used: [ ] Default Formula [ ] Tier + d4
  Clarity: Was it clear how turn count was determined?
  Fairness: Did turn count feel realistic for attack type?

DIFFICULTY
  Game difficulty: [ ] Too Easy [ ] Just Right [ ] Too Hard
  Cards/mechanics difficulty: [ ] Obvious [ ] Strategic [ ] Confusing

ADDITIONAL FEEDBACK
  House rules we used: ______________________________________________
  What would make this better: _______________________________________
```

---

## RetroVerse Digital Edition Roadmap

Incident Zero is part of the [RetroVerse Studios](https://retroverse.studio) portfolio — the studio's only multiplayer title. The digital edition will coexist with the tabletop game, sharing the same card definitions and rules as a single source of truth.

**Architecture:** One repo, two interfaces.

```
incident-zero/
├── cards/              ← single source of truth (both versions read from here)
├── docs/rules/         ← canonical rules (both versions implement these)
├── tabletop/           ← print templates, cutting guides, PDF generation
└── digital/            ← web app (the RetroVerse product)
```

### Phase A: Retro Rebrand + Tabletop Polish

Align visual identity with the RetroVerse aesthetic (8-bit pixel art, terminal/hacker/WarGames theme, CRT scanlines, neon accents) while keeping the game mechanically identical.

- [ ] 8-bit pixel art card templates for print
- [ ] Retro-themed print-ready PDF generation from card markdown
- [ ] Marketing positioning: lead with "game", education as a feature
- [ ] Update card art, box/cover design, component styling

### Phase B: Solo Digital Version (AI Threat Orchestrator)

Build a web app where AI replaces the human Threat Orchestrator role. This proves the digital format without requiring multiplayer networking.

- [ ] Web app with retro terminal UI
- [ ] AI generates attack chains and adapts difficulty based on player performance
- [ ] AI creates contextual scenarios (industry-specific, difficulty-scaled)
- [ ] Single-player mode: one defender vs. AI attacker
- [ ] Card data loaded directly from markdown definitions in `cards/`
- [ ] d20 resolution, budget tracking, turn management in browser
- [ ] Offline-capable (PWA, following SwipeVerse pattern)

### Phase C: Multiplayer Digital Version

Add real-time multiplayer — the full tabletop experience online.

- [ ] WebSocket lobbies, real-time or async turns
- [ ] One player as TO (human or AI), 2-6 Blue Team defenders
- [ ] Role-based UI (TO sees attack chain, defenders see investigation tools)
- [ ] Cross-module campaigns (chain modules with outcome modifiers)
- [ ] Community scenario sharing (custom attack chains, card sets)
- [ ] Integration with learning management systems for classroom use

**Note:** Phase B and C build on the database system described in item #4 above. The SQLite migration and automated card generator (#4, #5) become prerequisites for the digital edition.

---

### 18. Image Asset Plan (prioritized; execute in the Phase A retro style)

**Rule:** the game is playable text-only, so art is table presence + accessibility, not function. Do NOT generate generic placeholder art — the visual identity is decided; generate assets once, in that style.

**Style decision (2026-07-14, supersedes the plain "8-bit pixel" note above):** after a four-way generated style test, the locked identity is **pixel noir** — high-contrast black-and-white 8-bit pixel art, chiaroscuro/venetian-blind shadows, a single green phosphor glow as the only color accent, scanlines. It keeps the Phase A retro-terminal identity, adds the investigation mood, and prints cleanly in grayscale (classroom-friendly). The canonical style prompt prefix lives in `assets/art/README.md`; every generated asset must use it. Generated via limn (Gemini/Imagen fallback while the SwarmUI backends are down; prompts + params are committed as `.json` sidecars so assets can be re-rendered with the pixel-art-xl LoRA later).

Priority order:
- [ ] **Card backs** (~8, one per card type) — the only art with gameplay function: hidden decks (Threat, Pentester Tactic, Event) need uniform backs for face-down play
- [ ] **Card-type + vector icons** (~15 small vectors) — doubles as the colorblind-accessibility fix from #10 (replace color-only coding)
- [ ] **Hero banner** — README, docsify coverpage, GitHub social preview; worth doing early as the retro identity's first test piece
- [ ] Designed tracker sheets (replace ASCII layouts) — low priority
- [ ] Per-card illustrations — lowest priority; optional 2"×2" image space already reserved in card layouts

None of this blocks playtesting — playtest with text cards.

---

### 19. Companion Company Website & Interviewable Employees

**Concept:** a real (fictional) website for the scenario company — e.g., Meridian Logistics — with a staff directory and deliberately planted OSINT clues (email formats, staff names for phishing pretexts, tech stack in job postings). Players do genuine reconnaissance before Hardening/IR, and can *interview employees* during IR/Forensics/DR. Modeled on real OSINT training ranges / red-team exercise props.

**Hard rules (non-negotiable):**
1. **Optional enhancement, never a dependency** — the site adds flavor and an alternate clue path; tabletop-only play must stay complete. No win-critical information lives only on the site.
2. **Single source of truth** — every fact on the site is generated from a scenario pack (#16). A hand-maintained prop site WILL drift from the cards and recreate the pre-v2.2 consistency problem.
3. **Sequencing:** scenario packs first — the website is a scenario pack rendered as a prop.

**Mechanic hook:** "Interview Employee" as an Investigate-variant action (≈5 Budget, 3 questions per interview); in DR, stakeholder communication can literally be a conversation with the CEO/counsel persona.

**Build in three stages:**
- [ ] **v1 — Static prop site** (GitHub Pages, free): company pages + staff directory with planted clues for one scenario pack; used as pre-game recon homework or table prop
- [ ] **v2 — Scripted interviews**: Ink dialogue trees embedded on the site — deterministic, offline, and shares the engine/scenario format with the IF edition (#17)
- [ ] **v3 — LLM chatbot employees**: persona + bounded knowledge scope per employee; guardrails required (hallucinated clues that contradict the scenario are a game-breaking bug); consider API cost/privacy for schools. Ties into Phase B's AI TO.

**Pedagogical caution:** mid-game browsing splits table attention — best used as pre-game recon or turn-gated interviews with a question budget.

---

## Version History & Tracking

- **v2.1** (October 2025) - Initial Future Work document
  - Captured playtest validation needs (#1)
  - Documented technical infrastructure items (#4-5)
  - Listed design consistency opportunities (#6-7)
  - Identified long-term vision items (#10-15)

- **v2.2** (TBD - Post Playtesting)
  - Will prioritize items based on playtesting feedback
  - May drop low-priority items based on community feedback
  - Will add new items discovered during playtesting

---

## Contributing to Future Work

**Have an idea?** See [CONTRIBUTING.md](CONTRIBUTING.md) for how to:
- Suggest new card designs
- Propose rule clarifications
- Report balance issues
- Request accessibility improvements
- Contribute to this document

---

**Last Note:** This is a living document. As the game evolves and the community grows, this roadmap will change. The priority is always **core game balance** and **educational quality** first, with polish and digital tools as secondary goals.

