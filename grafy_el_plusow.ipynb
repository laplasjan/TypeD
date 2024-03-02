{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 36,
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
   "execution_count": 37,
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
   "execution_count": 38,
   "id": "a370a417-6026-480b-b4e9-01e907a6d780",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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jph87bXX9MorrxCTAADAMrgPZQz4fD7dcsstevXVV7V48WJdc801pkcCAACIGFYoo6wjJhcvXkxMAgAASyIoo8jv9xOTAADA8gjKKOkak6+88goxCQAALIugjIKOmHzllVdUVlama6+91vRIAAAAUUNQRpjf79ett97aGZPXXXed6ZEAAACiiqCMoI6YLCsr06JFi4hJAACQFAjKCPH7/fqnf/qnzpicMmWK6ZEAAABigqCMgI6YXLRokUpLS4lJAACQVAjKMPn9fv3mN7/pjMnrr7/e9EgAAAAxlZRPygkEg2po88nl8crl8crj98sfCMphtynN4VBOmlM5aU5lp6bIbrMd8zh+v19Tp07VwoULtWjRImISAAAkJVswGAyaHiJW3F6fvnK5tdPlljdw4Mu2Ser6B9D1Y6fdpqE5GTopJ0MZzkPbuyMmFyxYoNLSUt1www2x+BIAAADiTlIEpdcf0PbaRu1qaD0iILvT8foh2ekqzMuS02GX3+/XP//zP2v+/PnEJAAASHqWD8qaljZt2utSmz8Q9rHSHHadmd9P/9//8zvNnz9fCxcu1I033hiBKQEAABKXpd9D+WV9i6r3NUbseB5/QB9/16Aar42YBAAAOMiyK5SRjsnDFQ3M0rDczKgdHwAAIFFY8rZBNS1tUY1JSare16ialraongMAACARWC4ovf6ANu11xeRcm/e65I3AezMBAAASmeWCcntto9pjFHmeg1ePAwAAJDNLBWWL16ddDa09ui1QuHY1tMrt9cXwjAAAAPHFUld573S5Q7rP5BebN2jd8qX6n+rN2l/zvVoaG5WbN1AnDj9VV9/2O/1s1OiQz2k7eN7T87LCGR0AACBhWeYq70AwqBV/q+l8As7x/PHB/613Fy845q/f8fAMXTTlppDP7bTbNOnk/OM+phEAAMCqLLPl3dDmCykmJclmt2vMxMv0wItlKq36m57/YLPGTLys89dL//C4/H5/yOf2Bg48GxwAACAZWWaFcqfLrS01DSG91t3cpIy+/Q75XMP+Ov3mvMLOj+eu26rcvIEhn//M/GwNzckI+fUAAABWYZkVSpfHq1A3nA+PSUlqa23t/Hlqerr65eSGfG7bwfMDAAAkI8sEpcfv7/XV3cFgUPP/8+HOjy+a8mulOJ2h//6D5wcAAEhGlglKf4jvnzyct71dT993tz5+Z7kkqfDcn+tX90yP2fkBAAASnWVuG+Sw9/wKa3dzk/7zrqna/smHkqSzx03Q//uH2XL2SY3J+QEAAKzAMkGZ5nCEdA/KDnU1e/XYb3+t3X/9XJJ08S9v1W9+/4gcDkePz207eH4AAIBkZJmgzElzKhjaRd76+n/+okd/e5Pqvt8rm82mX/3b73XV1P/V63MHD54fAAAgGVnmtkH1Hq8qdv8Q0muf+fdpqlz66nFf8x8vv64zzjkv5POXnDhAuUQlAABIQpa5KCc7NUVOQ+9jdNptyk61zGIvAABAj1hmhVKS/lzbqB37W3p9+6DesEk65YRMnuUNAACSlmVWKCXppJyMmMakdOD9kzwhBwAAJDNLBWWGM0VDstNjes4h2enKcLLdDQAAkpelglKSCvOylOaIzZeV5rCrkK1uAACQ5CwXlE6HXcUFOTE5V3FBjpwxilcAAIB4Zckays9MVdHA6K4cFg3MUn5mz5+oAwAAYDWWDEpJGpabGbWoLBqYpWG5mVE5NgAAQKKx1G2DjqampU2b97rk8QfCPlbawe10ViYBAAD+zvJBKUlef0Dbaxu1q6G1R8/7ltT5+iHZ6SrMy+I9kwAAAIdJiqDs4Pb6tNPl1lcut7yBA1/24YHZ9WOn3aaTcjI0NCeDWwMBAAAcQ1IFZYdAMKiGNp9cHq9cHq88fr/8gaAcdpvSHA7lpDmVk+ZUdmqK7DYzj3MEAABIFEkZlAAAAIgc3hAIAACAsBCUAAAACAtBCQAAgLAQlAAAAAgLQQkAAICwEJQAAAAIC0EJAACAsBCUAAAACAtBCQAAgLAQlAAAAAgLQQkAAICwEJQAAAAIC0EJAACAsBCUAAAACAtBCQAAgLAQlAAAAAgLQQkAAICwEJQAAAAIC0EJAACAsBCUAAAACAtBCQAAgLAQlAAAAAgLQQkAAICwEJQAAAAIC0EJAACAsBCUAAAACAtBCQAAgLAQlAAAAAgLQQkAAICwEJQAAAAIC0EJAACAsBCUAAAACAtBCQAAgLAQlAAAAAjL/wXgc7Nrf7izugAAAABJRU5ErkJggg==\n",
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
   "execution_count": 64,
   "id": "5d25891a-1e6f-4fc4-8d5e-b119006660c3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "node 0 has weight 1\n",
      "node 1 has weight 1\n",
      "node 2 has weight 2\n",
      "node 3 has weight 0\n"
     ]
    }
   ],
   "source": [
    "nodes = D5.nodes()\n",
    "weights = [1,1,2,0]\n",
    "for node, weight in zip(nodes, weights):\n",
    "    D5.add_node(node, weight=weight)\n",
    "for node, weight in D5.nodes(data = 'weight'):\n",
    "    print(f\"node {node} has weight {weight}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
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
   "execution_count": 49,
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
   "id": "27facdc3-da8d-4741-abdc-9a572935a1e7",
   "metadata": {
    "tags": []
   },
   "source": [
    "### Eliminacja plusów"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "d187acde-f613-4a61-a09c-f234e515c127",
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
   "execution_count": 51,
   "id": "77980bf7-e75f-49a6-a411-f8e8b9a5b6c5",
   "metadata": {},
   "outputs": [],
   "source": [
    "def ujemne(G):\n",
    "    for node, w in G.nodes(data='weight'):\n",
    "        if w is not None and w > 0:\n",
    "            return False\n",
    "    return True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "c2cc92b7-6263-4637-8b72-ef6c6ba07c81",
   "metadata": {},
   "outputs": [],
   "source": [
    "def zmiana_na_ujemne(G, count = 0):\n",
    "    nodes_z_odbiciem = []\n",
    "    wagi = []\n",
    "    while True: \n",
    "        nodes_dodatnie = [node for node, data in G.nodes(data='weight') if data is not None and data > 0]\n",
    "        for node in nodes_dodatnie:\n",
    "            odbicie(G, node)\n",
    "            nodes_z_odbiciem.append(node)\n",
    "            count +=1\n",
    "\n",
    "        if count > 1000:\n",
    "            print(\"Maximum number of iterations reached. Exiting loop.\")\n",
    "            break\n",
    "        if not nodes_dodatnie:\n",
    "            break\n",
    "    for _, w in G.nodes(data='weight'):\n",
    "        wagi.append(w) \n",
    "    print(f\"Wierzchołki w kolejności wywoływania:  {nodes_z_odbiciem}, wagi na końcu: {wagi}, count:  {count}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "9a79d55c-2ef9-4aaa-9a08-14ac03b0bcda",
   "metadata": {},
   "outputs": [],
   "source": [
    "def zmiana_na_ujemnee(G):\n",
    "    nodes_z_odbiciem = []\n",
    "    wagi = []\n",
    "    count = 0\n",
    "    \n",
    "    while True: \n",
    "        sorted_nodes = sorted(G.nodes(data=True), key=lambda x: x[1]['weight'], reverse=True)\n",
    "        nodes_dodatnie = [node for node, data in sorted_nodes if isinstance(data['weight'], (int, float)) and data['weight'] > 0]\n",
    "        \n",
    "        if not nodes_dodatnie:\n",
    "            break\n",
    "        \n",
    "        for node, data in sorted_nodes:\n",
    "            if data['weight'] > 0:\n",
    "                odbicie(G, node) \n",
    "                nodes_z_odbiciem.append(node)\n",
    "                count += 1\n",
    "\n",
    "    for _, w in G.nodes(data='weight'):\n",
    "        wagi.append(w) \n",
    "\n",
    "\n",
    "    print(f\"Wierzchołki w kolejności wywoływania: {nodes_z_odbiciem}, wagi na końcu: {wagi}, count: {count}\")\n",
    "    return count"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "fd3acd3e-70e9-4e4b-9143-e89562219cab",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Wierzchołki w kolejności wywoływania:  [0, 1, 2, 0, 3, 0, 1, 2, 0, 1, 2], wagi na końcu: [-1, -1, -2, 0], count:  11\n"
     ]
    }
   ],
   "source": [
    "zmiana_na_ujemne(D5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "1e3d1e07-b16f-4494-bbab-ccdc244936dd",
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
   "id": "675befd1-281f-4c86-8517-eb1febf6b3d6",
   "metadata": {},
   "source": [
    "### Do komandera"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "19de8226-fd3c-499a-b792-929421eacd32",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Podaj wartość dla p:  2\n",
      "Podaj wartość dla q:  2\n",
      "Podaj wartość dla r:  2\n",
      "Podaj wartości wag jako listę oddzieloną przecinkami:  -1,1,-1,1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Wierzchołki w kolejności wywoływania:  [], wagi na końcu: [-2, 0, -2, 0], count:  0\n"
     ]
    }
   ],
   "source": [
    "def main(p, q, r, G, wagi_lista):\n",
    "    p = int(p)\n",
    "    q = int(q)\n",
    "    r = int(r)\n",
    "    G = T_pqr(p, q, r)\n",
    "    wagi_lista = [int(waga) for waga in wagi_lista] \n",
    "    nadawanie_wag(G, wagi_lista)\n",
    "    ujemne(G)\n",
    "    ro_1(G)\n",
    "    zmiana_na_ujemnee(G, count=0)\n",
    "    ro_2(G)\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    p = int(input(\"Podaj wartość dla p: \"))\n",
    "    q = int(input(\"Podaj wartość dla q: \"))\n",
    "    r = int(input(\"Podaj wartość dla r: \"))\n",
    "    wagi_lista = input(\"Podaj wartości wag jako listę oddzieloną przecinkami: \").split(\",\")\n",
    "    G = T_pqr(p, q, r)\n",
    "    main(p, q, r, G, wagi_lista)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f9b354cd-ec69-4ad6-8351-7cc167c88876",
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
