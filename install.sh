#!/bin/bash
# Installation script for Terminal Fortune Cookie

set -e

echo "🍪 Installing Terminal Fortune Cookie..."

# Install the package
pip install -e .

echo "✅ Package installed successfully!"
echo ""
echo "🔧 Setting up shell integration..."

# Function to add fortune-cookie to shell profile
add_to_shell_profile() {
    local shell_profile=$1
    local shell_name=$2
    
    if [[ -f "$shell_profile" ]]; then
        # Check if already added
        if ! grep -q "fortune-cookie" "$shell_profile"; then
            echo "" >> "$shell_profile"
            echo "# Terminal Fortune Cookie - delightful developer fortunes" >> "$shell_profile"
            echo "fortune-cookie" >> "$shell_profile"
            echo "✅ Added to $shell_name profile: $shell_profile"
        else
            echo "⚠️  Already configured in $shell_name profile: $shell_profile"
        fi
    else
        echo "📝 Creating $shell_name profile: $shell_profile"
        echo "# Terminal Fortune Cookie - delightful developer fortunes" > "$shell_profile"
        echo "fortune-cookie" >> "$shell_profile"
        echo "✅ Added to $shell_name profile: $shell_profile"
    fi
}

# Detect shell and add to appropriate profile
if [[ "$SHELL" == *"zsh"* ]]; then
    add_to_shell_profile "$HOME/.zshrc" "Zsh"
elif [[ "$SHELL" == *"bash"* ]]; then
    # Try .bash_profile first, then .bashrc
    if [[ -f "$HOME/.bash_profile" ]]; then
        add_to_shell_profile "$HOME/.bash_profile" "Bash"
    else
        add_to_shell_profile "$HOME/.bashrc" "Bash"
    fi
elif [[ "$SHELL" == *"fish"* ]]; then
    # For fish shell
    mkdir -p "$HOME/.config/fish"
    add_to_shell_profile "$HOME/.config/fish/config.fish" "Fish"
else
    echo "⚠️  Unknown shell: $SHELL"
    echo "📝 Please manually add 'fortune-cookie' to your shell profile"
fi

echo ""
echo "🎉 Installation complete!"
echo ""
echo "To start getting fortunes immediately, either:"
echo "  1. Open a new terminal window, or"
echo "  2. Run: source ~/.zshrc (or your shell's config file)"
echo ""
echo "🍪 Enjoy your delightful developer fortunes!"