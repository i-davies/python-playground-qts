nome = "Ana"
idade = 17
altura = 1.65
estudante = True

# Listas (mutável)
notas = [8, 7, 9]
notas.append(10)

# Tupla (imutável)
coordenada = (10, 20)


# Dicionário (Chave valor)
aluno = {
    "nome": "Ana",
    "turma": "2A"
}

# Conjunto (elementos únicos)
numeros = {1,1,1,2,2,2,3,3,3,3,4,4,4}
print(numeros)


# Type hints (opcional)
nome2: str = "Ana"
idade2: int = 17
altura2: float = 1.65
estudante2: bool = True

MAX_TENTATIVAS = 3

def somar(a: int, b) -> int:
    return a + b

