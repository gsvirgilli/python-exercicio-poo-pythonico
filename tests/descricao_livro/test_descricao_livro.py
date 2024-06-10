from src.livro.livro import Livro


def test_descricao_livro():
    livreta = Livro("olá mundo", "Gui", 19)
    assert (
        repr(livreta) == "O livro olá mundo de Gui possui 19 páginas."
    )
