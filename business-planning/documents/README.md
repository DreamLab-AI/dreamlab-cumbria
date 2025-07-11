# Business Documentation LaTeX Suite

## Overview

This directory contains a comprehensive LaTeX documentation suite for the Business Excellence Initiative. All documents follow consistent styling, use UK English spelling, and are designed for professional business documentation.

## Directory Structure

```
documents/
├── templates/          # Master LaTeX class and examples
├── timeline/          # Project timeline with Gantt charts
├── pitch/             # Investor pitch deck (beamer)
├── executive/         # Executive summary document
├── risk/              # Risk management framework
├── implementation/    # Implementation roadmap
├── bibliography/      # Bibliography and citation resources
└── Makefile          # Build automation
```

## Key Features

### Master LaTeX Class (`businessdocs.cls`)

- Consistent corporate styling across all documents
- Predefined colour scheme matching brand identity
- Custom environments for key points, risks, and opportunities
- Financial formatting commands for UK/EU/US currencies
- Integrated TikZ/PGF support for professional diagrams
- Bibliography management with biblatex
- Cross-referencing support with cleveref

### Document Types

1. **Template Example** - Demonstrates all features of the custom class
2. **Project Timeline** - Comprehensive Gantt charts and milestone tracking
3. **Investor Pitch Deck** - Professional beamer presentation
4. **Executive Summary** - Complete business overview with links to all sections
5. **Risk Management Framework** - ISO 31000-based risk assessment
6. **Implementation Roadmap** - Detailed execution plan with milestones
7. **Citation Guide** - How to use the bibliography system

## Building Documents

### Prerequisites

- XeLaTeX (for font support)
- Biber (for bibliography)
- Full TeXLive installation recommended

### Quick Build

```bash
# Build all documents
make all

# Build specific document
make executive
make pitch

# Clean auxiliary files
make clean

# Remove all generated files
make cleanall
```

### Manual Compilation

For documents with bibliography:
```bash
xelatex document.tex
biber document
xelatex document.tex
xelatex document.tex
```

For documents without bibliography:
```bash
xelatex document.tex
xelatex document.tex
```

## Usage Guidelines

### Creating New Documents

1. Start with this template:
```latex
\documentclass{businessdocs}

\title{Document Title}
\author{Author Name}
\date{\today}

\addbibresource{../bibliography/references.bib}  % If using citations

\begin{document}

\maketitle
\tableofcontents
\newpage

\section{Introduction}
Your content here...

\printbibliography  % If using citations

\end{document}
```

2. Place in appropriate subdirectory
3. Update Makefile if needed

### Custom Commands

Financial formatting:
- `\pounds{1000000}` → £1,000,000
- `\euros{500000}` → €500,000
- `\dollars{750000}` → $750,000

Key performance indicators:
- `\kpi{Metric}{Value}{Description}`

Milestone markers:
- `\milestone{x}{y}{label}`

### Custom Environments

```latex
\begin{keypoint}
Important information highlighted in blue
\end{keypoint}

\begin{riskbox}
Risk assessment highlighted in red
\end{riskbox}

\begin{opportunitybox}
Opportunity highlighted in green
\end{opportunitybox}

\begin{executivesummary}
Executive summary with special formatting
\end{executivesummary}
```

## Style Guidelines

1. **UK English**: Use British spelling throughout
2. **Dates**: Format as DD/MM/YYYY
3. **Numbers**: Use comma separators for thousands
4. **Currency**: Default to GBP (£) unless specified
5. **Capitalisation**: Use title case for headings
6. **References**: Use author-year citation style

## Troubleshooting

### Common Issues

1. **Missing fonts**: Install TeX Gyre fonts or use default Computer Modern
2. **Bibliography errors**: Ensure biber is installed and run after first compilation
3. **Package conflicts**: Use full TeXLive distribution for best compatibility
4. **Compilation errors**: Check log files in each directory

### Font Issues

If TeX Gyre fonts are not available, comment out font commands in `businessdocs.cls`:
```latex
% \setmainfont{TeX Gyre Termes}
% \setsansfont{TeX Gyre Heros}
% \setmonofont{TeX Gyre Cursor}
```

## Corporate Branding

### Colour Palette

- Corporate Blue: RGB(0,48,87)
- Corporate Light Blue: RGB(70,130,180)
- Corporate Grey: RGB(128,128,128)
- Accent Green: RGB(46,125,50)
- Accent Orange: RGB(255,152,0)
- Accent Red: RGB(198,40,40)

### Typography

- Main text: Serif (TeX Gyre Termes / Times)
- Headings: Sans-serif (TeX Gyre Heros / Helvetica)
- Code: Monospace (TeX Gyre Cursor / Courier)

## Contributing

When adding new documents:
1. Follow existing naming conventions
2. Use the master class for consistency
3. Add bibliography entries to `references.bib`
4. Update this README
5. Add build target to Makefile

## Support

For LaTeX-specific questions, consult:
- [LaTeX Stack Exchange](https://tex.stackexchange.com/)
- [CTAN Documentation](https://ctan.org/)
- Internal documentation team

## Version History

- v1.0 (2024-01-01): Initial release with all core documents
- Master class version: 2024/01/01

---

*This documentation suite is proprietary to TechVenture Ltd and should not be distributed without authorisation.*