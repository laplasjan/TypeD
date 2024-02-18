{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
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
      "image/png": "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6UgAAMAgCiVqpaysTP3799dnn32mnJwcderUyXQkAABgCIUStVZYWKhevXppx44dysvLU7t27UxHAgAABlAo4Zfdu3crIyNDHo9Hubm5atGihelIAAAgyNjYHH5p2rSpsrOzVVFRob59+6qgoMB0JAAAEGQUSvitdevWysrK0o4dOzRo0CCVlJSYjgQAAIKIQomAOO2007R48WJt3rxZI0aMUGVlpelIAAAgSCiUCJjk5GTNnTtXK1as0NixY+XxeExHAgAAQUChRECdc845euuttzR79mxdffXVYs0XAADWR6FEwA0fPlzTpk3TCy+8oKlTp5qOAwAA6hhHL6JOjB8/XgUFBbr55puVlJSkG2+80XQkAABQRyiUqDM33XST8vPzddNNNykhIUGXXnqp6UgAAKAOUChRpx544AE5nU5dfvnlcjgcGj58uOlIAAAgwDgpB3XO4/Hooosu0ty5c7V48WL17t3bdCQAABBAFEoERWVlpYYMGaI1a9Zo+fLlSk5ONh0JAAAECIUSQVNSUqLMzEx98803Wr16tU499VTTkQAAQABQKBFUTqdTPXr0kMvlUm5urlq3bm06EgAA8BOFEkG3Y8cOpaenq169esrNzVXTpk1NRwIAAH5gY3MEXYsWLZSdna3i4mL1799fhYWFpiMBAAA/UChhRPv27bV06VJt27ZN5557rsrKykxHAgAAtUShhDF/+ctftHDhQm3cuFGjRo2S2+02HQkAANQChRJGde3aVe+9956WLFmi8ePHy+v1mo4EAABqiEIJ4/r376/XX39db7zxhm644QaxTgwAgPDC0YsICaNGjVJBQYEmTpyopKQk3XXXXaYjAQCAaqJQImRcddVVcjqduuOOO5SYmKhrrrnGdCQAAFANFEqElClTpig/P1/XXnutEhISNGbMGNORAADAUVAoEVJsNpseffRROZ1OXXLJJXI4HBo0aJDpWAAA4Ag4KQchqaqqShdccIGWLFmirKwsdevWzXQkAADwJyiUCFnl5eUaOHCgPvroI61atUp//etfTUcCAAB/gEKJkFZcXKzevXvrxx9/VG5urk466STTkQAAwG9QKBHy9u7dq27duqmsrEy5ubk6/vjjTUcCAACHYWNzhLzGjRsrKytLXq9X/fr1U35+vulIAADgMBRKhIUTTjhB2dnZ2rNnjwYOHKji4mLTkQAAwAEUSoSNU045RUuWLNGWLVs0fPhwVVRUmI4EAABEoUSYOfPMMzV//nzl5eXpoosuUlVVlelIAABEPAolwk6PHj309ttva968ebrqqqvEujIAAMyiUCIsDRkyRK+88oqmT5+uW2+91XQcAAAiGkcvImyNHTtWTqdT119/vZKSkiiWAAAYQqFEWJs0aZKcTqduu+02JSYm6oorrjAdCQCAiEOhRNi755575HQ6deWVV8rhcOiCCy4wHQkAgIhCoUTYs9lseuqpp+R0OjVmzBjFx8erb9++pmMBABAxOHoRluF2uzVs2DCtXLlSH3zwgdLS0kxHAgAgIlAoYSmlpaXq16+fvvjiC+Xk5Khjx46mIwEAYHkUSliOy+VSz549tXv3buXl5alt27amIwEAYGkUSljSrl27lJGRIZ/Pp9zcXDVv3tx0JAAALIuNzWFJzZo1U3Z2tsrKytSvXz+5XC7TkQAAsCwKJSyrTZs2ysrK0k8//aTBgwertLTUdCQAACyJQglLO/3007V48WJt2rRJ559/viorK01HAgDAciiUsLyUlBTNnTtXH3zwgS655BJ5PB7TkQAAsBQKJSJCnz59NHPmTL399tu69tprxVo0AAACh0KJiDFixAi98MILeu6553TXXXeZjgMAgGVw9CIiyuWXX66CggJNnjxZSUlJuv76601HAgAg7FEoEXFuueUW5efn64YbblBiYqIuvvhi05EAAAhrFEpEpIceekhOp1Pjx49XfHy8hg4dajoSAABhi5NyELE8Ho8uvPBCzZ8/X0uWLFHPnj1NRwIAICxRKBHRKioqNGTIEK1bt04rVqxQly5dTEcCACDsUCgR8fbt26fMzEx99913Wr16tTp06GA6EgAAYYVCCUhyOp3q3r27ioqKlJubq1atWpmOBABA2KBQAgf88ssvSk9PV0xMjFavXq0mTZqYjgQAQFhgY3PggOOOO07Z2dlyuVzq37+/ioqKTEcCACAsUCiBw5x44olaunSptm7dqqFDh6q8vNx0JAAAQh6FEviNzp07a+HChVq/fr1GjRqlqqoq05EAAAhpFErgD6Snp+vdd9/VokWLdPnll8vr9ZqOBABAyKJQAn9iwIABmjFjhmbMmKGbbrpJrF8DAOCPcfQicASjR4+Wy+XS3//+dyUlJWnq1KmmIwEAEHIolMBRTJw4Ufn5+brzzjuV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ciiUsKzi4mJ17dpVZWVlWr9+vZKSkkxHAgDAkphDCUvyeDwaM2aMfvjhB61bt44yCQBAHaJQwpKmTp2qBQsWaMGCBTrttNNMxwEAwNIolLCcN954Qw8//LAeffRRDRw40HQcAAAsjzmUsJT169erR48eGj16tF5++WXZbDbTkQAAsDwKJSzjp59+UnJystq2basVK1YoJibGdCQAACIChRKWUFpaqu7du2v37t3auHGjmjVrZjoSAAARgzmUCHs+n0/jx4/Xli1blJubS5kEACDIKJQIew888IBmzZql2bNn64wzzjAdBwCAiGM3HQDwx3vvvac777xT9957r0aMGGE6DgAAEYk5lAhbmzZtUnp6ugYNGqRZs2axohsAAEMolAhLu3fvVnJysho3bqzVq1crLi7OdCQAACIWj7wRdioqKnTeeeepoqJCc+fOpUwCAGAYi3IQVnw+nyZOnKgPP/xQK1eu1AknnGA6EgAAEY9CibDy5JNP6pVXXtGMGTOUlpZmOg4AABBzKBFGFi9erMGDB+vmm2/WP//5T9NxAADAARRKhIWvvvpKqamp6t69u+bOnauoqCjTkQAAwAEUSoQ8p9Op1NRUxcTEaM2aNWrUqJHpSAAA4DDMoURIc7vdGjlypAoKCrRhwwbKJAAAIYhCiZB24403atWqVcrOzla7du1MxwEAAH+AQomQ9cILL+iZZ57R888/r549e5qOAwAA/gRzKBGSVq5cqczMTF155ZV65plnTMcBAABHQKFEyPn++++VnJysM844Q4sXL1Z0dLTpSAAA4AgolAgpRUVF6tq1qyoqKrR+/XolJiaajgQAAI6COZQIGR6PR2PGjNH//vc/yiQAAGGEQomQcccdd2jRokVasGCBOnToYDoOAACoJgolQsLrr7+uf/7zn3rsscc0YMAA03EAAEANMIcSxq1bt049e/bURRddpOnTp8tms5mOBAAAaoBCCaN++uknnXXWWWrfvr2WL1+umJgY05EAAEANUShhTGlpqbp166a9e/dqw4YNatasmelIAACgFphDCSN8Pp/GjRunr776Snl5eZRJAADCGIUSRtx///1655139O677+qvf/2r6TgAAMAPdtMBEHneffdd3X333brvvvt03nnnmY4DAAD8xBxKBNWmTZuUnp6uIUOG6M0332RFNwAAFkChRNDs2rVLycnJatq0qXJychQXF2c6EgAACAAeeSMoKioqNHz4cLndbs2bN48yCQCAhbAoB3XO5/Ppqquu0scff6xVq1apZcuWpiMBAIAAolCizj3++ON69dVX9d///lepqamm4wAAgABjDiXq1KJFizRkyBBNnjxZDz30kOk4AACgDlAoUWe2bNmitLQ09ejRQ3PnzpXdzpRdAACsiEKJOpGfn6/U1FTVr19fa9as0bHHHms6EgAAqCPMoUTAud1ujRw5Ui6XS9nZ2ZRJAAAsjkKJgLv++uuVk5OjZcuWqW3btqbjAACAOkahREA999xzevbZZ/Xiiy+qR48epuMAAIAgYA4lAmbFihXKzMzU3//+dz399NOm4wAAgCChUCIgtm7dqpSUFJ155plavHix6tXjzW8AACIFhRJ+KyoqUlpamqqqqrR+/XolJCSYjgQAAIKIt5HgF4/Ho4suuki//PKL1q1bR5kEACACUSjhlylTpmjx4sVatGiROnToYDoOAAAwgEKJWpsxY4b+9a9/6YknnlC/fv1MxwEAAIYwhxK1snbtWvXs2VN/+9vf9NJLL8lms5mOBAAADKFQosb+97//KTk5WSeddJKWLVummJgY05EAAIBBFErUSElJibp166b8/Hxt3LhRTZs2NR0JAAAYxhxKVJvX69W4ceP0zTffKC8vjzIJAAAkUShRA/fff79mz56tOXPmqHPnzqbjAACAEGE3HQDh4Z133tE999yjf/zjHxo2bJjpOAAAIIQwhxJH9cknnyg9PV1Dhw7VzJkzWdENAAB+hUKJI9q5c6eSk5PVvHlz5eTkqH79+qYjAQCAEMMjb/yp8vJyDR8+XB6PR3PnzqVMAgCAP8SiHPwhn8+nK6+8Up988olycnLUsmVL05EAAECIolDiDz322GOaMWOG3njjDaWkpJiOAwAAQhhzKPE7Cxcu1JAhQ3TbbbfpwQcfNB0HAACEOAolfuXLL79UWlqaevfurffee092O9NsAQDAkVEocUh+fr5SUlIUFxenNWvW6NhjjzUdCQAAhAHmUEKS5Ha7dcEFF6ioqEjLli2jTAIAgGqjUEKSNGnSJOXm5mrZsmVq27at6TgAACCMUCihZ599Vs8995ymTZum7t27m44DAADCDHMoI9zy5cvVt29fXXPNNXryySdNxwEAAGGIQhnBvvvuO6WkpOiss87SokWLVK8eb1gDAICao1BGqMLCQp199tnyeDxat26dEhISTEcCAABhirekIpDH49Ho0aP1yy+/aP369ZRJAADgFwplBLrtttu0dOlSLV68WKeccorpOAAAIMxRKCPMa6+9pkcffVRPPvmk+vbtazoOAACwAOZQRpA1a9aoV69euvjii/Xiiy/KZrOZjgQAACyAQhkhfvzxRyUnJ+uUU07RsmXLdMwxx5iOBAAALIJCGQFKSkqUkZEhl8ulDRs2qEmTJqYjAQAAC2EOpcV5vV5dcskl+u6777RmzRrKJAAACDgKpcXde++9eu+99zRnzhx16tTJdBwAAGBBFEoLe/vtt3XffffpwQcf1NChQ03HAQAAFsUcSov6+OOPlZGRoeHDh+u///0vK7oBAECdoVBa0I4dO5SSkqIWLVpo1apVql+/vulIAADAwuymAyCwysvLNXz4cHm9Xs2dO5cyCQAA6hxzKC3E5/NpwoQJ+vTTT5WTk6PjjjvOdCQAABABKJQW8q9//Uuvv/66Zs6cqeTkZNNxAABAhGAOpUUsWLBA5557rm6//Xb94x//MB0HAABEEAqlBXzxxRdKS0tTnz599O6778puZ2osAAAIHgplmNu7d69SU1PVsGFD5eXlqWHDhqYjAQCACMMcyjBWWVmp888/X8XFxVq+fDllEgAAGEGhDFM+n0/XXXed1qxZo+XLl6t169amIwEAgAhFoQxTzz77rF544QW99NJLysjIMB0HAABEMOZQhqEPPvhA/fr107XXXqsnnnjCdBwAABDhKJRh5ttvv1VqaqpSUlK0YMEC1avHm8wAAMAsCmUYKSwsVFpamnw+n9atWyeHw2E6EgAAAHMow4XH49GFF16onTt3av369ZRJAAAQMiiUYWLy5MnKzs7W4sWLdfLJJ5uOAwAAcAiFMgy88sorevzxx/X0008rMzPTdBwAAIBfYQ5liMvLy1OvXr106aWX6vnnn5fNZjMdCQAA4FcolCHshx9+UEpKijp06KDs7Gwdc8wxpiMBAAD8DoUyRO3bt08ZGRkqLCzUxo0b1bhxY9ORAAAA/hBzKEOQ1+vVxRdfrK1bt2rt2rWUSQAAENIolCHonnvu0dy5czV37lx17NjRdBwAAIAjolCGmFmzZun+++/XQw89pHPPPdd0HAAAgKNiDmUI+fDDD9WtWzeNGDFCr7/+Oiu6AQBAWKBQhogdO3YoOTlZLVu21KpVqxQbG2s6EgAAQLXYTQeAVFZWpmHDhkmS5s6dS5kEAABhhTmUhvl8Pl1xxRXavHmzVq9erRYtWpiOBAAAUCMUSsMeeeQRvfHGG3rrrbfUpUsX03EAAABqjDmUBs2fP19Dhw7V1KlTdd9995mOAwAAUCsUSkM+//xznX322crMzNTs2bNltzOdFQAAhCcKpQF79uxRSkqK4uPjlZubq4YNG5qOBAAAUGvMoQyyyspKnX/++SopKdHKlSspkwAAIOxRKIPI5/Ppmmuu0dq1a7VixQq1bt3adCQAAAC/USiryevzqbCiSq5yt1zlbpV7PPJ4fYqy2xQbFSVHbLQcsdGKj6kn+5+ccPPMM89o2rRpevnll5Wenh7knwAAAKBuMIfyKErdVfreVaptrlK5vft/VTZJh//SDv842m5TW0ec2jniFBf9/309OztbAwYM0KRJk/TYY48FKz4AAECdo1D+CbfHq817irS9sOx3BfJoDl7fJr6+OjVppG1bv1NqaqrS0tK0YMECRUVF1U1oAAAAAyiUf2BXSYU+3OFShcfr972OsUvP33mLtn76kdatW6f4+PgAJAQAAAgdFMrf2FpQok93FwXsfl6vV3a7XcfZKpR2cpuA3RcAACBUsJv2YQJdJiUd2rD8F1+MthaUBPTeAAAAoYBCecCukoqAl8nf+nR3kXaVVNTpGAAAAMFGodT+BTgf7nAFZayPdrjkDsDcTAAAgFBBoZS0eU+RKoNU8soPrB4HAACwiogvlCXuKm0vLKvRtkD+2l5YplJ3VRBHBAAAqDsRf1LONldptfeZ3PLReq1eMFfffPqRnLt2qqSoSAlNmqr1Kadq+BVXq8OZKdUa03Zg3NObNPInOgAAQEiI6G2DvD6fFn6369AJOEfzwt23KmvW63/69avu+5cyR46p1r2i7TYNOrHZnx7TCAAAEC4i+pF3YUVVtcukJNnsdp3db7Dumv6m3vj4O7246iOd3W/woa+/8fiD8ng81bqX27v/bHAAAIBwF9HvUG5zleqTXYXVvr50X7HiGh77q88VOvM1vmunQx+/tHqTEpo0rdb9zmgWr7aOuGqPDwAAEIoi+h1KV7lbNXng/NsyKUkVZWWHXsfUr69jHQnVupftwPgAAADhLqILZbnH49fqbp/PpxmP3Hfo48yRY1UvOrp633tgfAAAgHAX0YXSU4P5k7/lrqzU05Ov1dqlCyRJndIy9LebpgRtfAAAgFAR0dsGRdlrt8K6dF+xHrnmMm1elytJSu7dVzc8/pyij4kJyvgAAAChJKILZWxUVLX3oDwof9cOPTBhrH74+ktJUv+Lxmn8HfcrKiqqRmPbDowPAAAQ7iK6UDpio+Wr/iJv/fjNV/rHhDHK37lDNptNf7v5Dg277O+1Gtt3YHwAAIBwF9HbBhWUu7Xih73Vvv7ft12vlXPfPuI19742Wx1Tu1brfr1aN1YCpRIAAIS5iF6UEx9TT9GG5jFG222Kj4noN4gBAIBFRPQ7lJL0+Z4ifess8Wv7oJqySTo5sQFneQMAAEuI6HcoJamdIy6oZVLaP3+SE3IAAIBVRHyhjIuupzbx9YM6Zpv4+oqL5nE3AACwhogvlJLUqUkjxUYF51cRG2VXJx51AwAAC6FQSoqOsqtLC0dQxurSwqHoIJVXAACAYKDZHNCsQYw6N63bdw47N22kZg1qdpoOAABAqKNQHqZ9QoM6K5WdmzZS+4QGdXJvAAAAkyJ+26A/squkQh/tcKnc4/X7XrEHHqfzziQAALAqCuWfcHu82rynSNsLy2p83vfB69vE11enJo2YMwkAACyNQnkUpe4qbXOV6ntXqdze/b+q3xbMwz+OttvUzhGnto44tgYCAAARgUJZTV6fT4UVVXKVu+Uqd6vc45HH61OU3abYqCg5YqPliI1WfEw92W1mjnMEAAAwgUIJAAAAvzC5DwAAAH6hUAIAAMAvFEoAAAD4hUIJAAAAv1AoAQAA4BcKJQAAAPxCoQQAAIBfKJQAAADwC4USAAAAfqFQAgAAwC8USgAAAPiFQgkAAAC/UCgBAADgFwolAAAA/EKhBAAAgF8olAAAAPALhRIAAAB+oVACAADALxRKAAAA+IVCCQAAAL9QKAEAAOAXCiUAAAD8QqEEAACAXyiUAAAA8AuFEgAAAH6hUAIAAMAvFEoAAAD4hUIJAAAAv1AoAQAA4BcKJQAAAPxCoQQAAIBfKJQAAADwC4USAAAAfqFQAgAAwC//B2ih56Y9/u10AAAAAElFTkSuQmCC\n",
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
   "execution_count": 143,
   "id": "7a995687-56a9-4e4d-b97e-a3d9159a41cc",
   "metadata": {},
   "outputs": [],
   "source": [
    "wagi_lista = [1,-1,-1,1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 144,
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
   "execution_count": 145,
   "id": "c7edae33-fbbd-480e-b161-4678c075ef7e",
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
   "execution_count": 146,
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
    "    print(f\"Wierzchołki w kolejności wywoływania:  {nodes_z_odbiciem}, wagi na końcu: {wagi}, count:  {count}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 148,
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
   "id": "9ae0a7f9-1217-4bc0-9ae4-188c48fdd02f",
   "metadata": {},
   "source": [
    "# omijanie miejsc minusów"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "a153e943-ed0a-4ab9-975d-5904269df5e9",
   "metadata": {},
   "outputs": [],
   "source": [
    "def omijanie_ujemnych(G, lista, count=0):\n",
    "    nodes_z_odbiciem = []\n",
    "    wagi = []\n",
    "    Y = lista\n",
    "    while True:\n",
    "        nodes_dodatnie = [node for node, data in G.nodes(data='weight') if (data is not None and data < 0 and node not in Y)]\n",
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
   "cell_type": "code",
   "execution_count": 12,
   "id": "1afb9b9d-2ffb-4e31-b341-12b3d7f29b32",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Wierzchołki w kolejności wywoływania:  [], wagi na końcu: [None, None, None, None], count:  0\n"
     ]
    }
   ],
   "source": [
    "lista = (1,2,3)\n",
    "omijanie_ujemnych(D5, lista, count=0)"
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
   "execution_count": 14,
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
      "Podaj wartości wag jako listę:  1,2,-3,4\n",
      "Wskaż wierzchołki do omijania:  2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Wierzchołki w kolejności wywoływania:  [], wagi na końcu: [1, 2, -3, 4], count:  0\n"
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
    "    omijanie_ujemnych(G, lista, count=0)\n",
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
   "id": "121d9a5c-9f88-4ebc-9fcc-7ece1d1e4198",
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
