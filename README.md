# Incident Zero

> A cooperative/competitive cybersecurity board game for educational environments

**Incident Zero** is a hands-on, engaging tabletop game that teaches cybersecurity concepts through gameplay. Players take on the roles of security professionals responding to cyberattacks, managing incident response, and building defensive strategies.

## Overview

Incident Zero combines strategic decision-making, resource management, and technical knowledge to create an immersive educational experience. Whether you're teaching incident response, security architecture, or crisis management, Incident Zero provides a flexible framework for multiple learning outcomes.

### What You'll Learn

- **Incident Response:** How to detect and investigate cyberattacks using the MITRE ATT&CK framework
- **Defense-in-Depth:** Building layered security controls to protect critical systems
- **Crisis Management:** Managing a breach response under pressure with stakeholder communication
- **Cyber Kill Chain:** Understanding attack progression from initial access to data exfiltration
- **Resource Prioritization:** Making security decisions under budget constraints
- **Real-World Threats:** Modern attack scenarios including supply chain, insider threats, IoT, and cloud-based attacks

## How It Works

### Core Gameplay

One player acts as the **Threat Orchestrator** (facilitator), while other players form **Blue Teams** (defenders). The Threat Orchestrator creates a hidden attack chain using Threat cards, and Blue Teams have a limited budget and turns to detect all cards in the chain through Investigation, Defense Deployment, or Emergency Response actions.

**Key Mechanics:**
- 1d20 roll-based investigation and defense actions
- Budget-constrained resource allocation
- Technical justification bonuses for strategic decisions
- Uncontained Threats penalties that escalate pressure
- Flexible, modular gameplay structure

### Game Modules: 6 Ways to Play

Incident Zero features **6 interchangeable modules** covering the complete cybersecurity incident lifecycle from planning through assessment:

**The 6 Core Modules (30-45 minutes each):**
1. **Network Building** - Design and secure network infrastructure
2. **Hardening** - Build layered defenses against known threats
3. **Incident Response** - Detect and investigate hidden attack chains
4. **Disaster Recovery** - Manage a breach crisis with stakeholder communication
5. **Forensics** - Investigate compromised systems and attribute attacks (NEW in v2.1)
6. **Audit & Compliance** - Conduct security assessments and compliance audits

**Recommended Combinations:**
- **Solo Play:** Any single module (30-45 min)
- **Detect & Investigate:** Incident Response → Forensics (90 min)
- **Crisis & Investigation:** Disaster Recovery → Forensics (90 min)
- **Detect & Defend:** Incident Response → Hardening (90 min)
- **Build, Test, Fix:** Network Building → Incident Response → Hardening (120 min)
- **Complete Lifecycle:** Network Building → Hardening → Incident Response → Disaster Recovery → Forensics → Audit (2.5+ hours)

Each module can also be **generated procedurally** (dice rolls, cards) when played solo, so modules connect seamlessly in any educator-chosen sequence.

See [Module Combinations](docs/module-combinations.md) and [Gameplay Modes](docs/gameplay-modes.md) for detailed guidance on combining modules.

## Project Structure

```
incident-zero/
├── README.md                          # This file
├── LICENSE                            # CC BY-NC-SA 4.0
├── CONTRIBUTING.md                    # Contribution guidelines
├── .gitignore
│
├── docs/
│   ├── FRAMEWORK.md                   # Module philosophy & flexibility guide
│   ├── VARIABLE_GAME_LENGTH_SYSTEM.md # Variable game length system (v2.1)
│   ├── module-combinations.md         # Module combinations & recommended sequences
│   ├── gameplay-modes.md              # Recommended module combinations & tournaments
│   ├── rules/
│   │   ├── core-rules.md              # Core mechanics (v2.1)
│   │   ├── module-network-building.md # Network Building rules (full)
│   │   ├── module-hardening.md        # Hardening module rules (full)
│   │   ├── module-incident-response.md # Incident Response rules (full)
│   │   ├── module-disaster-recovery.md # Disaster Recovery rules (full)
│   │   ├── module-forensics.md        # Forensics module rules (full) [NEW v2.1]
│   │   └── module-audit-compliance.md # Audit & Compliance rules (full)
│   └── standalone-games/
│       ├── network-building.md        # Network Building solo setup & play
│       ├── hardening.md               # Hardening module solo setup & play
│       ├── incident-response.md       # Incident Response solo setup & play
│       ├── disaster-recovery.md       # Disaster Recovery solo setup & play
│       ├── forensics.md               # Forensics solo setup & play [NEW v2.1]
│       └── audit-compliance.md        # Audit & Compliance solo setup & play
│
├── cards/
│   ├── incident-response/            # Incident Response cards
│   │   ├── core-deck/
│   │   │   └── threat-defense-cards.md    # 12 threat cards + 24 defense cards
│   │   └── expansion-deck/
│   │       ├── advanced-threats.md        # 8 modern threat cards
│   │       └── advanced-defenses.md       # Advanced defense cards
│   ├── hardening/                    # Hardening module cards
│   ├── network-building/             # Network Building module cards
│   ├── disaster-recovery/            # Disaster Recovery module cards
│   ├── forensics/                    # Forensics module cards [NEW v2.1]
│   │   ├── README.md                 # Forensics card overview
│   │   ├── core-deck/
│   │   │   ├── investigation-cards.md    # 12 Investigation Action cards
│   │   │   └── evidence-cards.md         # 12 Evidence + 4 Findings cards
│   │   └── expansion-deck/
│   │       └── advanced-cards.md         # Advanced forensics scenarios
│   ├── audit-compliance/             # Audit & Compliance module cards
│   └── print-templates/
│       └── [Card printing guides and templates]
│
└── assets/
    └── [Placeholder for future images, templates, and digital assets]
```

## Getting Started

### 📚 Documentation
- **[GitHub Pages Documentation](https://retroverse-studios.github.io/incident-zero/)** - Full game documentation with searchable sidebar
- **[DeepWiki Documentation](https://deepwiki.com/retroverse-studios/incident-zero)** - Alternative self-documenting wiki format

### For Educators
1. **Understand the framework:** Read [FRAMEWORK.md](docs/FRAMEWORK.md) to understand the 6 modules and how they combine
2. **Review Variable Game Length:** Read [VARIABLE_GAME_LENGTH_SYSTEM.md](docs/VARIABLE_GAME_LENGTH_SYSTEM.md) for game pacing options
3. **Choose your modules:** Decide which modules serve your learning objectives and in what sequence (see [Module Combinations](docs/module-combinations.md))
4. **Set up your game:** Follow standalone setup instructions for your chosen module(s)
5. **Print cards:** Download and print cards for your chosen modules
6. **Run the session:** Each module includes gameplay loops and debrief guidance

### For Threat Orchestrators
1. Review [Core Rules](docs/rules/core-rules.md) for core mechanics (v2.1)
2. Choose the module(s) you want to run (see [Gameplay Modes](docs/gameplay-modes.md) for recommendations)
3. Build your scenario using the [12 core threat cards](cards/core-deck/threat-defense-cards.md) or [8 expansion threats](cards/expansion-decks/advanced-threats.md)
4. Follow the module-specific rules and setup procedures
5. Use debrief questions to reinforce learning

## Game Components

### Core Deck
- **12 Threat Cards:** Attack chain cards representing attacker actions
- **24 Defense Cards:** Tools and procedures to counter attacks (tiered by cost: 10/15/25 Budget)
- **Trackers:** Turn, Budget, Discovery, Reputation, Uncontained Threats

### Expansion Decks
- **8 Modern Threats:** Supply chain attacks, insider threats, IoT compromise, cloud API abuse, DNS tunneling, physical security bypass
- **Advanced Defenses:** Specialized countermeasures for expansion threats
- **Pentester Tactic Cards:** Advanced attack scenarios for Phase 2

## Key Features

✅ **Complete Lifecycle Coverage:** 6 interchangeable modules covering planning through assessment (~95% of incident response lifecycle)
✅ **Flexible Game Length:** Default formula or advanced tier system with dice rolling for realistic variable timelines
✅ **Modular Design:** Play solo or combine modules in any sequence (30-45 min per module, up to 2.5+ hours for complete lifecycle)
✅ **Educational Focus:** Teaches real-world cybersecurity concepts grounded in MITRE ATT&CK framework
✅ **Scalable Difficulty:** Difficulty levels for beginner to advanced players (3-card to 6-card attack chains)
✅ **Forensics Integration:** NEW investigation and attribution module for post-incident analysis (v2.1)
✅ **Engaging Gameplay:** Competitive and cooperative play modes with meaningful decisions under resource constraints
✅ **Modern Threats:** Covers current threats (supply chain, cloud, IoT, insider threats, ransomware)
✅ **Discussion-Based:** Built-in debrief moments and learning outcome tracking

## Printing Your Deck

### Quick Start
Print the cards from [Card Decks](cards/core-deck/threat-defense-cards.md) on cardstock, cut along dotted lines, and optionally sleeve them.

### For A4 Printing (8 cards per sheet)
See [A4 Layout Guide](cards/print-templates/a4-layout-guide.md) for detailed instructions on:
- Paper specifications (250 gsm cardstock)
- Cutting guides and margins
- Multiple-card-per-sheet layouts
- Color recommendations by vector

### Digital Production (Future)
Future versions may include:
- PDF templates for professional printing services
- Programmatic card generation (Squib/Ruby)
- Print-on-demand integration (The Game Crafter, DriveThruCards)

## Licenses

### Game Design & Rules
**CC BY-NC-SA 4.0 (Creative Commons Attribution - Non-Commercial - Share-Alike)**

This allows you to:
- ✅ Play and teach with Incident Zero
- ✅ Remix and create your own scenarios
- ✅ Share with educators and community
- ❌ Sell commercial products without permission
- ❌ Restrict others from remixing your adaptations

### Code (If applicable)
Any digital tools, scripts, or software components are licensed under MIT license.

**Full license text:** See [LICENSE](LICENSE) file

## Contribution Guidelines

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for:
- How to propose new card designs
- Creating custom scenarios
- Reporting issues or suggesting improvements
- Ethical guidelines for security content

## Community & Support

### Documentation
- **[GitHub Pages Documentation](https://retroverse-studios.github.io/incident-zero/)** - Searchable game rules, modules, and card decks
- **[DeepWiki Documentation](https://deepwiki.com/retroverse-studios/incident-zero)** - Self-documenting wiki alternative

### Get Involved
- **Issues & Suggestions:** [GitHub Issues](https://github.com/retroverse-studios/incident-zero/issues)
- **Discussions:** [GitHub Discussions](https://github.com/retroverse-studios/incident-zero/discussions)
- **Scenarios:** Share your custom scenarios in Discussions

## Recommended Classroom Setup

### 60-Minute Session (Beginner)
- Setup: 10 min
- Phase 1 (3-card chain, Startup difficulty): 30 min
- Lessons Learned debrief: 10 min
- Discussion: 10 min

### 90-Minute Session (Intermediate)
- Setup: 5 min
- Phase 1 (4-card chain): 30-35 min
- Lessons Learned: 10 min
- Phase 2 Hardening: 30 min
- Debrief: 10 min

### 2-Hour Tournament (Multiple Teams)
- Setup: 10 min
- Phase 1 (all teams simultaneous): 40 min
- Phase 2 (split by outcome): 35 min
- Awards & debrief: 30 min

## Design Philosophy

**Incident Zero** is built on the principle that **security is a team sport**. By combining:
- Educational rigor (based on MITRE ATT&CK framework)
- Game mechanics (meaningful decisions, resource constraints)
- Real-world scenarios (from actual breach reports)

We create an environment where players learn by doing, make mistakes in a safe space, and develop intuition for security decision-making.

## What Makes This Game Unique

1. **Kill Chain Focus:** Players don't just detect threats; they understand the complete attack progression
2. **Justification Bonuses:** Success requires explaining *why* a decision matters, not just rolling dice
3. **Dual Outcomes:** Win against the attack → go to hardening; lose → manage the crisis
4. **Scalable Complexity:** From 3-card beginner chains to 5-card enterprise scenarios with expansion cards
5. **Modern Threats:** Includes supply chain, cloud, IoT, and insider threats alongside traditional attacks

## FAQ

**Q: How many players does this support?**
A: 2-6+ players. Best with 1 Threat Orchestrator and 2-4 Blue Team members (or multiple teams).

**Q: How long does a game take?**
A: 30-45 minutes for a mini-game, 90-120 minutes for a campaign.

**Q: Can we play this with no cybersecurity background?**
A: Yes! The game teaches concepts through play. New players start with beginner scenarios.

**Q: Can I create my own scenarios?**
A: Absolutely! See [CONTRIBUTING.md](CONTRIBUTING.md) for scenario design guidelines.

**Q: What if we want to play competitively instead of cooperatively?**
A: The rules support both. See [Gameplay Modes](docs/gameplay-modes.md#competitive-mode) for competitive variants.

**Q: Can this be played online?**
A: The current version is tabletop-focused. A digital adaptation is a future possibility.

## Version History

- **v2.1** (Current) - Balanced & Refined Edition
  - Added Uncontained Threats penalty mechanics
  - Balanced Fast-Track discovery reward
  - Introduced Pentester Tactic Cards for Phase 2
  - Expanded with 8 modern threat cards (supply chain, insider, IoT, cloud, DNS, physical)
  - Added 6 gameplay modes and tournament structure

## Acknowledgments

Incident Zero draws inspiration from:
- **MITRE ATT&CK Framework** for attack patterns
- **Cybersecurity breach reports** (VERIZON DBIR, SANS, etc.)
- **Board game design principles** (resource management, meaningful choices)
- **Tabletop RPGs** (cooperative storytelling, role-based gameplay)

## Connect with Retroverse Studios

**Incident Zero** is developed by [Retroverse Studios](https://github.com/retroverse-studios), an indie game design studio focused on educational games.

- GitHub: [retroverse-studios](https://github.com/retroverse-studios)
- Games: Incident Zero, Reality Reigns (and more coming soon!)

## License Summary

```
Incident Zero - A Cybersecurity Board Game
Copyright (C) 2025

This work is licensed under CC BY-NC-SA 4.0:
- You may use, remix, and share this work
- You must credit Incident Zero
- Non-commercial use only
- Any adaptations must use the same license

See LICENSE file for full legal text.
```

---

**Ready to teach cybersecurity through play?** [Start here](docs/rules/core-rules.md)
**Want to contribute?** [See CONTRIBUTING.md](CONTRIBUTING.md)
**Questions?** [Open an issue](https://github.com/retroverse-studios/incident-zero/issues)

