pokemon = ['pikachu', 'charmander', 'squirtle', 'bulbasaur']
types = ['electric', 'fire', 'water', 'grass']
levels = [16, 11, 9, 12]
fainted = [True, False, False, False]

def next_pokemon(pokemon, levels, fainted):
  best_level = -1
  best_choice = pokemon[0]
  for curr_pokemon, level, has_fainted in zip(pokemon, levels, fainted):
    if not has_fainted and level > best_level:
      best_level = level
      best_choice = curr_pokemon
  return best_choice

next_pokemon(pokemon, levels, fainted)  # returns bulbasaur
