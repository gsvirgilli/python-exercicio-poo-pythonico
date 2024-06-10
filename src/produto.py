class Produto:
    def __init__(
        self, __nome: str, __codigo: str, __preco: float, __quantidade: int
    ) -> None:
        self.__nome = __nome
        self.__codigo = __codigo
        self.__preco = __preco
        self.__quantidade = __quantidade

    def get_preco(self) -> float:
        return self.__preco

    def get_quantidade(self) -> int:
        return self.__quantidade

    def atualizar_preco_do_produto(self, novo_preco: float) -> None:
        if novo_preco < 0:
            raise ValueError("O preço do produto não pode ser negativo.")
        self.__preco = novo_preco

    def adicionar_estoque_do_produto(self, quantidade: int) -> None:
        self.__quantidade += quantidade

    def remover_estoque_do_produto(self, quantidade: int) -> None:
        if quantidade > self.__quantidade:
            raise ValueError(
                "Quantidade a ser removida é maior que a quantidade em estoque"
            )
        self.__quantidade -= quantidade
