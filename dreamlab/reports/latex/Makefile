# Makefile for DreamLab Business Plan LaTeX Document - Version 3
# Includes house renovation and revenue comparison sections

# LaTeX compiler
LATEX = xelatex -interaction=nonstopmode
BIBER = biber
VIEWER = xdg-open

# Main document (v3 with integrated planning)
MAIN = dreamlab-business-plan-v3
CLASS = dreamlab-business.cls

# All tex files including new sections
TEX_FILES = $(MAIN).tex $(CLASS) \
	sections/executive-summary-final.tex \
	sections/company-overview.tex \
	sections/market-opportunity.tex \
	sections/revenue-model-comparison.tex \
	sections/service-offerings-updated.tex \
	sections/facility-description-updated.tex \
	sections/house-renovation-plan.tex \
	sections/business-model.tex \
	sections/financial-projections-integrated.tex \
	sections/implementation-timeline-updated.tex \
	sections/marketing-strategy.tex \
	sections/operations-plan.tex \
	sections/risk-analysis-updated.tex \
	sections/appendix-equipment.tex \
	sections/appendix-solar-analysis.tex \
	sections/appendix-training-packages.tex \
	sections/agentic-engineering-services.tex

# Build directory
BUILD_DIR = build

# Default target
all: $(MAIN).pdf

# Main compilation rule
$(MAIN).pdf: $(TEX_FILES) references.bib
	@echo "Building DreamLab Business Plan v3 with integrated renovations..."
	@mkdir -p $(BUILD_DIR)
	$(LATEX) -output-directory=$(BUILD_DIR) $(MAIN)
	cd $(BUILD_DIR) && makeindex $(MAIN).idx
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
	@rm -f dreamlab-business-plan-complete.pdf
	@rm -f dreamlab-business-plan-complete-v2.pdf

# Test compilation
test:
	@echo "Testing LaTeX installation..."
	@which $(LATEX) || (echo "Error: xelatex not found" && exit 1)
	@which $(BIBER) || (echo "Error: biber not found" && exit 1)
	@echo "All required tools found."

# Check for missing sections
check-sections:
	@echo "Checking for all required sections..."
	@for file in $(TEX_FILES); do \
		if [ ! -f $$file ]; then \
			echo "Warning: Missing file $$file"; \
		fi; \
	done
	@echo "Section check complete."

# Create any missing sections with placeholders
create-missing:
	@echo "Creating placeholder files for missing sections..."
	@mkdir -p sections
	@for file in $(TEX_FILES); do \
		if [ ! -f $$file ] && [ $$file != $(MAIN).tex ] && [ $$file != $(CLASS) ]; then \
			echo "\\section{Placeholder}" > $$file; \
			echo "Created placeholder: $$file"; \
		fi; \
	done

# Build all versions
all-versions: all
	@echo "Building previous versions for comparison..."
	@if [ -f dreamlab-business-plan-complete.tex ]; then \
		$(LATEX) -output-directory=$(BUILD_DIR) dreamlab-business-plan-complete; \
		mv $(BUILD_DIR)/dreamlab-business-plan-complete.pdf . 2>/dev/null || true; \
	fi
	@if [ -f dreamlab-business-plan-complete-v2.tex ]; then \
		$(LATEX) -output-directory=$(BUILD_DIR) dreamlab-business-plan-complete-v2; \
		mv $(BUILD_DIR)/dreamlab-business-plan-complete-v2.pdf . 2>/dev/null || true; \
	fi

# Help
help:
	@echo "DreamLab Business Plan LaTeX Build System v3"
	@echo "==========================================="
	@echo "Available targets:"
	@echo "  make              - Full build with bibliography"
	@echo "  make quick        - Quick build without bibliography"
	@echo "  make view         - Build and open PDF"
	@echo "  make clean        - Remove auxiliary files"
	@echo "  make cleanall     - Remove all generated files"
	@echo "  make test         - Test LaTeX installation"
	@echo "  make check-sections - Check for missing section files"
	@echo "  make create-missing - Create placeholder files"
	@echo "  make all-versions - Build all document versions"
	@echo "  make help         - Show this help message"

.PHONY: all quick view clean cleanall test check-sections create-missing all-versions help