#correção do #7 - nova view 

from pathlib import Path
import sys

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from model.item import Item
from controler.itemControler import ItemControler

class Janela3:
    
    @staticmethod
    def mostrar_janela3(database_name: str) -> None:
        print('------Cadastrar Novo Item no Menu------\n')
        
        nome = input('Nome do item: ').strip()
        tipo = input('Tipo (ex: pizza, bebida): ').strip()
        descricao = input('Descrição: ').strip()
        
        #adicionei código para validar dados
        if not nome or not tipo or not descricao:
            print('Todos os campos são obrigatórios. Operação cancelada.')
            return
        
        try:
            preco = float(input('Preço (ex: 29.90): '))
        except ValueError:
            print('Preço inválido. Operação cancelada.')
            return

        item = Item(nome, preco, tipo, descricao)
        sucesso = ItemControler.insert_into_item(database_name, item)

        if sucesso == True:
            print('\nItem cadastrado com sucesso!')
        else:
            print('\nErro ao cadastrar item.')
