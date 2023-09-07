import pandas as pd
df = pd.DataFrame(
    # store given data in a table 
    #A DataFrame is a 2-dimensional data structure 
    
        {
            "Name": [
                "Alice, Ms. Duong",
                "Bob, Mr. Henzal",
                "Steve, Mr. Wall",
            ],
            "Age": [23, 27, 30],
            "Sex": ["female", "male", "male"],
        #table has 3 columns: name, age, sex
        }
    )