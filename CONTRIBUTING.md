# Contributing to Incident Zero

Thank you for your interest in contributing to **Incident Zero**! This document provides guidelines for submitting scenarios, card designs, feedback, and other contributions.

## How to Contribute

### 1. Share Custom Scenarios

Have a great cybersecurity scenario in mind? We'd love to hear it!

**Where:** Open a discussion or PR with your scenario
**Format:** Follow the [Scenario Template](#scenario-template) below
**Requirements:**
- Include a realistic attack chain (3-5 cards)
- Provide educational learning objectives
- Suggest appropriate difficulty level
- Include TO clues and teaching notes

### 2. Design New Threat Cards

Expand Incident Zero with modern attack vectors and real-world threats.

**Where:** Submit via PR to `cards/expansion-decks/`
**Format:** Follow the [Card Design Template](#card-design-template)
**Requirements:**
- Align with MITRE ATT&CK framework
- Include educational "Why This Works" explanation
- Specify attack chain step and vector
- Provide real-world examples or references

### 3. Design New Defense Cards

Create countermeasures for new threat scenarios.

**Where:** Submit via PR to `cards/expansion-decks/`
**Format:** Follow the [Defense Card Template](#defense-card-template)
**Requirements:**
- Match a specific threat card or vector
- Include cost tier (BASIC 10, ADVANCED 15, ELITE 25)
- Explain effectiveness and limitations
- Reference real security tools/techniques

### 4. Report Issues or Suggest Improvements

Found a bug? Have a balance suggestion? Rules clarification needed?

**Where:** [GitHub Issues](https://github.com/retroverse-studios/incident-zero/issues)
**Include:**
- Clear description of the issue
- Steps to reproduce (if applicable)
- Suggested fix or improvement
- Context (what game mode, difficulty level, etc.)

### 5. Submit Teaching Notes or Classroom Reports

Share how you used Incident Zero in your classroom or training.

**Where:** [GitHub Discussions](https://github.com/retroverse-studios/incident-zero/discussions)
**Include:**
- Student/team size and experience level
- Which game mode you used
- Key learning moments
- Suggestions for improvement
- Feedback on balance and difficulty

### 6. Improve Documentation

Help clarify rules, expand examples, or improve explanations.

**Where:** Submit via PR to `docs/`
**Include:**
- What was unclear or incomplete?
- Your suggested improvement
- Examples if helpful

---

## Contribution Standards

### Ethical Guidelines

All contributions must align with **educational and defensive cybersecurity** contexts:

✅ **Encouraged:**
- Incident response and investigation techniques
- Defensive security controls and hardening
- Security awareness and training scenarios
- Authorized penetration testing frameworks
- CTF (Capture The Flag) challenges and educational contexts

❌ **Not Acceptable:**
- Techniques for detection evasion (for malicious purposes)
- Mass targeting or DoS attack methods
- Supply chain compromise strategies
- Tools or techniques for offensive hacking without authorization
- Content that could enable illegal activities

**Philosophy:** Incident Zero teaches defenders how to recognize and respond to attacks. All content should support that mission.

### Quality Standards

1. **Accuracy:** Content should be technically accurate or clearly marked as simplified for learning
2. **Balance:** Threat/Defense pairs should be relatively balanced (not trivially easy to detect/defend)
3. **Clarity:** Rules and card descriptions should be understandable to both experts and newcomers
4. **Consistency:** Follow existing card format, terminology, and game mechanics
5. **Playtesting:** New scenarios should be tested for balance and learning value

---

## Templates

### Scenario Template

```markdown
## Scenario: [Title]

**Difficulty:** Beginner / Intermediate / Advanced / Expert
**Duration:** 30-45 min / 60-90 min / 90-120 min
**Best For:** [Type of learner or classroom context]

### Learning Objectives
- Students will understand [concept 1]
- Students will practice [skill 2]
- Students will analyze [decision 3]

### Setup
- **Attack Chain:** [List 3-5 threat cards in sequence]
- **Starting Budget:** [50-150 Budget]
- **Turn Limit:** [8-12 turns]
- **Special Rules:** [Any modifications to standard rules]

### Attack Chain Details

#### Card 1: [Threat Name]
- **Vector:** [SOCIAL ENGINEERING / WEB EXPLOIT / CREDENTIAL ABUSE / MALWARE / NETWORK / DATA EXFIL]
- **Step:** [INITIAL COMPROMISE / PIVOT & ESCALATE / PERSISTENCE / C2 & EXFIL]
- **Clue:** "..."

#### Card 2: [Threat Name]
...

### Teaching Notes
- **Why this scenario?** [Educational value]
- **Common mistakes:** [Misconceptions teams might have]
- **Discussion questions:**
  - Q1?
  - Q2?
  - Q3?

### References
- [Real-world example or data source]
- [MITRE ATT&CK techniques]

---
```

### Card Design Template

```markdown
#### Card T-[Number]: [Title]

**Type:** Threat Card
**Step:** INITIAL COMPROMISE / PIVOT & ESCALATE / PERSISTENCE / C2 & EXFIL
**Vector:** [SOCIAL ENGINEERING / WEB EXPLOIT / CREDENTIAL ABUSE / MALWARE / NETWORK / DATA EXFIL]

**Clue for Threat Orchestrator:**
```
"Your [system] detects [indicator]. [Additional context that doesn't give away the card]."
```

**Why This Works:**
[1-2 paragraphs explaining the attack technique, why it's effective, and what enables it]

**Real-World Examples:**
- [Example 1]: [Brief description and year]
- [Example 2]: [Brief description and year]

**Detection Difficulty:** Easy / Medium / Hard / Very Hard
**Detection Requirements:** [What tools/techniques are needed]

**Suggested Defenses:**
- [Defense card name or vector]
- [Defense card name or vector]

---
```

### Defense Card Template

```markdown
#### Card D-[Number]: [Title]

**Type:** Defense Card
**Tier:** BASIC (10 Budget) / ADVANCED (15 Budget) / ELITE (25 Budget)
**Countermeasure Vector:** [SOCIAL ENGINEERING / WEB EXPLOIT / CREDENTIAL ABUSE / MALWARE / NETWORK / DATA EXFIL]

**Description:**
[1-2 sentences explaining what this defense does]

**Effectiveness:**
[Explains what threats this defends against well, and what it doesn't cover]

**Implementation Notes:**
- [Key consideration 1]
- [Key consideration 2]
- [Real-world caveat]

**Real-World Tools/Techniques:**
- [Tool/service name]
- [Tool/service name]

**Limitations:**
[What can bypass this defense or why it's not a complete solution]

---
```

---

## Submission Process

### For Code Changes or New Files

1. **Fork** the repository
2. **Create a branch:** `git checkout -b feature/your-feature-name`
3. **Make changes** following contribution standards above
4. **Test** (playtest if it's a scenario or card)
5. **Commit:** `git commit -m "Clear description of changes"`
6. **Push:** `git push origin feature/your-feature-name`
7. **Create a Pull Request** with:
   - Title: Brief description
   - Description: What was added/changed and why
   - Testing: How you tested this (playtesting notes, etc.)

### For Issues or Discussions

1. Check existing [Issues](https://github.com/retroverse-studios/incident-zero/issues) first to avoid duplicates
2. Open a new issue with:
   - **Title:** Clear, specific description
   - **Type:** Bug / Suggestion / Question / Other
   - **Details:** As much context as possible
   - **Reproduction:** Steps to recreate (if applicable)

---

## Licensing

By contributing to Incident Zero, you agree that:
- **Game design, cards, scenarios, and documentation** are licensed under **CC BY-NC-SA 4.0**
- **Any code/scripts** are licensed under **MIT**
- You have the right to contribute this work

See [LICENSE](LICENSE) for full license details.

---

## Community Standards

### Be Respectful
- Treat all contributors with respect
- Assume good intent
- Provide constructive feedback
- Remember: We're building an educational resource

### Be Helpful
- Share knowledge and experience
- Help others understand the game
- Provide feedback on contributions
- Celebrate others' work

### Focus on the Mission
- Content should support defensive/educational cybersecurity
- Avoid political or unrelated discussions
- Keep contributions focused and relevant

---

## Review Process

1. **Submission:** You submit a PR or discussion post
2. **Review:** Core team reviews for quality, balance, and alignment
3. **Feedback:** We may ask questions or suggest changes
4. **Iteration:** Work together to refine the contribution
5. **Merge:** Once approved, your contribution is merged!

**Timeline:** We aim to review within 1-2 weeks, but it may take longer for complex changes.

---

## Recognition

Contributors are recognized in:
- PR/Issue comments (GitHub)
- [CONTRIBUTORS.md](CONTRIBUTORS.md) file (for significant contributions)
- Changelog entries
- README acknowledgments (for major contributions)

---

## Questions?

- **How do I...?** → Check the README or ask in [Discussions](https://github.com/retroverse-studios/incident-zero/discussions)
- **Found a bug?** → Open an [Issue](https://github.com/retroverse-studios/incident-zero/issues)
- **Want to suggest?** → Start a [Discussion](https://github.com/retroverse-studios/incident-zero/discussions) or [Issue](https://github.com/retroverse-studios/incident-zero/issues)

---

## Thank You!

Every contribution—no matter how small—helps make Incident Zero better for educators, students, and security professionals. Thank you for being part of this community!

---

*Last updated: October 2025*
*For the latest guidelines, always check the main branch of this repository*

