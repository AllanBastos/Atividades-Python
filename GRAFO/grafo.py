class VerticeInvalidoException(Exception):
    pass


class ArestaInvalidaException(Exception):
    pass


class Grafo:
    QTDE_MAX_SEPARADOR = 1
    SEPARADOR_ARESTA = '-'

    def __init__(self, N=[], A={}):
        """
        Constrói um objeto do tipo Grafo. Se nenhum parâmetro for passado, cria um Grafo vazio.
        Se houver alguma aresta ou algum vértice inválido, uma exceção é lançada.
        :param N: Uma lista dos vértices (ou nodos) do GRAFO.
        :param V: Uma dicionário que guarda as arestas do GRAFO. A chave representa o nome da aresta e o valor é uma string que contém dois vértices separados por um traço.
        """
        for v in N:
            if not (Grafo.verticeValido(v)):
                raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

        self.N = N

        for a in A:
            if not (self.arestaValida(A[a])):
                raise ArestaInvalidaException('A aresta ' + A[a] + ' é inválida')

        self.A = A

    def arestaValida(self, aresta=''):
        """
        Verifica se uma aresta passada como parâmetro está dentro do padrão estabelecido.
        Uma aresta é representada por um string com o formato a-b, onde:
        a é um substring de aresta que é o nome de um vértice adjacente à aresta.
        - é um caractere separador. Uma aresta só pode ter um único caractere como esse.
        b é um substring de aresta que é o nome do outro vértice adjacente à aresta.
        Além disso, uma aresta só é válida se conectar dois vértices existentes no GRAFO.
        :param aresta: A aresta que se quer verificar se está no formato correto.
        :return: Um valor booleano que indica se a aresta está no formato correto.
        """

        # Não pode haver mais de um caractere separador
        if aresta.count(Grafo.SEPARADOR_ARESTA) != Grafo.QTDE_MAX_SEPARADOR:
            return False

        # Índice do elemento separador
        i_traco = aresta.index(Grafo.SEPARADOR_ARESTA)

        # O caractere separador não pode ser o primeiro ou o último caractere da aresta
        if i_traco == 0 or aresta[-1] == Grafo.SEPARADOR_ARESTA:
            return False

        # Verifica se as arestas antes de depois do elemento separador existem no Grafo
        if not (self.existeVertice(aresta[:i_traco])) or not (self.existeVertice(aresta[i_traco + 1:])):
            return False

        return True

    @classmethod
    def verticeValido(self, vertice=''):

        """
        Verifica se um vértice passado como parâmetro está dentro do padrão estabelecido.
        Um vértice é um string qualquer que não pode ser vazio e nem conter o caractere separador.
        :param vertice: Um string que representa o vértice a ser analisado.
        :return: Um valor booleano que indica se o vértice está no formato correto.
        """
        return vertice != '' and vertice.count(Grafo.SEPARADOR_ARESTA) == 0

    def existeVertice(self, vertice=''):
        '''
        Verifica se um vértice passado como parâmetro pertence ao GRAFO.
        :param vertice: O vértice que deve ser verificado.
        :return: Um valor booleano que indica se o vértice existe no GRAFO.
        '''
        return Grafo.verticeValido(vertice) and self.N.count(vertice) > 0

    def existeAresta(self, aresta=''):
        '''
        Verifica se uma aresta passada como parâmetro pertence ao GRAFO.
        :param aresta: A aresta a ser verificada
        :return: Um valor booleano que indica se a aresta existe no GRAFO.
        '''
        existe = False
        if Grafo.arestaValida(self, aresta):
            for k in self.A:
                if aresta == self.A[k]:
                    existe = True

        return existe

    def adicionaVertice(self, v):
        '''
        Adiciona um vértice no Grafo caso o vértice seja válido e não exista outro vértice com o mesmo nome
        :param v: O vértice a ser adicionado
        :raises: VerticeInvalidoException se o vértice passado como parâmetro não puder ser adicionado
        '''
        if self.verticeValido(v) and not self.existeVertice(v):
            self.N.append(v)
        else:
            raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

    def adicionaAresta(self, nome, a):
        """
        Adiciona uma aresta no Grafo caso a aresta seja válida e não exista outra aresta com o mesmo nome
        :param v: A aresta a ser adicionada
        :raises: ArestaInvalidaException se a aresta passada como parâmetro não puder ser adicionada
        """
        if self.arestaValida(a):
            self.A[nome] = a
        else:
            ArestaInvalidaException('A aresta ' + self.A[a] + ' é inválida')

    """
        ======================================================
       ||           ##### minhas funções #####               ||
        ======================================================
    """

    # roteiro 1
    def vertices_nao_adjacentes(self):
        vertices = self.N
        arestas = self.A.values()
        nao_adjacentes = []
        for i in vertices:
            for j in vertices:
                verificar_indo = "{}-{}".format(i, j)
                verificar_vindo = "{}-{}".format(j, i)
                if verificar_indo not in arestas and verificar_vindo not in arestas:
                    nao_adjacentes.append(verificar_indo)
        return nao_adjacentes

    def ha_laco(self):
        arestas = self.A.values()
        for i in arestas:
            a, b = i.split('-')
            if a == b:
                return True
        return False

    def ha_paralelas(self):
        arestas = list(self.A.values())
        arestas_ao_contrario = []
        cont = 0
        for i in arestas:
            a, b = i.split('-')
            arestas_ao_contrario.append('{}-{}'.format(b, a))

        for i in range(len(arestas)):
            for j in range(len(arestas)):
                if arestas[i] == arestas[j] or arestas_ao_contrario == arestas[i]:
                    cont += 1
        if cont > len(arestas):
            return True
        return False

    def grau(self, v):
        cont = 0
        arestas = list(self.A.values())

        for i in arestas:
            a, b = i.split('-')
            if a == v or b == v:
                cont += 1
        return cont

    def arestas_sobre_vertice(self, v):
        incidentes = []
        arestas = list(self.A.values())
        key = list(self.A.keys())

        for i in range(len(arestas)):
            a, b = arestas[i].split('-')
            if a == v or b == v:
                incidentes.append(key[i])

        return incidentes

    def so_ha_laco(self):
        vertices = self.N
        arestas = self.A.values()

        for i in vertices:
            for j in vertices:
                verificar = "{}-{}".format(i, j)
                if i != j and verificar in arestas:
                    return False
        return True

    def eh_completo(self):
        n_ver_na = len(self.vertices_nao_adjacentes())
        n_ver = len(self.N)
        if n_ver == 1:
            return True
        elif n_ver_na > n_ver or (self.so_ha_laco()):
            return False

        return True

    # roteiro 2
    def buscar_profundidade_dfs(self, raiz, dfs=[]):
        if raiz not in self.N:
            return None
        av = self.arestas_sobre_vertice(raiz)
        for i in av:
            if i not in dfs:
                if len(dfs) == 0:
                    dfs.append(raiz)
                a, j = self.A[i].split("-")
                if raiz == j:
                    a, j = j, a
                if (raiz not in dfs or j not in dfs):
                    dfs.append(i)
                    dfs.append(j)
                    self.buscar_profundidade_dfs(j, dfs)
        if raiz == dfs[0]:
            aux = dfs.copy()
            dfs.clear()
            return aux
        return dfs

    # roteiro 3
    def ciclo(self):

        av = self.A.items()  # Contém chave de ligação entre aresta e vertice
        vertices = self.N  # Lista de vertices

        import random  # Definir o vertice da raiz

        lista_ciclo = []  # Final do laço
        vertices_proib = []  # vertices a desconsiderar
        arestas_proib = []  # arestas a descconsiderar
        vertice_prox = random.choice(vertices)  # Próximo vertice a ser buscado
        while True:
            eh = False  # Auxiliar de busca

            for e in av:
                # Varrendo posições
                aresta = e[0]
                v1 = e[1][0]
                v2 = e[1][2]
                # Se meu vertice 1 é igual meu vertice de procura
                if (v1 == vertice_prox):
                    if (v1 not in lista_ciclo and v1 not in vertices_proib):
                        lista_ciclo.append(v1)
                    if (aresta not in lista_ciclo and aresta not in arestas_proib):
                        lista_ciclo.append(aresta)
                        if (v2 not in lista_ciclo and v2 not in vertices_proib):
                            lista_ciclo.append(v2)
                            vertice_prox = v2
                            eh = True
                            break
                        else:
                            lista_ciclo.append(v2)
                            return lista_ciclo

            if not eh:
                for e in av:
                    aresta = e[0]
                    v1 = e[1][0]
                    v2 = e[1][2]
                    if (v2 == vertice_prox):
                        if (v2 not in lista_ciclo and v2 not in vertices_proib):
                            lista_ciclo.append(v2)
                        if (aresta not in lista_ciclo and aresta not in arestas_proib):
                            lista_ciclo.append(aresta)
                            if (v1 not in lista_ciclo and v1 not in vertices_proib):
                                lista_ciclo.append(v1)
                                vertice_prox = v1
                                eh = True
                                break
                            else:
                                lista_ciclo.append(v1)
                                return lista_ciclo

            if not eh:
                if (len(lista_ciclo) > 1):
                    vertices_proib.append(lista_ciclo.pop())
                    arestas_proib.append(lista_ciclo.pop())
                    vertice_prox = lista_ciclo[-1]
                else:
                    return False

    def ha_ciclo(self):

        ha_ciclo = self.ciclo()  # Usa ciclo com auxiliar nas funções de verificar se tem ou não ciclo
        lista_ciclo = []  # Vertices e arestas do ciclo
        ciclo_inicial = False  # Ponto inicial
        if ha_ciclo:  # Teste se ha_ciclo não é null
            for e in ha_ciclo:  # Se ha_ciclo for verdade, nesta linha ele irá percorrer
                if (e == ha_ciclo[-1]):  # Quando encontrar
                    ciclo_inicial = True  # Será o marco inicial
                if ciclo_inicial:
                    lista_ciclo.append(e)  # Começa adicionar elementos
            return lista_ciclo
        return False

    def caminho_entre_dois(self, x, y):

        av = self.A.items()  # Dicionário demostra as arestas com as suas chaves de ligação
        vertices_ligados = self.N  # Vertices do grafo

        # Preciso verificar se os vertices existe

        if x not in vertices_ligados or y not in vertices_ligados:
            return False

        lista_caminho = []
        vertices_prob = []
        arestas_prob = []
        vertices_prox = x

        while True:
            if (len(lista_caminho) > 0 and lista_caminho[0] == x and lista_caminho[-1] == y):
                return lista_caminho

            else:
                eh = False

                for e in av:
                    aresta = e[0]
                    v1 = e[1][0]
                    v2 = e[1][2]

                    if (v1 == vertices_prox):
                        if (v1 not in lista_caminho and v1 not in vertices_prob):
                            lista_caminho.append(v1)

                        if (aresta not in lista_caminho and aresta not in arestas_prob):
                            lista_caminho.append(aresta)
                            if (v2 not in lista_caminho and v2 not in vertices_prob):
                                lista_caminho.append(v2)
                                vertices_prox = v2
                                eh = True
                                break
                            else:
                                arestas_prob.append(lista_caminho.pop())

                if not eh:
                    for e in av:
                        aresta = e[0]
                        v1 = e[1][0]
                        v2 = e[1][2]

                        if (v2 == vertices_prox):
                            if (v2 not in lista_caminho and v2 not in vertices_prob):
                                lista_caminho.append(v2)

                            if (aresta not in lista_caminho and aresta not in arestas_prob):
                                lista_caminho.append(aresta)
                                if (v1 not in lista_caminho and v1 not in vertices_prob):
                                    lista_caminho.append(v1)
                                    vertices_prox = v1
                                    eh = True
                                    break
                                else:
                                    arestas_prob.append(lista_caminho.pop())
                if not eh:
                    if (len(lista_caminho) > 1):
                        # Para iniciar a busca pelo ultimos
                        vertices_prob.append(lista_caminho.pop())
                        arestas_prob.append(lista_caminho.pop())
                        vertices_prox = lista_caminho[-1]

                    else:
                        return False

    def caminho(self, n):

        vertices_ligados = self.N

        for v1 in vertices_ligados:
            for v2 in vertices_ligados:
                av = self.caminho_entre_dois(v1, v2)
                if (n * 2 + 1 == len(av)):
                    return av
        return False

    def conexo(self):

        vertices_ligados = self.N

        # Verificar os caminhos entre os vertices
        for v1 in vertices_ligados:
            for v2 in vertices_ligados:
                if (not self.caminho_entre_dois(v1, v2)):
                    # Se não existir um caminho entre dois vertices retornará falso
                    # Se existir retorna verdadeiro depois de verificar todos os caminhos
                    return False
        return True

    """
    ##### fim das minhas funções #####
    """

    def __str__(self):
        '''
        Fornece uma representação do tipo String do GRAFO.
        O String contém um sequência dos vértices separados por vírgula, seguido de uma sequência das arestas no formato padrão.
        :return: Uma string que representa o GRAFO
        '''
        grafo_str = ''

        for v in range(len(self.N)):
            grafo_str += self.N[v]
            if v < (len(self.N) - 1):  # Só coloca a vírgula se não for o último vértice
                grafo_str += ", "

        grafo_str += '\n'

        for i, a in enumerate(self.A):
            grafo_str += self.A[a]
            if not (i == len(self.A) - 1):  # Só coloca a vírgula se não for a última aresta
                grafo_str += ", "

        return grafo_str
