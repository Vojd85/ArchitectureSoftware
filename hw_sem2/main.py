from random import choice
from gold_generator import GoldGenerator
from gem_generator import GemGenerator
from potion_generator import PotionGenerator
from charm_generator import CharmGenerator


if __name__ == '__main__':
    
    lst = [GoldGenerator(), GemGenerator(), PotionGenerator(), CharmGenerator()]
    for i in range(20):
        choice(lst).open_reward()