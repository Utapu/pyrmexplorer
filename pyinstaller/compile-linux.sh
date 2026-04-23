#!/usr/bin/env bash

# This file is part of the pyrmexplorer software that allows exploring
# and downloading content stored on Remarkable tablets.
#
# Copyright 2019 Nicolas Bruot (https://www.bruot.org/hp/)
#
#
# pyrmexplorer is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyrmexplorer is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pyrmexplorer.  If not, see <http://www.gnu.org/licenses/>.


set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "${script_dir}/.." && pwd)"
build_dir="${repo_root}/build"
dist_dir="${repo_root}/dist"
spec_dir="${repo_root}"

cd "${script_dir}"

rm -rf "${build_dir}" "${dist_dir}" "${spec_dir}/rmexplorer.spec"

pyinstaller --paths=.. \
    --workpath "${build_dir}" \
    --distpath "${dist_dir}" \
    --specpath "${spec_dir}" \
    --add-data "${repo_root}/README:." \
    --add-data "${repo_root}/COPYING:." \
    --add-data "${repo_root}/rmexplorer/icon.ico:." \
    --add-data "${repo_root}/rmexplorer/icon.svg:." \
    --icon="${repo_root}/rmexplorer/icon.svg" \
    -n rmexplorer -w "${script_dir}/rmexplorer_pyi.py"

printf '\nLinux bundle created at %s\n' "${repo_root}/dist/rmexplorer"
