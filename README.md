# TWRPG Builder

Билдер персонажа для карты Warcraft III **The World RPG**: экипировка, сумма статов, дерево крафта, боссы и дроп, база предметов.

**Открыть:** https://krikyxa.github.io/TWRPG_builder/

## Возможности
- 5 слотов экипировки, выбор героя (фильтр оружия и специализаций), сумма статов и пассивок.
- Дерево крафта с отметками «уже есть» и списком «что ещё добыть» с боссами и шансами дропа.
- Боссы: локация, условия, характеристики, способности, дроп с шансами.
- Предметы: поиск, фильтры, рецепты, «падает с», «используется в».
- Сохранение сборок в браузере и обмен сборками через код (`TWB1:...`).

## Как устроено
- `index.html` — готовая страница (всё внутри: код, данные, иконки).
- `src/app.html` — исходник интерфейса, правьте его.
- `tools/build.py` — пересобирает `index.html` из `src/app.html` и свежих данных.

Обновить данные:
```
git clone --depth 1 https://github.com/sfarmani/twrpg-info.git ../twrpg-info
git clone --depth 1 https://github.com/sfarmani/twicons.git ../twicons
pip install pillow
python3 tools/build.py ../twrpg-info ../twicons
```

Данные: [sfarmani/twrpg-info](https://github.com/sfarmani/twrpg-info), иконки: [sfarmani/twicons](https://github.com/sfarmani/twicons).
