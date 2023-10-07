from grafo import Grafo
from fortemente_conexas import FortementeConexas
import argparse

def main():
    # Paramêtro de programa
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', action='store', type=str, required=True, help="Path do arquivo que tem o grafo")
    args = parser.parse_args()

    grafo = Grafo()
    grafo.ler(args.file)

    FortementeConexas().buscarPorComponentes(grafo)


if __name__ == "__main__":
    main()