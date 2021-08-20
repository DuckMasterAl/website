# ----------------------------------------------------------------
# DO NOT REMOVE THE TEXT BELOW IF YOU USE THIS IN YOUR OWN PROJECT
# ----------------------------------------------------------------
#
# Optimize Image GitHub Workflow | Optimizes images via tinypng.com
# Copyright (C) 2021 DuckMasterAl @ bduck.xyz
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os, tinify
tinify.key = os.environ['api_key']
for x in eval(os.environ['added_files']):
  if x.split(".")[-1] not in ['png', 'jpg', 'jpeg', 'webp']:
    continue
  source = tinify.from_file(x)
  source.to_file(x)
