{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
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
   "execution_count": 12,
   "id": "8330a73e-cfaa-473e-a66e-24d5809956e5",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Tworzenie grafu pzrez funkcję\n",
    "def T_pqr(p,q,r):\n",
    "    p = int(p)\n",
    "    q = int(q)\n",
    "    r = int(r)\n",
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
   "execution_count": 13,
   "id": "a370a417-6026-480b-b4e9-01e907a6d780",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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xhlauXKlbr75Zt1+++166qmn2AQdISnadAAAACJZQkKCZs6cqU6dOumPf/yjNm/erBkzZqhFixamowFeYw0lAABBYtGiRbrzzjvVpk0bFRQUKCcnx3QkwCvc8gYAIEjcdNNNWr9+vWpqatSlSxctW7bMdCTAKxRKAACCyFlnnaUNGzaoS5cuuu666/TKK6+Im4kIdhRKAACCTEpKihYvXqyRI0dq5MiRGjRokGpqakzHAk6INZQAAASx6dOna/Dgwbrooos0b948nXLKKaYjAcehUAIAEOTWr1+vW2+9VVarVXl5ebroootMRwJ+hlveAAAEuW7duqmoqEgZGRm6/PLLNXPmTNORgJ+hUAIAEAJOPfVUffLJJ+rbt6/69++vJ554Qi6Xy3QsQBK3vAEACCkej0cvvvii/vCHP+j666/XzJkzlZycbDoWIhyFEgCAELR06VL169dPGRkZKigoUPv27U1HQgTjljcAACHouuuu04YNG+TxeNS1a1ctXbrUdCREMAolAAAhqn379lq/fr0uvfRS/e53v9MLL7zAJugwgkIJAEAIS05O1oIFC/T73/9eo0eP1oABA+RwOEzHQoRhDSUAAGFi5syZGjhwoM477zzl5eXp1FNPNR0JEYJCCQBAGCkqKlKvXr3kdruVl5enbt26mY6ECMAtbwAAwshFF12koqIiZWZm6sorr9T06dNNR0IEoFACABBmTjnlFC1fvlz9+/fXgAEDNGrUKNXW1pqOhTDGLW8AAMKUx+PRq6++qscee0xXX3213nnnHaWkpJiOhTBEoQQAIMwtW7ZMffv2VatWrVRQUKCzzjrLdCSEGW55AwAQ5q6++moVFhaqWbNm6tatmxYvXmw6EsIMhRIAgAiQk5OjtWvXqkePHurZs6f+8Y9/sAk6/IZCCQBAhGjRooXy8vL0pz/9SU8++aT69++v6upq07EQBlhDCQBABJozZ44GDBigs846S/n5+TrjjDNMR0IIY0IJAEAE6tu3r9asWaMffvhBXbp00erVq01HQgijUAIAEKHOP/98FRYWqn379urRo4feeOMN05EQoiiUAABEsNatW+ujjz7Sfffdp0GDBmnEiBFyOp2mYyHEsIYSAABIkiZMmKARI0boiiuu0LvvvqvU1FTTkRAiKJQAAKDOihUr1KdPHyUnJ6ugoEDnnnuu6UgIAdzyBgAA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\n",
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
   "execution_count": 14,
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
   "execution_count": 15,
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
   "cell_type": "markdown",
   "id": "62328bc9-e69b-463e-908a-961798a87614",
   "metadata": {
    "tags": []
   },
   "source": [
    "### Eliminacja minusów"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "954584ef-085e-411b-9e22-c7956355c60d",
   "metadata": {},
   "outputs": [],
   "source": [
    "def pozytywne(G):\n",
    "    for node, data in G.nodes(data=True):\n",
    "        if data['weight'] is not None and data['weight'] < 0:\n",
    "            return False\n",
    "    return True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "529496de-6933-4866-a46c-35ce73aec8d9",
   "metadata": {},
   "outputs": [],
   "source": [
    "def ro_1(G):    \n",
    "    weights = []\n",
    "    for node in G.nodes():\n",
    "        G.nodes[node]['weight'] -= 1\n",
    "        weights.append( G.nodes[node]['weight'])\n",
    "    return weights"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "f1f1ad09-6c30-48f0-92bd-6793c71b5d75",
   "metadata": {},
   "outputs": [],
   "source": [
    "# nieefektywnie jedzie po ujemnych wierzchołkach\n",
    "def zmiana_na_dodatnie(G, count = 0):\n",
    "    nodes_z_odbiciem = []\n",
    "    wagi = []\n",
    "    while True: \n",
    "        nodes_ujemne = [node for node, data in G.nodes(data='weight') if data is not None and data < 0]\n",
    "        for node in nodes_ujemne:\n",
    "            odbicie(G, node)\n",
    "            nodes_z_odbiciem.append(node)\n",
    "            count +=1\n",
    "\n",
    "        if count > 1000:\n",
    "            print(\"Maximum number of iterations reached. Exiting loop.\")\n",
    "            break\n",
    "        if not nodes_ujemne:\n",
    "            break\n",
    "    for _, w in G.nodes(data='weight'):\n",
    "        wagi.append(w) \n",
    "    print(f\"Wierzchołki w kolejności wywoływania w procedurze eliminacja minusów:  {nodes_z_odbiciem}, wagi na końcu: {wagi}, count:  {count}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "10402e57-5180-4844-bc9d-6b37d1ca301e",
   "metadata": {},
   "outputs": [],
   "source": [
    "## efective way\n",
    "def zmiana_na_dodatniee(G, count=0):\n",
    "    nodes_z_odbiciem = []\n",
    "    wagi = []\n",
    "    \n",
    "    while True:\n",
    "        sorted_nodes = sorted(G.nodes(data=True), key=lambda x: x[1][\"weight\"], reverse=False)\n",
    "        nodes_ujemne = [node for node, data in sorted_nodes if isinstance(data['weight'], (int, float)) and data['weight'] < 0]\n",
    "        \n",
    "        if not nodes_ujemne:\n",
    "            break\n",
    "        \n",
    "        for node, data in sorted_nodes:\n",
    "            if data['weight'] < 0:\n",
    "                odbicie(G, node)\n",
    "                nodes_z_odbiciem.append(node)\n",
    "                count += 1\n",
    "\n",
    "    for _, w in G.nodes(data='weight'):\n",
    "        wagi.append(w) \n",
    "\n",
    "    print(f\"Wierzchołki w kolejności wywoływania: {nodes_z_odbiciem}, wagi na końcu: {wagi}, count: {count}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "6bf7a722-7a34-4165-a041-add7b873d170",
   "metadata": {},
   "outputs": [],
   "source": [
    "def ro_2(G):\n",
    "    weights = []\n",
    "    for node in G.nodes():\n",
    "        G.nodes[node]['weight'] += 1\n",
    "        weights.append( G.nodes[node]['weight'])\n",
    "    return weights"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0855e347-584f-4f70-a730-cbfc5271a82f",
   "metadata": {},
   "source": [
    "### Do komandera"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "f598c3f2-b42b-4b98-b645-69cc9f85e9bc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Podaj wartość dla p:  10\n",
      "Podaj wartość dla q:  10\n",
      "Podaj wartość dla r:  1\n",
      "Podaj wartości wag jako listę:  -1,-2,-3,-4,5,6,7,8,9,-10,11,12,13,14,15,16,17,18,19\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Wierzchołki w kolejności wywoływania w procedurze eliminacja minusów:  [0, 1, 2, 3, 9, 0, 1, 2, 4, 8, 10, 0, 1, 3, 5, 0, 2, 4, 1], wagi na końcu: [4, 1, 4, 0, 3, 2, 1, 4, 3, 7, 1, 10, 12, 13, 14, 15, 16, 17, 18], count:  19\n"
     ]
    }
   ],
   "source": [
    "def main(p, q, r, G, wagi_lista):\n",
    "    p = int(p)\n",
    "    q = int(q)\n",
    "    r = int(r)\n",
    "    G = T_pqr(p, q, r)\n",
    "    wagi_lista = [int(waga) for waga in wagi_lista]  # Zamienia stringi na liczby\n",
    "    nadawanie_wag(G, wagi_lista)\n",
    "    pozytywne(G)\n",
    "    ro_1(G)\n",
    "    zmiana_na_dodatniee(G, count=0)\n",
    "    ro_2(G)\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    p = int(input(\"Podaj wartość dla p: \"))\n",
    "    q = int(input(\"Podaj wartość dla q: \"))\n",
    "    r = int(input(\"Podaj wartość dla r: \"))\n",
    "    wagi_lista = input(\"Podaj wartości wag jako listę: \").split(\",\")\n",
    "    G = T_pqr(p, q, r)\n",
    "    main(p, q, r, G, wagi_lista)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "40a0d793-6c36-4628-9d25-b46b438dd759",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7f2f544e-6c19-4866-aec0-1af61e8135b2",
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
