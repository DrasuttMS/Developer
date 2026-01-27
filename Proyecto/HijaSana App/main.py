from datetime import date

def get_stimulation_advice(months):
    """Returns advice based on baby's age in months"""
    if months < 3:
        return "Visual stimulation: Use high-contrast black and white cards."
    elif 3 <= months < 6:
        return "Motor skills: Practice 'tummy time' to strengthen neck muscles."
    elif 6 <= months < 9:
        return "Social skills: Play 'peek-a-boo' (escondite) to develop object permanence."
    elif 9 <= months < 12:
        return "Coordination: Encourage crawling by placing toys slightly out of reach."
    else:
        return "Discovery: Safe exploration of different textures (sand, water, fabric)."

# 1. Input: A hypothetical birth date (Year, Month, Day)
# Let's assume a birth date of August 15, 2025 for this example
birth_date = date(2025, 8, 15)
today = date.today()

# 2. Logic: Calculate total months
total_days = (today - birth_date).days
total_months = total_days // 30

# 3. Output: Display results
print("--- Early Stimulation Guide ---")
print(f"Status: Based on the hypothetical date, the age is {total_months} months.")
print(f"Daily Activity: {get_stimulation_advice(total_months)}")
