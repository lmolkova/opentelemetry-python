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

SYSTEM_CPU_LOGICAL_NUMBER = "system.cpu.logical_number"
"""
The logical CPU number [0..n-1]
"""

SYSTEM_CPU_STATE = "system.cpu.state"
"""
The state of the CPU
"""

SYSTEM_DEVICE = "system.device"
"""
The device identifier
"""

SYSTEM_FILESYSTEM_MODE = "system.filesystem.mode"
"""
The filesystem mode
"""

SYSTEM_FILESYSTEM_MOUNTPOINT = "system.filesystem.mountpoint"
"""
The filesystem mount path
"""

SYSTEM_FILESYSTEM_STATE = "system.filesystem.state"
"""
The filesystem state
"""

SYSTEM_FILESYSTEM_TYPE = "system.filesystem.type"
"""
The filesystem type
"""

SYSTEM_MEMORY_STATE = "system.memory.state"
"""
The memory state
"""

SYSTEM_NETWORK_STATE = "system.network.state"
"""
A stateless protocol MUST NOT set this attribute
"""

SYSTEM_PAGING_DIRECTION = "system.paging.direction"
"""
The paging access direction
"""

SYSTEM_PAGING_STATE = "system.paging.state"
"""
The memory paging state
"""

SYSTEM_PAGING_TYPE = "system.paging.type"
"""
The memory paging type
"""

SYSTEM_PROCESS_STATUS = "system.process.status"
"""
The process state, e.g., [Linux Process State Codes](https://man7.org/linux/man-pages/man1/ps.1.html#PROCESS_STATE_CODES)
"""

SYSTEM_PROCESSES_STATUS = "system.processes.status"
"""
Deprecated: Replaced by `system.process.status`.
"""


class SystemCpuStateValues(Enum):
    USER = "user"

    SYSTEM = "system"

    NICE = "nice"

    IDLE = "idle"

    IOWAIT = "iowait"

    INTERRUPT = "interrupt"

    STEAL = "steal"


class SystemFilesystemStateValues(Enum):
    USED = "used"

    FREE = "free"

    RESERVED = "reserved"


class SystemFilesystemTypeValues(Enum):
    FAT32 = "fat32"

    EXFAT = "exfat"

    NTFS = "ntfs"

    REFS = "refs"

    HFSPLUS = "hfsplus"

    EXT4 = "ext4"


class SystemMemoryStateValues(Enum):
    USED = "used"

    FREE = "free"

    SHARED = "shared"
    """Deprecated: Removed, report shared memory usage with `metric.system.memory.shared` metric"""

    BUFFERS = "buffers"

    CACHED = "cached"


class SystemNetworkStateValues(Enum):
    CLOSE = "close"

    CLOSE_WAIT = "close_wait"

    CLOSING = "closing"

    DELETE = "delete"

    ESTABLISHED = "established"

    FIN_WAIT_1 = "fin_wait_1"

    FIN_WAIT_2 = "fin_wait_2"

    LAST_ACK = "last_ack"

    LISTEN = "listen"

    SYN_RECV = "syn_recv"

    SYN_SENT = "syn_sent"

    TIME_WAIT = "time_wait"


class SystemPagingDirectionValues(Enum):
    IN = "in"

    OUT = "out"


class SystemPagingStateValues(Enum):
    USED = "used"

    FREE = "free"


class SystemPagingTypeValues(Enum):
    MAJOR = "major"

    MINOR = "minor"


class SystemProcessStatusValues(Enum):
    RUNNING = "running"

    SLEEPING = "sleeping"

    STOPPED = "stopped"

    DEFUNCT = "defunct"


class SystemProcessesStatusValues(Enum):
    RUNNING = "running"

    SLEEPING = "sleeping"

    STOPPED = "stopped"

    DEFUNCT = "defunct"
