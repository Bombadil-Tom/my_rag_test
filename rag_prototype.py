import os
import os.path
from llama_index import (
    ServiceContext,
    PromptHelper,
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    OpenAIEmbedding,
    load_index_from_storage,
)
from llama_index import set_global_service_context
from llama_index.llms import OpenAI
from llama_index.text_splitter import SentenceSplitter


key = ""
os.environ['OPENAI_API_KEY'] = key

llm = OpenAI(model="text-davinci-003", temperature=0, max_tokens=256)
embed_model = OpenAIEmbedding()
text_splitter = SentenceSplitter(chunk_size=1024, chunk_overlap=20)
prompt_helper = PromptHelper(
    context_window=4096,
    num_output=1000,
    chunk_overlap_ratio=0.1,
    chunk_size_limit=None,
)

service_context = ServiceContext.from_defaults(
    llm=llm,
    embed_model=embed_model,
    text_splitter=text_splitter,
    prompt_helper=prompt_helper,
)
set_global_service_context(service_context)

# check if storage already exists
if not os.path.exists("./storage"):
    # load the documents and create the index
    documents = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(documents)
    # store it for later
    index.storage_context.persist()
else:
    # load the existing index
    storage_context = StorageContext.from_defaults(persist_dir="./storage")
    index = load_index_from_storage(storage_context)

# either way we can now query the index
query_engine = index.as_query_engine(service_context=service_context)
response = query_engine.query("describe the difference between medicine 1.0, 2.0 and 3.0")
print(response)