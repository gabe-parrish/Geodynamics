# ===============================================================================
# Copyright 2019 Gabriel Parrish
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ===============================================================================
import os
import numpy as np
import math
from matplotlib import pyplot as plt


"""Write your first code to visualize sin, cos functions in 2d. Gerya pg. 9"""


# === 2d ====
circle_arr = np.linspace(start=0, stop=(2*math.pi), num=50)

print(circle_arr)
sin_arr = np.sin(circle_arr)

cos_arr = np.cos(circle_arr)

plt.plot(circle_arr, sin_arr)
plt.show()

plt.plot(circle_arr, cos_arr)
plt.show()

# ==== 3d =====
# TODO - implement 3d.