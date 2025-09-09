"""Core fortune engine for selecting and formatting developer fortunes."""

import json
import random
import os
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import box
from .ascii_art import AsciiArtEngine

class FortuneEngine:
    """Handles fortune selection and display formatting."""
    
    def __init__(self):
        self.console = Console()
        self.data_dir = Path(__file__).parent / "data"
        self.fortunes = self._load_fortunes()
        self.ascii_engine = AsciiArtEngine()
    
    def _load_fortunes(self):
        """Load fortunes from JSON file."""
        fortune_file = self.data_dir / "fortunes.json"
        try:
            with open(fortune_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {"motivational": ["Keep coding! 💻"], "humor": ["Hello World! 🌍"], "wisdom": ["Code wisely! 🧠"]}
    
    def get_random_fortune(self, category=None):
        """Get a random fortune from specified category or all categories."""
        if category and category in self.fortunes:
            return random.choice(self.fortunes[category]), category
        
        # Select from all categories
        all_fortunes = []
        for cat, fortunes in self.fortunes.items():
            for fortune in fortunes:
                all_fortunes.append((fortune, cat))
        
        if not all_fortunes:
            return "Keep coding! 💻", "default"
        
        return random.choice(all_fortunes)
    
    def _get_category_color(self, category):
        """Get color scheme for different categories."""
        colors = {
            "motivational": "bright_green",
            "humor": "bright_yellow", 
            "wisdom": "bright_cyan",
            "default": "bright_magenta"
        }
        return colors.get(category, "bright_magenta")
    
    def _get_category_emoji(self, category):
        """Get emoji for different categories."""
        emojis = {
            "motivational": "✨",
            "humor": "😄",
            "wisdom": "🧠",
            "default": "🍪"
        }
        return emojis.get(category, "🍪")
    
    def _get_category_display_name(self, category):
        """Get cute display names for categories."""
        display_names = {
            "motivational": "Today's Coding Magic ✨",
            "humor": "Giggles & Bytes 😄",
            "wisdom": "Ancient Dev Wisdom 🧠",
            "default": "Sweet Surprises 🍪"
        }
        return display_names.get(category, "Sweet Surprises 🍪")
    
    def display_fortune(self, category=None, with_ascii=True):
        """Display a beautifully formatted fortune with optional ASCII art."""
        fortune, fortune_category = self.get_random_fortune(category)
        color = self._get_category_color(fortune_category)
        emoji = self._get_category_emoji(fortune_category)
        display_name = self._get_category_display_name(fortune_category)
        
        if with_ascii and random.choice([True, False, True]):  # 66% chance of ASCII art
            # Get ASCII art that matches the vibe
            art_category = self._get_art_category_for_fortune(fortune_category)
            art_item = self.ascii_engine.get_random_art(art_category)
            
            if art_item:
                # Format art
                formatted_art = self.ascii_engine.format_art(art_item, color)
                
                # Create combined content
                content = Text()
                content.append(formatted_art)
                content.append("\n\n")
                content.append(f"{emoji} {fortune}", style=f"bold {color}")
            else:
                content = Text(f"{emoji} {fortune}", style=f"bold {color}")
        else:
            content = Text(f"{emoji} {fortune}", style=f"bold {color}")
        
        # Create a beautiful panel
        panel = Panel(
            content,
            title=f"[bold bright_white]🍪 Fortune Cookie[/bold bright_white]",
            subtitle=f"[dim]{display_name}[/dim]",
            border_style=color,
            box=box.ROUNDED,
            padding=(1, 2)
        )
        
        # Add some spacing and display
        self.console.print()
        self.console.print(panel)
        self.console.print()
    
    def _get_art_category_for_fortune(self, fortune_category):
        """Map fortune categories to ASCII art categories."""
        mapping = {
            "motivational": "animals",
            "humor": "tech", 
            "wisdom": "symbols",
            "default": None
        }
        return mapping.get(fortune_category)
    
    def get_stats(self):
        """Get statistics about the fortune database."""
        total = sum(len(fortunes) for fortunes in self.fortunes.values())
        return {
            "total_fortunes": total,
            "categories": list(self.fortunes.keys()),
            "by_category": {cat: len(fortunes) for cat, fortunes in self.fortunes.items()}
        }