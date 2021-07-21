
import sys
sys.path.append('../src')

from auto import auto
import state

_ = auto(state)

print('pefa_inputs = '+_.pefa_inputs)