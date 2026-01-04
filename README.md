# Projection-Induced Arrows as a Structural Constraint

**Author:** A. R. Wells  
**Affiliation:** Dual-Frame Research Group  
**License:** CC BY 4.0 (see LICENSE)  
**Contact:** No solicitation for correspondence or media contact. (Email is provided for attribution/archival purposes only.)  
**Paper email:** arwells.research@proton.me  

---

## What this repository contains

This repository hosts the LaTeX source for the paper:

**“Projection-Induced Arrows as a Structural Constraint”**

The paper presents a **constraint (no-go) theorem**: under **time-reversal symmetric admissible dynamics** and **boundary-symmetric operational reduction**, any arrow-like diagnostic in the reduced description must be **boundary-radial**—depending only on **unsigned separation** from a conditioning boundary, not on an intrinsic temporal orientation.

The contribution is **taxonomic and diagnostic**, not mechanistic: it classifies arrow explanations by the **locus of asymmetry** (dynamics / projection / boundary selection) and provides an operational **boundary-reflection test**.

---

## What this paper does **not** do

- It does **not** propose a mechanism for conditioning-boundary selection
- It does **not** claim to resolve the arrow-of-time problem
- It does **not** introduce new dynamics or domain-specific models
- It does **not** assert that all arrows are projection-induced (only those satisfying the theorem’s premises)

Boundary selection is treated as an **orthogonal explanatory axis**.

---

## Build

Requirements: `latexmk` with a standard LaTeX installation.

Build the PDF (authoritative master file):

    latexmk -pdf -interaction=nonstopmode -halt-on-error projection-boundary-arrow-constraint.tex

Clean build artifacts:

    latexmk -C

Optional: use the helper script (if you prefer):

    bash tools/build.sh

---

## Repository layout (actual)

- `projection-boundary-arrow-constraint.tex` — master LaTeX file (build this)
- `sections/` — one section per file
- `bib/references.bib` — bibliography
- `figures/` — figures directory
- `tools/` — helper scripts
- `notes/` — working notes / review logs (optional)

Build artifacts (`*.aux`, `*.bbl`, `*.log`, `*.pdf`, etc.) are currently present in-repo; you may wish to add them to `.gitignore` depending on your publication workflow.

---

## Status and release plan

- The paper currently builds as: `projection-boundary-arrow-constraint.pdf`
- Intended distribution: versioned releases via **Zenodo** (DOI per release)
- GitHub is the source archive and revision history; the DOI should be treated as the citable record

---

## How to cite

Once a Zenodo release exists, cite the corresponding DOI.

Recommended repo additions:
- `CITATION.cff`
- `LICENSE` (CC BY 4.0)
- `zenodo.json` (metadata for Zenodo/GitHub integration)

---

## Author / attribution policy

This work is an open scholarly release under **CC BY 4.0**.  
Reuse is permitted with attribution. No solicitation for correspondence or media contact.