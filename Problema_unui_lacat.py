import copy

""" definirea problemei """


class Nod:

    def getWord(self,scop):
        type_i = -1
        type_d = 1
        total = 0
        st = self.info
        sc = scop
        for i in range(len(st)):
            cod_start = 0
            if(st[i][0] == 'd'):
                cod_start = 1
            elif(st[i][0] == 'i'):
                cod_start = -1
            cod_sursa = 0
            if(scop[i][0] == 'd' and scop[i][0] != st[i][0]):
                cod_sursa = 1
            elif(scop[i][0] == 'i'):
                cod_sursa = -1
            total += pow(abs(cod_start - cod_sursa),2)
        return total


    def __init__(self, info, h=None, cheie = None):
        self.info = info
        self.cheie = cheie
        if h is not None:
            self.h = h
        else:
            scop = problema.nod_scop
            h = self.getWord(scop)
            self.h = h



    def __str__(self):
        return "{}".format(self.info)

    def __repr__(self):
        return f"{self.info}"



class Problema:
    def __init__(self):
        self.nod_start = Nod([['i',1],['i',1],['i',1],['i',1],['i',1],['i',1],['i',1]],float("inf"),"")
        self.nod_scop = [['d', 0], ['d', 0], ['d', 0], ['d', 0], ['d', 0], ['d', 0], ['d', 0]]


        list_of_lists = []
        with open('date.in') as f:
            for line in f:
                inner_list = [elt.strip() for elt in line.split(',')]
                list_of_lists.append(inner_list)
        self.nod_posibile = list_of_lists



class NodParcurgere:


    problema = None
    succesori = []
    def __init__(self, nod_graf: Nod, parinte=None, g=0, f=None):
        self.nod_graf = nod_graf
        self.parinte = parinte
        self.g = g
        if f is None:
            self.f = self.g + self.nod_graf.h
        else:
            self.f = f

    def drum_arbore(self):
        nod_c = self
        drum = [nod_c]
        while nod_c.parinte is not None:
            drum = [nod_c.parinte] + drum
            nod_c = nod_c.parinte
        return drum

    def contine_in_drum(self, nod):
        nod_c = self
        while nod_c.parinte is not None:
            if nod.info == nod_c.nod_graf.info:
                return True
            nod_c = nod_c.parinte
        return False

    def expandeaza(self):
        l_succesori = []
        for i in range(len(self.problema.nod_posibile)):
            #print(self.nod_graf.info[0][0], "second")
            x = copy.deepcopy(self.nod_graf.info)
            for j in range(len(self.problema.nod_posibile[i][0])):
                nod_actual = x[j][1]
                nod_scop = 0
                my_word = self.problema.nod_posibile[i][0][j]
                if(my_word == 'i'):
                    if(x[j][0] == 'i'):
                        x[j][1] += 1
                    else:
                        x[j][0] = 'i'
                        x[j][1] = 1
                elif(my_word == 'd'):
                    if(x[j][0] == 'i'):
                        if(x[j][1] > 1):
                            x[j][1] -= 1
                        else:
                            x[j][1] = 0
                            x[j][0] = 'd'
            l_succesori.append((Nod(x,None,self.problema.nod_posibile[i][0]), 1))

        return l_succesori

    def test_scop(self):
        return self.nod_graf.info == self.problema.nod_scop

    def __str__(self):
        parinte = ""
        if self.parinte is None:
            parinte = "Initial : "
            return f"{parinte} {self.nod_graf}"
        else:
            parinte = "\n" + "Incuietori : " + str(self.parinte.nod_graf.info) + "\n"
            return f"{parinte} Folosim cheia : {self.nod_graf.cheie} pentru a ajunge la {self.nod_graf}"

    def test_scop(self):
        return self.nod_graf.info == self.problema.nod_scop

    def __str__(self):
        parinte = ""
        if self.parinte is None:
            parinte = "Initial : "
            return f"{parinte} {self.nod_graf}"
        else:
            parinte = "\n" + "Incuietori : " + str(self.parinte.nod_graf.info) + "\n"
            return f"{parinte} Folosim cheia : [{self.nod_graf.cheie}] pentru a ajunge la {self.nod_graf}"



def str_info_noduri(l):
    #sir = "["

    sir = ""
    for x in l:
       sir += str(x) + "  \n"
    sir += "]"
    return sir


def afis_succesori_cost(l):
    sir = ""
    for (x, cost) in l:
        sir += "\nnod: " + str(x) + ", cost arc:" + str(cost)
    return sir


def in_lista(l, nod):
    for i in range(len(l)):
        if l[i].nod_graf.info == nod.info:
            return l[i]
    return None


def a_star():
    rad_arbore = NodParcurgere(NodParcurgere.problema.nod_start)
    open = [rad_arbore]
    closed = []

    while len(open) > 0:
        print(str_info_noduri(open))
        nod_curent = open.pop(0)
        closed.append(nod_curent)

        if nod_curent.test_scop():
            break

        l_succesori = nod_curent.expandeaza()
        for (nod_succesor, cost_succesor) in l_succesori:

            nod_nou = None
            if not nod_curent.contine_in_drum(nod_succesor):
                g_succesor = nod_curent.g + cost_succesor
                f_succesor = g_succesor + nod_succesor.h

                nod_parcg_vechi = in_lista(closed, nod_succesor)

                if nod_parcg_vechi is not None:
                    if (g_succesor < nod_parcg_vechi.g):
                        closed.remove(nod_parcg_vechi)
                        nod_parcg_vechi.parinte = nod_curent
                        nod_parcg_vechi.g = g_succesor
                        nod_parcg_vechi.f = f_succesor
                        nod_nou = nod_parcg_vechi

                else:
                    nod_parcg_vechi = in_lista(open, nod_succesor)

                    if nod_parcg_vechi is not None:
                        if (f_succesor < nod_parcg_vechi.f):
                            open.remove(nod_parcg_vechi)
                            nod_parcg_vechi.parinte = nod_curent
                            nod_parcg_vechi.g = g_succesor
                            nod_parcg_vechi.f = f_succesor
                            nod_nou = nod_parcg_vechi

                    else:
                        nod_nou = NodParcurgere(nod_graf=nod_succesor, parinte=nod_curent, g=g_succesor)

                if nod_nou:
                    i = 0
                    while i < len(open):
                        if open[i].f < nod_nou.f:
                            i += 1
                        else:
                            while i < len(open) and open[i].f == nod_nou.f and open[i].g > nod_nou.g:
                                i += 1
                            break

                    open.insert(i, nod_nou)

    print("\n------------------ Concluzie -----------------------")
    if len(open) == 0:
        print("Lista open e vida, nu avem drum de la nodul start la nodul scop")
    else:
        print(str_info_noduri(nod_curent.drum_arbore()))


if __name__ == "__main__":
    problema = Problema()
    NodParcurgere.problema = problema
    a_star()
