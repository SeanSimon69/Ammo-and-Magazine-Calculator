def calculate_mags(total_rounds, mag_capacity, total_mags):
    # Calculate maximum full magazines you can fill
    full_mags_possible = total_rounds // mag_capacity  
    full_mags_used = min(full_mags_possible, total_mags)  # Limited by the number of mags available
    remaining_rounds = total_rounds - (full_mags_used * mag_capacity)  # Leftover rounds after full mags

    # Determine if there's a partially filled magazine
    partial_mag_rounds = 0
    if remaining_rounds > 0 and full_mags_used < total_mags:
        partial_mag_rounds = remaining_rounds
        remaining_rounds = 0  # All leftover rounds go into the partial mag

    # Calculate empty magazines
    empty_mags = total_mags - full_mags_used - (1 if partial_mag_rounds > 0 else 0)

    # Calculate needed rounds to fill the partial magazine
    needed_rounds = mag_capacity - partial_mag_rounds if partial_mag_rounds > 0 else 0

    return full_mags_used, partial_mag_rounds, remaining_rounds, empty_mags, needed_rounds

# Example usage
total_rounds = int(input("Enter the total number of rounds: "))
mag_capacity = int(input("Enter the magazine capacity (default is 30): ") or 30)
total_mags = int(input("Enter the total number of magazines you have: "))

# Call the function
full_mags, partial_mag_rounds, remaining_rounds, empty_mags, needed_rounds = calculate_mags(total_rounds, mag_capacity, total_mags)

# Output results
print(f"You can fully load {full_mags} magazines.")
if partial_mag_rounds > 0:
    print(f"You have one partially filled magazine with {partial_mag_rounds} rounds.")
if remaining_rounds > 0:
    print(f"You have {remaining_rounds} rounds left over (not in a magazine).")
if partial_mag_rounds > 0:
    print(f"You need {needed_rounds} more rounds to fill the rest of the partial magazine.")
if empty_mags > 0:
    print(f"You have {empty_mags} empty magazines left.")

input("Press Enter to exit...")