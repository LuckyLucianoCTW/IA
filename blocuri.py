import copy
""" definirea problemei """


class Nod:
    def __init__(self, info, h=None):
        self.info = info
        if h is not None:
            self.h = h
        else:
            scop = problema.nod_scop
            self.h = 0
            for i in range(problema.N):
                for j in range(len(info[i])):
                    if len(scop[i]) <= j:
                        self.h += 1
                    elif info[i][j] != scop[i][j]:
                        self.h += 1

    def __str__(self):
        return "({}, h={})".format(self.info, self.h)

    def __repr__(self):
        return f"({self.info}, h={self.h})"


class Problema:
    def __init__(self):
        self.N = 3
        self.M = 4

        self.nod_start = Nod([['a'],['c', 'b'], ['d']],float('inf'))
        self.nod_scop = [['b','c'], [], ['a', 'd']]
class NodParcurgere:

	problema=None

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
		while nod_c.parinte is not None :
			drum = [nod_c.parinte] + drum
			nod_c = nod_c.parinte
		return drum


	def contine_in_drum(self, nod):
		nod_c = self
		while nod_c.parinte is not None :
			if nod.info == nod_c.nod_graf.info:
				return True
			nod_c = nod_c.parinte
		return False

	def expandeaza(self):
		l_succesori = []
		for i in range(self.problema.N):
			a = copy.deepcopy(self.nod_graf.info)
			if not a[i]:
				continue
			b = a[i].pop()
			for j in range(self.problema.N):
				if i != j:
					c = copy.deepcopy(a)
					c[j].append(b)
					l_succesori.append((Nod(c),1))
		return l_succesori

	def test_scop(self):
		return self.nod_graf.info == self.problema.nod_scop


	def __str__(self):
		parinte = self.parinte if self.parinte is None else self.parinte.nod_graf.info
		return f"({self.nod_graf}, parinte={parinte}, f={self.f}, g={self.g})"

	def test_scop(self):
		return self.nod_graf.info == self.problema.nod_scop


	def __str__ (self):
		parinte=self.parinte if self.parinte is None else self.parinte.nod_graf.info
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
		sir += "\nnod: "+str(x)+", cost arc:"+ str(cost)
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

	while len(open) > 0 :
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

				else :
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
					i=0
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