from Modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Matheus', 8)
restaurante_praca.receber_avaliacao('Geovanna', 7)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()