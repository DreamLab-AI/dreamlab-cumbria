#!/bin/bash
# DreamLab LaTeX Document Compilation Script
# Usage: ./compile.sh document-name (without .tex extension)
# Example: ./compile.sh business-strategy-overview

if [ $# -eq 0 ]; then
    echo "Usage: $0 document-name (without .tex extension)"
    echo "Example: $0 business-strategy-overview"
    echo ""
    echo "Available documents:"
    echo "  - business-strategy-overview"
    echo "  - strategic-roadmap"
    echo "  - governance-structure"
    exit 1
fi

DOCUMENT=$1

# Check if the tex file exists
if [ ! -f "${DOCUMENT}.tex" ]; then
    echo "Error: ${DOCUMENT}.tex not found!"
    exit 1
fi

echo "Compiling ${DOCUMENT}.tex..."
echo "============================="

# First pass
echo "Pass 1: Initial compilation..."
pdflatex -interaction=nonstopmode "${DOCUMENT}.tex" > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "Error in initial compilation. Running again to see errors..."
    pdflatex "${DOCUMENT}.tex"
    exit 1
fi

# Bibliography
if [ -f "references.bib" ]; then
    echo "Pass 2: Processing bibliography..."
    biber "${DOCUMENT}" > /dev/null 2>&1
fi

# Glossary
echo "Pass 3: Processing glossary..."
makeglossaries "${DOCUMENT}" > /dev/null 2>&1

# Second pass
echo "Pass 4: Intermediate compilation..."
pdflatex -interaction=nonstopmode "${DOCUMENT}.tex" > /dev/null 2>&1

# Final pass
echo "Pass 5: Final compilation..."
pdflatex -interaction=nonstopmode "${DOCUMENT}.tex" > /dev/null 2>&1

# Check if PDF was created successfully
if [ -f "${DOCUMENT}.pdf" ]; then
    echo ""
    echo "✅ Success! ${DOCUMENT}.pdf has been created."
    echo ""
    # Show file size
    ls -lh "${DOCUMENT}.pdf" | awk '{print "📄 File size: " $5}'
    
    # Clean up auxiliary files (optional)
    echo ""
    read -p "Clean up auxiliary files? (y/n) " -n 1 -r
    echo ""
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        rm -f *.aux *.log *.out *.toc *.lof *.lot *.bbl *.blg *.bcf *.run.xml *.glo *.gls *.glg *.acn *.acr *.alg
        echo "✨ Auxiliary files cleaned up."
    fi
else
    echo ""
    echo "❌ Error: PDF creation failed. Check the log file for details."
    echo "Run 'pdflatex ${DOCUMENT}.tex' manually to see detailed errors."
    exit 1
fi