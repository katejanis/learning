require_relative('main')
puts 'Banking v0.2'
puts 'Input amount'
amount = gets.chomp
amount = amount.to_i

discount(amount)
