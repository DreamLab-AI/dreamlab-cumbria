# Makefile for Business Documentation Suite
# Compiles all LaTeX documents with bibliography support

# LaTeX compiler settings
LATEX = xelatex
BIBER = biber
LATEXFLAGS = -interaction=nonstopmode -file-line-error

# Find all .tex files
TEXFILES = $(wildcard */*.tex)
PDFFILES = $(TEXFILES:.tex=.pdf)

# Main targets
.PHONY: all clean templates timeline pitch executive risk implementation bibliography test

all: templates timeline pitch executive risk implementation bibliography

templates:
	@echo "Building template documents..."
	cd templates && $(LATEX) $(LATEXFLAGS) template-example.tex
	cd templates && $(BIBER) template-example
	cd templates && $(LATEX) $(LATEXFLAGS) template-example.tex
	cd templates && $(LATEX) $(LATEXFLAGS) template-example.tex

timeline:
	@echo "Building timeline document..."
	cd timeline && $(LATEX) $(LATEXFLAGS) project-timeline.tex
	cd timeline && $(LATEX) $(LATEXFLAGS) project-timeline.tex

pitch:
	@echo "Building pitch deck..."
	cd pitch && $(LATEX) $(LATEXFLAGS) investor-pitch-deck.tex
	cd pitch && $(LATEX) $(LATEXFLAGS) investor-pitch-deck.tex

executive:
	@echo "Building executive summary..."
	cd executive && $(LATEX) $(LATEXFLAGS) executive-summary.tex
	cd executive && $(BIBER) executive-summary
	cd executive && $(LATEX) $(LATEXFLAGS) executive-summary.tex
	cd executive && $(LATEX) $(LATEXFLAGS) executive-summary.tex

risk:
	@echo "Building risk framework..."
	cd risk && $(LATEX) $(LATEXFLAGS) risk-management-framework.tex
	cd risk && $(LATEX) $(LATEXFLAGS) risk-management-framework.tex

implementation:
	@echo "Building implementation roadmap..."
	cd implementation && $(LATEX) $(LATEXFLAGS) implementation-roadmap.tex
	cd implementation && $(LATEX) $(LATEXFLAGS) implementation-roadmap.tex

bibliography:
	@echo "Building citation guide..."
	cd bibliography && $(LATEX) $(LATEXFLAGS) citation-guide.tex
	cd bibliography && $(BIBER) citation-guide
	cd bibliography && $(LATEX) $(LATEXFLAGS) citation-guide.tex
	cd bibliography && $(LATEX) $(LATEXFLAGS) citation-guide.tex

# Test compilation of a single document
test:
	@echo "Testing template compilation..."
	cd templates && $(LATEX) $(LATEXFLAGS) template-example.tex

# Clean auxiliary files
clean:
	@echo "Cleaning auxiliary files..."
	find . -name "*.aux" -type f -delete
	find . -name "*.log" -type f -delete
	find . -name "*.out" -type f -delete
	find . -name "*.toc" -type f -delete
	find . -name "*.lof" -type f -delete
	find . -name "*.lot" -type f -delete
	find . -name "*.bbl" -type f -delete
	find . -name "*.blg" -type f -delete
	find . -name "*.bcf" -type f -delete
	find . -name "*.run.xml" -type f -delete
	find . -name "*.nav" -type f -delete
	find . -name "*.snm" -type f -delete
	find . -name "*.vrb" -type f -delete
	find . -name "*.synctex.gz" -type f -delete

# Clean everything including PDFs
cleanall: clean
	@echo "Removing all PDF files..."
	find . -name "*.pdf" -type f -delete

# Install dependencies (for Ubuntu/Debian)
install-deps:
	@echo "Installing LaTeX dependencies..."
	sudo apt-get update
	sudo apt-get install -y texlive-full
	sudo apt-get install -y texlive-xetex
	sudo apt-get install -y texlive-fonts-extra
	sudo apt-get install -y biber

# Help
help:
	@echo "Business Documentation LaTeX Makefile"
	@echo ""
	@echo "Usage:"
	@echo "  make all          - Build all documents"
	@echo "  make templates    - Build template example"
	@echo "  make timeline     - Build project timeline"
	@echo "  make pitch        - Build investor pitch deck"
	@echo "  make executive    - Build executive summary"
	@echo "  make risk         - Build risk framework"
	@echo "  make implementation - Build implementation roadmap"
	@echo "  make bibliography - Build citation guide"
	@echo "  make test         - Test compilation"
	@echo "  make clean        - Remove auxiliary files"
	@echo "  make cleanall     - Remove all generated files"
	@echo "  make install-deps - Install LaTeX dependencies"
	@echo "  make help         - Show this help message"