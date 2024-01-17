from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Tcp:
    '''
    Handles TCP parameters connections

    Args:
        ip (str)        : The ip address ("000.000.000.000")
        hostname (str)  : The given name in the network
        mac (str)       : The address embedded in the device ()
    
    Raises:
        None

    Returns:
        None
    '''

    ip          : Optional[str] = ''
    hostname    : Optional[str] = ''
    mac         : Optional[str] = ''

@dataclass(repr=True)
class Controller:
    '''
    Stores controllers data

    Args:
        networks (list) : Available connections to the device
    
    Raises:
        None

    Returns:
        None
    '''
    
    networks : Optional[Tcp] = None

spu_t_pp01 = Controller(
    networks=Tcp(
        ip = '10.33.35.20', 
        hostname='DMC4103-22962.abtlus.org.br', 
        mac='00-50-4c-38-59-b2'
        )
    )

coi_pp01 = Controller(
    networks = Tcp(
        ip = '10.20.56.33', 
        hostname = 'DMC4103-716.abtlus.org.br', 
        mac = '00-50-4c-38-02-cc'
        )
    )

# print(spu_t_pp01)
# print(spu_t_pp01.networks.hostname)