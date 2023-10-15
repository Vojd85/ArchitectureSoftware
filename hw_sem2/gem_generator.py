from i_item_fabric import ItemFabric
from i_game_item import IGameItem


class GemReward(IGameItem):
    def open(self):
        print('Gem')


class GemGenerator(ItemFabric):
    def create_item(self):
        print('Create new bag')
        return GemReward()