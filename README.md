# Inevitability of Projection-Induced Arrows  
## Projection-Induced Arrows as a Structural Constraint
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18143356.svg)](https://doi.org/10.5281/zenodo.18143356)

**Author:** A. R. Wells  
**Affiliation:** Dual-Frame Research Group  
**License:** CC BY 4.0 (see LICENSE)  
**Contact:** No solicitation for correspondence or media contact. (Email is provided for attribution/archival purposes only.)  
**Paper email:** arwells.research@proton.me  

---

## What this repository contains

This repository hosts the LaTeX source for the paper:

**“Inevitability of Projection-Induced Arrows: Arrow-Like Directedness as Boundary-Radial Fallout of Symmetric Admissible Dynamics”**

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

Build artifacts are not considered part of the scholarly record; the LaTeX source
and Zenodo DOI constitute the authoritative version.

---

## Status and release plan

- The paper currently builds as: `projection-boundary-arrow-constraint.pdf`
- Intended distribution: versioned releases via **Zenodo** (DOI per release)
- GitHub is the source archive and revision history; the DOI should be treated as the citable record

---

## How to cite

Cite the corresponding Zenodo DOI for the version used.

Recommended repo additions:
- `CITATION.cff`
- `LICENSE` (CC BY 4.0)
- `zenodo.json` (metadata for Zenodo/GitHub integration)

---

## Author / attribution policy

This work is an open scholarly release under **CC BY 4.0**.  
Reuse is permitted with attribution. No solicitation for correspondence or media contact.