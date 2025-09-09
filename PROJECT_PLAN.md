# Terminal Fortune Cookie

A cute Python application that displays developer-friendly fortunes and ASCII art every time you open your terminal.

## Project Vision

Improve developer experience by providing encouraging, humorous, and motivational messages at terminal startup to set a positive tone for coding sessions.

## Core Features (MVP)

- **Random Fortune Display**: Developer-specific quotes, tips, and humor
- **ASCII Art Integration**: Cute animals and symbols with messages
- **Colorful Output**: Rich terminal formatting for visual appeal
- **Fast Execution**: <100ms startup time
- **Easy Installation**: Simple shell profile integration

## Content Categories

1. **Motivational Quotes**
   - "Code is poetry, debug with patience"
   - "Every expert was once a beginner"
   - "Great code comes from great debugging"

2. **Programming Humor**
   - "404: Motivation not found... just kidding, here it is!"
   - "Syntax errors are just the compiler's way of saying 'try again'"
   - "Coffee: the fuel of successful deployments"

3. **ASCII Art + Wisdom**
   - Cute animals (cats, penguins, owls) with dev tips
   - Simple symbols and decorations
   - Seasonal/contextual themes

4. **Daily Tips**
   - Code best practices
   - Git workflow reminders
   - Performance optimization hints

## Technical Architecture

### Tech Stack
- **Language**: Python 3.8+
- **Libraries**: 
  - `rich` - Beautiful terminal formatting and ASCII art
  - `click` - CLI framework (if needed for options)
  - `random` - Fortune selection
  - `json` - Fortune database storage

### Project Structure
```
terminal-fortune-cookie/
├── fortune_cookie/
│   ├── __init__.py
│   ├── main.py              # CLI entry point
│   ├── fortune_engine.py    # Core fortune logic
│   ├── ascii_art.py         # ASCII art handling
│   └── data/
│       ├── fortunes.json    # Fortune database
│       └── ascii_art.json   # ASCII art collection
├── setup.py                 # Package installation
├── requirements.txt         # Dependencies
├── README.md               # Usage instructions
└── PROJECT_PLAN.md         # This file
```

## Installation & Usage

### Installation
```bash
pip install terminal-fortune-cookie
```

### Shell Integration
Add to your `~/.bashrc`, `~/.zshrc`, or equivalent:
```bash
fortune-cookie
```

### Usage
```bash
# Basic usagess
fortune-cookie

# With options (future)
fortune-cookie --theme cute
fortune-cookie --category motivation
```

## Success Metrics

- Fast execution time (<100ms)
- Positive developer feedback
- Easy installation process
- Active community contributions (future)

## Development Timeline

- **Week 1**: Core functionality and basic fortune display
- **Week 2**: ASCII art and visual enhancements
- **Week 3**: Polish, installation, and documentation
- **Future**: Community features and advanced integrations