# Contributing to PromptChan API Skill

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## 🎯 How to Contribute

### Reporting Bugs

Before creating bug reports, please check existing issues. When creating a bug report, include:

- **Clear title and description**
- **Steps to reproduce** the behavior
- **Expected vs actual behavior**
- **Screenshots** if applicable
- **Environment details** (OS, Python version, etc.)

**Example:**
```markdown
**Bug**: Script fails with HTTP 401 error

**Steps to Reproduce:**
1. Run `python scripts/promptchan_generate.py --prompt "test" --api-key "xxx"`
2. See error

**Expected:** Image generated successfully
**Actual:** HTTP 401 Unauthorized error

**Environment:**
- OS: Windows 11
- Python: 3.11.5
```

### Suggesting Features

Feature suggestions are welcome! Please provide:

- **Use case**: Why is this feature needed?
- **Proposed solution**: How should it work?
- **Alternatives considered**: Other approaches you've thought about

### Pull Requests

1. **Fork** the repository
2. **Create a branch** from `main`:
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make your changes**
4. **Test** your changes thoroughly
5. **Commit** with clear messages:
   ```bash
   git commit -m "feat: add new style option"
   ```
6. **Push** to your branch:
   ```bash
   git push origin feature/amazing-feature
   ```
7. **Open a Pull Request**

## 📋 Code Style

### Python Style

- Follow [PEP 8](https://pep8.org/) style guide
- Use type hints where appropriate
- Add docstrings to functions and classes
- Keep functions focused and small

**Example:**
```python
def generate_image(
    api_key: str,
    prompt: str,
    style: str = "Cinematic"
) -> dict:
    """
    Generate an image using PromptChan API.
    
    Args:
        api_key: PromptChan API key
        prompt: Text prompt for image generation
        style: Art style (default: "Cinematic")
    
    Returns:
        dict: API response containing image data
    """
    # Implementation
```

### Documentation

- Update README.md for user-facing changes
- Update SKILL.md for technical details
- Keep all language versions (EN/ZH/JA) in sync
- Use clear, concise language

## 🧪 Testing

Before submitting a PR:

1. **Test all scripts** with valid API key
2. **Verify error handling** works correctly
3. **Check documentation** links and examples
4. **Test on multiple platforms** if possible (Windows, macOS, Linux)

## 📝 Commit Message Convention

We follow a simplified conventional commits format:

- `feat:` - New features
- `fix:` - Bug fixes
- `docs:` - Documentation changes
- `style:` - Code style changes (formatting, etc.)
- `refactor:` - Code refactoring
- `test:` - Test additions/changes
- `chore:` - Maintenance tasks

**Examples:**
```
feat: add new anime style option
fix: handle timeout errors correctly
docs: update Japanese README
refactor: simplify API request logic
```

## 🌍 Translations

We support multiple languages:

- `README.md` - English (default)
- `README_zh.md` - Chinese (简体中文)
- `README_ja.md` - Japanese (日本語)

When adding new features:

1. Update **all language versions**
2. Mark PR with `translations` label
3. Ensure consistency across versions

## 🚀 Release Process

Releases are managed by maintainers:

1. Version bump in `_meta.json`
2. Update changelog
3. Create GitHub release
4. Tag commit with version

## 📞 Getting Help

- **Discord**: [Join our server](https://discord.gg/promptchan)
- **Email**: support@promptchan.com
- **Issues**: [GitHub Issues](https://github.com/promptchan/api/issues)

## 🎖️ Recognition

Contributors will be recognized in:

- CONTRIBUTORS.md file
- Release notes
- Project README

---

Thank you for contributing to PromptChan API Skill! 🎉
