#!/usr/bin/env python3
"""Main CLI entry point for Terminal Fortune Cookie."""

import sys
import argparse
from .fortune_engine import FortuneEngine

def main():
    """Main CLI function."""
    parser = argparse.ArgumentParser(
        description="Display delightful developer fortunes in your terminal! 🍪",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  fortune-cookie                    # Random fortune from any category
  fortune-cookie -c motivational   # Motivational fortune only
  fortune-cookie -c humor          # Funny fortune only
  fortune-cookie -c wisdom         # Wisdom fortune only
  fortune-cookie --stats           # Show fortune database stats
        """
    )
    
    parser.add_argument(
        "-c", "--category",
        choices=["motivational", "humor", "wisdom"],
        help="Choose fortune category"
    )
    
    parser.add_argument(
        "--stats",
        action="store_true",
        help="Show fortune database statistics"
    )
    
    parser.add_argument(
        "--version",
        action="version",
        version="Terminal Fortune Cookie 0.1.0 🍪"
    )
    
    args = parser.parse_args()
    
    try:
        engine = FortuneEngine()
        
        if args.stats:
            stats = engine.get_stats()
            print(f"\n🍪 Fortune Cookie Database Stats:")
            print(f"   Total Fortunes: {stats['total_fortunes']}")
            print(f"   Categories: {', '.join(stats['categories'])}")
            for category, count in stats['by_category'].items():
                print(f"   {category.title()}: {count} fortunes")
            print()
        else:
            engine.display_fortune(args.category)
            
    except KeyboardInterrupt:
        print("\n👋 Thanks for using Fortune Cookie!")
        sys.exit(0)
    except Exception as e:
        print(f"🐛 Oops! Something went wrong: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()