from i_item_fabric import ItemFabric
from i_game_item import IGameItem


class CharmReward(IGameItem):
    def open(self):
        print('Charm')


class CharmGenerator(ItemFabric):
    def create_item(self):
        print('Create new bag')
        return CharmReward()