import itertools
from matplotlib import pyplot as plt
import networkx as nx

def make_input(rules, rule_num):
    '''
    :param rules: Output of mlxtend - association rule
    :param rule_num: The number of rules you want to visualize

    :return: Antecedents, consequents, support and confidence after data preprocessing
    '''

    # Bring antecedents, consequents, support and confidence from output of mlxtend
    input = rules[['antecedents', 'consequents', 'support', 'confidence']]

    # Sort by confidence
    sorted_input = input.sort_values(by=['confidence'], ascending=False)

    # Bring only as much as the rule_num
    input_vis = sorted_input[0: rule_num]
    input_vis = input_vis.reset_index(drop = True)

    # Preprocess antecedents and consequents consisting of frozenset(data type) by separating one by one element
    consequent_set = []
    for consequent in input_vis['consequents']:
        consequent = list(consequent)
        consequent_set.append(consequent)

    for i in range(len(consequent_set)):
        input_vis['consequents'][i] = consequent_set[i]

    antecedent_set = []
    for antecedent in input_vis['antecedents']:
        antecedent = list(antecedent)
        antecedent_set.append(antecedent)

    for i in range(len(antecedent_set)):
        input_vis['antecedents'][i] = antecedent_set[i]

    return input_vis


def make_dict(input_vis, rule_num):
    '''
    :param input_vis: Output of Make_input
    :param rule_num: The number of rules you want to visualize

    :return: (Dictionary) Key: consequents / value: antecedents and corresponding support, confidence
    '''
    input_vis = make_input(input_vis, rule_num)

    consequent_set = []
    for consequent in input_vis['consequents']:
        consequent = list(consequent)
        consequent_set.append(consequent)

    # Set the list composed of consequents included in the rule
    consequent_set = list(itertools.chain.from_iterable(consequent_set))
    consequent_set = set(consequent_set)

    # Set up the consequents as key and each element of antecedents, support, confidence as value
    # e.g. {Consequent: [antecedent1, support1, confidence1], [antecedent2, support2, confidence2], [antecedent3, support3, confidence3],,,}
    rules = {str(key): [] for key in consequent_set}
    for i in range(len(input_vis)):
        for key in consequent_set:
            for j in range(len(input_vis['consequents'][i])):
                if input_vis['consequents'][i][j] == key:
                    for k in range(len(input_vis['antecedents'][i])):
                        rules[str(key)].append([input_vis['antecedents'][i][k], input_vis['support'][i], input_vis['confidence'][i]])

    new_rule={}

    # Calculate the sum of supports and max of confidence when antecedents corresponding to a consequent are duplicated
    for key, valuelist in rules.items():
        new_dic={}
        for value in valuelist:
            if value[0] in new_dic.keys():
                new_dic[value[0]] = [value[0],new_dic[value[0]][1]+value[1],max(new_dic[value[0]][2], value[2])]
            else:
                new_dic[value[0]] = value

        new_rule[key] = list(new_dic.values())

    return new_rule

def visual(new_rule):

    ruleGraph = nx.Graph()

    # Filled node = consequents, unfilled node = antecedents, edge thickness = support
    for key, value in new_rule.items():
        for j in value:
            ruleGraph.add_node((j[0].replace("'", "")), node_color = 'white',  with_labels = True,  nodesize = antecedent_nodesize)
            ruleGraph.add_node((key), pos = (5, 5), node_color = 'lightgray', with_labels = True,  nodesize = consequent_nodesize)
            ruleGraph.add_edge((key),(j[0].replace("'", "")), weight = int(j[1]), length = length)

    edges = ruleGraph.edges()
    weights = [ruleGraph[u][v]['weight'] for u, v in edges]

    # network options
    options = {'font_family': 'Times New Roman', 'font_size': font_size}

    with_labels = [ruleGraph.node[node]['with_labels'] for node in ruleGraph]
    colors = [ruleGraph.node[node]['node_color'] for node in ruleGraph]
    sizes = [ruleGraph.node[node]['nodesize'] for node in ruleGraph]

    plt.figure(figsize=(25, 25))
    pos = nx.spring_layout(ruleGraph)
    nx.draw(ruleGraph,  edges = edges, node_size = sizes, width = weights, node_color = colors, with_labels = True, pos = pos, **options)

    plt.show()
