{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 26,
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
   "execution_count": 27,
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
   "execution_count": 28,
   "id": "a370a417-6026-480b-b4e9-01e907a6d780",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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d7V48WLl5+dTJlFnmKEEACBO/PDDD8rMzNT111+viRMnGh0HJkKhBAAgTtxxxx2aP3++iouLlZ6ebnQcmAhL3gAAxIF58+Zp0qRJeu+99yiTqHPMUAIAYHLl5eVq3769WrdurYKCAk7EQZ1jhhIAAJP7y1/+ou+//54yibChUAIAYGJr167VK6+8omeffVZt2rQxOg5MiiVvAABMqrq6WpdddpkOHz6sNWvWyG63Gx0JJsUMJQAAJjVy5EitXbtWK1asoEwirJihBADAhHbu3Kl27drpnnvu0RtvvGF0HJgchRIAAJMJBALq3bu3Nm/erM8//1wNGjQwOhJMjiVvAABMZsqUKZo3b55mzJhBmUREMEMJAICJ7N+/X1lZWerSpYumTZtmdBzECavRAQAAQN15/PHHVVlZyX2TiCiWvAEAMInFixdr/PjxGjNmjM4991yj4yCOsOQNAIAJVFZWqmPHjkpPT9fSpUtltbIIichhhhIAABN47rnntGPHDuXl5VEmEXF8xwEAEOO2bNmiF154QU888YTatm1rdBzEIZa8AQCIYX6/X126dNG+ffu0fv16ORwOoyMhDrHkDQBADBs7dqyWL1+uxYsXUyZhGGYoAQCIUd99952ysrLUr18/jRs3zug4iGMUSgAAYtStt96qoqIiFRcXy+PxGB0HcYwlbwAAYtCMGTOUm5uryZMnUyZhOGYoAQCIMWVlZWrbtq06duyoWbNmyWKxGB0JcY5tgwAAiDFPPvmkSkpKNHr0aMokogJL3gAAxJCVK1dq1KhRGjFihJo3b250HEASS94AAMQMn8+nCy+8UImJiVq5cqUSEpgXQnTgOxEAgBjx8ssvq7i4WKtWraJMIqowQwkAQAzYtm2bsrOz9cADD+ill14yOg5wAgolAABRLhAI6JprrtH27du1efNmJScnGx0JOAHz5QAARLmJEyfqk08+0bx58yiTiErMUAIAEMX27NmjzMxMXXvttfrggw+MjgP8LPahBAAgij3yyCOSpFdeecXgJMCpseQNAECUys/P1wcffKB33nlHGRkZRscBToklbwAAolBFRYXat2+vFi1aaOHChZyIg6jGDCUAAFHo6aef1nfffaf58+dTJhH1uIcSAIAos379eo0YMUJ//vOfdf755xsdBzgjlrwBAIgiNTU1uuyyy1RZWak1a9aoXr16RkcC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xwFMjSVvAIDpzJ07Vx9++KEmTpxImQQigBlKAICpHDx4UO3bt9f555+v/Px8TsQBIoAZSgCAqTz11FPavXu3Fi5cSJkEIoRCCQAwjTVr1ui1117Tc889p9atWxsdB4gbLHkDAEyhurpal1xyiWpqarR69WrZ7XajIwFxgxlKAIApvP7661q/fr1WrlxJmQQijBlKAEDM27Fjh9q3b6///u//1uuvv250HCDuUCgBADEtEAiod+/e2rx5sz7//HM1aNDA6EhA3GHJGwAQ0yZPnqx58+Zp5syZlEnAIMxQAgBi1v79+5WZmamrrrpKH330kdFxgLhlNToAAABn649//KMOHz6sN954w+goQFxjyRsAEJMWLVqkCRMm6K233lLjxo2NjgPENZa8AQAxp7KyUh06dFCjRo20ZMkSWa0suAFGYoYSABBznn32We3cuVMzZsygTAJRgL+FAICYsnnzZr3wwgsaOnSosrKyjI4DQCx5AwBiiN/vV05Ojvbv368NGzYoMTHR6EgAxJI3ACCGvPXWW1qxYoWWLFlCmQSiCDOUAICY8O233yorK0v9+/fX2LFjjY4D4DgUSgBATLjlllu0fPlyFRcXy+PxGB0HwHFY8gYARL28vDzl5eVpypQplEkgCjFDCQCIamVlZcrKylKnTp308ccfy2KxGB0JwE+wbRAAIKoNHTpUpaWlGjVqFGUSiFIseQMAotaKFSs0evRovfLKK2revLnRcQCcAkveAICodPjwYXXu3FkOh0MrV66UzWYzOhKAU2CGEgAQlV5++WUVFxdr1apVlEkgyjFDCQCIOtu2bVN2drYefPBBDR8+3Og4AM6AQgkAiCqBQEBXX321du7cqc2bN8vpdBodCcAZsOQNAIgq7733nhYtWqT58+dTJoEYwQwlACBq/PDDD8rKylLv3r31/vvvGx0HQJAolACAqDFgwADNnTtXW7duVXp6utFxAASJJW8AQFSYP3++/v73v+vdd9+lTAIxhhlKAIDhysvL1b59e7Vq1UoLFizgRBwgxjBDCQAw3F/+8hd9//33KigooEwCMYhCCQAw1Nq1a/XKK6/omWeeUZs2bYyOA+AssOQNADBMdXW1LrvsMlVVVWnt2rWy2+1GRwJwFpihBAAYZuTIkVq7dq2WL19OmQRiGDOUAABD7Ny5U+3atdPAgQM1cuRIo+MACAGFEgAQcYFAQNddd502btyozz//XCkpKUZHAhAClrwBABE3depUzZ07V9OnT6dMAibADCUAIKJKSkqUmZmpnJwc5ebmGh0HQB2wGh0AABBfHn/8cVVWVuqNN94wOgqAOsKSNwAgYpYsWaK3335bo0ePVpMmTYyOA6COsOQNAIiIyspK/eIXv1BaWpoKCwtltbJIBpgFM5QAgIh4/vnntX37duXm5lImAZPhbzQAIOy2bNmi559/XkOGDFG7du2MjgOgjrHkDQAIK7/fry5dumjv3r3asGGDHA6H0ZEA1DGWvAEAYTV27FgtX75cixcvpkwCJsUMJQAgbL777jtlZWXp17/+td5++22j4wAIEwolACBsbr31VhUWFqq4uFipqalGxwEQJix5AwDCYsaMGcrNzdWHH35ImQRMjhlKAECdKysrU9u2bdWhQwfNnj1bFovF6EgAwohtgwAAdW7YsGEqKSnR6NGjKZNAHGDJGwBQpz799FO9+eabevnll9WiRQuj4wCIAJa8AQB1xufzqXPnzrLb7fr000+VkMC8BRAP+JsOAKgzI0aM0JYtW7Rq1SrKJBBHmKEEAJzEHwiotKpa3kqfvJU+VdbUqMYfkM1qkcNmk9thl9thlysxQdYj90j+85//VHZ2tu6//369/PLLBn8FACKJQgkAOKbCV63t3grt8FbI5//xx4NF0vE/KI5/2261qKXbqZYup27s3Uv//Oc/tWXLFiUnJ0c4OQAjUSgBAPLV+LVpT5l2lh46qUCeiUU/zmgu+OjvuuGSjrq2Z48wpQQQrSiUABDndpdXafUur6pq/CFdx+/3y2lPUOfGbjVKTqyjdABiAYUSAOLYVyXl2vBDWZ1ft2NGilp7WPYG4gUbmwNAnApXmZSkDT+U6auS8rBcG0D0oVACQBzaXV4VtjJ51IYfyrS7vCqsYwCIDhRKAIgzvhq/Vu/yRmSsNbu88oV4byaA6EehBIA4s2lPmQ5HqORVHnl6HIC5cYwBAMSRcl+1dpYeCvr1h8rLlTfuTa2Y97H2fPetEpOSdH7HC3XLoAfU9qJLg7rGztJDykyrL6edHzmAWfGUNwDEkc17yrRtf3lQ+0xWVlRo2ICbtOPzzSd9zGq16qGX3lTOdTed8ToWSRekJqtdekqt8wKIDSx5A0Cc8AcC2uGtCHrT8o/GvHqsTF5+bR9NWL5JT70zRYlJSfL7/frbU4N1wFtyxusEJG33VsjP/AVgWhRKAIgTpVXVx45TPJNAIKBPcicfe/vOx/4kV2qaOvyyiy7v1UeSVHHwgJbNnRnU9Xz+H88GB2BOFEoAiBPeSl/Qr939729Utn+fJCkpub4ymjQ99rFmF2Qd+/229WvDMj6A2EKhBIA44a30yRLka0v37jn2++SUE+99dDZo8J9r7tujYFhEoQTMjEIJAHGisqYm6Psnj3fSs5vHvW2xBFdRA0fGB2BO7OEAACZRU1Mjr9ervXv3nvRr3759avWr65TR6oKgruVqmH7s9+VlJ+4jWXHgwH9el5auYNUEef8mgNhDoQSAKOT3+1VaWnrKcvhz7y8pKZHff/KG5W63Ww0bNtR/d7pC6YFAULOK55zXXK60hirdt1eVFeX64dt/H7uP8usvtx573fkdOwX9NdmswS64A4g1FEoACLNAIKCysrJalcP9+/er5meWiFNSUtSwYcNjv1q3bq1LL71UaWlpJ7z/6K/U1FQlJPz4T/2670u1szT4bYO63dJfeePelCS9//Jf9bs/P6edWz/XivkfS5Kc9RvoimtvCOpaFkkOmy3IkQHEGjY2B4BaCAQCOnjwYNDF8OjHqqtP3jKnfv36P1sCT1cO69Wrd9bZd3grtG53adCvr6uNzY/q1Millm5n0K8HEDsolADiViAQUEVFRa3L4eHDh0+6ltPpDLoYHv1YYmJiRL/ekkqfFn29t1afc+jgQeW9PUrL536sPd/9W4lJSbqg44W6edADanfxZbW61q+aN5THYa/V5wCIDRRKAKZx6NChWpfDysrKk66TmJio9PT0WpXDpKQkA77i2vEHApr9z91Bb25el+xWi65r00jWIJ8KBxBbuIcSQFSqrKw8qQyeqhwefX9FRcVJ16lXr95JBfCCCy447VKz0+kMejucWGK1WNTS7Qz6LO+6YpHUyu2kTAImRqEEEHaHDx8+oQyeadZw7969Onjw4EnXSUhIOKkEtmrV6rTlsH79+qYsh2erldupL/eXR3TMgMS9k4DJUSgB1IrP59P+/ftrVQ7LfrKPoSTZbLaTlpGbNWt22nKYkpJCOQyR056gFq4k7Sw9FLExW7iS5LTz4wYwM+6hBOJYTU1Nrcuh1+s96ToWi+WEcnim+w0bNmwol8slq5XDuozgq/GrYMceVdacvGdlXXPYrOreMl12G3/WgJnFZaH0BwIqraqWt9Inb6VPlTU1qvEHZLNa5LDZ5HbY5XbY5UpM4J4fxAy/36+SkpKg7zc8uhH2z/0TkJqaWqty6Ha7ZWOPwZiyu7xKy/69P+zjXNE0VY2SI/s0O4DIi6tCWeGr1nZvhXZ4K4495WiRTrg5/fi37dYfb2Bv5XayXIOIOv6UlGBmDY9uhH26U1JOVw6Pf7/H4zm2ETbM7auScm344eTbEerK2KefUM+LO+rhhx8O2xgAokNc/NTw1fi1aU+ZdpYeOqlA/rRNH/+2zx/Qtv3l+nJ/uVq4kpSdnsKyDWrt+FNSgi2H+/btO+MpKWlpaWrZsqUuvvjiU5bD1NRU2e3s+4ef19qTLElhKZUdM1J0YYtz9cgjj6ikpERPP/00978CJmb6Gcrd5VVavcurqjq4V8hhs6pzYzfLN3Hs+FNSgi2He/fuPe0pKcEsKR/9fSinpACnsru8Smt2eevknsqf/js5fPhwDR48WA888IBee+017psFTMrUhTJcyzkdM1KO/c8esev4U1JqUw5Pd0pKbcqhw+Ew4KsGft7pVnLO5OjrT7WSM3bsWP3P//yPBgwYoAkTJnBLBWBCpi2U4b43iFIZfY6ekhLMwyhHf53ulJRg7jc8+rbTyR57MIcKX7V2eCu0vRb3mrdyO9XyDPeaT5kyRQMGDNB1112nyZMn8x8qwGRMWSh5ejH2VVVV1WrW8FSnpNjt9lqVQzOfkgLURjh2w5g7d6769u2rX/7yl5o+fboaNGgQ5q8CQKSYrlD6avzK37GnTu6ZPBP2VwuOz+erdTk81SkpwS4pH/3FKSlAdCksLNT111+vzMxMzZkzR2lpaUZHAlAHTFco137v1delhyJ2Tm0LV5IuPMcdodGMV11dfcJG2MGUw587JcVqtda6HHJKCmAOa9euVa9evZSRkaH8/Hyde+65RkcCECJTFcpyX7Xmb99zxtcVr/lUhbOm68sNa7R/9/cqLyuTJz1Dzf8rSzf/7n5lXnhJrcbt1So9JveprKmpOWEj7GDK4alOSTl+I+xgyiGnpADx7YsvvlD37t2VkJCgBQsWqFWrVkZHAhACUxXKzXvKtG1/+RlnJ//21GDlT3n/lB//n/97Sd373RHUmBZJF6Qmq116SvBBw8Dv98vr9QZdDE93SorH4wm6GHJKCoCz9c0336h79+46cOCA8vPz1b59e6MjAThLpimU/kBAs/+5+9hTiacz9uknVLZ/n7r3u0P/1elilR8o1TvPPaUV82dJkhq4PRq/bGPQJclutei6No3q7JjGQCBw7JSUYMvhqU5JcblctSqHnJICIJJ++OEH9ezZU19//bXmzp2rSy+91OhIAM6CaQplSaVPi77eG9RrKw4ekLP+iU8Xlu7fp4GXZx97++3C9fKkZwQ9/q+aN5THcfKJJIFAQAcOHKhVOTzVKSkNGjSoVTnklBQAscDr9er666/X+vXrNWPGDF199dVGRwJQS6aZivJW+oJ+7U/LpCRVHTp07PeJSUlq4PYEfb1AIKD3pnykL1YW/mw59PlOzpacnHxC+TvvvPPUqVOn05bDxES2KAJgPm63W/n5+brlllvUu3dvTZkyRTfddJPRsQDUgqkKZW1PdzgqEAho4vD/O/Z29353KqEWM3s11dX6194Sffrpp2rYsKEaN26s7Ozs0+59yKa+APAfTqdTM2fO1IABA3TrrbdqwoQJuuuuu4yOBSBIplnyXvHtfu06WFXrz/MdPqzRTz6ipR//Q5KUfVmOnhz7vuz1ajcb2Lh+on7ZJLXW4wMA/qOmpkb33nuvxo8frzfeeEMPPPCA0ZEABME0M5Q1QTyM81MVBw9o+P/eo00riyRJF3froYdfGVPrMnm24wMATmSz2TRu3Dh5PB49+OCDKikp0Z/+9Cf2oAWinGkKpc1au39s9u3epWcH3amvv/hcktTr9rs18Mm/nvX2N7UdHwDw8ywWi4YPHy6Px6Mnn3xSJSUlGjFiBHvXAlHMNIXSYbMFfQ/lN19u1TOD7tC+73fJYrFowGNP6qZ77jvrsS1HxgcA1A2LxaKhQ4fK7Xbr/vvvl9fr1bhx49jWDIhSprmHcoe3Qut2lwb12pFD/qDF06ee9jVPvzdN7S+9POjxOzVyqaXbGfTrAQDB+fvf/67f/va3uvHGGzVp0iR2vACikGnWD9w/swdkPI0PAGZ1xx13KC8vT7Nnz1afPn1UXl5udCQAP2GaGcranJRT1+r6pBwAwMkWL16sPn36KDs7W7Nnz5bHE/x+wQDCyzQzlFaLRS3dTkW60lkktXI7KZMAEGZdu3bVokWL9OWXX6pr1676/vvvjY4E4AjTFErpx2IX6fnJgMS9kwAQIRdddJGWLl2qvXv3qkuXLtq5c6fRkQDIZIXSaU9QC1dSRMds4UqS085ThwAQKW3btlVRUZECgYBycnJUXFxsdCQg7pmqUEpSdnqKHLbIfFkOm1XZ6SkRGQsA8B8tW7ZUYWGhUlNT1aVLF61evdroSEBcM12htNus6tzYHZGxOjd2yx6h8goAOFHjxo21ePFinX/++erWrZuWLFlidCQgbpmyDTVKTlTHjPDOHHbMSFGjZPZCAwAjpaamqqCgQJdeeql69eqlWbNmGR0JiEumLJSS1NqTHLZS2TEjRa09yWG5NgCgdurXr69Zs2apd+/euvnmmzVp0iSjIwFxx7SFUvqxVF7RNLXO7ql02Ky6omkqZRIAokxiYqKmTJmiAQMGaMCAARozZozRkYC4YvrHkxslJ6p7y3Rt2lOmnaWHgj7v+6ijr2/hSlJ2egr3TAJAlEpISND48ePldrt13333yev1asiQIbKwTzAQdqYvlNKPD+pceI5bmWn1tcNboe3eimMn6vy0YB7/tt1qUSu3Uy3dTrYGAoAYYLVa9corr8jj8Wjo0KEqKSnRiy++SKkEwsw0Ry/Whj8QUGlVtbyVPnkrfaqsqVGNPyCb1SKHzSa3wy63wy5XYgIn4ABAjHrjjTf00EMP6Xe/+53GjBkjm81mdCTAtOJy2s1qscjjsMvjsBsdBQAQJg8++KDcbrcGDhyo0tJSvf/++6pXr57RsQBTissZSgBA/Jg+fbp+85vfqFu3bsrNzZXTyXG5QF2jUAIATG/hwoW68cYb9Ytf/EKzZs2S2+02OhJgKhRKAEBcWLlypXr37q3mzZtr/vz5ysjIMDoSYBoUSgBA3Ni0aZN69OihlJQUFRQUqFmzZkZHAkyBTRUBAHEjOztbRUVF8vl8ysnJ0RdffGF0JMAUKJQAgLjSunVrFRYWqkGDBurSpYvWrVtndCQg5lEoAQBxp0mTJlq6dKlatGihrl27qrCw0OhIQEyjUAIA4lJaWpoWLlyozp07q2fPnpo7d67RkYCYRaEEAMStBg0aaM6cOerevbtuuOEGTZkyxehIQEyiUAIA4prD4dC0adPUv39/3XbbbRo3bpzRkYCYE5dHLwIAcDy73a733ntPLpdLgwYNUklJiR5//HGjYwExg0IJAIAkq9WqkSNHyuPxaPDgwSopKdFzzz0ni8VidDQg6lEoAQA4wmKx6K9//as8Ho8effRReb1ejRo1SlYrd4gBp0OhBADgJx555BG53W797ne/U1lZmd59913Z7XajYwFRi0IJAMDPGDhwoFJSUnT77berrKxMU6dOVVJSktGxgKjEWd4AAJzG/Pnzdcstt+jiiy/WzJkzlZKSYnQkIOpQKAEAOIPly5erd+/eatOmjebNm6eGDRsaHQmIKhRKAACCsGHDBvXo0UNpaWnKz89X06ZNjY4ERA0KJQAAQdq2bZuuueYaWSwWLViwQG3atDE6EhAV2AcBAIAgnX/++Vq2bJmSkpKUk5OjjRs3Gh0JiAoUSgAAaqFp06ZaunSpmjRpoquuukorVqwwOhJgOAolAAC1lJ6erk8++UQdOnTQNddco4KCAqMjAYaiUAIAcBZcLpfmzZunX/3qV7ruuuuUm5trdCTAMBRKAADOUlJSkvLy8tS3b1/169dP77zzjtGRAENwUg4AACGw2+364IMP5HK5NHDgQHm9Xj388MNGxwIiikIJAECIbDabxowZI4/Ho0ceeUQlJSV6+umnZbFYjI4GRASFEgCAOmCxWPT888/L7XZryJAh8nq9eu2112S1cncZzI9CCQBAHRo8eLDcbrd+//vfy+v1asKECUpI4MctzI3vcAAA6ti9994rl8ulO++8U2VlZZo8ebIcDofRsYCw4ehFAADCZM6cOerbt68uv/xyTZ8+XQ0aNDA6EhAWFEoAAMKosLBQ119/vTIzMzVnzhylpaUZHQmocxRKAADCbO3aterZs6caNWqk/Px8nXvuuUZHAuoUhRIAgAjYunWrunfvLrvdrgULFqhVq1ZGRwLqDHsZAAAQAZmZmSoqKlJCQoJycnK0efNmoyMBdYZCCQBAhDRv3lyFhYXKyMjQlVdeqU8//dToSECdoFACABBBjRo10uLFi9W2bVtdffXVWrhwodGRgJBRKAEAiDC326358+crJydHvXv31vTp042OBISEQgkAgAGSk5M1c+ZM3Xjjjbr11lv1/vvvGx0JOGsUSgAADFKvXj19+OGHuvvuu3XXXXdp5MiRRkcCzgpHLwIAYCCbzaZx48bJ4/HowQcflNfr1bBhw2SxWIyOBgSNQgkAgMEsFouGDx8uj8ejJ598UiUlJRoxYgSlEjGDQgkAQBSwWCwaOnSo3G637r//fnm9Xo0dO1YJCfyoRvTjuxQAgChy3333yeVy6be//a1KS0s1adIkJSYmGh0LOC2OXgQAIAp9/PHH+vWvf60rr7xSeXl5Sk5ONjoScEoUSgAAotTixYvVp08fZWdna/bs2fJ4PEZHAn4WhRIAgCi2atUq9erVS02bNtX8+fN1zjnnGB0JOAmFEgCAKLdlyxb16NFDTqdTBQUFatGihdGRgBOwsTkAAFGuXbt2Kioqkt/vV05OjoqLi42OBJyAQgkAQAxo2bKlioqK5PF41KVLF61evdroSMAxFEoAAGJE48aNtWTJErVp00bdunXTkiVLjI4ESKJQAgAQU1JTU7VgwQJdcskl6tWrl2bNmmV0JIBCCQBArKlfv75mz56ta6+9VjfffLMmTZpkdCTEOQolAAAxKDExUVOnTtUdd9yhAQMGaMyYMUZHQhzj6EUAAGJUQkKCJkyYILfbrfvuu09er1dDhgyRxWIxOhriDIUSAIAYZrVa9eqrr8rj8Wjo0KEqKSnRiy++SKlERFEoAQCIcRaLRU899ZTcbrf+8Ic/yOv1asyYMbLZbEZHQ5ygUAIAYBIPPfSQ3G63Bg4cqNLSUr3//vuqV6+e0bEQBzh6EQAAk8nLy1P//v3VrVs35ebmyul0Gh0JJkehBADAhBYsWKCbbrpJv/jFLzRr1iy53W6jI8HEKJQAAJjUypUr1bt3bzVv3lzz589XRkaG0ZFgUhRKAABMbNOmTerRo4dSUlJUUFCgZs2aGR0JJsTG5gAAmFh2draKiork8/mUk5OjL774wuhIMCEKJQAAJte6dWsVFhaqQYMG6tKli9atW2d0JJgMhRIAgDjQpEkTLV26VC1atFDXrl1VVFRkdCSYCIUSAIA4kZaWpoULF6pz587q0aOH5s2bZ3QkmASFEgCAONKgQQPNmTNH3bt31w033KCpU6caHQkmQKEEACDOOBwOTZs2Tb/5zW/Uv39/jRs3zuhIiHEcvQgAQByy2+1677335HK5NGjQIHm9Xv3xj380OhZiFIUSAIA4ZbVaNXLkSLndbj3++OMqKSnRs88+K4vFYnQ0xBgKJQAAccxiseiZZ56Rx+PRY489Jq/XqzfffFNWK3fFIXgUSgAAoEcffVRut1uDBg1SaWmp3n33XdntdqNjIUZQKAEAgCTpnnvukcvl0u23366ysjJNnTpVSUlJRsdCDOAsbwAAcIL58+fr5ptv1iWXXKKZM2cqJSXF6EiIchRKAABwkmXLlum6665TmzZtNG/ePDVs2NDoSIhiFEoAAPCz1q9fr549eyotLU35+flq2rSp0ZEQpSiUAADglL788kt1795dFotFCxYsUJs2bYyOhCjEngAAAOCULrjgAhUVFcnhcCgnJ0cbN240OhKiEIUSAACc1nnnnafCwkI1adJEV111lVasWGF0JEQZCiUAADij9PR0ffLJJ8rOztY111yjgoICoyMhilAoAQBAUFwul+bNm6euXbvquuuuU25urtGRECUolAAAIGhOp1N5eXnq27ev+vXrp3feecfoSIgCnJQDAABqpV69evrggw/kcrk0cOBAeb1ePfzww0bHgoEolAAAoNZsNpvGjBkjj8ejRx55RCUlJXr66adlsViMjgYDUCgBAMBZsVgsev755+V2uzVkyBB5vV699tprslq5oy7eUCgBAEBIBg8eLLfbrd///vfyer2aMGGCEhKoGPGEP20AABCye++9Vy6XS3feeafKyso0efJkORwOo2MhQjh6EQAA1Jk5c+aob9++uvzyyzV9+nQ1aNDA6EiIAAolAACoU4WFhbr++uuVmZmpuXPnKjU11ehICDMKJQAAqHNr165Vz5491ahRI+Xn5+vcc881OhLCiEIJAADCYuvWrerevbvq1aungoICtWrVyuhICBOe6wcAAGGRmZmpoqIiWa1W5eTkaMuWLUZHQphQKAEAQNg0b95cRUVFysjI0JVXXqnPPvvM6EgIAwolAAAIq0aNGmnx4sXKzMzU1VdfrU8++cToSKhjFEoAABB2brdb+fn5uvzyy9W7d2/NmDHD6EioQxRKAAAQEcnJyZo5c6b69Omjvn376v333zc6EuoIhRIAAERMYmKiJk+erLvvvlt33XWXRo4caXQk1AGOXgQAABFls9k0btw4ud1uPfjgg/J6vRo2bJgsFovR0XCWKJQAACDiLBaLXnrpJXk8Hg0bNkwlJSUaMWIEpTJGUSgBAIAhLBaLnnzySbndbv3v//6vvF6vxo4dq4QE6kms4U8MAAAY6v7775fL5dLdd9+t0tJSTZo0SYmJiUbHQi1w9CIAAIgKM2fOVL9+/XTllVcqLy9PycnJRkdCkCiUAAAgaixatEg33HCDsrOzNXv2bHk8HqMjIQgUSgAAEFVWrVqlXr16qWnTppo/f77OOeccoyPhDCiUAAAg6mzZskU9evSQ0+lUQUGBWrRoYXQknAYbmwMAgKjTrl07FRUVye/3KycnR8XFxUZHwmlQKAEAQFRq2bKlioqK5PF41KVLF61evdroSDgFCiUAAIhajRs31pIlS9SmTRt169ZNS5YsMToSfgaFEgAARLXU1FQtWLBAl1xyiXr16qVZs2YZHQk/QaEEAABRr379+po9e7auvfZa3XzzzZo0aZLRkXAcCiUAAIgJiYmJmjp1qu644w4NGDBAY8aMMToSjuDoRQAAEDMSEhI0YcIEud1u3XffffJ6vRoyZIgsFovR0eIahRIAAMQUq9WqV199VR6PR0OHDlVJSYlefPFFSqWBKJQAACDmWCwWPfXUU3K73frDH/4gr9erMWPGyGazGR0tLlEoAQBAzHrooYfkcrl0zz33qKysTBMnTlS9evWMjhV3OHoRAADEvH/84x+67bbbdPXVV2vatGlyOp1GR4orFEoAAGAKCxYs0E033aROnTpp1qxZcrlcRkeKGxRKAABgGitXrtS1116rli1bat68ecrIyDA6UlygUAIAAFPZtGmTevTooZSUFBUUFKhZs2ZGRzI9NjYHAACmkp2drcLCQh0+fFg5OTn68ssvjY5kehRKAABgOm3atFFRUZHq16+vnJwcrVu3zuhIpkahBAAAptSkSRMtXbpUzZs3V9euXVVUVGR0JNOiUAIAANNq2LChFi5cqAsvvFA9evTQvHnzjI5kShRKAABgaikpKZozZ46uueYa3XDDDZo6darRkUyHQgkAAEwvKSlJubm56tevn/r3769x48YZHclUOHoRAADEBbvdrokTJ8rtdmvQoEHyer364x//aHQsU6BQAgCAuGG1WjVy5Ei53W49/vjjKikp0bPPPiuLxXLGz/UHAiqtqpa30idvpU+VNTWq8Qdks1rksNnkdtjldtjlSkyQNYjrmQmFEgAAxBWLxaJnnnlGHo9Hjz32mLxer958801ZrT9/J2CFr1rbvRXa4a2Qz//jeTAWScefDGORFCj98fd2q0Ut3U61cjvltMdH1eKkHAAAELfGjx+vQYMGqX///nr33Xdlt9uPfcxX49emPWXaWXropAJ5Jkdf38KVpOz0FNlt5n5shUIJAADi2rRp03T77berZ8+emjp1qpKSkrS7vEqrd3lVVeMP+foOm1WdG7vVKDmxDtJGJwolAACIe/Pnz9fNN9+sSy65RKM+zNUXZYfrfIyOGSlq7Umu8+tGA3PPvwIAAAShZ8+eKigoUGqbtmEpk5K04YcyfVVSHpZrG40ZSgAAAEm7y6u07N/7wz7OFU1TTbf8zQwlAACIe74av1bv8kZkrDW7vPLVwb2Z0YRCCQAA4t6mPWU6HKGSV3nk6XEzoVACAIC4Vu6r1s7SQ7XaFihUO0sPqcJXHcERwys+dtsEAAA4hR3eiqD3mdy+ZaOmvfW6vv6iWGX796nyUIWc9VPU7Pz/0pU39NU1v749qFN3LEfGbZeeEmr8qEChBAAAccsfCGiHtyLo2cl/fbVNnxbMPeF9B0tL9Pnqlfp89Up9u/2funvIU2e8TkDSdm+Fsho2MMUxjSx5AwCAuFVaVX3sOMVgnHNec937lxf15vxl+nDDdo1dskZdb+p37OMLcz8M+lo+/49ng5sBhRIAAMQtb6WvVq//r04XqUf/O9W4eUvVS3QorVFj9fl/g459POG4oxvDMX60YskbAADELW+lr9bndB/l9/u1f/cuffzO2GPv63P3oNN8xoksolACAADEvMqamrMqk0N+c722bVh77G1bQoLufGxYrQpl4Mj4ZsCSNwAAiFs1tbh/8rTXqa7Wuy/8RdPfHmXI+Ebj6EUAABC3Vny7X7sOVp3V59bU1Mi79wctnPahpox8WdKP91COXbJWrtS0oK7RuH6iftkk9azGjybMUAIAgLjlsNl0tpv22Gw2pTVqrH73PyJngx/3k6z2+bT7X18H9fmWI+ObAfdQAgCAuOV22BUoDf71E577s7I6X6rW7TrIk9FIB0u9Wpj7oSoO/HiUotVmU6OmzYK6VuDI+GZAoQQAAHGrtoXuswXzNHvi26f8+C2DHpArrWHYxo9WFEoAABC3XIkJslstQW9u3qP/nVpftETf7fhKB7wlkiR3w4Zq3b6jru57mzp3vSbose1Wi1yJ5qhiPJQDAADi2uY9Zdq2v/ystg86WxZJF6Qmm+Ysbx7KAQAAca2V2xnRMin9eP9kS7czwqOGD4USAADENac9QS1cSREds4UrSU67OZa7JQolAACAstNT5LBFphY5bFZlm2Sp+ygKJQAAiHt2m1WdG7sjMlbnxm7ZI1ReI8VcXw0AAMBZapScqI4Z4Z057JiRokbJiWEdwwgUSgAAgCNae5LDVio7ZqSotSc5LNc2GtsGAQAA/MTu8iqt2eVVZY0/5Gs5jiynm3Fm8igKJQAAwM/w1fi1aU+ZdpYekkWq1dZCR1/fwpWk7PQU090z+VMUSgAAgNOo8FVrh7dC270Vx07U+WnBPP5tu9WiVm6nWrqdptoa6HQolAAAAEHwBwIqraqWt9Inb6VPlTU1qvEHZLNa5LDZ5HbY5XbY5UpMkNViMTpuRFEoAQAAEBJzL+gDAAAg7CiUAAAACAmFEgAAACGhUAIAACAkFEoAAACEhEIJAACAkFAoAQAAEBIKJQAAAEJCoQQAAEBIKJQAAAAICYUSAAAAIaFQAgAAICQUSgAAAISEQgkAAICQUCgBAAAQEgolAAAAQkKhBAAAQEgolAAAAAgJhRIAAAAhoVACAAAgJBRKAAAAhIRCCQAAgJBQKAEAABASCiUAAABCQqEEAABASCiUAAAACAmFEgAAACGhUAIAACAkFEoAAACEhEIJAACAkFAoAQAAEBIKJQAAAEJCoQQAAEBIKJQAAAAIyf8HCELD9NyyKQcAAAAASUVORK5CYII=\n",
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
   "execution_count": 29,
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
   "execution_count": 30,
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
   "execution_count": 31,
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
   "execution_count": 32,
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
   "execution_count": 33,
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
    "        if count > 10:\n",
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
   "execution_count": 34,
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
   "execution_count": 35,
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
      "Podaj wartości wag jako listę oddzieloną przecinkami:  1,1,1,1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Wierzchołki w kolejności wywoływania:  [], wagi na końcu: [0, 0, 0, 0], count:  0\n"
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
    "    zmiana_na_ujemne(G, count=0)\n",
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
