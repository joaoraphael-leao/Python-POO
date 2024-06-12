class Semafor:
    cores = ["Verde", "Amarelo", "Vermelho"]
    indice = 0
    indice_cor = 0
    cor_atual = cores[indice_cor]
    def trocar_cor(self):
        self.indice += 1
        indice_cor = self.indice % 2
