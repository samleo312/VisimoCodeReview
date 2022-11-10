#include <stdio.h>
#include <stdint.h>

#include <iostream>
#include <set>
#include <algorithm>
#include <map>

using namespace std;

uint32_t costMatrix[8][8];

// Initialize the cost matrix
void initCostMatrix()
{
    for (int i = 0; i < 8; i++)
        for (int j = 0; j < 8; j++)
            costMatrix[i][j] = 0xFFFF;

    costMatrix[0][1] = 5;
    costMatrix[0][2] = 6;
    costMatrix[0][4] = 2;

    costMatrix[1][0] = 5;
    costMatrix[1][3] = 6;
    costMatrix[1][5] = 9;
    costMatrix[1][6] = 8;

    costMatrix[2][0] = 6;
    costMatrix[2][6] = 9;

    costMatrix[3][1] = 6;
    costMatrix[3][7] = 3;

    costMatrix[4][0] = 2;
    costMatrix[4][6] = 2;

    costMatrix[5][1] = 9;
    costMatrix[5][6] = 3;

    costMatrix[6][1] = 8;
    costMatrix[6][2] = 9;
    costMatrix[6][4] = 2;
    costMatrix[6][5] = 3;
    costMatrix[6][7] = 9;

    costMatrix[7][3] = 3;
    costMatrix[7][6] = 9;
}

// l(s, n)
uint32_t linkCost(uint32_t s, uint32_t n)
{
    return costMatrix[s][n];
}

int main()
{
    initCostMatrix();

    uint32_t s;

    // Enter s
    cout << "Please enter the node ID (0-7): " << endl;
    cin >> s;


    // Initialization
    set<uint32_t> M;
    set<uint32_t> N;
    uint32_t C[8] = {0};

    for (uint32_t i = 0; i < 8; i++)
        N.insert(i);

    M.insert(s);

    N.erase(s);
    for (set<uint32_t>::iterator it = N.begin(); it != N.end(); ++it)
        C[*it] = linkCost(s, *it);
    N.insert(s);


  
    // Shortest path algorithm
   
    while(N != M){
        set<uint32_t> nMinusM;
        uint32_t minCost = 0xFFFF;
        uint32_t lowestNode;

        set_difference(N.begin(), N.end(), M.begin(), M.end(), inserter(nMinusM, nMinusM.end()));

        for (set<uint32_t>::iterator it = nMinusM.begin(); it != nMinusM.end(); ++it){
            if (C[*it] < minCost){
                minCost = C[*it];
                lowestNode = *it;
            }
        }
        M.insert(lowestNode);

        for (set<uint32_t>::iterator it = nMinusM.begin(); it != nMinusM.end(); ++it){
            C[*it] = std::min(C[*it], C[lowestNode] + linkCost(lowestNode, *it));
        }
    }





    // Output the shortest path cost from s to other nodes
    cout << "Shortest path cost is: " << endl;
    for (uint32_t i = 0; i < 8; i++)
        cout << s << "->" << i << ": " << C[i] << endl;
}
