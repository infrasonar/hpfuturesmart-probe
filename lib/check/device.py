from asyncsnmplib.mib.mib_index import MIB_INDEX
from libprobe.asset import Asset
from ..snmpclient import get_snmp_client
from ..snmpquery import snmpquery

QUERIES = (
    (MIB_INDEX['FUTURESMART-MIB']['id'], False),
    (MIB_INDEX['FUTURESMART-MIB']['settings-system'], False),
    (MIB_INDEX['FUTURESMART-MIB']['status-system'], False),
)


async def check_device(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:

    snmp = get_snmp_client(asset, asset_config, check_config)
    state = await snmpquery(snmp, QUERIES)
    return state
