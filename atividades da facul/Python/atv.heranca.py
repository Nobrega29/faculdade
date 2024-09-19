
#super class
class Empregado:
    def __init__(self , nome , salario_base) :
        self.nome = nome
        self.salario_base = salario_base
    
    def calcaular_salario(self):
        return self.salario_base

#sub=class
class Gerente(Empregado):
    def __init__(self, nome, salario_base, bonus_fixo):
        super().__init__(nome, salario_base)
        self.bonus_fixo = bonus_fixo
    
    def calcaular_salario(self):
        return super().calcaular_salario() + self.bonus_fixo
    
#sub-class
class Vendedor(Empregado):
    def __init__(self, nome, salario_base, bonus_venda, comissao):
        super().__init__(nome, salario_base)
        self.bonus_venda = bonus_venda
        self.comissao = comissao

    def calcaular_salario(self):
        return super().calcaular_salario() + (self.bonus_venda * self.comissao)


Gerente = Gerente('Higor' , 5000, 2000)
print(f'O salario total {Gerente.nome} (Gerente) é : {Gerente.calcaular_salario()} ')

Vendedor = Vendedor('Juliana' , 3000, 15000, 0.05)
print(f"O salário total de {Vendedor.nome} (Vendedor) é: R${Vendedor.calcaular_salario()}")



