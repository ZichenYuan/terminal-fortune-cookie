# Terminal Fortune Cookie 🍪

Delightful developer fortunes and ASCII art that appear every time you open your terminal! Brighten your coding sessions with motivational quotes, programming humor, and cute ASCII art.

## ✨ Features

- **🎭 Developer-focused fortunes** - Motivational quotes, programming humor, and coding wisdom
- **🎨 Beautiful ASCII art** - Cute animals, tech symbols, and decorative elements
- **🌈 Colorful terminal output** - Rich formatting that makes your terminal pop
- **⚡ Lightning fast** - < 100ms execution time, won't slow down your terminal startup
- **🔧 Easy installation** - One command setup with automatic shell integration

## 🖼️ Preview

```
╭───────────────────────────── 🍪 Fortune Cookie ──────────────────────────────╮
│                                                                              │
│     /\_/\                                                                    │
│    ( ^.^ )                                                                   │
│   o_(")(")                                                                   │
│                                                                              │
│  ✨ Every 'Hello World' was once someone's first step to greatness 👶        │
│                                                                              │
╰──────────────────────────────── Motivational ────────────────────────────────╯
```

## 🚀 Quick Install

### Option 1: Automatic Installation (Recommended)
```bash
git clone https://github.com/yourusername/terminal-fortune-cookie.git
cd terminal-fortune-cookie
chmod +x install.sh
./install.sh
```

### Option 2: Manual Installation
```bash
# 1. Install the package
git clone https://github.com/yourusername/terminal-fortune-cookie.git
cd terminal-fortune-cookie
pip install -e .

# 2. Add to your shell profile
echo "fortune-cookie" >> ~/.zshrc    # For Zsh
echo "fortune-cookie" >> ~/.bashrc   # For Bash
```

## 📖 Usage

### Basic Usage
```bash
fortune-cookie                    # Random fortune from any category
```

### Category-Specific Fortunes
```bash
fortune-cookie -c motivational   # Motivational quotes only
fortune-cookie -c humor          # Programming humor only
fortune-cookie -c wisdom         # Coding wisdom only
```

### Other Options
```bash
fortune-cookie --stats           # Show fortune database statistics
fortune-cookie --help           # Show help message
fortune-cookie --version        # Show version info
```

## 🎨 Fortune Categories

### 🌟 Motivational
Uplifting quotes to keep you coding with confidence and joy.

### 😄 Humor  
Programming jokes and witty observations about the developer life.

### 🧠 Wisdom
Practical coding advice and philosophical insights about software development.

## 🎭 ASCII Art Themes

- **🐱 Animals** - Cats, dogs, owls, penguins, and ducks
- **💻 Tech** - Computers, coffee mugs, bugs, and rockets  
- **✨ Symbols** - Stars, hearts, and geometric patterns

## 🛠️ Requirements

- Python 3.8+
- Terminal with color support (most modern terminals)

## 📦 Dependencies

- `rich` - For beautiful terminal formatting
- `colorama` - For cross-platform color support

## 🔧 Configuration

### Disable for Specific Sessions
If you need to temporarily disable fortunes:
```bash
# Comment out or remove this line from your shell profile:
# fortune-cookie
```

### Custom Installation Path
```bash
# Install to a specific location
pip install -e . --target /your/custom/path
```

## 🎯 Shell Compatibility

✅ **Zsh** (macOS default, Oh My Zsh)  
✅ **Bash** (Linux default, macOS)  
✅ **Fish** (Modern shell)  
✅ **PowerShell** (Windows)  
⚠️ Other shells may require manual configuration

## 📊 Statistics

Run `fortune-cookie --stats` to see your fortune database info:

```
🍪 Fortune Cookie Database Stats:
   Total Fortunes: 45
   Categories: motivational, humor, wisdom
   Motivational: 15 fortunes
   Humor: 15 fortunes
   Wisdom: 15 fortunes
```

## 🔄 Uninstall

To remove Terminal Fortune Cookie:

```bash
# 1. Remove from shell profile
# Edit ~/.zshrc or ~/.bashrc and remove the "fortune-cookie" line

# 2. Uninstall package
pip uninstall terminal-fortune-cookie
```

## 🤝 Contributing

We'd love your help making Terminal Fortune Cookie even more delightful!

### Adding New Fortunes
1. Edit `fortune_cookie/data/fortunes.json`
2. Add your fortune to the appropriate category
3. Test with `fortune-cookie -c [category]`

### Adding ASCII Art
1. Edit `fortune_cookie/data/ascii_art.json`
2. Add your art to the appropriate category
3. Test the display

### Development Setup
```bash
git clone https://github.com/yourusername/terminal-fortune-cookie.git
cd terminal-fortune-cookie
pip install -e .[dev]  # If you add dev dependencies
```

## 📝 License

MIT License - feel free to use, modify, and distribute!

## 🎉 Credits

Inspired by the classic Unix `fortune` command, but with a modern developer twist and delightful ASCII art.

---

**Made with 💝 by developers, for developers**

*Start every coding session with a smile! 😊*