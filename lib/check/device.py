from asyncsnmplib.mib.mib_index import MIB_INDEX
from libprobe.asset import Asset
from libprobe.exceptions import CheckException
from ..snmpclient import get_snmp_client
from ..snmpquery import snmpquery

QUERIES = (
    (MIB_INDEX['FUTURESMART-MIB']['consumables'], False),
    (MIB_INDEX['FUTURESMART-MIB']['id'], False),
    (MIB_INDEX['FUTURESMART-MIB']['printer-accounting'], False),
    (MIB_INDEX['FUTURESMART-MIB']['settings-system'], False),
    (MIB_INDEX['FUTURESMART-MIB']['status-system'], False),
)


async def check_device(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:

    snmp = get_snmp_client(asset, asset_config, check_config)
    state = await snmpquery(snmp, QUERIES)

    if not any(state.values()):
        raise CheckException('no data found')

    for item in state.get('printer-accounting', []):
        item.pop('print-meter-equivalent-impression-count', None)
        item.pop('usage-instructions-line1', None)
        item.pop('usage-instructions-line2', None)
        item.pop('usage-instructions-line3', None)
        item.pop('usage-instructions-line4', None)

    return state
