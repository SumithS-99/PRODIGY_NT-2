import re

# Function to check password complexity
def check_password_strength(password):
    # Initialize score
    strength_score = 0
    feedback = []

    # Check password length (at least 8 characters)
    if len(password) >= 8:
        strength_score += 1
    else:
        feedback.append("Password must be at least 8 characters long.")

    # Check for presence of uppercase letter
    if re.search(r'[A-Z]', password):
        strength_score += 1
    else:
        feedback.append("Password must contain at least one uppercase letter.")

    # Check for presence of lowercase letter
    if re.search(r'[a-z]', password):
        strength_score += 1
    else:
        feedback.append("Password must contain at least one lowercase letter.")

    # Check for presence of number
    if re.search(r'[0-9]', password):
        strength_score += 1
    else:
        feedback.append("Password must contain at least one number.")

    # Check for presence of special character
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength_score += 1
    else:
        feedback.append("Password must contain at least one special character.")

    # Evaluate password strength based on the score
    if strength_score == 5:
        feedback.append("Your password is strong!")
    elif strength_score == 4:
        feedback.append("Your password is moderately strong.")
    elif strength_score == 3:
        feedback.append("Your password is weak.")
    else:
        feedback.append("Your password is very weak.")

    return feedback

# Main function
def main():
    # Get password input from the user
    password = input("Enter your password: ")

    # Check the password strength
    feedback = check_password_strength(password)

    # Output the feedback
    for item in feedback:
        print(item)

# Run the program
if __name__ == "__main__":
    main()
