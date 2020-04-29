import time


def dist_manhattan(x1,y1,x2,y2):
    return (abs(x2-x1) + abs(y2- y1))

class Joc:
    """
    Clasa care defineste jocul. Se va schimba de la un joc la altul.
    """
    HOUNDS_SAME_MOVE = 0
    prev_Hounds = None
    JMIN = None
    JMAX = None

    def __init__(self, hounds = None, hare = None, tabla=None):
        self.matr = []
        if(tabla == None):
            for i in range(11):
                self.matr.append(str(i))
            self.matr[0] = 'c'
            self.matr[1] = 'c'
            self.matr[3] = 'c'
            self.matr[10] = 'i'
            self.Hounds = [0,1,3]
            self.Hare = 10
        else:
            self.matr = list(tabla)
            self.Hounds = list(hounds)
            self.Hare = hare


    def final(self):

        x = 0
        y = 1
        pos_x_y = [[0,1],[1,0],[1,1],[1,2],[1,1],[2,1],[2,2],[3,0],[3,1],[3,2],[4,1]]
        Hound_1 = pos_x_y[self.Hounds[0]]
        Hound_2 = pos_x_y[self.Hounds[1]]
        Hound_3 = pos_x_y[self.Hounds[2]]
        if(self.prev_Hounds == None):
            self.prev_Hounds = self.Hounds
        else:
            Hound_prev_1 = pos_x_y[self.prev_Hounds[0]]
            Hound_prev_2 = pos_x_y[self.prev_Hounds[1]]
            Hound_prev_3 = pos_x_y[self.prev_Hounds[2]]
            if(Hound_prev_1[x] == Hound_1[x] and Hound_prev_2[x] == Hound_2[x] and Hound_prev_3 == Hound_3[x]):
                self.HOUNDS_SAME_MOVE += 1
            else:
                self.HOUNDS_SAME_MOVE = 0

        if(self.HOUNDS_SAME_MOVE == 10):
            return "i"
        player = [
         [[1,2,3],[-1]]#0
        ,[[2,4,5],[-1]]#1
        ,[[1,5,3],[-1]]#2
        ,[[2,5,6],[-1]]#3
        ,[[5,7],[1]] #4
        ,[[4,6,7,9,8],[1,2,3]]#5
        ,[[5,9],[3]] #6
        ,[[8,10],[5,4]] #7
        ,[[7,9,10],[5]] #8
        ,[[8,10],[6,5]] #9
        ,[[-1],[7,8,9]]] #10
        numar_miscari = len(player[self.Hare][0] + player[self.Hare][1])
        if(-1 in player[self.Hare][0] or -1 in player[self.Hare][0]):
            numar_miscari -= 1
        if(self.Hare == 1 or self.Hare == 3 or self.Hare == 2):
            return "i"
        if(numar_miscari == 3):
            for i in range (3):
                if(self.Hounds[i] not in player[self.Hare][0] and self.Hounds[i] not in player[self.Hare][1]):
                    return False
            return "c"
        return False

    def mutari_joc(self, jucator):
        l_mutari = []
        player = [
         [[1,2,3],[-1]]#0
        ,[[2,4,5],[-1]]#1
        ,[[1,5,3],[-1]]#2
        ,[[2,5,6],[-1]]#3
        ,[[5,7],[1]] #4
        ,[[4,6,7,9,8],[1,2,3]]#5
        ,[[5,9],[3]] #6
        ,[[8,10],[5,4]] #7
        ,[[7,9,10],[5]] #8
        ,[[8,10],[6,5]] #9
        ,[[-1],[7,8,9]]] #10
        if(jucator == 'c'):
            for i in range(3):
                vec = player[self.Hounds[i]][0]
                for j in range(len(vec)):
                    if(int(vec[j]) in self.Hounds):
                        continue
                    if str(self.matr[vec[j]]) == str(vec[j]):
                        mutare_noua = Joc(self.Hounds,self.Hare,self.matr)
                        mutare_noua.matr[int(self.Hounds[i])] = self.Hounds[i]
                        mutare_noua.matr[vec[j]] = 'c'
                        mutare_noua.Hounds[i] = int(vec[j])
                        l_mutari.append(Joc(mutare_noua.Hounds,mutare_noua.Hare,mutare_noua.matr))
        else:
            vec = player[self.Hare]
            for i in range(len(vec)):
                for j in range(len(vec[i])):
                    if(int(self.Hare == vec[i][j])):
                        continue
                    if str(self.matr[vec[i][j]]) == str(vec[i][j]):
                        mutare_noua = Joc(self.Hounds,self.Hare,self.matr)
                        mutare_noua.matr[int(mutare_noua.Hare)] = mutare_noua.Hare
                        mutare_noua.matr[vec[i][j]] = 'i'
                        mutare_noua.Hare = int(vec[i][j])
                        l_mutari.append(Joc(mutare_noua.Hounds,mutare_noua.Hare,mutare_noua.matr))

        return l_mutari

    def calculeaza_scor(self, jucator):
        score = 0
        x = 0
        y = 1
        start_hound = 0
        start_hare = 10
        pos_x_y = [[0,1],[1,0],[1,1],[1,2],[1,1],[2,1],[2,2],[3,0],[3,1],[3,2],[4,1]]
        pos_start_hound = pos_x_y[start_hound]
        pos_start_hare = pos_x_y[start_hare]
        hound_1 = pos_x_y[self.Hounds[0]]
        hound_2 = pos_x_y[self.Hounds[1]]
        hound_3 = pos_x_y[self.Hounds[2]]
        hare = pos_x_y[self.Hare]
        '''
        #2nd Heuristic
        goal_hare_1 = pos_x_y[1]
        goal_hare_2 = pos_x_y[2]
        goal_hare_3 = pos_x_y[3]
        dist_hare_goal1 = dist_manhattan(hare[x],hare[y],goal_hare_1[x],goal_hare_1[y])
        dist_hare_goal2 = dist_manhattan(hare[x], hare[y], goal_hare_2[x], goal_hare_2[y])
        dist_hare_goal3 = dist_manhattan(hare[x], hare[y], goal_hare_3[x], goal_hare_3[y])
        dist_hound1_hare = dist_manhattan(hound_1[x],hound_1[y],hare[x],hare[y])
        dist_hound2_hare = dist_manhattan(hound_2[x], hound_2[y], hare[x], hare[y])
        dist_hound3_hare = dist_manhattan(hound_3[x], hound_3[y], hare[x], hare[y])
        dist_hare_houndStart = dist_manhattan(hare[x],hare[y],pos_start_hound[x],pos_start_hound[y])
        if jucator == 'c':
            if(dist_hound1_hare == 1 and dist_hound2_hare == 1 and dist_hound3_hare == 1):
                score = 99999
            else:
                score = 0
                if(hound_1[y] == hare[y]):
                    score += (dist_hound1_hare - 1)
                elif(hound_2[y] == hare[y]):
                    score += (dist_hound2_hare - 1)
                elif (hound_3[y] == hare[y]):
                    score += (dist_hound3_hare - 1)
                elif (hound_1[x] == hare[x]):
                    score += dist_hound1_hare
                elif (hound_2[x] == hare[x]):
                    score += dist_hound2_hare
                elif (hound_3[x] == hare[x]):
                    score += dist_hound3_hare

        elif jucator == 'i':
            if (dist_hare_houndStart == 1 or (hare[x] < hound_1[x] and hare[x] < hound_2[x] and hare[x] < hound_3[x])):
                score = 99999
            else:
                score = 0
                if(goal_hare_1[y] == hare[y]):
                    score += dist_hare_goal1
                elif(goal_hare_2[y] == hare[y]):
                    score += dist_hare_goal2
                elif(goal_hare_3[y] == hare[y]):
                    score += dist_hare_goal3
        '''


        #First Heuristic
        dist_hound1_hare = dist_manhattan(hound_1[x],hound_1[y],hare[x],hare[y])
        dist_hound2_hare = dist_manhattan(hound_2[x], hound_2[y], hare[x], hare[y])
        dist_hound3_hare = dist_manhattan(hound_3[x], hound_3[y], hare[x], hare[y])
        dist_hare_houndStart = dist_manhattan(hare[x],hare[y],pos_start_hound[x],pos_start_hound[y])
        dist_hare_hareStart = dist_manhattan(hare[x], hare[y], pos_start_hare[x], pos_start_hare[y])
        dist_hound1_houndStart = dist_manhattan(hound_1[x],hound_1[y],pos_start_hound[x],pos_start_hound[y])
        dist_hound2_houndStart = dist_manhattan(hound_2[x], hound_2[y], pos_start_hound[x], pos_start_hound[y])
        dist_hound3_houndStart = dist_manhattan(hound_3[x], hound_3[y], pos_start_hound[x], pos_start_hound[y])
        dist_hound1_hareStart = dist_manhattan(hound_1[x],hound_1[y],pos_start_hare[x],pos_start_hare[y])
        dist_hound2_hareStart = dist_manhattan(hound_2[x], hound_2[y], pos_start_hare[x], pos_start_hare[y])
        dist_hound3_hareStart = dist_manhattan(hound_3[x], hound_3[y], pos_start_hare[x], pos_start_hare[y])
        if jucator == 'c':
            if(dist_hound1_hare == 1 and dist_hound2_hare == 1 and dist_hound3_hare == 1):
                score = 99999
            else:
                score = (dist_hound1_hare + dist_hound2_hare + dist_hound3_hare) / 3 #media celor 3 distante
                if(hound_1[x] < hare[x]):
                    score += (dist_hare_houndStart - dist_hound1_hare) - 1
                if(hound_2[x] < hare[x]):
                    score += (dist_hare_houndStart - dist_hound2_hare) - 1
                if(hound_3[x] < hare[x]):
                    score += (dist_hare_houndStart - dist_hound2_hare) - 1
                if(hound_1[x] == hare[x]):
                    score += dist_hound1_hare
                if(hound_2[x] == hare[x]):
                    score += dist_hound2_hare
                if(hound_3[x] == hare[x]):
                    score += dist_hound3_hare
        else:
            if(dist_hare_houndStart == 1 or (hare[x] < hound_1[x] and hare[x] < hound_2[x] and hare[x] < hound_3[x])):
                score = 99999
            else:
                score = dist_hare_houndStart - dist_hare_hareStart
                if(hound_1[x] < hare[x]):
                    score += dist_hound1_hare - 1
                if(hound_2[x] < hare[x]):
                    score += dist_hound2_hare - 1
                if(hound_3[x] < hare[x]):
                    score += dist_hound2_hare - 1
                if(hound_1[x] == hare[x]):
                    score += dist_hound1_hare
                if(hound_2[x] == hare[x]):
                    score += dist_hound2_hare
                if(hound_3[x] == hare[x]):
                    score += dist_hound3_hare


        return score

    def estimeaza_scor(self, adancime):
        t_final = self.final()
        if t_final == Joc.JMAX:
            return (99 + adancime)
        elif t_final == Joc.JMIN:
            return (-99 - adancime)
        else:
            return self.calculeaza_scor(Joc.JMAX) - self.calculeaza_scor(Joc.JMIN)

    def __str__(self):
        sir = ("  " + str(self.matr[1]) + "-" + str(self.matr[4]) + "-" + str(self.matr[7]) + "\n"
        + " /|\|/|\ \n" + str(self.matr[0]) + "-" + str(self.matr[2]) + "-" + str(self.matr[5]) + "-"+ str(self.matr[8]) + "-"+ str(self.matr[10]) + "\n"
        + " \|/|\|/ \n" + "  " + str(self.matr[3]) + "-" + str(self.matr[6]) + "-" + str(self.matr[9]) + "\n")


        return sir


class Stare:
    """
    Clasa folosita de algoritmii minimax si alpha-beta
    Are ca proprietate tabla de joc
    Functioneaza cu conditia ca in cadrul clasei Joc sa fie definiti JMIN si JMAX (cei doi jucatori posibili)
    De asemenea cere ca in clasa Joc sa fie definita si o metoda numita mutari_joc() care ofera lista cu
    configuratiile posibile in urma mutarii unui jucator
    """

    ADANCIME_MAX = None

    def __init__(self, tabla_joc, j_curent, adancime, parinte=None, scor=None):
        self.tabla_joc = tabla_joc  # un obiect de tip Joc => „tabla_joc.matr”
        self.j_curent = j_curent  # simbolul jucatorului curent

        # adancimea in arborele de stari
        #	(scade cu cate o unitate din „tata” in „fiu”)
        self.adancime = adancime

        # scorul starii (daca e finala, adica frunza a arborelui)
        # sau scorul celei mai bune stari-fiice (pentru jucatorul curent)
        self.scor = scor

        # lista de mutari posibile din starea curenta
        self.mutari_posibile = []  # lista va contine obiecte de tip Stare

        # cea mai buna mutare din lista de mutari posibile pentru jucatorul curent
        self.stare_aleasa = None

    def IsAvailable(self,pos_player,pos_wish):
        player = [
         [[1,2,3],[-1]]#0
        ,[[2,4,5],[-1]]#1
        ,[[1,5,3],[-1]]#2
        ,[[2,5,6],[-1]]#3
        ,[[5,7],[1]] #4
        ,[[4,6,7,9,8],[1,2,3]]#5
        ,[[5,9],[3]] #6
        ,[[8,10],[5,4]] #7
        ,[[7,9,10],[5]] #8
        ,[[8,10],[6,5]] #9
        ,[[-1],[7,8,9]]] #10

        if(self.j_curent == 'c'):
            if(pos_wish in player[pos_player][0]):
                return True
            else:
                return False
        else:
            if(pos_wish in player[pos_player][0] or pos_wish in player[pos_player][1] and pos_wish):
                return True
            else:
                return False
    def jucator_opus(self):
        if self.j_curent == Joc.JMIN:
            return Joc.JMAX
        else:
            return Joc.JMIN

    def mutari_stare(self):
        l_mutari = self.tabla_joc.mutari_joc(self.j_curent)
        juc_opus = self.jucator_opus()

        l_stari_mutari = [Stare(mutare, juc_opus, self.adancime - 1, parinte=self) for mutare in l_mutari]
        return l_stari_mutari

    def __str__(self):
        sir = str(self.tabla_joc) + "(Juc curent:" + self.j_curent + ")\n"
        return sir




def min_max(stare):
    # Daca am ajuns la o frunza a arborelui, adica:
    # - daca am expandat arborele pana la adancimea maxima permisa
    # - sau daca am ajuns intr-o configuratie finala de joc
    if stare.adancime == 0 or stare.tabla_joc.final():
        # calculam scorul frunzei apeland "estimeaza_scor"
        stare.scor = stare.tabla_joc.estimeaza_scor(stare.adancime)
        return stare

    # Altfel, calculez toate mutarile posibile din starea curenta
    stare.mutari_posibile = stare.mutari_stare()

    # aplic algoritmul minimax pe toate mutarile posibile (calculand astfel subarborii lor)
    mutari_scor = [min_max(mutare) for mutare in stare.mutari_posibile]


    if stare.j_curent == Joc.JMAX:
        # daca jucatorul e JMAX aleg starea-fiica cu scorul maxim
        stare.stare_aleasa = max(mutari_scor, key=lambda x: x.scor)
    else:
        # daca jucatorul e JMIN aleg starea-fiica cu scorul minim
        stare.stare_aleasa = min(mutari_scor, key=lambda x: x.scor)

    # actualizez scorul „tatalui” = scorul „fiului” ales
    stare.scor = stare.stare_aleasa.scor
    return stare


def alpha_beta(alpha, beta, stare):
    # Daca am ajuns la o frunza a arborelui, adica:
    # - daca am expandat arborele pana la adancimea maxima permisa
    # - sau daca am ajuns intr-o configuratie finala de joc
    if stare.adancime == 0 or stare.tabla_joc.final():
        # calculam scorul frunzei apeland "estimeaza_scor"
        stare.scor = stare.tabla_joc.estimeaza_scor(stare.adancime)
        return stare

    # Conditia de retezare:
    if alpha >= beta:
        return stare  # este intr-un interval invalid, deci nu o mai procesez

    # Calculez toate mutarile posibile din starea curenta (toti „fiii”)
    stare.mutari_posibile = stare.mutari_stare()

    if stare.j_curent == Joc.JMAX:
        scor_curent = float('-inf')  # scorul „tatalui” de tip MAX

        # pentru fiecare „fiu” de tip MIN:
        for mutare in stare.mutari_posibile:
            # calculeaza scorul fiului curent
            stare_noua = alpha_beta(alpha, beta, mutare)

            # incerc sa imbunatatesc (cresc) scorul si alfa
            # „tatalui” de tip MAX, folosind scorul fiului curent
            if scor_curent < stare_noua.scor:
                stare.stare_aleasa = stare_noua
                scor_curent = stare_noua.scor

            if alpha < stare_noua.scor:
                alpha = stare_noua.scor
                if alpha >= beta:  # verific conditia de retezare
                    break  # NU se mai extind ceilalti fii de tip MIN


    elif stare.j_curent == Joc.JMIN:
        scor_curent = float('inf')  # scorul „tatalui” de tip MIN

        # pentru fiecare „fiu” de tip MAX:
        for mutare in stare.mutari_posibile:
            stare_noua = alpha_beta(alpha, beta, mutare)

            # incerc sa imbunatatesc (scad) scorul si beta
            # „tatalui” de tip MIN, folosind scorul fiului curent
            if scor_curent > stare_noua.scor:
                stare.stare_aleasa = stare_noua
                scor_curent = stare_noua.scor

            if beta > stare_noua.scor:
                beta = stare_noua.scor
                if alpha >= beta:  # verific conditia de retezare
                    break  # NU se mai extind ceilalti fii de tip MAX

    # actualizez scorul „tatalui” = scorul „fiului” ales
    stare.scor = stare.stare_aleasa.scor

    return stare


def afis_daca_final(stare_curenta):

    final = stare_curenta.tabla_joc.final()
    if (final):
        if(final == 'c'):
            print("A castigat cainele!")
        else:
            print("A castigat iepurele!")
        return True

    return False





def main():
    #init
    numar_mutari_jucator = 0
    numar_mutari_calculator = 0
    t_joc_inceput = int(round(time.time()))
    nivel = 0
    raspuns_valid = False
    while not raspuns_valid:
        tip_algoritm = input("Algoritmul pe care-l doriti[1-MinMax/2-AlphaBeta] : ")
        if tip_algoritm == "exit":
            t_joc_final = int(round(time.time()))
            print("Jocul a tinut timp de : ", str(t_joc_final - t_joc_inceput) + " secunde\n")
            return 0
        elif tip_algoritm in ['1', '2']:
            raspuns_valid = True
        else:
            print("Nu ati ales o varianta corecta.")
    raspuns_valid = False
    while not raspuns_valid:
        simbol = input("Cu cine doriti sa jucati?[1-Hounds/2-Hares] : ")
        if simbol == "exit":
            t_joc_final = int(round(time.time()))
            print("Jocul a tinut timp de : ", str(t_joc_final - t_joc_inceput) + " secunde\n")
            return 0
        elif simbol in ['1', '2']:
            if(simbol == '1'):
                Joc.JMIN = 'c'
                Joc.JMAX = 'i'
            else:
                Joc.JMIN = 'i'
                Joc.JMAX = 'c'
            raspuns_valid = True
        else:
            print("Nu ati ales o varianta corecta.")
    raspuns_valid = False
    while not raspuns_valid:
        n = input("Nivelul de joc?[1-Incepator/2-Medium/3-Hard] : ")
        if n == "exit":
            t_joc_final = int(round(time.time()))
            print("Jocul a tinut timp de : ", str(t_joc_final - t_joc_inceput) + " secunde\n")
            return 0
        elif n in ['1', '2', '3']:
            if(n == '1'):
                Stare.ADANCIME_MAX = 2
            elif (n == '2'):
                Stare.ADANCIME_MAX = 4
            elif (n == '3'):
                Stare.ADANCIME_MAX = 6
            raspuns_valid = True
        else:
            print("Nu ati ales o varianta corecta.")
    tabla_curenta = Joc()
    print(str(tabla_curenta))
    stare_curenta = Stare(tabla_curenta, 'c', Stare.ADANCIME_MAX)
    while True:
        if (stare_curenta.j_curent == Joc.JMIN):
            raspuns_valid = False
            while not raspuns_valid:
                try:
                        t_inainte = int(round(time.time() * 1000))
                        if(Joc.JMIN != 'c'):

                            numar_tabla = input("Un numar liber : ")
                            if(numar_tabla == "exit"):
                                t_joc_final = int(round(time.time()))
                                print("Jocul a tinut timp de : ", str(t_joc_final - t_joc_inceput) + " secunde\n")
                                return 0
                            else:
                                numar_tabla = int(numar_tabla)
                            while (numar_tabla < 0 or numar_tabla > 10):
                                numar_tabla = input("Un numar liber : ")
                                if (numar_tabla == "exit"):
                                    t_joc_final = int(round(time.time()))
                                    print("Jocul a tinut timp de : ", str(t_joc_final - t_joc_inceput) + " secunde\n")
                                    return 0
                                else:
                                    numar_tabla = int(numar_tabla)

                            while(stare_curenta.IsAvailable(stare_curenta.tabla_joc.Hare,numar_tabla) == False):
                                numar_tabla = input("Un numar liber : ")
                                if (numar_tabla == "exit"):
                                    t_joc_final = int(round(time.time()))
                                    print("Jocul a tinut timp de : ", str(t_joc_final - t_joc_inceput) + " secunde\n")
                                    return 0
                                else:
                                    numar_tabla = int(numar_tabla)
                            while(numar_tabla in stare_curenta.tabla_joc.Hounds or numar_tabla == stare_curenta.tabla_joc.Hare):
                                numar_tabla = input("Un numar liber : ")
                                if (numar_tabla == "exit"):
                                    t_joc_final = int(round(time.time()))
                                    print("Jocul a tinut timp de : ", str(t_joc_final - t_joc_inceput) + " secunde\n")
                                    return 0
                                else:
                                    numar_tabla = int(numar_tabla)
                            stare_curenta.tabla_joc.matr[stare_curenta.tabla_joc.Hare] = str(stare_curenta.tabla_joc.Hare)
                            stare_curenta.tabla_joc.Hare = numar_tabla
                            stare_curenta.tabla_joc.matr[numar_tabla] = Joc.JMIN
                        else:
                            while(1):
                                cainele_pe_table = input("Cainele de pe pozitia : ")

                                if (cainele_pe_table == "exit"):
                                    t_joc_final = int(round(time.time()))
                                    print("Jocul a tinut timp de : ", str(t_joc_final - t_joc_inceput) + " secunde\n")
                                    return 0
                                else:
                                    cainele_pe_table = int(cainele_pe_table)
                                numar_tabla = input("Un numar liber : ")
                                if (numar_tabla == "exit"):
                                    t_joc_final = int(round(time.time()))
                                    print("Jocul a tinut timp de : ", str(t_joc_final - t_joc_inceput) + " secunde\n")
                                    return 0
                                else:
                                    numar_tabla = int(numar_tabla)
                                if (numar_tabla < 0 or numar_tabla > 10):
                                    continue
                                if (numar_tabla in stare_curenta.tabla_joc.Hounds):
                                    continue
                                if (cainele_pe_table not in stare_curenta.tabla_joc.Hounds):
                                    continue
                                if(stare_curenta.IsAvailable(cainele_pe_table,numar_tabla) == False):
                                     continue

                                break
                            for i in range(3):
                                if(stare_curenta.tabla_joc.Hounds[i] == cainele_pe_table):
                                    stare_curenta.tabla_joc.Hounds[i] = numar_tabla
                                    break
                            stare_curenta.tabla_joc.matr[cainele_pe_table] = str(cainele_pe_table)
                            stare_curenta.tabla_joc.matr[numar_tabla] = Joc.JMIN
                        raspuns_valid = True
                except ValueError:
                    print("Numarul nu este bun")
                print("\nTabla dupa mutarea jucatorului")
                t_dupa = int(round(time.time() * 1000))
                numar_mutari_jucator += 1
                print("Runda jucatorului a tinut timp de ", str(t_dupa - t_inainte) + " milisecunde\n")
                if (numar_mutari_calculator == 1):
                    print("Jucatorul a facut prima mutare!\n")
                else:
                    print("Jucatorul a mutat de ", numar_mutari_jucator, " ori" "\n")
                print(str(stare_curenta))

                if (afis_daca_final(stare_curenta)):
                    t_joc_final = int(round(time.time()))
                    print("Jocul a tinut timp de : ", str(t_joc_final - t_joc_inceput) + " secunde\n")
                    return 0
                stare_curenta.j_curent = stare_curenta.jucator_opus()
        else:
            t_inainte = int(round(time.time() * 1000))
            if tip_algoritm == '1':
                stare_actualizata = min_max(stare_curenta)
            else:
                stare_actualizata = alpha_beta(-500, 500, stare_curenta)
            stare_curenta.tabla_joc = stare_actualizata.stare_aleasa.tabla_joc
            print("Tabla dupa mutarea calculatorului")
            print(str(stare_curenta))
            t_dupa = int(round(time.time() * 1000))
            print("Runda calculatorului a tinut timp de " + str(t_dupa - t_inainte) + " milisecunde.")
            numar_mutari_calculator+=1
            if(numar_mutari_calculator == 1):
                print("Calculatorul a facut prima mutare!\n")
            else:
                print("Calculatorul a mutat de ", numar_mutari_calculator, " ori" "\n")
            if (afis_daca_final(stare_curenta)):
                t_joc_final = int(round(time.time()))
                print("Jocul a tinut timp de : ", str(t_joc_final - t_joc_inceput) + " secunde\n")
                return 0
            stare_curenta.j_curent = stare_curenta.jucator_opus()


if __name__ == "__main__":
    main()