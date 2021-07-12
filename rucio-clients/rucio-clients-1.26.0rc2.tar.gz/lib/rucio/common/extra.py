# -*- coding: utf-8 -*-
# Copyright 2021 CERN
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Authors:
# - Benedikt Ziemons <benedikt.ziemons@cern.ch>, 2021

import importlib
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List, Dict, Any


def import_extras(module_list):
    # type: (List[str]) -> Dict[str, Any]
    out = dict()
    for mod in module_list:
        out[mod] = None
        try:
            out[mod] = importlib.import_module(mod)
        except ImportError:
            pass
    return out
