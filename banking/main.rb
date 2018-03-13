def discount(amount)
  if amount >= 1000.00
    return 0.1
  elsif amount >= 500.00
    return 0.05
  elsif amount >= 100.00
    return 0.01
  else
    return false
  end
end
