from viptela import ViptelaClient
import argparse
import logging
import yaml
import helpers


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", "-c", help="Path to the configuration file", default="viptela.cfg")
    parser.add_argument("--debug", "-d", help="Display debug logs", action="store_true")
    return parser.parse_args()


def init_logger(log_level=logging.INFO):
    logger = logging.getLogger(__file__)
    logger.setLevel(log_level)

    console_handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    if log_level == 10:
        # create file handler which logs even debug messages
        fh = logging.FileHandler('log_file.txt')
        formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
        fh.setFormatter(formatter)
        fh.setLevel(logging.DEBUG)
        logger.addHandler(fh)
    return logger


class ConfigSync:

    def __init__(self, config, log):
        self.log = log
        self.config_file = config
        self.log.info('Initializing ConfigSync Class.')
        self.config = self._parse_config(config)
        self.viptela = self._init_viptela_client(self.config)
        self.log.debug('Finished initializing the configSync class.')

    def _parse_config(self, config_file):
        self.log.info('Parsing the configuration file.')
        with open(config_file, 'r') as f:
            config = yaml.safe_load(f)
        self.log.debug(f'The following parameters were received: {config}')
        return config

    def _init_viptela_client(self, config):
        self.log.info('Initializing ViptelaClient class.')
        host = config.get('viptela_host')
        username = config.get('viptela_username')
        password = config.get('viptela_password')
        port = config.get('viptela_port')
        self.log.debug(f'Username is {username} and password is {password}')
        viptela = ViptelaClient(host, username=username, password=password, port=port, log=self.log)
        self.log.info('Login to Viptela.')
        viptela.login_sdk()
        return viptela


if __name__ == "__main__":
    args = parse_arguments()

    if args.debug:
        log = init_logger(logging.DEBUG)
    else:
        log = init_logger()
    log.info(f'Viptela ConfigSync started.')
    log.info(f'Viptela module ViptelaClient is starting.')
    # Instantiate ConfigSync which will launch connection to Viptela, setup logging, and
    # load configuration from config file.
    cs = ConfigSync(config=args.config, log=log)
    # Start custom scripting here.  Use the CS object to interact with functions above or pull modules
    # directly from the helper file.

    log.info(f'Viptela ConfigSync finished.')

