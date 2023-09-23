

# Classe por enquanto bem simples, mas pode ser aprimorada para melhor controle da posição
# e velocidade do veículo, para isso, planeja-se implementar no arduino auxiliar alguns sensores 
# para a coleta de dados, como um sensor hall, gps, acelerômetro e 

class control:
    def __init__(self) -> None:
        self.throtle = 0
        self.direction = 0
        self.velocity = 0
        self.acceleration = 0

    def upadte(self):
        pass

