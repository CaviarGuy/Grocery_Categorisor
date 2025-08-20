import ollama
import os

model = "llama3.2:latest"



input_file = input("Please enter item_list path [for e.g:./data/input_list.txt]:")
output_file = "./data/output_list.txt"


if not os.path.exists(input_file):
    print(f"invalid file path '{input_file}'")
    exit(1)

with open(input_file,"r") as f:
    items = f.read().strip()

prompt = f""" 
You are a smart grocery assistant.
Your job is to take a list of grocery items and classify them into categories.

Categories:
1. Fresh Produce (Fruits & Vegetables)
2. Dairy & Eggs
3. Meat, Fish & Poultry
4. Grains, Pulses & Pantry Staples
5. Snacks & Packaged Foods
6. Beverages
7. Frozen Foods
8. Oils, Spices & Condiments
9. Bakery Items
10. Household & Cleaning

Always return the result in this format:

Fresh Produce:
- item1
- item2

Dairy & Eggs:
- item3
...

The user has provided a mixed list of items.

Your task:
1. Categorize **grocery items** into subcategories like Vegetables, Fruits, Dairy, Beverages, Grains, Packaged Food, Cleaning Essentials, Personal Care, etc.  
2. For **non-grocery items**, detect the correct category (such as Stationery, Electronics, Clothing, Household Items, Toys, etc.) and place them in a separate section.  
3. Every item must belong to some category.  
4. Keep output neat with clear section headers.


PARAMETER temperature 0.3
PARAMETER top_p 0.9

# Template prompt
TEMPLATE 
Categorize the following grocery items:

{items}

"""


try:
    res = ollama.generate(model = model, prompt= prompt)
    generated_text = res.get("response", "")
    print(generated_text)

    with open(output_file , "w") as f:
        f.write(generated_text.strip())
        print(f"categorized list is saved in '{output_file}'")

except Exception as e:
    print("error occurred:" , str(e))