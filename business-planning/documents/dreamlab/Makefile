# Makefile for DreamLab Business Plan LaTeX Document

# LaTeX compiler
LATEX = xelatex
BIBER = biber
VIEWER = xdg-open

# Main document
MAIN = dreamlab-business-plan-complete
CLASS = dreamlab-business.cls

# All tex files
TEX_FILES = $(MAIN).tex $(CLASS)

# Build directory
BUILD_DIR = build

# Default target
all: $(MAIN).pdf

# Main compilation rule
$(MAIN).pdf: $(TEX_FILES) references.bib
	@echo "Building DreamLab Business Plan..."
	@mkdir -p $(BUILD_DIR)
	$(LATEX) -output-directory=$(BUILD_DIR) $(MAIN)
	cd $(BUILD_DIR) && $(BIBER) $(MAIN)
	$(LATEX) -output-directory=$(BUILD_DIR) $(MAIN)
	$(LATEX) -output-directory=$(BUILD_DIR) $(MAIN)
	@mv $(BUILD_DIR)/$(MAIN).pdf .
	@echo "Build complete: $(MAIN).pdf"

# Quick build without bibliography
quick: $(TEX_FILES)
	@echo "Quick build (no bibliography)..."
	@mkdir -p $(BUILD_DIR)
	$(LATEX) -output-directory=$(BUILD_DIR) $(MAIN)
	@mv $(BUILD_DIR)/$(MAIN).pdf .

# View the PDF
view: $(MAIN).pdf
	$(VIEWER) $(MAIN).pdf &

# Clean auxiliary files
clean:
	@echo "Cleaning auxiliary files..."
	@rm -rf $(BUILD_DIR)
	@rm -f *.aux *.bbl *.bcf *.blg *.log *.out *.run.xml *.toc *.lof *.lot

# Clean all including PDF
cleanall: clean
	@echo "Removing PDF..."
	@rm -f $(MAIN).pdf

# Test compilation
test:
	@echo "Testing LaTeX installation..."
	@which $(LATEX) || (echo "Error: xelatex not found" && exit 1)
	@which $(BIBER) || (echo "Error: biber not found" && exit 1)
	@echo "All required tools found."

# Help
help:
	@echo "DreamLab Business Plan LaTeX Build System"
	@echo "========================================"
	@echo "Available targets:"
	@echo "  make          - Full build with bibliography"
	@echo "  make quick    - Quick build without bibliography"
	@echo "  make view     - Build and open PDF"
	@echo "  make clean    - Remove auxiliary files"
	@echo "  make cleanall - Remove all generated files"
	@echo "  make test     - Test LaTeX installation"
	@echo "  make help     - Show this help message"

.PHONY: all quick view clean cleanall test help