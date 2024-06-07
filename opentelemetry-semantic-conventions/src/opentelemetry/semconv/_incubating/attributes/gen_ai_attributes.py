# Copyright The OpenTelemetry Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from enum import Enum

GENAI_COMPLETION = "gen_ai.completion"
"""
The full response received from the LLM.
Note: It's RECOMMENDED to format completions as JSON string matching [OpenAI messages format](https://platform.openai.com/docs/guides/text-generation)
"""

GENAI_PROMPT = "gen_ai.prompt"
"""
The full prompt sent to an LLM.
Note: It's RECOMMENDED to format prompts as JSON string matching [OpenAI messages format](https://platform.openai.com/docs/guides/text-generation)
"""

GENAI_REQUEST_MAXTOKENS = "gen_ai.request.max_tokens"
"""
The maximum number of tokens the LLM generates for a request.
"""

GENAI_REQUEST_MODEL = "gen_ai.request.model"
"""
The name of the LLM a request is being made to.
"""

GENAI_REQUEST_TEMPERATURE = "gen_ai.request.temperature"
"""
The temperature setting for the LLM request.
"""

GENAI_REQUEST_TOPP = "gen_ai.request.top_p"
"""
The top_p sampling setting for the LLM request.
"""

GENAI_RESPONSE_FINISHREASONS = "gen_ai.response.finish_reasons"
"""
Array of reasons the model stopped generating tokens, corresponding to each generation received.
"""

GENAI_RESPONSE_ID = "gen_ai.response.id"
"""
The unique identifier for the completion.
"""

GENAI_RESPONSE_MODEL = "gen_ai.response.model"
"""
The name of the LLM a response was generated from.
"""

GENAI_SYSTEM = "gen_ai.system"
"""
The Generative AI product as identified by the client instrumentation.
Note: The actual GenAI product may differ from the one identified by the client. For example, when using OpenAI client libraries to communicate with Mistral, the `gen_ai.system` is set to `openai` based on the instrumentation's best knowledge.
"""

GENAI_USAGE_COMPLETIONTOKENS = "gen_ai.usage.completion_tokens"
"""
The number of tokens used in the LLM response (completion).
"""

GENAI_USAGE_PROMPTTOKENS = "gen_ai.usage.prompt_tokens"
"""
The number of tokens used in the LLM prompt.
"""


class GenaiSystemValues(Enum):
    OPENAI = "openai"
    """
    OpenAI
    """
