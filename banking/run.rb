require_relative('main')
puts 'Banking v0.3'
puts "\n"

# Set defaults
dscnt = false
offer_membership = false

# Get age
puts 'Customer age (integer):'
age = gets.chomp
age = age.to_i

if age >= 21
  # Check if member
  puts 'Is customer a member? (y, n)'
  member = gets.chomp
  case member
  when 'y'
    member = true
  when 'n'
    member = false
  end

  # Get historical transactions if not member
  if not member
    puts 'Input number of previous transactions:'
    trns = gets.chomp
    trns = trns.to_i
    offer_membership = true if trns >= 10
  end
  
else
  member = false
end

# Process request if appropriate age
if age >= 13
  customer_service = true
  # Get transaction value
  puts 'Input transaction value, $'
  value = gets.chomp
  value = value.to_f

  # Get item number
  unless age <= 19 and value >= 100.00
    puts 'Input # of items in transaction:'
    items = gets.chomp
    items = items.to_i
    dscnt = discount(value) if member and items >= 3 and age >= 21
    dscnt = 0.03 if items >= 3 and value <= 99.99 and (13..20) === age
  end
else
  customer_service = false
end

## OUTPUT ##
puts "\nCustomer service: #{customer_service}\nOffer membership: #{offer_membership}\nDiscount rate: #{dscnt}"

