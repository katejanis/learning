def discount(amount)
  if amount > 10000
    puts "Disount is 10%"
  elsif amount >= 5000
    puts "Discount is 5%"
  elsif amount > 999
    puts "Discount is 1%"
  else
    puts "No discount"
  end
end
