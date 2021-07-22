
import sys
sys.path.append('../src')

from auto import auto
import state

_ = auto(state)

print('filenames = '+str(_.filenames))
print('contents = '+str(_.contents))