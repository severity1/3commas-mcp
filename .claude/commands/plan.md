---
allowed-tools: TodoWrite, Read, Grep, LS, Bash
description: Generate comprehensive implementation plan for 3Commas MCP APIs with dynamic analysis
---

# 3Commas MCP Implementation Plan Generator

**API Target**: `$ARGUMENTS`

I'll analyze your API request and generate a complete implementation plan. Let me start by examining the project context and identifying the specific API.

## 🔍 Comprehensive Analysis & Validation

I'll perform complete project analysis including API validation to generate a solid, ready-to-execute plan.

### Step 1: API Identification & Mapping
**Analyzing**: `$ARGUMENTS`

I'll examine:
- MVP_GET_APIS.md for API priority, phase, and endpoint details
- API_REFERENCES.md for current implementation status and official API documentation
- TASKS.md for overall progress context and next logical steps

### Step 2: Script Validation & Parameter Discovery
I'll validate the API by:
- Checking available testing scripts (`ls scripts/`)
- Testing API endpoint: `python scripts/test_api.py <endpoint>` with realistic parameters
- Documenting actual response structure and field names
- Extracting exact parameter names from API response (not documentation)
- Verifying token count < 25,000 for MCP efficiency

### Step 3: Implementation Pattern Analysis
I'll identify:
- Best reference implementation to copy patterns from (with line numbers)
- Required model and tool file locations
- Server registration requirements
- Documentation update paths and cross-references

### Step 4: Progress Impact Assessment
I'll calculate:
- Current phase progress and completion percentages
- Impact of this implementation on overall MVP progress
- Next recommended APIs after completion
- Dependencies and prerequisites

---

## 📋 2-Phase Implementation Plan

Based on validated analysis, memory system principles from CLAUDE.md, and patterns from @docs/PATTERNS.md:

### ⚙️ Phase 1: Implementation
**🎯 GOAL**: Implement API using script-validated parameters and established patterns

**Required Steps (Reference @docs/PATTERNS.md for HOW):**
1. **📋 TodoWrite Setup**: Create todos for both implementation phases
2. **🏗️ Pydantic Model** (`models/{domain}.py`) - Use ONLY analysis-validated parameters
3. **🔧 Tool Function** (`tools/{domain}.py`) - Follow @docs/PATTERNS.md exactly
4. **📋 Tool Registration** (`server.py`) - Add `mcp.tool()(domain.function_name)`
5. **✅ Quality Assurance** - All checks: `uv run -m black . && uv run -m ruff format . && uv run -m ruff check . && uv run -m mypy .`

**✅ Phase 1 Completion Checklist:**
- [ ] TodoWrite tool used to create phase tracking todos
- [ ] Pydantic model created using ONLY analysis-validated parameter names
- [ ] Tool function implemented following @docs/PATTERNS.md exactly
- [ ] Function registered in server.py
- [ ] All quality checks pass (black, ruff format, ruff check, mypy)
- [ ] MCP server loads without errors (test with import)
- [ ] Mark Phase 1 todo as completed in TodoWrite

**🛑 CHECKPOINT**: Complete ALL Phase 1 before Phase 2

### 📚 Phase 2: Documentation
**🎯 GOAL**: Complete all documentations

**Required Steps (ALL documentation layers mandatory):**
1. **📝 Mark Phase 2 in progress** in TodoWrite
2. **📊 Status Updates**: TASKS.md, docs/API_REFERENCES.md (⏸️ → ✅)
3. **📖 Tool Documentation**: `docs/tools/{domain}.md`
4. **🏗️ Model Documentation**: `docs/models/{domain}.md`
5. **💬 Conversation Examples**: `docs/conversations/{domain}-conversation.md`
6. **📄 Project Documentation**: `README.md`
7. **📐 Patterns**: Update `docs/PATTERNS.md` if new pattern is identified.
8. **🔄 Cross-References**: Ensure all documentation layers reference each other

**✅ Phase 2 Completion Checklist:**
- [ ] Phase 2 marked as in_progress in TodoWrite
- [ ] TASKS.md progress updated (increment counters, mark ✅)
- [ ] docs/API_REFERENCES.md status changed (⏸️ → ✅)
- [ ] Tool documentation created/updated in docs/tools/{domain}.md
- [ ] Model documentation created/updated in docs/models/{domain}.md
- [ ] Conversation examples created/updated in docs/conversations/{domain}-conversation.md
- [ ] Project documentation updated in README.md
- [ ] Patterns updated in docs/PATTERNS.md
- [ ] Cross-references verified between all documentation layers
- [ ] Mark Phase 2 todo as completed in TodoWrite

**✅ FINAL CHECKPOINT**: API implementation complete when ALL boxes checked

## Success Criteria

### Requirements (Non-Negotiable)
- **Trading Safety**: Validate operations before execution
- **Pattern Compliance**: Follow @docs/PATTERNS.md exactly for implementation details
- **Privacy**: Use dummy data only (bot ID 12345678, $245.67 profit)
- **Analysis Validation**: APIs validated during analysis phase before plan generation

### Common Violations to Avoid
- Using documentation parameters instead of analysis-validated ones
- Implementing before thorough analysis validation
- Missing TodoWrite phase tracking
- Implementing without following @docs/PATTERNS.md
- Incomplete documentation (missing any of the 4 layers)

---

## Implementation Execution

Now I'll perform the dynamic analysis and generate your specific implementation plan:

### 🔍 Analysis Results
*I'll examine the project files and provide:*
- **API Mapping**: Exact priority, phase, and endpoint details
- **Current Status**: Implementation progress and next logical steps  
- **Pattern Reference**: Best existing implementation to copy from
- **File Locations**: Specific paths for models, tools, and documentation
- **Test Commands**: Exact scripts and parameters for validation
- **Progress Impact**: How this implementation affects overall project progress

### 📋 Your Specific Implementation Plan
*Generated after analysis with:*
- **Realistic Test Commands**: Using actual project scripts and valid parameters
- **Specific File Paths**: Exact locations for all required changes
- **Pattern References**: Copy-paste-modify approach with line number references
- **Progress Tracking**: Updated counters and completion percentages
- **Next Steps**: Recommended follow-up APIs after completion

Let me begin the analysis...