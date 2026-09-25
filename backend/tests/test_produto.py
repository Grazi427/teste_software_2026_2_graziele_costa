from backend.entity.produto import Produto
import pytest
from backend.exceptions.excecoes import NomeInvalidoError

def test_criar_produto_com_sucesso():
    """Garante que o Produto seja criado com dados válidos."""
    cafe = Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    assert cafe._nome == "cafe"
    assert cafe._preco == 18 and cafe._quant_estoque == 50 and \
        cafe._validade == 3 and cafe._codigo_barras == 1234567890 and \
        cafe._categoria == "alimenticio" and cafe._peso == 250

def test_criar_produto_sem_nome():
    """Garante que o Produto rejeite um nome vazio."""
    with pytest.raises(NomeInvalidoError, match='Nome não pode ser vazio'):
        Produto("", 18, 50, 3, 1234567890, "alimenticio", 250)

def test_criar_produto_sem_preco():
    """Garante que o Produto rejeite um nome vazio."""
    with pytest.raises(ValueError):
        Produto("cafe", None, 50, 3, 1234567890, "alimenticio", 250)

def test_criar_produto_sem_estoque():
    """Garante que o Produto rejeite um nome vazio."""
    with pytest.raises(ValueError):
        Produto("cafe", 18, None, 3, 1234567890, "alimenticio", 250)

def test_criar_produro_sem_validade():
    """Garante que o Produto rejeite um nome vazio."""
    with pytest.raises(ValueError):
        Produto("cafe", 18, 50, None, 1234567890, "alimenticio", 250)

def test_criar_produto_sem_codigo_barras():
    """Garante que o Produto rejeite um nome vazio."""
    with pytest.raises(ValueError):
        Produto("cafe", 18, 50, 3, None, "alimenticio", 250)

def test_criar_produto_com_categoria_vazia():
    """Garante que o Produto rejeite um nome vazio."""
    with pytest.raises(ValueError):
        Produto("cafe", 18, 50, 3, 1234567890, "", 250)

def test_criar_produto_sem_peso():
    """Garante que o Produto rejeite um nome vazio."""
    with pytest.raises(ValueError):
        Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", None)

def test_validar_nome_produto():
    bebida = Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    assert bebida.nome == 'cafe'
    bebida.valida_nome('cafe')

def test_validar_preco_produto():
    bebida = Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    assert bebida.preco == 18
    bebida.valida_preco(18)

def test_validar_quant_estoque_produto():
    bebida = Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    assert bebida.quant_estoque == 50
    bebida.valida_quant_estoque(50)

def test_validar_validade_produto():
    bebida = Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    assert bebida.validade == 3
    bebida.valida_validade(3)

def test_validar_codigo_barras_produto():
    bebida = Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    assert bebida.codigo_barras == 1234567890
    bebida.valida_codigo_barras(1234567890)

def test_validar_categoria_produto():
    bebida = Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    assert bebida.categoria == 'alimenticio'
    bebida.valida_categoria('alimenticio')

def test_validar_peso_produto():
    bebida = Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    assert bebida.peso == 250
    bebida.valida_peso(250)

def test_atualizar_nome_produto():
    produto = Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    produto.nome = 'cappucino'

def test_atualizar_preco_produto():
    produto = Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    produto.preco = 20

def test_atualizar_quant_estoque_produto():
    produto = Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    produto.quant_estoque=50

def test_atualizar_validade_produto():
    produto = Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    produto.validade= 3

def test_atualizar_codigo_barras_produto():
    produto = Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    produto.codigo_barras = 1234567899

def test_atualizar_categoria_produto():
    produto = Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    produto.categoria = 'limpeza'

def test_atualizar_peso_produto():
    produto = Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    produto.peso = 350




