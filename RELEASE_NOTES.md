# Release Notes v0.2.0

**Release Date**: August 23, 2025  
**Branch**: `feature/p3.2`  

## What Changed

### 🔧 Dynamic Validation System
- **Enhanced `validate_endpoint.py`**: Automatically fetches account IDs and bot IDs from API instead of using hardcoded values
- **Zero Hardcoded Test Data**: Complete elimination of hardcoded account/bot IDs for cross-account compatibility
- **Fixed Market Pairs Endpoint**: Corrected path from `ver1/market_pairs` to `ver1/accounts/market_pairs`

### 📚 Documentation Updates  
- **KISS & DRY Principles**: Updated core development principles focusing on simplicity
- **Claude Memory System**: Enhanced `.claude/` commands for better AI context management
- **Plan Command**: Added `/plan` slash command for systematic implementation workflow

### 🛠️ Development Improvements
- **Parameter Validation**: Enhanced request validation in scripts
- **Testing Scripts**: Updated `test_api.py` for better cross-account compatibility  
- **Code Cleanup**: General cleanup and consistency improvements across scripts

## Files Modified
- `scripts/validate_endpoint.py` - Major rewrite for dynamic ID fetching
- `scripts/test_api.py` - Updated for better parameter handling
- `CLAUDE.md` - Updated core principles and workflow guidance
- `.claude/commands/` - Enhanced memory optimization and plan commands