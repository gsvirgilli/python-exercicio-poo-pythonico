from typing import Dict


class Estoque:
    def __init__(self, produtos: Dict[str, int]) -> None:
        self.produtos = produtos

    def adicionar_produto_no_estoque(self, nome: str, quantidade: int) -> None:
        if nome in self.produtos:
            self.produtos[nome] += quantidade
        else:
            self.produtos[nome] = quantidade

    def remover_produto_do_estoque(self, nome: str, quantidade: int) -> None:
        if self.produtos[nome] < quantidade:
            raise ValueError("Quatidade incorreta")

        self.produtos[nome] -= quantidade
        if self.produtos[nome] == 0:
            del self.produtos[nome]

    def atualizar_produto_no_estoque(
        self, nome: str, nova_quantidade: int
    ) -> None:
        if nome in self.produtos:
            self.produtos[nome] = nova_quantidade
        else:
            raise ValueError("Produto não existe")

    def visualizar_estoque(self) -> None:
        for produto, quantidade in self.produtos.items():
            print(f"{produto}: {quantidade}")
