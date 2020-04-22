import subprocess

import pytest


def capture(command):
	proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, _ = proc.communicate()

	return out


file = 'manual.py'


@pytest.mark.parametrize('i, state, expected', [
	('1', '25H0,32S0,46R1,63H1,76S1', b'........\n........\n........\n...S..H.\n........\n...H....\n....R..S\n........\n'),
	('2', '25H0,32S0,46R1,63H1,76S1', b'........\n........\n........\n....S.H.\n...S....\n........\n....R..S\n........\n'),
	('3', '25H0,32S0,46R1,63H1,76S1', b'........\n........\n....S...\n......H.\n..S.....\n........\n....R..S\n........\n'),
	('4', '25H0,32S0,46R1,63H1,76S1', b'........\n........\n.....S..\n......S.\n.S......\n........\n....R..S\n........\n'),
	('13', '25H0,32S0,46R1,63H1,76S1', b'........\n.S......\n........\n......S.\n........\n.......S\n....R..S\n........\n'),
	('14', '25H0,32S0,46R1,63H1,76S1', b'.R......\n........\n........\n......S.\n.......S\n........\n....R..R\n........\n'),
	('20', '25H0,32S0,46R1,63H1,76S1', b'.R......\n........\n........\n......RR\n........\n........\n....R..R\n........\n'),
	('30', '25H0,32S0,46R1,63H1,76S1', b'.R......\n........\n........\n......R.\n........\n........\n.R..R..R\n........\n'),
])
def test_something(i, state, expected):
	assert capture(['python3', file, i, state]) == expected
