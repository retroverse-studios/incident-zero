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
- Budget-constrained resource allocation (starting at 100 Budget)
- Technical justification bonuses for strategic decisions
- Uncontained Threats penalties that escalate pressure
- Three optional phases: Incident Response, Hardening, and Disaster Recovery

### Game Modes

**Three Mini-Games (30-45 minutes each):**
- **Phase 1: Incident Response** - Detect and investigate hidden attack chains
- **Phase 2: Hardening** - Build layered defenses against known threats
- **Phase 2: Disaster Recovery** - Manage a breach crisis with stakeholder communication

**Two Full Campaigns (90-120 minutes each):**
- **Campaign A: Detect & Defend** - Win Phase 1 → Transition to Hardening
- **Campaign B: Attack & Recover** - Lose Phase 1 → Transition to Disaster Recovery

**Tournament Mode** - Multiple teams compete simultaneously with split brackets

See [Gameplay Modes](docs/gameplay-modes.md) for detailed descriptions.

## Project Structure

```
incident-zero/
├── README.md                          # This file
├── LICENSE                            # CC BY-NC-SA 4.0
├── CONTRIBUTING.md                    # Contribution guidelines
├── .gitignore
│
├── docs/
│   ├── gameplay-modes.md              # All play variations (6 ways to play)
│   ├── rules/
│   │   ├── core-rules.md              # Complete game specification (v2.1)
│   │   ├── phase-network-building.md  # Network-building phase rules
│   │   ├── phase-audit.md             # Audit phase rules
│   │   └── phase-disaster-recovery.md # Disaster recovery rules
│   └── standalone-games/
│       ├── network-building.md        # Standalone network-building mini-game
│       └── audit-variations.md        # Audit phase variations
│
├── cards/
│   ├── core-deck/
│   │   └── threat-defense-cards.md    # 12 threat cards + 24 defense cards (with ASCII layouts)
│   ├── expansion-decks/
│   │   ├── advanced-threats.md        # 8 modern threat scenarios (supply chain, insider, IoT, cloud, DNS, physical)
│   │   └── advanced-defenses.md       # Advanced defense cards for expansion threats
│   └── print-templates/
│       └── a4-layout-guide.md         # A4 printing instructions and specifications
│
└── assets/
    └── [Placeholder for future images, templates, and digital assets]
```

## Getting Started

### For Players
1. **First time?** Start with [Core Rules](docs/rules/core-rules.md)
2. **Choose your game mode:** [Gameplay Modes](docs/gameplay-modes.md) describes 6 ways to play
3. **Get the cards:** Print from [Card Decks](cards/core-deck/threat-defense-cards.md)
4. **Read the scenarios:** Each game mode includes detailed setup instructions

### For Threat Orchestrators
1. Review [Threat Orchestrator Tips](docs/rules/core-rules.md#tips-for-the-threat-orchestrator) in core rules
2. Build your first attack chain using the [12 sample threat cards](cards/core-deck/threat-defense-cards.md)
3. Use one of the [provided scenarios](docs/rules/core-rules.md#sample-attack-chain-with-full-details)
4. Optionally add [expansion threat cards](cards/expansion-decks/advanced-threats.md) for advanced groups

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

✅ **Flexible:** 3 mini-games, 2 campaigns, tournament mode, or custom scenarios
✅ **Scalable:** Difficulty levels for beginner to advanced players
✅ **Educational:** Teaches real-world cybersecurity concepts and decision-making
✅ **Engaging:** Competitive and cooperative play options
✅ **Modern:** Covers current threats (supply chain, cloud, IoT, insider risks)
✅ **Discussion-Based:** Built-in debrief moments for reflection and learning

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

