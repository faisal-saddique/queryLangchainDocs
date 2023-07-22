Chat Message History
====================

The primary interface with language models at the moment in through a chat interface. The ChatMessageHistory class is responsible for remembering all previous chat interactions. These can then be passed directly back into the model, summarized in some way, or some combination.

ChatMessageHistory exposes two methods and one attribute. The two methods it exposes are `add_user_message` and `add_ai_message`, used for storing messages from users and responses from the AI accordingly. The attribute it exposes is a `messages` attribute, used for accessing all previous messages.