# Declaring the appropriate variable and assigning values

hourly_rate_member=2
hourly_rate_non_member=5

tax_rate_for_member=0.1
tax_rate_for_non_member=0.2

hours_users_spent=int(input('Enter the hours spent:'))

is_a_member=str(input('Are you a member?:'))
if is_a_member.lower()=='yes':
    hourly_rate=hourly_rate_member
    tax_rate=tax_rate_for_member
    membership_status='The user is a member'
else:
    hourly_rate=hourly_rate_non_member
    tax_rate=tax_rate_for_non_member
    membership_status='The user is NOT a member'
    
total_amount=hours_users_spent*hourly_rate
tax_fee=total_amount*tax_rate
total_amount+=tax_fee
return total_amount
        
# print(membership_status, 'stayed', hours_users_spent, 'hours for', hourly_rate, '$/hour', 'plus the', tax_rate, 'the totalamount is:')