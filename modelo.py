# -*- coding: utf-8 -*-
import os
import shutil

from src.features.paths import paths_list
#Caminhos a serem limpos

rp = input("Deseja realmente realizar a limpeza?  S-sim / N-não")

if ((rp == 'S') or (rp == 'sim') or (rp == 's')):
    for di in paths_list: #percorre o array de diretorios
        for files in os.listdir(di):    #pra cada diretorio é feito a limpeza
            path = os.path.join(di, files)
            try:
                shutil.rmtree(path)
            except OSError:
                os.remove(path)
