# Smart Linking of Opportunities and Profiles (SLOP)

A RAG-powered agent that job postings, retrieves relevant experience from a knowledge base, and tailors resumes to specific opportunities.

## Notes
###  08/06/2026
Looked into embedding models.
They're just models trained on sentences to encode
them properly semantically. 

Choosing [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
because it's considered "lightweight" (~1.6 gB of usage?) fast embedding times with the tradeoff that
it has a lower retrieval accuracy.  Might change to BGE-Base-v1.5? 

Control flow for new person:  
User logs in maybe idk yet -> user has to upload a resume and is parsed and stored in user_info DB -> 
user gets to submit a url for a job whomp whomp stored in embedding_db based off of url job description -> 
chat gets enabled, website parsing, priming stuff? (look into this) ->
retrieve semantic stuff, generate new/refined bullets for jobs -> send back to user and wait for user input

### 08/07/2026
Based on the control flow and the usecase, there may be no need for additional executors.
ResumeExecutor will execute uploading, searching, and response generation. 

### 08/15/2026
Integrating PostgresSQL.
asyncpg connection pools natively optimize for high-concurrency, asynchronous environments, whereas psycopg2-binary 
connection pools are strictly designed for traditional, multi-threaded synchronous applications.