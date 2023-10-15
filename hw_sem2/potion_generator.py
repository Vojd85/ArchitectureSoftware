from i_item_fabric import ItemFabric
from i_game_item import IGameItem


class PotionReward(IGameItem):
    def open(self):
        print('Potion')


class PotionGenerator(ItemFabric):
    def create_item(self):
        print('Create new bag')
        return PotionReward()