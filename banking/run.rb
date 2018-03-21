require_relative('main')
puts 'Banking v0.4'
puts "\n"

# Get age
puts 'Customer age (integer):'
age = gets.chomp
age = age.to_i

# Initialize
customer = Customer.new(age)

if customer.age >= 21
  # Check if member
  puts 'Is customer a member? (y, n)'
  member = gets.chomp
  case member
  when 'y'
    customer.member = true
  when 'n'
    customer.member = false
  end
  # Get historical transactions if not member
  if not customer.member
    puts 'Input number of previous transactions:'
    trns = gets.chomp
    customer.trns = trns.to_i
    customer.offer_membership = true if customer.trns >= 10
  end
else
  customer.member = false
end

# Process request if appropriate age
if customer.age >= 13
  customer.service = true
  # Get transaction value
  puts 'Input transaction value, $'
  value = gets.chomp
  transaction = Transaction.new(value.to_f)

  # Get item number
  unless customer.age <= 19 and transaction.value >= 100.00
    puts 'Input # of items in transaction:'
    items = gets.chomp
    transaction.items = items.to_i
    customer.dscnt = transaction.discount(transaction.value) if customer.member and transaction.items >= 3 and customer.age >= 21
    customer.dscnt = 0.03 if transaction.items >= 3 and transaction.value <= 99.99 and (13..19) === customer.age
  end
else
  customer.service = false
end

## OUTPUT ##
puts "\nCustomer service: #{customer.service}\nOffer membership: #{customer.offer_membership}\nDiscount rate: #{customer.dscnt}"

