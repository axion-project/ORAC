# ORAC Minimum Command Protocol (MCP)

![MCP Status](https://img.shields.io/badge/status-active-brightgreen)
![License](https://img.shields.io/badge/license-Apache%202.0-blue)
![AI Sovereignty](https://img.shields.io/badge/sovereignty-Civitas%20Machina-critical)

> **Command the Machine. Contain the Chaos.**

**ORAC** — the *Operational Reasoning and Analytics Core* — is a private LLM system designed for sovereign AI operations under the strategic aegis of **Civitas Machina**. This repository defines the **Minimum Command Protocol (MCP)**, the hardened control framework that governs ORAC’s behavior, execution, and containment logic.

---

## 🧠 What is MCP?

The **Minimum Command Protocol** is a rigorously defined set of:

- System-level directives
- Execution schemas and sandboxed modes
- Containment and audit strategies
- Ethical alignment constraints

All designed to empower **ORAC** with high-autonomy reasoning while respecting strict sovereignty and operational integrity.

---

## 🛡️ Key Features

- ✅ **Execution Modes**: ANALYTICA, CODEX, SHADOWDOC, LEGATUS  
- 🔐 **Failsafe Protocols**: Auto-lockdown, moral crossroad detection, memory loop guard  
- 📊 **Audit Logging**: Immutable logs, hash-stamped with SHA-512  
- 🧾 **I/O Control**: Schema-based input validation, output with confidence tagging  
- ⚙️ **Deployment Scripts**: Secure initialization, diagnostics, override engagement  

---

## 📁 Repository Structure

```plaintext
orac-mcp/
├── README.md                  # This file
├── LICENSE                    # Apache 2.0 License
├── .gitignore
│
├── MCP/
│   ├── mcp_core.yaml          # Core command protocol
│   ├── modes.yaml             # Mode definitions
│   ├── command_schema.json    # Standard input/output schema
│   ├── execution_hooks.sh     # Runtime hooks for mode switching
│   └── failsafe_protocol.md   # Failsafe triggers and actions
│
├── config/
│   ├── orac_identity.json     # Identity & purpose definition
│   ├── system_context.md      # Strategic deployment context
│   ├── knowledge_bounds.md    # External I/O boundaries
│   └── audit_logging_rules.yaml # Logging policy
│
├── diagnostics/
│   ├── diagscan_template.json         # Scan request format
│   └── lockdown_trigger_conditions.md # Lockdown rules
│
├── scripts/
│   ├── deploy_orac.sh         # Main deploy script
│   ├── mcp_test_runner.py     # Test suite for MCP logic
│   └── secure_startup.sh      # Combined init + lock checks
│
└── utils/
    ├── confidence_flagger.py     # Adds confidence scores to output
    └── logtrace_query_tool.py    # CLI tool for secure audit tracing
