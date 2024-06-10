from src.livro.livro import Livro


def test_cria_livro():
    livreta = Livro("olá mundo", "Gui", 19)

    assert livreta.titulo == "olá mundo"
    assert livreta.autor == "Gui"
    assert livreta.paginas == 19
