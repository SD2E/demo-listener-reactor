import os
from attrdict import AttrDict
from reactors.utils import Reactor

SPECIAL_VARS_MAP = {'_abaco_actor_id': 'x_src_actor_id',
                    '_abaco_execution_id': 'x_src_execution_id',
                    'APP_ID': 'x_src_app_id',
                    'JOB_ID': 'x_src_job_id',
                    'EVENT': 'x_src_event',
                    'UUID': 'x_src_uuid',
                    '_event_uuid': 'x_external_event_id'}


def main():
    """Receive a message and provide as much debugging info as possible"""
    r = Reactor()
    m = AttrDict(r.context.message_dict)

    r.logger.info("Message: {}".format(m))
    r.logger.debug("Config: {}".format(r.settings))
    r.logger.debug("Raw Message: {}".format(r.context.raw_message))
    r.logger.debug("Parse Log: {}".format(r.context.raw_message_parse_log))

    # Look for sender tags
    for (k, v) in SPECIAL_VARS_MAP.items():
        if os.environ.get(v) is not None:
            r.logger.debug("tag {}: {}".format(v, os.environ.get(v)))


if __name__ == '__main__':
    main()
