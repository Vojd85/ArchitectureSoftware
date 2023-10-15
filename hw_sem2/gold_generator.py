from i_item_fabric import ItemFabric
from i_game_item import IGameItem


class GoldReward(IGameItem):
    def open(self):
        print('Gold')


class GoldGenerator(ItemFabric):
    def create_item(self):
        print('Create new bag')
        return GoldReward()