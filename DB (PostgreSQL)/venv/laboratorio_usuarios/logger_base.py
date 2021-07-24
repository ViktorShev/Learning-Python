import logging as log

log.basicConfig(level=log.DEBUG, 
                format='%(asctime)s: %(levelname)s: %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('usuario_laboratorio.log'),
                    log.StreamHandler()
                ])
