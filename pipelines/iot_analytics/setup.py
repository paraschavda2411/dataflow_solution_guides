#  Copyright 2025 Google LLC
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
"""
Setup file for the IoT Analytics pipeline.
"""

from setuptools import setup, find_packages

with open("requirements.txt", encoding="utf-8") as f:
  requirements = f.readlines()

setup(
    name="IoT Dataflow Anaytics Pipeline",
    version="0.1",
    packages=find_packages(),
    install_requires=requirements,
    package_data={"iot_analytics_pipeline": ["maintenance_model.pkl"]})
