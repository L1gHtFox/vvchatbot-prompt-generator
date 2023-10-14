from dataclasses import dataclass
import re

@dataclass
class Recipe:
    name: str
    recipe: str
    all_time: str
    act_time: str
    level: str
    description: str
    ingredients: str
    value: str

    def _get_context(self) -> str:
        """
        :return:
        """
        return f"""
        Общее время: {self.all_time} \n Активное время: {self.act_time} \n Сложность: {self.level} \n  
        Рецепт: {self._clean_text(self.recipe)} \n Ингредиенты на 4 порции: {self.ingredients} \n Способ приготовления: 
        {self._clean_text(self.value)} 
        """

    @staticmethod
    def _clean_text(text) -> str:
        return re.sub(r'[\r\n\t]', '', re.sub(r'<.*?>', '', text))

    def __call__(self, *args, **kwargs):
        return {
            'title': self.name,
            'context': self._get_context()
        }
