from collections import defaultdict
from math import inf, ceil


def read_factory(filename):
    factory = {}
    with open(filename) as f:
        for line in f.readlines():
            inputs, output = line.split('=>')
            output_quantity, output_chemical = output.strip().split(' ')
            inputs = map(lambda x: x.split(' '), inputs.strip().split(', '))

            factory[output_chemical] = {
                'quantity': int(output_quantity),
                'requires': []
            }
            for input_quantity, input_chemical in inputs:
                factory[output_chemical]['requires'].append({
                    'quantity': int(input_quantity),
                    'chemical': input_chemical
                })
    return factory


def calc_depth(factory):
    depth = {'ORE': 0}
    for output_chemical in factory.keys():
        depth[output_chemical] = _calc_depth(factory, output_chemical)
    return depth


def _calc_depth(factory, output_chemical):
    if output_chemical == 'ORE':
        return 0
    depth = 0
    for input_chemical in factory[output_chemical]['requires']:
        depth = max(depth, _calc_depth(factory, input_chemical['chemical']))
    return depth + 1


def produce_ore(factory, depth, quantity_to_produce):
    ore_needed = 0
    to_produce = [{
        'chemical': 'FUEL',
        'quantity': quantity_to_produce
    }]

    remainders = defaultdict(int)
    while to_produce:
        # select with highest depth
        highest_depth_idx = -1
        highest_depth = -inf
        for output_idx, output in enumerate(to_produce):
            output_chemical = output['chemical']
            if depth[output_chemical] > highest_depth:
                highest_depth_idx = output_idx
                highest_depth = depth[output_chemical]

        output = to_produce.pop(highest_depth_idx)
        output_chemical = output['chemical']
        output_quantity = output['quantity']

        if remainders[output_chemical] >= output_quantity:
            remainders[output_chemical] -= output_quantity
            continue

        if output_chemical == 'ORE':
            ore_needed += output_quantity
            continue

        reaction = factory[output_chemical]
        reaction_quantity = reaction['quantity']
        reaction_inputs = reaction['requires']

        quantity_produced = ceil(output_quantity / reaction_quantity)
        for reaction_input in reaction_inputs:
            input_name = reaction_input['chemical']
            input_quantity = quantity_produced * reaction_input['quantity']

            for idx in range(len(to_produce)):
                if to_produce[idx]['chemical'] == input_name:
                    to_produce[idx]['quantity'] += input_quantity
                    break
            else:
                to_produce.append({
                    'chemical': input_name,
                    'quantity': input_quantity,
                })

        diff = quantity_produced * reaction_quantity - output_quantity
        remainders[output_chemical] += diff

    return ore_needed

factory = read_factory('14.txt')
depth = calc_depth(factory)

units_ore = 1000000000000

fuel_quantity = 1

ore_needed = produce_ore(factory, depth, 1)
fuel_quantity = round(units_ore / ore_needed)
ore_needed = produce_ore(factory, depth, fuel_quantity)

fuel_quantity = round(units_ore / ore_needed * fuel_quantity)

ore_needed = produce_ore(factory, depth, fuel_quantity)
if ore_needed > units_ore:
    fuel_quantity -= 1

print(fuel_quantity)
