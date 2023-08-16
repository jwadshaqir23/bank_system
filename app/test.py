# ANSI escape codes for text colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"  # Reset the color back to default

def print_colored_text(color, text):
    print(f"{color}{text}{RESET}")

# Example usage
print_colored_text(RED, "This is a red text.")
print_colored_text(GREEN, "This is a green text.")
print_colored_text(YELLOW, "This is a yellow text.")
print_colored_text(BLUE, "This is a blue text.")
