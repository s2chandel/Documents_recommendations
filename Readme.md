# GETTING STARTED
Run flask HTTP server

>app.py

# API ENDPOINT
>'Content-Type: application/json'

```POST /```

## Request Body : 
    ```json
    {"text":<"Enter your question">}
    ```
## Response from the model: 
    ```json
    {"ques_recs_ids": [
        869,
        3285,
        4185,
        4697,
        5505
    ]
    }```   

## Model Description

> Question recommendations model.

> feature extraction over questions asked in the db implemented to convert words to vectors, analyzing words over 1-2gram pairs.

> Cosine similarity metric calculates the similarities between the input question and rest.

> During inference 5 similar ques_ids are served by the model.




***
***
