"""ASCII art handling for Terminal Fortune Cookie."""

import json
import random
from pathlib import Path
from rich.text import Text
from rich.align import Align

class AsciiArtEngine:
    """Handles ASCII art selection and formatting."""
    
    def __init__(self):
        self.data_dir = Path(__file__).parent / "data"
        self.ascii_art = self._load_ascii_art()
    
    def _load_ascii_art(self):
        """Load ASCII art from JSON file."""
        art_file = self.data_dir / "ascii_art.json"
        try:
            with open(art_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {"animals": [], "tech": [], "symbols": []}
    
    def get_random_art(self, category=None):
        """Get random ASCII art from specified category or all categories."""
        if category and category in self.ascii_art:
            art_items = self.ascii_art[category]
        else:
            # Combine all categories
            art_items = []
            for items in self.ascii_art.values():
                art_items.extend(items)
        
        if not art_items:
            return None
        
        return random.choice(art_items)
    
    def format_art(self, art_item, color="bright_white"):
        """Format ASCII art for rich display."""
        if not art_item or "art" not in art_item:
            return None
        
        # Create rich text for each line
        art_lines = []
        for line in art_item["art"]:
            art_lines.append(Text(line, style=color))
        
        # Join lines with newlines
        return Text("\n").join(art_lines)
    
    def get_art_with_message(self, message, art_category=None, art_color="bright_white"):
        """Combine ASCII art with a message."""
        art_item = self.get_random_art(art_category)
        
        if not art_item:
            return Text(message, style="bold bright_white")
        
        formatted_art = self.format_art(art_item, art_color)
        message_text = Text(f"\n{message}", style="bold bright_white")
        
        # Combine art and message
        return Text.assemble(formatted_art, message_text)