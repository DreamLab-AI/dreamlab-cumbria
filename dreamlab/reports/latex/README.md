# DreamLab AI Consulting Business Plan

This directory contains the complete LaTeX source for the DreamLab AI Consulting business plan, featuring a dual revenue model combining AI training facilities with sustainable holiday accommodation.

## Structure

```
dreamlab/
├── dreamlab-business.cls     # Custom LaTeX class with DreamLab branding
├── dreamlab-business-plan.tex # Main document
├── references.bib            # Bibliography
├── Makefile                  # Build automation
├── sections/                 # Document sections
│   ├── executive-summary.tex
│   ├── company-overview.tex
│   ├── market-opportunity.tex
│   ├── service-offerings.tex
│   ├── facility-description.tex
│   ├── business-model.tex
│   ├── financial-projections.tex
│   ├── risk-analysis.tex
│   ├── implementation-timeline.tex
│   ├── appendix-equipment.tex
│   ├── appendix-training-packages.tex
│   └── appendix-solar-analysis.tex
└── figures/                  # Images and diagrams (to be added)
```

## Building the Document

### Prerequisites
- XeLaTeX (for font support)
- Biber (for bibliography)
- Standard LaTeX packages

### Build Commands
```bash
# Full build with bibliography, glossary, and index
make

# Quick single-pass build
make quick

# Build and view PDF
make view

# Clean temporary files
make clean

# Remove all generated files
make cleanall
```

## Key Features

### Custom LaTeX Class
The `dreamlab-business.cls` file provides:
- DreamLab corporate colors (purple, blue, green, orange)
- Custom environments for training packages, solar ROI, etc.
- Dual revenue KPI displays
- Specialized commands for financial formatting

### Document Sections
1. **Executive Summary** - High-level overview with key metrics
2. **Company Overview** - Vision, mission, team, and structure
3. **Market Opportunity** - AI training market analysis
4. **Service Offerings** - Training programmes and holiday lets
5. **Facility Description** - Lab specs and accommodation features
6. **Business Model** - Dual revenue streams and pricing
7. **Financial Projections** - 5-year forecasts and ROI
8. **Risk Analysis** - Comprehensive risk assessment
9. **Implementation Timeline** - Phased development plan

### Appendices
- Detailed equipment specifications
- Complete training package curricula
- Solar investment analysis and ROI

## Customization

### Adding Images
Place images in the `figures/` directory and reference them:
```latex
\includegraphics[width=\textwidth]{figures/lab-layout.png}
```

### Modifying Colors
Edit the color definitions in `dreamlab-business.cls`:
```latex
\definecolor{dreamlab-purple}{RGB}{102,51,153}
```

### Financial Updates
Key financial commands:
```latex
\trainingrevenue{150000}  % Shows £150,000ᵀ
\lettingrevenue{45000}    % Shows £45,000ᴸ
\totalrevenue{195000}     % Shows £195,000ᵀᵒᵗᵃˡ
```

## Dependencies

The document uses several specialized packages:
- `pgfplots` - Financial charts and graphs
- `pgfgantt` - Gantt charts for timelines
- `tcolorbox` - Styled information boxes
- `tikz` - Diagrams and visualizations
- `siunitx` - Proper number formatting

## Notes

- The document is designed for A4 paper with UK English spelling
- All financial figures use UK pound sterling (£)
- Dates follow UK format (DD/MM/YYYY)
- The class file includes commands for both training and letting revenue streams

## Future Enhancements

- Add actual facility photos once available
- Include testimonials from pilot programmes
- Update financial projections with actual data
- Add QR codes for digital appendices
- Create executive summary standalone version