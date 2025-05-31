import re

# Check password strength and return score + suggestions
def check_password_strength(password):
    score = 0
    suggestions = []

    # ✅ Check against common passwords list
    try:
        with open("common_passwords.txt", "r") as f:
            common_passwords = f.read().splitlines()
        if password.lower() in common_passwords:
            suggestions.append("⚠️ This password is too common! Choose something more unique.")
            score = 20  # Force low score for common password
            return score, suggestions
    except FileNotFoundError:
        suggestions.append("⚠️ Common password file not found. Skipping blacklist check.")

    # ✅ Scoring logic
    if len(password) >= 8:
        score += 20
    else:
        suggestions.append("Include at least 8 characters.")

    if any(c.islower() for c in password):
        score += 20
    else:
        suggestions.append("Include at least one lowercase letter.")

    if any(c.isupper() for c in password):
        score += 20
    else:
        suggestions.append("Include at least one uppercase letter.")

    if any(c.isdigit() for c in password):
        score += 20
    else:
        suggestions.append("Include at least one number.")

    if any(c in "!@#$%^&*()-_=+[{]}|;:'\",<.>/?`~" for c in password):
        score += 20
    else:
        suggestions.append("Include at least one special character.")

    return score, suggestions

# Return fictional character based on score
def character_feedback(score):
    if score <= 20:
        return "🐭 Tom & Jerry – Fun to watch, but not safe at all!"
    elif score <= 40:
        return "🤷 Mr. Bean – Quirky, but not reliable for security."
    elif score <= 60:
        return "🕷️ Spider-Man – Agile and smart, but could be stronger."
    elif score <= 80:
        return "🛡️ Captain America – Reliable and pretty solid!"
    elif score <= 90:
        return "⚡ Thor – Powerful and tough to beat!"
    else:
        return "🦇 Batman – Silent, prepared, and nearly uncrackable!"

# For command-line testing
if __name__ == "__main__":
    password = input("Enter your password: ")
    score, feedback = check_password_strength(password)

    print(f"\nPassword Strength Score: {score}/100")
    print("Character Match:", character_feedback(score))

    if feedback:
        print("\nSuggestions to improve your password:")
        for tip in feedback:
            print(f" - {tip}")
    else:
        print("✅ Excellent! Your password is very strong.")
