# Rule_visualization 
This repo contains an association rule visualization project, Python.

### Association rule
One of the major techniques to detect and extract useful information from large scale transaction data

introduced by **Agrawal, Imielinski, and Swami (1993)**



### Installation
NetworkX

  * Python library for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks.

  * Get NetworkX from the Python Package Index at **http://pypi.python.org/pypi/networkx** 
  
    or install it with ```pip install networkx```
    

### Usage
```python
new_rule = make_dict(make_input(rules, rules_num), rules_num)
```

![image](https://user-images.githubusercontent.com/41055617/58598861-f0f9b200-82b8-11e9-9ebb-945b63e842da.png)

 * Function
   * **Make_input** 
   
     [Input]

     Rules: Output of ```mlxtend```

     Rule_num: The number of rules you want to visualize


     [Output]

     Input_vis: Antecedents, consequents, support and confidence after data preprocessing

   * **Make_dict**

     [Input]

     Input_vis: Output of Make_input

     Rule_num: The number of rules you want to visualize


     [Output]

     Rules: (Dictionary) Key: consequents / value: antecedents and corresponding support, confidence

   * **Visualize_rule**
    
     [Input]

     Rules: (Dictionary) Key: consequents / value: antecedents and corresponding support, confidence


     [Output]

     Figure
  
  
