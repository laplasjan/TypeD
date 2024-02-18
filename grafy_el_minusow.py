{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 82,
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
   "execution_count": 83,
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
   "execution_count": 85,
   "id": "a370a417-6026-480b-b4e9-01e907a6d780",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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EkFpoalTp2r79u26/PLLNX/+fF1yySWqra21eiwAAIAu4aGcKPG3v/1N8+bNk2maWrRokb773e9aPRIAAEBQuEIZJb7zne9ox44dys/P12WXXaYrr7xSDQ0NVo8FAABwXFyhjDKmaWrx4sW66aablJWVpSVLlqioqMjqsQAAAL4WVyijjM1m01VXXaXt27dr8ODBmjZtmm699Va1tbVZPRoAAMBX4gplFPP5fFq4cKF+8YtfaPjw4SopKVFubq7VYwEAAHTCFcoo5nA4dNttt6myslJJSUmaNGmSHn30UTZDBwAAUYWgjAHZ2dlav369br31Vt19990qKCjQ7t27rR4LAABAEkEZM5KTk/Xoo49q5cqVOnjwoHJycrRo0SI2QwcAAJYjKGNMfn6+tm7dqiuuuELXXnutLr74Yh08eNDqsQAAQALjoZwY9ve//13z5s2T1+vViy++qO9973tWjwQAABIQVyhj2EUXXaSqqioVFBTo+9//vubOnctm6AAAIOK4QhkHTNPU0qVLdcMNNygrK0uLFy9WcXGx1WMBAIAEwRXKOGCz2TR37lxVVVVp6NChmjZtmhYsWMBm6AAAICK4Qhln/H6/fvWrX+nnP/+5hg0bpmXLlrEZOgAACCuuUMYZu92uBQsWqLKyUr169dLEiRP18MMPy+v1Wj0aAACIU1yhjGMdHR26//779dhjj2nSpElaunSpzjjjDKvHAgAAcYYrlHGsV69eevjhh7Vq1SrV1tYqJydHL774IpuhAwCAHkVQJoBzzz1X27Zt06xZs/STn/xEF110kWpqaqweCwAAxAmWvBPMG2+8oauvvlper1cvvPCCvv/971s9EgAAiHFcoUwwF154oXbs2KGioiL94Ac/0OzZs+V2u60eCwAAxDCuUCYo0zS1bNky/exnP1NmZqYWL16sadOmWT0WAACIQVyhTFA2m02zZ89WVVWVzjjjDJ133nm6+eab1draavVoAAAgxnCFEvL7/XrmmWd01113aejQoSopKdG4ceOsHgsAAMQIrlBCdrtdt9xyizZt2qSUlBRNnjxZDz74IJuhAwCAoHCFEp10dHTogQce0KOPPqoJEyZo6dKlGjFihNVjAQCAKMYVSnTSq1cvPfTQQ1q9erUOHz6s3Nxc/eY3v2EzdAAA8LUISnylvLw8bd26VXPmzNF1112nb3/72/rk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\n",
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
   "execution_count": 86,
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
   "execution_count": 89,
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
   "execution_count": 13,
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
   "execution_count": 76,
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
   "execution_count": 70,
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
    "        if count > 10:\n",
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
   "execution_count": 80,
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
   "execution_count": 91,
   "id": "f598c3f2-b42b-4b98-b645-69cc9f85e9bc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Podaj wartość dla p:  2\n",
      "Podaj wartość dla q:  2\n",
      "Podaj wartość dla r:  2\n",
      "Podaj wartości wag jako listę:  1,1,1,1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Wierzchołki w kolejności wywoływania w procedurze eliminacja minusów:  [], wagi na końcu: [0, 0, 0, 0], count:  0\n"
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
    "    zmiana_na_dodatnie(G, count=0)\n",
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
