class Bank:
    def __init__(self, holder_name, initial_deposit):
        self.holder_name = holder_name  # public attribute
        self._branch = 'bonani 11' # protected
        self.__balance = initial_deposit # privet

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
    
    def withdrow(self, amount):
        if amount < self.__balance:
            self.__balance = self.__balance - amount
            return amount
        else:
            print('fokira taka nai')

rafsun = Bank('choooto bro', 10000)

print(rafsun.holder_name)
rafsun.holder_name = 'boro vai'
rafsun.deposit(40000)
print(rafsun.get_balance())
print(rafsun.holder_name)
print(rafsun._branch)