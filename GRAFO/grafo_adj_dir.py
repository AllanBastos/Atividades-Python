import sys


class VerticeInvalidoException(Exception):
    pass

class ArestaInvalidaException(Exception):
    pass

class MatrizInvalidaException(Exception):
    pass

class ValorInvalidoException(Exception):
    pass

class Grafo:

    QTDE_MAX_SEPARADOR = 1
    SEPARADOR_ARESTA = '-'
    __maior_vertice = 0
    __PESOS = {}

    def __init__(self, V=None, M=None):
        '''
        Constrói um objeto do tipo Grafo. Se nenhum parâmetro for passado, cria um Grafo vazio.
        Se houver alguma aresta ou algum vértice inválido, uma exceção é lançada.
        :param V: Uma lista dos vértices (ou nodos) do grafo.
        :param V: Uma matriz de adjacência que guarda as arestas do grafo. Cada entrada da matriz tem um inteiro que indica a quantidade de arestas que ligam aqueles vértices
        '''


        if V == None:
            V = list()
        if M == None:
            M = list()

        self.__PESOS = {}

        for v in V:
            if not(Grafo.verticeValido(v)):
                raise VerticeInvalidoException('O vértice ' + v + ' é inválido')
            if len(v) > self.__maior_vertice:
                self.__maior_vertice = len(v)

        self.N = list(V)

        if M == []:
            for k in range(len(V)):
                M.append(list())
                for l in range(len(V)):
                    M[k].append(0)
                    # if k>l:
                    #     M[k].append('-')
                    # else:
                    #     M[k].append(0)


        if len(M) != len(V):
            raise MatrizInvalidaException('A matriz passada como parâmetro não tem o tamanho correto')

        for c in M:
            if len(c) != len(V):
                raise MatrizInvalidaException('A matriz passada como parâmetro não tem o tamanho correto')

        for i in range(len(V)):
            for j in range(len(V)):
                # '''
                # Verifica se os índices passados como parâmetro representam um elemento da matriz abaixo da diagonal principal.
                # Além disso, verifica se o referido elemento é um traço "-". Isso indica que a matriz é não direcionada e foi construída corretamente.
                # '''
                # if i>j and not(M[i][j] == '-'):
                #     raise MatrizInvalidaException('A matriz não representa uma matriz não direcionada')


                aresta = V[i] + Grafo.SEPARADOR_ARESTA + V[j]
                if not(self.arestaValida(aresta)):
                    raise ArestaInvalidaException('A aresta ' + aresta + ' é inválida')

        self.M = list(M)

    def arestaValida(self, aresta=''):
        '''
        Verifica se uma aresta passada como parâmetro está dentro do padrão estabelecido.
        Uma aresta é representada por um string com o formato a-b, onde:
        a é um substring de aresta que é o nome de um vértice adjacente à aresta.
        - é um caractere separador. Uma aresta só pode ter um único caractere como esse.
        b é um substring de aresta que é o nome do outro vértice adjacente à aresta.
        Além disso, uma aresta só é válida se conectar dois vértices existentes no grafo.
        :param aresta: A aresta que se quer verificar se está no formato correto.
        :return: Um valor booleano que indica se a aresta está no formato correto.
        '''

        # Não pode haver mais de um caractere separador
        if aresta.count(Grafo.SEPARADOR_ARESTA) != Grafo.QTDE_MAX_SEPARADOR:
            return False

        # Índice do elemento separador
        i_traco = aresta.index(Grafo.SEPARADOR_ARESTA)

        # O caractere separador não pode ser o primeiro ou o último caractere da aresta
        if i_traco == 0 or aresta[-1] == Grafo.SEPARADOR_ARESTA:
            return False

        if not(self.existeVertice(aresta[:i_traco])) or not(self.existeVertice(aresta[i_traco+1:])):
            return False

        return True

    @classmethod
    def verticeValido(self, vertice: str):
        '''
        Verifica se um vértice passado como parâmetro está dentro do padrão estabelecido.
        Um vértice é um string qualquer que não pode ser vazio e nem conter o caractere separador.
        :param vertice: Um string que representa o vértice a ser analisado.
        :return: Um valor booleano que indica se o vértice está no formato correto.
        '''
        return vertice != '' and vertice.count(Grafo.SEPARADOR_ARESTA) == 0

    def existeVertice(self, vertice: str):
        '''
        Verifica se um vértice passado como parâmetro pertence ao grafo.
        :param vertice: O vértice que deve ser verificado.
        :return: Um valor booleano que indica se o vértice existe no grafo.
        '''
        return Grafo.verticeValido(vertice) and self.N.count(vertice) > 0

    def __primeiro_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o vértice X
        :param a: a aresta a ser analisada
        :return: O primeiro vértice da aresta
        '''
        return a[0:a.index(Grafo.SEPARADOR_ARESTA)]

    def __segundo_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o vértice Y
        :param a: A aresta a ser analisada
        :return: O segundo vértice da aresta
        '''
        return a[a.index(Grafo.SEPARADOR_ARESTA)+1:]

    def __indice_primeiro_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o índice do vértice X na lista de vértices
        :param a: A aresta a ser analisada
        :return: O índice do primeiro vértice da aresta na lista de vértices
        '''
        return self.N.index(self.__primeiro_vertice_aresta(a))

    def __indice_segundo_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o índice do vértice Y na lista de vértices
        :param a: A aresta a ser analisada
        :return: O índice do segundo vértice da aresta na lista de vértices
        '''
        return self.N.index(self.__segundo_vertice_aresta(a))

    def existeAresta(self, a: str):
        '''
        Verifica se uma aresta passada como parâmetro pertence ao grafo.
        :param aresta: A aresta a ser verificada
        :return: Um valor booleano que indica se a aresta existe no grafo.
        '''
        existe = False
        if Grafo.arestaValida(self, a):
            for i in range(len(self.M)):
                for j in range(len(self.M)):
                    if self.M[self.__indice_primeiro_vertice_aresta(a)][self.__indice_segundo_vertice_aresta(a)]:
                        existe = True

        return existe

    def adicionaVertice(self, v):
        '''
        Inclui um vértice no grafo se ele estiver no formato correto.
        :param v: O vértice a ser incluído no grafo.
        :raises VerticeInvalidoException se o vértice já existe ou se ele não estiver no formato válido.
        '''
        if v in self.N:
            raise VerticeInvalidoException('O vértice {} já existe'.format(v))

        if self.verticeValido(v):
            if len(v) > self.__maior_vertice:
                self.__maior_vertice = len(v)

            self.N.append(v) # Adiciona vértice na lista de vértices
            self.M.append([]) # Adiciona a linha

            for k in range(len(self.N)):
                if k != len(self.N) -1:
                    self.M[k].append(0) # adiciona os elementos da coluna do vértice
                    self.M[self.N.index(v)].append(0) # adiciona os elementos da linha do vértice
                else:
                    self.M[self.N.index(v)].append(0)  # adiciona um zero no último elemento da linha
        else:
            raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

    def adicionaAresta(self, a):
        '''
        Adiciona uma aresta ao grafo no formato X-Y, onde X é o primeiro vértice e Y é o segundo vértice
        :param a: a aresta no formato correto
        :raise: lança uma exceção caso a aresta não estiver em um formato válido
        '''
        if self.arestaValida(a):
            i_a1 = self.__indice_primeiro_vertice_aresta(a)
            i_a2 = self.__indice_segundo_vertice_aresta(a)
            # if i_a1 < i_a2:
            #     self.M[i_a1][i_a2] += 1
            # else:
            #     self.M[i_a2][i_a1] += 1
            self.M[i_a1][i_a2] += 1
            self.__PESOS[a] = 1
        else:
            raise ArestaInvalidaException('A aresta {} é inválida'.format(a))

    def remove_aresta(self, a):
        '''
        Remove uma aresta ao grafo no formato X-Y, onde X é o primeiro vértice e Y é o segundo vértice
        :param a: a aresta no formato correto
        :raise: lança uma exceção caso a aresta não estiver em um formato válido
        '''
        if self.arestaValida(a):
            if self.existeAresta(a):
                i_a1 = self.__indice_primeiro_vertice_aresta(a)
                i_a2 = self.__indice_segundo_vertice_aresta(a)
                # if i_a1 < i_a2:
                #     self.M[i_a1][i_a2] -= 1
                # else:
                #    self.M[i_a2][i_a1] -= 1
                self.M[i_a1][i_a2] -= 1
        else:
            raise ArestaInvalidaException('A aresta {} é inválida'.format(a))



    ### Meus codigos

    def __copy(self, Matriz):
        aux = []
        for i in range(len(Matriz)):
            aux.append([])
            for p in range(len(Matriz[i])):
                aux[i].append(Matriz[i][p])
        return aux


    def caminho_entre_dois(self, v1, v2, visitados=[]):
        if (self.N.index(v1) > self.N.index(
                v2)):  # Já que o grafo não é direcionado então 'J-Z' == 'Z-J' e o índice de v1 é sempre <= ao índice de v2
            aux = v2  # já que apenas da diagonal principal para cima é considerada na matriz de adjacência para grafos não direcionados.
            v2 = v1
            v1 = aux

        visitados.append(v1)
        ind_1 = self.N.index(v1)
        ind_2 = self.N.index(v2)

        if (self.M[ind_1][ind_2] > 0):
            return True

        vertices = self.vertices_adjacentes_euleriano(v1, visitados)
        if (vertices == []):
            return False

        if (self.grau(v1) == 0 or self.grau(v2) == 0):
            return False

        for vertice in vertices:
            if (self.caminho_entre_dois(vertice, v2, visitados)):
                return True

        return False


    def vertices_nao_adjacentes(self):
        vertives_n_adj = []
        matriz = self.M
        vertice = self.N

        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if matriz[i][j] == 0:
                    vertives_n_adj.append("{}-{}".format(vertice[i], vertice[j]))

        return vertives_n_adj


    def ha_laco(self):
        for i in range(len(self.M)):
            if self.M[i][i] > 0:
                return True
        return False


    def grau(self, v):

        indice = self.N.index(v)
        soma = 0

        for i in range(len(self.M)):
            for j in range(len(self.M)):
                if i == indice:
                    soma += self.M[i][j]

        return soma


    def ha_paralelas(self):
        for i in range(len(self.M)):
            for j in range(len(self.M[i])):
                if self.M[i][j] == 2:
                    return True
        return False


    def arestas_sobre_vertice(self, v):
        lista_arestas = []

        index = self.N.index(v)
        for i in range(len(self.M)):
            for j in range(len(self.M)):
                if i == index and self.M[i][j] > 0:
                    for l in range(self.M[i][j]):
                        lista_arestas.append(v + '-' + self.N[j])
                if j == index and self.M[i][j] > 0:
                    for k in range(self.M[i][j]):
                        lista_arestas.append(self.N[i] + '-' + v)
        return lista_arestas


    def conexo(self):
        vertice = self.N[0]
        for i in self.N[1::]:
            if not self.caminho_entre_dois(vertice, i, []):
                return False
        return True


    def eh_completo(self):
        # w = self.warshall()
        #
        # for i in range(len(w.M)):
        #     for j in range(len(w.M)):
        #         if w.M[i][j] == 0:
        #             return False
        # return True
        m = self.M
        for i in range(len(m)):
            if (sum(m[i]) + 1) < len(self.N):
                return False
        return True


    def caminho_euleriano(self):
        if not self.conexo():
            return []

        impar = 0
        vertice_impar = []
        for i in (self.N):
            if self.grau(i) % 2 != 0:
                impar += 1
                vertice_impar.append(i)

        if impar == 0 or impar == 2:
            matriz = self.M[:]
            for v in self.N:
                caminho = self.procurar_caminho_euleriano(v, [], [], matriz)
                if caminho != []:
                    caminho.append(v)
                    return caminho

        return []


    def matriz_vazia(self):
        for vertice in self.N:
            if (self.grau(vertice) > 0):
                return False
        return True


    def procurar_caminho_euleriano(self, v, caminho, visitados, matriz):
        visitados.append(v)
        vertices = self.vertices_adjacentes_euleriano(v, visitados)


        if self.matriz_vazia() and vertices == []:
            return True

        for i in vertices:
            indice1 = self.N.index(v)
            indice2 = self.N.index(i)
            if (indice1 > indice2):
                aux = indice2
                indice2 = indice1
                indice1 = aux

            matriz[indice1][indice2] -= 1
            aresta = v + self.SEPARADOR_ARESTA + i

            if (self.procurar_caminho_euleriano(i, caminho, visitados, matriz)):
                caminho.append(i)
                caminho.append(aresta)
                return caminho
            else:
                matriz[indice1][indice2] += 1

        return []


    def vertices_adjacentes_euleriano(self, vertice, visitados):
        vertices = []
        index = self.N.index(vertice) + 1

        for indice_1 in range(index):
            for indice_2 in range(indice_1, len(self.M)):
                if (self.M[indice_1][indice_2] > 0 and index - 1 in (indice_1, indice_2)):
                    v1, v2 = self.N[indice_1], self.N[indice_2]
                    if (v1 != vertice and (v1 not in visitados or self.grau(
                            v1) > 0)):
                        vertices.append(v1)
                    elif (v2 not in visitados or self.grau(v2) > 0):
                        vertices.append(v2)

        return vertices


    def warshall(self):
        E = self.__copy(self.M)

        for i in range(len(E)):
            for j in range(len(E)):
                if E[j][i] > 0:
                    for k in range(len(E)):
                        E[j][k] = max(E[j][k], E[i][k])

        w = Grafo(self.N)

        for i in range(len(E)):
            for j in range(len(E)):
                if E[i][j] > 0:
                    w.adicionaAresta(self.N[i] + self.SEPARADOR_ARESTA + self.N[j])


        return w


    def dijkstra(self, u, v):
        vertices = self.N
        MAX = sys.maxsize
        b = {}
        f = {}
        p = {}
        peso = self.__PESOS
        for i in vertices:
            b[i] = MAX
            f[i] = 0
            p[i] = None

        b[u] = 0
        f[u] = 1

        w = u

        while True:
            if w == v:
                caminho = []
                temp = w
                while temp != u:
                    caminho.append(p[temp])
                    temp = p[temp]
                caminho.reverse()
                return caminho

            adj = self.verticesAdj(w)

            for i in adj:
                dis = b[w] + peso["{}-{}".format(w, i)]
                if f[i] == 0 and b[i] > dis:
                    b[i] = dis
                    p[i] = w

            existe_r = False

            betas = []
            for i in vertices:
                if f[i] == 0:
                    betas.append(b[i])

            for i in vertices:
                if f[i] == 0 and b[i] < MAX and b[i] == min(betas):
                    existe_r = True
                    f[i] = 1
                    w = i
                    break

            if not existe_r:
                return "Caminho Inexistente"


    def VerificarAresta(self, A):
        if self.arestaValida(A):
            v = self.N
            indexa = v.index(A[0])
            indexb = v.index(A[2])
            for i in range(len(self.M)):
                for j in range(len(self.M)):
                    if self.M[indexa][indexb] > 0:
                        return True
                    else:
                        raise ArestaInvalidaException("A aresta {} não existe!".format(A))
        raise ArestaInvalidaException("A aresta {} é invalida!".format(A))


    def setPeso(self, a, p):
        if p < 1:
            raise ValorInvalidoException('O valor {} é invalido'.format(p))
        if self.VerificarAresta(a):
            self.__PESOS[a] = p


    def getPesos(self):
        return self.__PESOS


    def verticesAdj(self, v):
        matrix = self.M
        vertice = self.N
        index = vertice.index(v)
        adj = []
        for i in range(len(matrix)):
            if i == index:
                for j in range(len(matrix[i])):
                    if matrix[i][j] > 0:
                        adj.append(vertice[j])

        return adj


    def __str__(self):
        '''
        Fornece uma representação do tipo String do grafo.
        O String contém um sequência dos vértices separados por vírgula, seguido de uma sequência das arestas no formato padrão.
        :return: Uma string que representa o grafo
        '''

        # Dá o espaçamento correto de acordo com o tamanho do string do maior vértice
        espaco = ' '*(self.__maior_vertice)

        grafo_str = espaco + ' '

        for v in range(len(self.N)):
            grafo_str += self.N[v]
            if v < (len(self.N) - 1):  # Só coloca o espaço se não for o último vértice
                grafo_str += ' '

        grafo_str += '\n'

        for l in range(len(self.M)):
            grafo_str += self.N[l] + ' '
            for c in range(len(self.M)):
                grafo_str += str(self.M[l][c]) + ' '
            grafo_str += '\n'

        return grafo_str




