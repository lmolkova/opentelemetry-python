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

from deprecated import deprecated

# messaging.destination.name undefined
MESSAGING_DESTINATION_NAME = "messaging.destination.name"
"""# false
# true
The message destination name
Note: Destination name SHOULD uniquely identify a specific queue, topic or other entity within the broker. If
the broker doesn't have such notion, the destination name SHOULD uniquely identify the broker.
"""

# messaging.message.body.size undefined
MESSAGING_MESSAGE_BODY_SIZE = "messaging.message.body.size"
"""# false
# true
The size of the message body in bytes.
Note: This can refer to both the compressed or uncompressed body size. If both sizes are known, the uncompressed
body size should be used.
"""

# messaging.message.conversation_id undefined
MESSAGING_MESSAGE_CONVERSATION__ID = "messaging.message.conversation_id"
"""# false
# true
The conversation ID identifying the conversation to which the message belongs, represented as a string. Sometimes called "Correlation ID".
"""

# messaging.message.envelope.size undefined
MESSAGING_MESSAGE_ENVELOPE_SIZE = "messaging.message.envelope.size"
"""# false
# true
The size of the message body and metadata in bytes.
Note: This can refer to both the compressed or uncompressed size. If both sizes are known, the uncompressed
size should be used.
"""

# messaging.message.id undefined
MESSAGING_MESSAGE_ID = "messaging.message.id"
"""# false
# true
A value used by the messaging system as an identifier for the message, represented as a string.
"""
