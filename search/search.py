# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"

    borda = util.Stack() #BP eh LIFO -> Pilha
    expandidos = []
    borda.push((problem.getStartState(), []))
    expandidos.append(problem.getStartState())

    while borda.isEmpty() == False:
        estado_atual, acoes = borda.pop()

        for proximo_estado in problem.getSuccessors(estado_atual):
            estado = proximo_estado[0]
            direcao = proximo_estado[1]
            if estado not in expandidos:
                if problem.isGoalState(estado):
                    return acoes + [direcao]
                else:
                    borda.push((estado, acoes + [direcao]) )
                    expandidos.append(estado)

    util.raiseNotDefined()


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    borda = util.Queue()
    explorados = []
    borda.push((problem.getStartState(), []))
    #print 'Start',problem.getStartState()
    #Visited.append( problem.getStartState() )

    while not borda.isEmpty():
        estado_atual, acoes = borda.pop()  # BP eh FIFO -> Fila
        print estado_atual, acoes
        for proximo_estado in problem.getSuccessors(estado_atual):
            estado = proximo_estado[0]
            direcao = proximo_estado[1]
            if estado not in explorados:
                if problem.isGoalState(estado):
                    return acoes + [direcao]
                borda.push((estado, acoes + [direcao]))
                explorados.append(estado)

    util.raiseNotDefined()


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    return aStarSearch(problem)


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    from game import Directions
    S = Directions.SOUTH
    O = Directions.WEST
    L = Directions.EAST
    N = Directions.NORTH

    posicao_inicial = problem.getStartState()
    custo_inicial = 0
    caminhos = []

    borda = []
    explorados = []

    borda.append([posicao_inicial, caminhos, custo_inicial])

    #print 'Start',problem.getStartState()
    #Visited.append( problem.getStartState() )

    while len(borda) != 0:

        #### Calculo de menor f, sendo f = custo + heuristica
        lowest_f = borda[0][2] + heuristic(borda[0][0], problem)
        lowest_f_position = 0

        for i in range(len(borda)):
            f = borda[i][2] + heuristic(borda[i][0], problem)

            # print borda[i], "; f =", f

            if f < lowest_f:
                lowest_f = f
                lowest_f_position = i
        #### /Fim do calculo de menor f, sendo f = custo + heuristica

        # Verifica posicao escolhida e seus parametros para calcular os proximos sucessores
        posicao_atual, caminhos, custo_acumulado = borda.pop(lowest_f_position)  # Ve a pos com menor f
        explorados.append(problem.getStartState())

        # print posicao_atual, caminhos, custo_acumulado

        # Verifica proximos sucessores e adiciona na lista de borda
        for proxima_posicao in problem.getSuccessors(posicao_atual):
            # print "prox_pos:", proxima_posicao

            posicao = proxima_posicao[0]
            nova_direcao = proxima_posicao[1]
            custo = proxima_posicao[2] + custo_acumulado

            if posicao not in explorados:
                caminhos += [nova_direcao]

                if problem.isGoalState(posicao):
                    print caminhos
                    return caminhos

                borda.append([posicao, caminhos, custo])
                explorados.append(posicao)

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
