# 🧠 Natural Language → Symbolic Logic Translator

A context-specific Python tool that converts English **system specifications** into precise **symbolic logic expressions**, helping eliminate ambiguity in technical statements.

---

## 🎯 Objective
- Translate **English statements** → **Symbolic logic**
- Assign unique symbols (`p, q, r...`) to atomic propositions
- Provide a legend for formal logic interpretation
- Help students, developers, and engineers rigorously model system rules

---

## 🏗️ Background
System specifications (software or hardware) are often written in English, which can be ambiguous.  
To ensure clarity, developers translate rules into logical expressions using formal connectives like:

- **AND** → `∧`
- **OR** → `∨`
- **NOT** → `¬`
- **IF…THEN** → `→`

This tool performs that translation **recursively**, standardizes inputs, and builds a symbol table for reference.

---

## ✅ Supported Logical Connectives
- `AND` (conjunction)
- `OR` (disjunction)
- `NOT` (negation)
- `IF...THEN` (implication)
- Also supports **comma-style** IF statements (e.g., `If X, Y`)

---

## 🌍 Real-World Benefits
- Prevents **misinterpretation in technical fields**
- Reduces **logic modeling errors**
- Makes policies, authentication rules, and network access conditions **clear and unambiguous**
- Helps confidently model access control, authentication logic, and system behavior

---

## 🚀 Features
- Automatic symbol assignment for unique propositions ✅
- Recursive logic parsing ✅
- Text normalization for consistent interpretation ✅
- Outputs a symbolic statement + legend ✅
- Runs offline ✅

---

## 🛠️ Built With
- Python
- Standard logical notation (`∧, ∨, ¬, →`)
- Git & GitHub  
  (referenced platform: GitHub)

---

## ⚙️ Installation & Usage

1. Clone the repository from GitHub
2. Run the script with Python:

```bash
python translator.py
