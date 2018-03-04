require_relative('main')

puts 'Input amount'
amount = gets.chomp
amount = amount.to_i

discount(amount)
