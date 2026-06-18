
from pinecone import Pinecone
pc = Pinecone(api_key="pcsk_Nz1vW_DrnygV5ZJaMUkde3nPg2dX8tuygBzrYKyAnnta9WXkSsbazcxDFwdymHAG947zF")

# assistant = pc.assistant.create_assistant(
#     assistant_name="example-assistant",
#     instructions="Answer in polite, short sentences. Use American English spelling and vocabulary.",
#     timeout=30 # Wait 30 seconds for assistant operation to complete.
# )




# Connect to the assistant you just created
# Fetch the existing assistant instead of using the broken constructor
assistant = pc.assistant.describe_assistant(assistant_name="example-assistant")

# Upload a file from your local machine
response = assistant.upload_file(
    file_path="./do.txt",
    metadata={"type": "project_data"}, # Optional: Useful for filtering later
    timeout=None
)

print("File successfully uploaded and is processing!")






print("Thinking...")
chat_response = assistant.chat(
    messages=[
        {"role": "user", "content": "Who is the Chief Security Officer for Project Orion and what are they responsible for?"}
    ]
)

# 4. Print the assistant's generated answer
print("\nAnswer:")
print(chat_response.message.content)






