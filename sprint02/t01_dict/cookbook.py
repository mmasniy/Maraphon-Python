def search_cookbook(cookbook, recipe, section):
    search_recipe = cookbook.get(recipe, False)
    if search_recipe:
        search_section = search_recipe.get(section, False)
        if search_section:
            return search_section
        else:
            return f'There is no section "{section}" in the "{recipe}" recipe.'
    else:
        return f'There is no "{recipe}" recipe in the cookbook.'
