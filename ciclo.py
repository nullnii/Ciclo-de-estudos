import sys
def main():
	modo, config = get_config()
	ciclo = ciclo(modo, config)


def get_config():
	#TODO: receber configuracoes da linha de comando
	STD_CONFIG = {
		"D": 6,
		"H_D": 3,
		"L": "hobby, faculdade, outro",
	}

	config = sys.argv
	argc = len(config)
	if argc == 1:
		return ("-o", STD_CONFIG)
	#TODO: implementar regex

	return match_ops([op for op in ops])
	


def match_ops(ops):
	#TODO: implementar verificacoes das opcoes passadas pela linha de comando
	OPS = [
		'o',
		'h',
		'u',
		'config',
	] # add mais ops conforme a necessidade
	for 

def ciclo(modo, config):
	#TODO: match com as funcoes de operacao 
	


def _help():
	#TODO: implementar -h


def _out():
	#TODO: implementar -o


def _pseudo_interativo():
	#TODO: implementar -u (update)


def _temas():
	#TODO: implementar recebimento de temas e suas especificacoes


def get_tema():
	#TODO: implementar recebimento de temas
