import copy
""" definirea problemei """


class Nod:
    def __init__(self, info, h=None):
        self.info = info
        if h is not None:
            self.h = h
        else:
            h = 0
            n = problema.N
            for i in range(n):
                for j in range(n):
                    nr = info[i][j]
                    if nr == 0:
                        scop_i = n - 1
                        scop_j = n - 1
                    else:
                        scop_i = (nr - 1) // n
                        scop_j = (nr - 1) % n

                    h += abs(i - scop_i) + abs(j - scop_j)
            self.h = h

    def __str__(self):
        return "({}, h={})".format(self.info, self.h)

    def __repr__(self):
        return f"({self.info}, h={self.h})"


class Problema:
    def __init__(self):
        self.N = 3
        self.nod_start = Nod([[7, 5, 2],
                              [8, 0, 6],
                              [3, 4, 1]], float('inf'))
        self.nod_scop = [[1, 2, 3],
                         [4, 5, 6],
                         [7, 8, 0]]


""" Sfarsit definire problema """

""" Clase folosite in algoritmul A* """


class NodParcurgere:
    """O clasa care cuprinde informatiile asociate unui nod din listele open/closed
        Cuprinde o referinta catre nodul in sine (din graf)
        dar are ca proprietati si valorile specifice algoritmului A* (f si g).
        Se presupune ca h este proprietate a nodului din graf

    """

    problema = None

    def __init__(self, nod_graf: Nod, parinte=None, g=0, f=None):
        self.nod_graf = nod_graf  # obiect de tip Nod
        self.parinte = parinte  # obiect de tip NodParcurgere
        self.g = g  # costul drumului de la radacina pana la nodul curent
        if f is None:
            self.f = self.g + self.nod_graf.h
        else:
            self.f = f

    def drum_arbore(self):
        """
            Functie care calculeaza drumul asociat unui nod din arborele de cautare.
            Functia merge din parinte in parinte pana ajunge la radacina
        """
        nod_c = self
        drum = [nod_c]
        while nod_c.parinte is not None:
            drum = [nod_c.parinte] + drum
            nod_c = nod_c.parinte
        return drum

    def contine_in_drum(self, nod):
        """
            Functie care verifica daca nodul "nod" se afla in drumul dintre radacina si nodul curent (self).
            Verificarea se face mergand din parinte in parinte pana la radacina
            Se compara doar informatiile nodurilor (proprietatea info)
            Returnati True sau False.

            "nod" este obiect de tip Nod (are atributul "nod.info")
            "self" este obiect de tip NodParcurgere (are "self.nod_graf.info")
        """
        nod_c = self
        while nod_c.parinte is not None:
            if nod.info == nod_c.nod_graf.info:
                return True
            nod_c = nod_c.parinte
        return False

    def expandeaza(self):
        l_succesori = []
        n = self.problema.N
        for i in range(n):
            for j in range(n):
                if(self.nod_graf.info[i][j] != 0):
                    continue
                directii = [[1,0],[0,1],[-1,0],[0,-1]]
                for c in range(len(directii)):
                    i_aux = i + directii[c][0]
                    j_aux = j + directii[c][1]
                    if(i_aux >= 0 and j_aux >= 0 and i_aux < n and j_aux < n):
                        a = copy.deepcopy(self.nod_graf.info)
                        a[i][j] = a[i_aux][j_aux]
                        a[i_aux][j_aux] = 0
                        l_succesori.append((Nod(a),1))

        return l_succesori

    def test_scop(self):
        return self.nod_graf.info == self.problema.nod_scop

    def __str__(self):
        parinte = self.parinte if self.parinte is None else self.parinte.nod_graf.info
        return f"({self.nod_graf}, parinte={parinte}, f={self.f}, g={self.g})"

    def test_scop(self):
        return self.nod_graf.info == self.problema.nod_scop

    def __str__(self):
        parinte = self.parinte if self.parinte is None else self.parinte.nod_graf.info
        return f"({self.nod_graf}, parinte={parinte}, f={self.f}, g={self.g})"


def str_info_noduri(l):
    sir = "["
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
        print("Drum de cost minim: " + str_info_noduri(nod_curent.drum_arbore()))


if __name__ == "__main__":
    problema = Problema()
    NodParcurgere.problema = problema
    a_star()