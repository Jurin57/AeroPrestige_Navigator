print('Welcome to the AeroPrestige Navigator.\n')

# customers' information input-------------------------------------------------------------
# Ask the user to input information about themselves
FirstName = input('What is your first name?')
AnnualMiles = input('How many miles have you flown this year?')
AnnualSegments = input('How many segments have you flown this year?')
AnnualDollars = input('How much money have you spent this year(USD)?')
LifetimeMiles = input('How many lifetime miles have you flown?')
LoungeCheck = input('Is your next flight to(or through) the Chicago airport?')
TicketPrice = input('How much will a Coach Class ticket for your next flight cost(USD)?')

# Convert the inputs to the appropriate data type
FirstName = str(FirstName)
AnnualMiles = int(AnnualMiles)
AnnualSegments = int(AnnualSegments)
AnnualDollars = float(AnnualDollars)
LifetimeMiles = int(LifetimeMiles)
LoungeCheck = bool(LoungeCheck)
TicketPrice = float(TicketPrice)
input_summary = '\n{},this year, you have flown {:,} flights for {:,} miles and spent ${:,.2f} USD with our Airlines. Lifetime, you have flown {:,} miles.\n'
print(input_summary.format(FirstName, AnnualSegments, AnnualMiles, AnnualDollars, LifetimeMiles))


# Build the customer segmentation system---------------------------------------------------
# Assign the user the appropriate tier base on the criteria
annual_membership_tier = ''
lifetime_membership_tier = ''

if (AnnualMiles >= 25000 and AnnualMiles < 50000) or ((AnnualSegments >=30 and AnnualSegments < 60) and (AnnualDollars >= 3000 and AnnualDollars < 7000)):
    annual_membership_tier = 'Sapphire'
elif (AnnualMiles >= 50000 and AnnualMiles < 75000) or ((AnnualSegments >=60 and AnnualSegments < 90) and (AnnualDollars >= 7000 and AnnualDollars < 15000)):
    annual_membership_tier = 'Emerald'
elif (AnnualMiles >= 75000 and AnnualMiles < 100000) or ((AnnualSegments >=90 and AnnualSegments < 120) and (AnnualDollars >= 15000 and AnnualDollars < 24000)):
    annual_membership_tier = 'Ruby'
elif AnnualMiles >= 100000 or (AnnualSegments >=120 and AnnualDollars >= 24000):
    annual_membership_tier = 'Diamond'
    
if LifetimeMiles >= 1000000 and LifetimeMiles < 2000000:
    lifetime_membership_tier = 'Emerald'
elif LifetimeMiles >= 2000000 and LifetimeMiles < 3000000:
    lifetime_membership_tier = 'Ruby'
elif LifetimeMiles >= 3000000:
    lifetime_membership_tier = 'Diamond'

# display the customer's membership status
display_membership = ''
annual_membership_class = 0
lifetime_membership_class = 0

# A dictionary mapping membership tier names to their respective class levels
membership_tiers = {'Sapphire': 1, 'Emerald': 2, 'Ruby': 3, 'Diamond': 4}

# Retrieve the class level for annual and lifetime membership tiers
# If the tier is not found, it defaults to 0 (which indicates no status)
annual_membership_class = membership_tiers.get(annual_membership_tier, 0)
lifetime_membership_class = membership_tiers.get(lifetime_membership_tier, 0)

if lifetime_membership_class != 0:
    if annual_membership_class >= lifetime_membership_class:
        display_membership = 'You have achieved life time frequent-flier status at the {} level!\nThis year, you have also achieved annual frequent-flier status at the {} level!'.format(lifetime_membership_tier, annual_membership_tier)
    elif annual_membership_class < lifetime_membership_class:
        display_membership = 'This year, you have achieved annual frequent-flier status at the {} level!'.format(annual_membership_tier)
elif lifetime_membership_class == 0:
    if annual_membership_class != 0:
        display_membership = 'This year, you have achieved annual frequent-flier status at the {} level!'.format(annual_membership_tier)
    else:
        display_membership = 'You are on your way to achieving annual frequent-flier status with our Airlines!'

print(display_membership + '\n')



# Build the rewards system-----------------------------------------------------------------

# Determine the user's rewards based on the highest memberhsip tier
rewards_bags = 0
rewards_upgrades = ''
rewards_lounge = False
rewards_discount = 0
rewards_discount_str = ''

if annual_membership_tier == 'Sapphire':
    rewards_bags = 0
    rewards_upgrades = 'Business Class'
    rewards_lounge = False
    rewards_discount = 0.15

elif annual_membership_tier == 'Emerald':
    rewards_bags = 1
    rewards_upgrades = 'Business Class'
    rewards_lounge = False
    rewards_discount = 0.20

elif annual_membership_tier == 'Ruby':
    rewards_bags = 2
    rewards_upgrades = 'First Class'
    rewards_lounge = False
    rewards_discount = 0.25

elif annual_membership_tier == 'Diamond':
    rewards_bags = 3
    rewards_upgrades = 'First Class'
    rewards_lounge = True
    rewards_discount = 0.30

# display the customer's rewards
# Initialize empty strings for various display messages related to rewards
display_reward_summary = ''
display_reward_upgrades = ''
display_reward_discount = ''
display_reward_bag = ''
display_reward_lounge = ''

# Calculate the discount percentage string (e.g., '25%') from the rewards_discount float value
rewards_discount_str = str(int(rewards_discount * 100)) + '%'
# Calculate the discounted ticket price
discounted_price = TicketPrice * (1 - rewards_discount)

if annual_membership_class != 0:
    display_reward_summary = 'You have unlocked the following rewards:\n'
    display_reward_upgrades = '- Free seat upgrades to {}.\n'.format(rewards_upgrades)
    display_reward_discount = '- Your upcoming flight ticket price of ${:,.2f} USD was reduced by {} to ${:,.2f} USD.\n'.format(TicketPrice, rewards_discount_str, discounted_price)

    if rewards_bags != 0: 
        display_reward_bag = '- {} free checked bags per flight.\n'.format(rewards_bags)

    if rewards_lounge:
        display_reward_lounge = '- Enjoy free access to the club lounge in Chicago on your next/upcoming flight!' if LoungeCheck else '- Free access to the club lounge next time flying to/through in Chicago.'

print(display_reward_summary + display_reward_bag + display_reward_upgrades + display_reward_discount + display_reward_lounge)















    
