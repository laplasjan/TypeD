{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "9d8f2277-d6c7-4921-871c-91d4ca825083",
   "metadata": {},
   "outputs": [],
   "source": [
    "import networkx as nx\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bb281324-758f-4044-b975-a8a00424ab1b",
   "metadata": {
    "tags": []
   },
   "source": [
    "### T_pqr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "8330a73e-cfaa-473e-a66e-24d5809956e5",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Tworzenie grafu pzrez funkcję\n",
    "def T_pqr(p,q,r):\n",
    "    G = nx.Graph()\n",
    "    if p> 1 and q>1 and r >1:\n",
    "        for i in range(p+q+r-2):\n",
    "            G.add_node(i, waga=i)\n",
    "        for i in range (0, p-1):\n",
    "            G.add_edge(i,i+1)\n",
    "        for i in range (p,p+q-2):\n",
    "            G.add_edge(i,i+1)\n",
    "            G.add_edge(0,p)\n",
    "        for i in range(p+q-1,p+q+r-3):\n",
    "            G.add_edge(i,i+1)\n",
    "            G.add_edge(0,p+q-1)\n",
    "    if p == 1 or q ==1 or r == 1:\n",
    "        for i in range(p+q+r-2):\n",
    "            G.add_node(i, waga=i)\n",
    "        for i in range (0, p+q+r-3):\n",
    "            G.add_edge(i,i+1)\n",
    "    if p == 2:\n",
    "        for i in range(0,p+q+r-2):\n",
    "            G.add_node(i, waga=i)\n",
    "        for i in range (0, 1):\n",
    "            G.add_edge(i,i+1)\n",
    "        for i in range (2,q):\n",
    "            G.add_edge(i,i+1)\n",
    "            G.add_edge(0,2)\n",
    "        for i in range(q+1,q+r-1):\n",
    "            G.add_edge(i,i+1)\n",
    "            G.add_edge(0,q+1)\n",
    "    if q ==2 :\n",
    "        for i in range(0,p+q+r-2):\n",
    "            G.add_node(i, waga=i)\n",
    "        for i in range (0, p-1):\n",
    "            G.add_edge(i,i+1)\n",
    "            G.add_edge(0,p)\n",
    "        for i in range(p+2,p+q+r-3):\n",
    "            G.add_edge(i,i+1)\n",
    "            G.add_edge(0,p+2)\n",
    "    if r == 2:\n",
    "        for i in range(0,p+q+r-2):\n",
    "            G.add_node(i, waga=i)\n",
    "        for i in range (0, p-1):\n",
    "            G.add_edge(i,i+1)\n",
    "        for i in range (p,p+q-2):\n",
    "            G.add_edge(i,i+1)\n",
    "            G.add_edge(0,p)\n",
    "        G.add_edge(0,p+q-1)\n",
    "    return G"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5f22c16a-332e-4459-9fec-ce1aee5fa615",
   "metadata": {
    "tags": []
   },
   "source": [
    "### T_pqr DLA UST. p,q,r o skończonych reprezentacjach"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "a370a417-6026-480b-b4e9-01e907a6d780",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "D5 = T_pqr(2,2,2)\n",
    "labels = {n: D5.nodes[n] for n in D5.nodes}\n",
    "nx.draw(D5, with_labels=True, node_size=500, node_color='lightblue', font_weight='bold')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cff09b9e-be73-42fe-a71d-921850c6d9fe",
   "metadata": {
    "tags": []
   },
   "source": [
    "### WAGI WIERZCHOŁKÓW z listy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "aba30c3d-e3b8-4a43-862a-8b76e1b6511a",
   "metadata": {},
   "outputs": [],
   "source": [
    "def nadawanie_wag(G, wagi_lista):\n",
    "    wagi = []\n",
    "    for idx, weight in enumerate(wagi_lista):\n",
    "        G.add_node(idx, weight=weight) \n",
    "    for _, w in G.nodes(data='weight'):\n",
    "        wagi.append(w)\n",
    "    return wagi "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "16b21acf-fd7a-4814-acb3-87970941b6bf",
   "metadata": {},
   "source": [
    "### Odbicie do listy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "d712d72a-8e8c-47e4-82a8-334948fa1dcf",
   "metadata": {},
   "outputs": [],
   "source": [
    "def odbicie(G, node):\n",
    "    #jeśli chcesz sprawdzić, czy odbicie działa oraz chcesz mieć wypisane wagi, komenda poniżej to umożliwia:\n",
    "    #print(nadawanie_wag(G, wagi_lista))\n",
    "    \n",
    "    wagi = [] \n",
    "    \n",
    "    neighbors = list(G.neighbors(node))\n",
    "    \n",
    "    nowa_waga1 = - G.nodes[node]['weight']\n",
    "    G.nodes[node]['weight'] = nowa_waga1\n",
    "    \n",
    "    for neighbor in neighbors:\n",
    "        nowa_waga = G.nodes[neighbor]['weight'] -  G.nodes[node]['weight']\n",
    "        G.nodes[neighbor]['weight'] = nowa_waga\n",
    "    for _, w in G.nodes(data='weight'):\n",
    "        wagi.append(w)\n",
    "    return wagi"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "07a4bf29-96ca-4f5a-9272-0a0aae30ef51",
   "metadata": {},
   "outputs": [],
   "source": [
    "def relations(tableau):\n",
    "    rows, cols = tableau.shape\n",
    "    for i in range(rows):\n",
    "        for j in range(cols - 1):\n",
    "            if tableau[i, j] > tableau[i, j + 1]:\n",
    "                tableau[i, j], tableau[i, j + 1] = tableau[i, j + 1], tableau[i, j]\n",
    "\n",
    "    for i in range(rows - 1):\n",
    "        for j in range(cols):\n",
    "            if j == 0 and tableau[i, j] > tableau[i + 1, j]:\n",
    "                tableau[i, j], tableau[i + 1, j] = tableau[i + 1, j], tableau[i, j]\n",
    "            elif tableau[i, j] > tableau[i + 1, j] and tableau[i, j - 1] < tableau[i + 1, j]:\n",
    "                tableau[i, j], tableau[i + 1, j] = tableau[i + 1, j], tableau[i, j]\n",
    "    \n",
    "    return tableau"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "c5906088-129e-47d2-97d7-e69fa91e9550",
   "metadata": {},
   "outputs": [],
   "source": [
    "def wiersze_relacje(tableau):\n",
    "    for row in tableau:\n",
    "        for i in range(len(row)-1):\n",
    "            if row[i] > row[i + 1]:\n",
    "                row[i], row[i + 1] = row[i + 1], row[i]\n",
    "    return tableau"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "855dca71-d1a2-4cf1-bcf9-9d2aab2bacd4",
   "metadata": {},
   "source": [
    "### Omijanie miejsc plusów"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "556142d3-2ace-4ea5-8c6d-51989836a9fc",
   "metadata": {},
   "outputs": [],
   "source": [
    "def omijanie_dodatnich(G, lista, count=0):\n",
    "    nodes_z_odbiciem = []\n",
    "    wagi = []\n",
    "    Y = lista \n",
    "    while True:\n",
    "        nodes_dodatnie = [node for node, data in G.nodes(data='weight') if (data is not None and data > 0 and node not in Y)]\n",
    "        if not nodes_dodatnie:\n",
    "            break \n",
    "        for node in nodes_dodatnie:\n",
    "            odbicie(G, node)  \n",
    "            nodes_z_odbiciem.append(node)\n",
    "            count += 1\n",
    "            if count > 10:  \n",
    "                print(\"Maximum number of iterations reached. Exiting loop.\")\n",
    "                break\n",
    "    for _, w in G.nodes(data='weight'):\n",
    "        wagi.append(w)\n",
    "    print(f\"Wierzchołki w kolejności wywoływania:  {nodes_z_odbiciem}, wagi na końcu: {wagi}, count:  {count}\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d7a621ff-3d9e-444f-8d0d-0a7181de110d",
   "metadata": {},
   "source": [
    "### Do komandera"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "0a5f385b-8db6-4039-b134-5406e3e49923",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Podaj wartość dla p:  2\n",
      "Podaj wartość dla q:  2\n",
      "Podaj wartość dla r:  2\n",
      "Podaj wartości wag jako listę:  -1,1,1,1\n",
      "Wskaż wierzchołki do omijania:  0\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Wierzchołki w kolejności wywoływania:  [1, 2, 3], wagi na końcu: [2, -1, -1, -1], count:  3\n"
     ]
    }
   ],
   "source": [
    "def main(p, q, r, G, wagi_lista, lista):\n",
    "    p = int(p)\n",
    "    q = int(q)\n",
    "    r = int(r)\n",
    "    G = T_pqr(p, q, r)\n",
    "    wagi_lista = [int(waga) for waga in wagi_lista] \n",
    "    lista = [int(waga) for waga in lista]\n",
    "    nadawanie_wag(G, wagi_lista)\n",
    "    omijanie_dodatnich(G, lista, count=0)\n",
    "    \n",
    "if __name__ == \"__main__\":\n",
    "    p = int(input(\"Podaj wartość dla p: \"))\n",
    "    q = int(input(\"Podaj wartość dla q: \"))\n",
    "    r = int(input(\"Podaj wartość dla r: \"))\n",
    "    wagi_lista = input(\"Podaj wartości wag jako listę: \").split(\",\")\n",
    "    lista = input(\"Wskaż wierzchołki do omijania: \").split(\",\")\n",
    "    G = T_pqr(p, q, r)\n",
    "    main(p, q, r, G, wagi_lista, lista)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "143f1f66-469f-4868-8510-38a4b5869f73",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
