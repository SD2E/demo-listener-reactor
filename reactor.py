import os
from attrdict import AttrDict
from reactors.utils import Reactor

SPECIAL_VARS_MAP = {'_abaco_actor_id': 'x_src_actor_id',
                    '_abaco_execution_id': 'x_src_execution_id',
                    'APP_ID': 'x_src_app_id',
                    'JOB_ID': 'x_src_job_id',
                    'EVENT': 'x_src_event',
                    'UUID': 'x_src_uuid',
                    '_event_uuid': 'x_session',
                    'SESSION': 'x_session'}


def main():
    """Receive a message and provide as much debugging info as possible"""
    r = Reactor()
    m = AttrDict(r.context.message_dict)
    aname = r.get_attr('name')

    r.logger.info("invoker.username: {}".format(r.username))

    r.logger.info("reactor.name: {}".format(aname))
    r.logger.info("reactor.session: {}".format(r.session))
    r.logger.info("reactor.nickname: {}".format(r.nickname))

    r.logger.info("parsed.message: {}".format(m))

    r.logger.debug("raw.message: {}".format(r.context.raw_message))
    r.logger.debug("parse.log: {}".format(
        r.context.raw_message_parse_log))

    # Log contents of os.environ
    for (k, v) in os.environ.items():
        r.logger.debug("{} = {}".format(k, v))


if __name__ == '__main__':
    main()
