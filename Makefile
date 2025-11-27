# -------------------------------
# Interactive Makefile for Decision Tree Pipeline
# -------------------------------

# Variables
PYTHON = python3 
ENV_NAME = env
REQUIREMENTS = requirements.txt

# Quality Gate Thresholds (adjust as needed)
PYLINT_MIN_SCORE = 8.0
TEST_MIN_PASS = 0

# Colors and Icons
GREEN=\033[0;32m
RED=\033[0;31m
YELLOW=\033[1;33m
BLUE=\033[0;34m
PURPLE=\033[0;35m
CYAN=\033[0;36m
NC=\033[0m # No Color

# Icons
CHECK=✅
CROSS=❌
WARN=⚠️
ROCKET=🚀
ROBOT=🤖
SNAKE=🐍
TREE=🌳

.PHONY: all
all: setup ci data train evaluate visualize
	@echo "${GREEN}${CHECK} All pipeline steps completed successfully!${NC}"

# -------------------------------
# 🎯 INTERACTIVE MAIN MENU
# -------------------------------
.PHONY: interactive menu
interactive: menu

.PHONY: menu
menu:
	@echo ""
	@echo "${PURPLE}╔══════════════════════════════════════╗${NC}"
	@echo "${PURPLE}║         ${CYAN}DECISION TREE PIPELINE${PURPLE}         ║${NC}"
	@echo "${PURPLE}║              ${YELLOW}Interactive Menu${PURPLE}             ║${NC}"
	@echo "${PURPLE}╚══════════════════════════════════════╝${NC}"
	@echo ""
	@echo "${BLUE}1${NC}  ${CHECK}  Quick Setup Wizard"
	@echo "${BLUE}2${NC}  ${ROCKET}  Run Full Pipeline"
	@echo "${BLUE}3${NC}  ${TREE}  Data & Model Pipeline"
	@echo "${BLUE}4${NC}  🔒  Code Quality & Security"
	@echo "${BLUE}5${NC}  🧪  Testing Suite"
	@echo "${BLUE}6${NC}  📊  Visualization & Analysis"
	@echo "${BLUE}7${NC}  ⚙️   Individual Steps"
	@echo "${BLUE}8${NC}  🧹  Clean & Maintenance"
	@echo "${BLUE}9${NC}  📋  Project Status"
	@echo "${BLUE}0${NC}  🆘  Help & Documentation"
	@echo ""
	@printf "${YELLOW}Choose an option (0-9): ${NC}" && read choice && \
	case $$choice in \
		1) make wizard;; \
		2) make pipeline-wizard;; \
		3) make data-pipeline;; \
		4) make quality-suite;; \
		5) make test-suite;; \
		6) make visualization-suite;; \
		7) make individual-steps;; \
		8) make maintenance-menu;; \
		9) make status;; \
		0) make help;; \
		*) echo "${RED}${CROSS} Invalid option!${NC}"; make menu;; \
	esac

# -------------------------------
# 🧙 QUICK SETUP WIZARD
# -------------------------------
.PHONY: wizard
wizard:
	@echo ""
	@echo "${PURPLE}🧙 Quick Setup Wizard${NC}"
	@echo "${BLUE}=================================${NC}"
	@printf "${YELLOW}Create new virtual environment? [Y/n]: ${NC}" && read create_env
	@case $$create_env in \
		[nN]) ;; \
		*) make setup;; \
	esac
	@echo ""
	@printf "${YELLOW}Run code quality checks? [Y/n]: ${NC}" && read run_ci
	@case $$run_ci in \
		[nN]) ;; \
		*) make ci;; \
	esac
	@echo ""
	@printf "${YELLOW}Download and prepare data? [Y/n]: ${NC}" && read prep_data
	@case $$prep_data in \
		[nN]) ;; \
		*) make data;; \
	esac
	@echo ""
	@echo "${GREEN}${CHECK} Setup wizard completed!${NC}"
	@make status

# -------------------------------
# 🚀 PIPELINE WIZARD
# -------------------------------
.PHONY: pipeline-wizard
pipeline-wizard:
	@echo ""
	@echo "${PURPLE}${ROCKET} Pipeline Execution Wizard${NC}"
	@echo "${BLUE}=================================${NC}"
	@echo "${YELLOW}This will run the complete ML pipeline:${NC}"
	@echo "  • Environment setup"
	@echo "  • Code quality checks"
	@echo "  • Data preparation"
	@echo "  • Model training"
	@echo "  • Evaluation & Visualization"
	@echo ""
	@printf "${RED}Are you sure you want to continue? [y/N]: ${NC}" && read confirm
	@case $$confirm in \
		[yY]) make all;; \
		*) echo "${YELLOW}Pipeline cancelled${NC}"; make menu;; \
	esac

# -------------------------------
# 📊 DATA & MODEL PIPELINE MENU
# -------------------------------
.PHONY: data-pipeline
data-pipeline:
	@echo ""
	@echo "${PURPLE}${TREE} Data & Model Pipeline${NC}"
	@echo "${BLUE}=================================${NC}"
	@echo "${BLUE}1${NC} Prepare data only"
	@echo "${BLUE}2${NC} Train model only"
	@echo "${BLUE}3${NC} Evaluate model"
	@echo "${BLUE}4${NC} Visualize results"
	@echo "${BLUE}5${NC} Full data pipeline (prepare → train → evaluate → visualize)"
	@echo "${BLUE}6${NC} Back to main menu"
	@echo ""
	@printf "${YELLOW}Choose option (1-6): ${NC}" && read choice && \
	case $$choice in \
		1) make data;; \
		2) make train;; \
		3) make evaluate;; \
		4) make visualize;; \
		5) make data train evaluate visualize && echo "${GREEN}${CHECK} Data pipeline complete!${NC}";; \
		6) make menu;; \
		*) echo "${RED}Invalid option!${NC}"; make data-pipeline;; \
	esac

# -------------------------------
# 🔒 CODE QUALITY SUITE
# -------------------------------
.PHONY: quality-suite
quality-suite:
	@echo ""
	@echo "${PURPLE}🔒 Code Quality & Security Suite${NC}"
	@echo "${BLUE}=================================${NC}"
	@echo "${BLUE}1${NC} Run all quality checks"
	@echo "${BLUE}2${NC} Code formatting (Black)"
	@echo "${BLUE}3${NC} Code quality (Pylint)"
	@echo "${BLUE}4${NC} Security scan (Bandit)"
	@echo "${BLUE}5${NC} Auto-fix formatting"
	@echo "${BLUE}6${NC} Back to main menu"
	@echo ""
	@printf "${YELLOW}Choose option (1-6): ${NC}" && read choice && \
	case $$choice in \
		1) make ci;; \
		2) make code_format;; \
		3) make code_quality;; \
		4) make security_check;; \
		5) make lint-fix;; \
		6) make menu;; \
		*) echo "${RED}Invalid option!${NC}"; make quality-suite;; \
	esac

# -------------------------------
# 🧪 TESTING SUITE
# -------------------------------
.PHONY: test-suite
test-suite:
	@echo ""
	@echo "${PURPLE}🧪 Testing Suite${NC}"
	@echo "${BLUE}=================================${NC}"
	@echo "${BLUE}1${NC} Run all tests"
	@echo "${BLUE}2${NC} Run tests with coverage"
	@echo "${BLUE}3${NC} Run fast tests (fail fast)"
	@echo "${BLUE}4${NC} Back to main menu"
	@echo ""
	@printf "${YELLOW}Choose option (1-4): ${NC}" && read choice && \
	case $$choice in \
		1) make run_tests;; \
		2) make coverage-test;; \
		3) make fast-test;; \
		4) make menu;; \
		*) echo "${RED}Invalid option!${NC}"; make test-suite;; \
	esac

# -------------------------------
# 📊 VISUALIZATION SUITE
# -------------------------------
.PHONY: visualization-suite
visualization-suite:
	@echo ""
	@echo "${PURPLE}📊 Visualization & Analysis${NC}"
	@echo "${BLUE}=================================${NC}"
	@echo "${BLUE}1${NC} Visualize decision tree"
	@echo "${BLUE}2${NC} Start Jupyter notebook"
	@echo "${BLUE}3${NC} Generate model report"
	@echo "${BLUE}4${NC} Back to main menu"
	@echo ""
	@printf "${YELLOW}Choose option (1-4): ${NC}" && read choice && \
	case $$choice in \
		1) make visualize;; \
		2) make notebook;; \
		3) make report;; \
		4) make menu;; \
		*) echo "${RED}Invalid option!${NC}"; make visualization-suite;; \
	esac

# -------------------------------
# ⚙️ INDIVIDUAL STEPS MENU
# -------------------------------
.PHONY: individual-steps
individual-steps:
	@echo ""
	@echo "${PURPLE}⚙️ Individual Steps${NC}"
	@echo "${BLUE}=================================${NC}"
	@echo "${BLUE}1${NC} Setup environment"
	@echo "${BLUE}2${NC} Prepare data"
	@echo "${BLUE}3${NC} Train model"
	@echo "${BLUE}4${NC} Evaluate model"
	@echo "${BLUE}5${NC} Deploy model"
	@echo "${BLUE}6${NC} Back to main menu"
	@echo ""
	@printf "${YELLOW}Choose option (1-6): ${NC}" && read choice && \
	case $$choice in \
		1) make setup;; \
		2) make data;; \
		3) make train;; \
		4) make evaluate;; \
		5) make deploy;; \
		6) make menu;; \
		*) echo "${RED}Invalid option!${NC}"; make individual-steps;; \
	esac

# -------------------------------
# 🧹 MAINTENANCE MENU
# -------------------------------
.PHONY: maintenance-menu
maintenance-menu:
	@echo ""
	@echo "${PURPLE}🧹 Maintenance & Cleanup${NC}"
	@echo "${BLUE}=================================${NC}"
	@echo "${BLUE}1${NC} Quick clean"
	@echo "${BLUE}2${NC} Deep clean (remove env)"
	@echo "${BLUE}3${NC} Check disk usage"
	@echo "${BLUE}4${NC} Update dependencies"
	@echo "${BLUE}5${NC} Back to main menu"
	@echo ""
	@printf "${YELLOW}Choose option (1-5): ${NC}" && read choice && \
	case $$choice in \
		1) make clean;; \
		2) make deep-clean;; \
		3) make disk-usage;; \
		4) make update-deps;; \
		5) make menu;; \
		*) echo "${RED}Invalid option!${NC}"; make maintenance-menu;; \
	esac

# -------------------------------
# 📋 PROJECT STATUS DASHBOARD
# -------------------------------
.PHONY: status
status:
	@echo ""
	@echo "${PURPLE}📋 Project Status Dashboard${NC}"
	@echo "${BLUE}=================================${NC}"
	
	@# Check virtual environment
	@if [ -d "$(ENV_NAME)" ]; then \
		echo "${GREEN}${CHECK} Virtual Environment: Active ($(ENV_NAME))${NC}"; \
		$(ENV_NAME)/bin/python --version | xargs echo "   → "; \
	else \
		echo "${RED}${CROSS} Virtual Environment: Not found${NC}"; \
	fi
	
	@# Check requirements
	@if [ -f "$(REQUIREMENTS)" ]; then \
		echo "${GREEN}${CHECK} Requirements: Found ($(shell wc -l < $(REQUIREMENTS)) packages)${NC}"; \
	else \
		echo "${RED}${CROSS} Requirements: Missing${NC}"; \
	fi
	
	@# Check Python files
	@PY_FILES=$$(find . -name "*.py" -not -path "./$(ENV_NAME)/*" | wc -l); \
	echo "${BLUE}📝 Python Files: $$PY_FILES${NC}"
	
	@# Check for data directory
	@if [ -d "data" ]; then \
		echo "${GREEN}${CHECK} Data Directory: Present${NC}"; \
	else \
		echo "${YELLOW}${WARN} Data Directory: Missing${NC}"; \
	fi
	
	@# Last modification
	@echo "${BLUE}📅 Last Modified: $(shell find . -name "*.py" -type f -exec stat -c %y {} \; 2>/dev/null | sort -r | head -1 | cut -d' ' -f1)${NC}"
	@echo ""
	@printf "${YELLOW}Press Enter to continue...${NC}" && read

# -------------------------------
# 🆘 HELP & DOCUMENTATION
# -------------------------------
.PHONY: help
help:
	@echo ""
	@echo "${PURPLE}🆘 Decision Tree Pipeline Help${NC}"
	@echo "${BLUE}=================================${NC}"
	@echo "${GREEN}Quick Start:${NC}"
	@echo "  ${YELLOW}make interactive${NC} - Launch interactive menu"
	@echo "  ${YELLOW}make wizard${NC}     - Guided setup wizard"
	@echo "  ${YELLOW}make all${NC}        - Run complete pipeline"
	@echo ""
	@echo "${GREEN}Key Commands:${NC}"
	@echo "  ${YELLOW}make setup${NC}      - Create environment & install deps"
	@echo "  ${YELLOW}make ci${NC}         - Run all quality checks"
	@echo "  ${YELLOW}make data${NC}       - Prepare data"
	@echo "  ${YELLOW}make train${NC}      - Train model"
	@echo "  ${YELLOW}make evaluate${NC}   - Evaluate model"
	@echo "  ${YELLOW}make visualize${NC}  - Visualize decision tree"
	@echo ""
	@echo "${GREEN}Quality Assurance:${NC}"
	@echo "  ${YELLOW}make test${NC}       - Run tests"
	@echo "  ${YELLOW}make lint-fix${NC}   - Auto-format code"
	@echo "  ${YELLOW}make deploy${NC}     - Deployment ready check"
	@echo ""
	@printf "${YELLOW}Press Enter to return to menu...${NC}" && read
	@make menu

# -------------------------------
# NEW INTERACTIVE TARGETS
# -------------------------------

# Enhanced test targets
.PHONY: coverage-test
coverage-test:
	@echo "${BLUE}Running tests with coverage report...${NC}"
	@$(ENV_NAME)/bin/pytest --cov=main --cov-report=html --cov-report=term-missing -v
	@echo "${GREEN}Coverage report generated in htmlcov/${NC}"

.PHONY: fast-test
fast-test:
	@echo "${YELLOW}Running fast tests (fail on first error)...${NC}"
	@$(ENV_NAME)/bin/pytest --maxfail=1 -x

.PHONY: report
report:
	@echo "${BLUE}Generating model report...${NC}"
	@$(ENV_NAME)/bin/python main.py --report 2>/dev/null || echo "${YELLOW}Report generation not implemented${NC}"

# Enhanced clean targets
.PHONY: deep-clean
deep-clean:
	@echo "${RED}🧹 Deep cleaning...${NC}"
	@make clean
	@rm -rf $(ENV_NAME)
	@rm -rf .pytest_cache htmlcov .coverage
	@echo "${GREEN}${CHECK} Deep clean completed!${NC}"

.PHONY: disk-usage
disk-usage:
	@echo "${BLUE}📊 Disk Usage Analysis:${NC}"
	@du -sh $(ENV_NAME) 2>/dev/null || echo "No virtual environment"
	@du -sh data 2>/dev/null || echo "No data directory"
	@du -sh ./*.py | sort -hr

.PHONY: update-deps
update-deps:
	@echo "${BLUE}Updating dependencies...${NC}"
	@$(ENV_NAME)/bin/pip install --upgrade pip
	@$(ENV_NAME)/bin/pip freeze --local | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 $(ENV_NAME)/bin/pip install -U
	@echo "${GREEN}${CHECK} Dependencies updated!${NC}"

# -------------------------------
# ORIGINAL TARGETS (Enhanced with colors)
# -------------------------------

.PHONY: setup
setup:
	@echo "${BLUE}📦 Creating virtual environment and installing dependencies...${NC}"
	@$(PYTHON) -m venv $(ENV_NAME)
	@echo "${BLUE}⚡ Activating virtual environment and installing requirements...${NC}"
	@$(ENV_NAME)/bin/pip install --upgrade pip
	@$(ENV_NAME)/bin/pip install -r $(REQUIREMENTS)
	@echo "${GREEN}${CHECK} Environment setup completed!${NC}"

.PHONY: ci
ci: code_quality code_format security_check run_tests
	@echo "${GREEN}${CHECK} All CI checks passed! Quality gates satisfied.${NC}"

.PHONY: lint-fix
lint-fix:
	@echo "${BLUE}🛠 Running auto-formatting with Black...${NC}"
	@$(ENV_NAME)/bin/black *.py
	@echo "${GREEN}${CHECK} Code formatted with Black!${NC}"

.PHONY: code_quality
code_quality:
	@echo "${BLUE}📌 Running Pylint code quality check...${NC}"
	@echo "${YELLOW}Quality Gate: Minimum score $(PYLINT_MIN_SCORE)/10${NC}"
	@$(ENV_NAME)/bin/pylint *.py --fail-under=$(PYLINT_MIN_SCORE) || (echo "${RED}${CROSS} Pylint quality gate failed!${NC}"; exit 1)
	@echo "${GREEN}${CHECK} Code quality check passed!${NC}"

.PHONY: code_format
code_format:
	@echo "${BLUE}📌 Running Flake8 formatting check...${NC}"
	@$(ENV_NAME)/bin/flake8 *.py --count --max-complexity=10 --max-line-length=127 --statistics || (echo "${RED}${CROSS} Code formatting gate failed!${NC}"; exit 1)
	@echo "${GREEN}${CHECK} Code formatting check passed!${NC}"

.PHONY: security_check
security_check:
	@echo "${BLUE}🔒 Running Bandit security check only on main code...${NC}"
	@$(ENV_NAME)/bin/bandit main.py model_pipeline.py -f json --quiet \
		|| (echo "${RED}${CROSS} Security check failed!${NC}"; exit 1)
	@echo "${GREEN}${CHECK} Security check passed!${NC}"

.PHONY: run_tests
run_tests:
	@echo "${BLUE}🧪 Running pytest with quality gate...${NC}"
	@$(ENV_NAME)/bin/pytest --maxfail=$(TEST_MIN_PASS) --disable-warnings -v || (echo "${RED}${CROSS} Tests quality gate failed!${NC}"; exit 1)
	@echo "${GREEN}${CHECK} All tests passed!${NC}"

.PHONY: data
data: ci
	@echo "${BLUE}📁 Data preparation...${NC}"
	@$(ENV_NAME)/bin/python main.py --prepare

.PHONY: train
train: data
	@echo "${BLUE}${ROBOT} Model training...${NC}"
	@$(ENV_NAME)/bin/python main.py --train

.PHONY: evaluate
evaluate: train
	@echo "${BLUE}📊 Model evaluation...${NC}"
	@$(ENV_NAME)/bin/python main.py --evaluate

.PHONY: visualize
visualize: train
	@echo "${BLUE}${TREE} Visualizing Decision Tree...${NC}"
	@$(ENV_NAME)/bin/python main.py --visualize

.PHONY: test
test: run_tests

.PHONY: deploy
deploy: ci evaluate
	@echo "${BLUE}${ROCKET} Model deployment (placeholder)...${NC}"
	@echo "${GREEN}${CHECK} Deployment ready - all quality gates passed!${NC}"

.PHONY: notebook
notebook: setup
	@echo "${BLUE}📓 Starting Jupyter Notebook...${NC}"
	@$(ENV_NAME)/bin/jupyter notebook

.PHONY: clean
clean:
	@echo "${YELLOW}🧹 Cleaning up...${NC}"
	@rm -rf __pycache__ *.pyc .pytest_cache
	@echo "${GREEN}${CHECK} Clean completed!${NC}"

# Default target
.DEFAULT_GOAL := interactive