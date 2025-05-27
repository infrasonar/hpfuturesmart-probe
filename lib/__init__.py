import time
from asyncsnmplib.mib.mib_index import MIB_INDEX
from asyncsnmplib.mib.syntax_funs import SYNTAX_FUNS


def on_date_and_time(value: bytes):
    '''
    date-and-time   OBJECT-TYPE
        SYNTAX          OCTET STRING
        ACCESS           read-write
        STATUS            optional
        DESCRIPTION "A C structure containing the following fields:  typedef
            struct {
                ubyte yr; /* year: 0 to 99 */
                ubyte mon; /* month: 1 to 12 */
                ubyte day; /* day: 1 to 31 */
                ubyte wday; /* Day of week: 1 to 07 */
                ubyte hr; /* hour: 0 to 23 */
                ubyte min; /* minute: 0 to 59 */
                ubyte sec; /* second: 0 to 59 */
                } date_t;
                where ubyte is an unsigned byte (0-255)."
        ::= { status-system 17 }
    '''
    try:
        return int(time.mktime((
            value[0] + 2000,
            value[1],
            value[2],
            value[3],
            value[4],
            value[5],
            value[6],
            0,
            -1,
        )))
    except Exception:
        return None


SYNTAX_FUNS['date-and-time'] = on_date_and_time

# patch the syntax function because we need the raw bytes for these metrics
MIB_INDEX[MIB_INDEX['FUTURESMART-MIB']['date-and-time']]['syntax'] = {
    'tp': 'CUSTOM', 'func': 'date-and-time',
}

DOCS_URL = 'https://docs.infrasonar.com/collectors/probes/snmp/hpfuturesmart/'
