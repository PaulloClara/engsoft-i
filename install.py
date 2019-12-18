from os import path
from subprocess import run
from sys import argv


ALIAS = '\nalias stuki="~/.stuki/dist/run"\n'


def main():
    instalado = False
    caminho_do_arquivo_bash = path.expanduser('~/.zshrc')

    try:
        arquivo_bash = open(caminho_do_arquivo_bash, 'r')
    except FileNotFoundError as e:
        caminho_do_arquivo_bash = path.expanduser('~/.bashrc')
        arquivo_bash = open(caminho_do_arquivo_bash, 'r')

    conteudo_do_arquivo_bash = arquivo_bash.readlines()
    arquivo_bash.close()

    for line in conteudo_do_arquivo_bash:
        if 'alias stuki' in line:
            instalado = True
            break

    if not instalado or '--update' in argv:
        caminho_dist = path.expanduser('~/.stuki/dist')
        caminho_arquivo = path.expanduser('~/.stuki/run.py')

        try:
            run(['cxfreeze', caminho_arquivo, '--target-dir', caminho_dist])
        except Exception as e:
            try:
                run(['pip3', 'install', 'cx-Freeze', '--user'])
                run(['cxfreeze', caminho_arquivo, '--target-dir', caminho_dist])
            except Exception as e:
                print('Não foi possivel instalar o cxfreeze, pip necessario')
                return

    if not instalado:
        conteudo_do_arquivo_bash.append(ALIAS)

        try:
            arquivo_bash = open(caminho_do_arquivo_bash, 'w')
            arquivo_bash.writelines(conteudo_do_arquivo_bash)
        except Exception as e:
            raise
        finally:
            arquivo_bash.close()

    print(f'\n\n\tStuki instalado')
    print(f'\n\tReinicie o terminal ou "$ source {caminho_do_arquivo_bash}"\n')

if __name__ == '__main__':
    main()
