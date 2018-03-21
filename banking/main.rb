class Customer
  def initialize(age)
    @age = age
    @dscnt = false
    @offer_membership = false
  end
  attr_accessor :age, :service,  :dscnt, :member, :trns, :offer_membership
end  

class Transaction
  def initialize(value)
    @value = value
  end
  attr_accessor :value, :items
  def discount(amnt)
    if amnt >= 1000.00
      return 0.1
    elsif amnt >= 500.00
      return 0.05
    elsif amnt >= 100.00
      return 0.01
    else
      return false
    end
  end
end
