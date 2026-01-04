#!/usr/bin/env bash
set -euo pipefail

latexmk -pdf -interaction=nonstopmode -halt-on-error projection-boundary-arrow-constraint.tex