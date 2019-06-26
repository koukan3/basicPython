import collections
'''
1. __*__：双下方法/特殊方法(dunder-method)：
python解释器会使用特殊方法去激活一些基本的对象操作.
2.特殊方法的存在是为了让解释器调用，不是让用户调用。
3.通过实现特殊方法，自定义数据类型可以表现得跟内置类型一样.
4.“Data Model”（https://docs.python.org/3/reference/datamodel.html）
在特殊方法中，有近一半的方法是用于实现算术运算、位运算和比较操作。
'''
#namedtuple：创建一个有少量属性但没有方法的对象
Card = collections.namedtuple("card",['rank','suit'])
c = Card("1st","nothing")
print(c.rank,c.suit)

#创建一副纸牌
class FrenchDeck:
    #13张牌
    ranks = [str(n) for n in range(2,11)]+list("JQKA")
    #4种花色
    suits = ["hearts","diamonds","clubs","spades"]
    def __init__(self):
        #得到一副完整的扑克牌
        self.cards = [Card(rank,suit) for rank in self.ranks for suit in self.suits]
    def __getitem__(self, position):  #使得对象的实例可迭代、可切片
        return self.cards[position]
    def __len__(self):
        return len(self.cards)


print("#########测试纸牌")
fd = FrenchDeck()  #会去调用__init__(self)
print(fd.cards)
print(len(fd))   #会去调用__len__(self)
print(fd[9]) #会去调用__getitem__(self, position)

print("#########使用内置函数")
from random import choice
print(choice(fd))  #随机抽一张牌
print(choice(fd))
print("#########使用切片抽牌")
print("第1张牌：",fd[0])
print("前3张牌：",fd[:3])
print("第13张牌：",fd[12])
print("第23张牌：",fd[22])
print("第13张牌，再每隔10张抽一张牌：",fd[12::10])
print("#########反向罗列/迭代抽牌")
for c in reversed(fd):
    #先调用__len__获取长度，再调用__getitem__迭代出每个元素。
    print(c)
print(Card("3","spades") in fd)
print("####排序：2最小，A最大，从小到大：梅花、方块、红桃、黑桃")
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    #print("rank_value: ",rank_value)
    #对纸牌(牌面+花色)进行排序，
    return rank_value * len(suit_values) + suit_values[card.suit]
for c in reversed(sorted(fd,key=spades_high)):  #逆序/正序
    print(c)
