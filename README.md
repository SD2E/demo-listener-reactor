# Listener

This Reactor listens for a message and verbosely logs its Reactor context when
it receives one. Importantly, it logs not just the message but all the sender
metadata that `reactors.utils.Reactor.send_message()` decorates inter-actor
messages with.

## Usage

This Reactor is usable by all SD2 program participants. Its alias is
`demo-listener` and its permissions are set to `EXECUTE` for the `world`
user. Here's a trivial example of `reactor.py` code:

```python
from reactors.utils import Reactor

r = Reactor()
exec_id = r.send_message(
    'demo-listener',
        {'text': 'Hello, Reactor. This is another Reactor calling.'})
r.logger('demo-listener launched execution id {}'.format(exec_id))
```

Now, here's an example log from `demo-listener` to illustrate what it looks on
the other end. Note the last two lines of the log, where the source actor and
execution id are reported. Agave apps and jobs are similarly integrated, making
it quite feasible to trace chains of invocation across components in your
workflow or pipeline.


```bash
2018-04-17T04:21:44Z [INFO] gO0JeWaBM4p3J:60YByl8WQlRY0 - Message: AttrDict({'text': 'Hello, Reactor. This is another Reactor calling.'})
2018-04-17T04:21:44Z [DEBUG] gO0JeWaBM4p3J:60YByl8WQlRY0 - Config: AttrDict({'logs': {'token': None, 'file': None, 'level': 'DEBUG'}})
2018-04-17T04:21:44Z [DEBUG] gO0JeWaBM4p3J:60YByl8WQlRY0 - Context: {'_abaco_jwt_header_name': 'X-Jwt-Assertion-Sd2E', 'REACTORS_VERSION': '0.6.1', '_abaco_actor_id': 'gO0JeWaBM4p3J', 'actor_dbid': 'SD2E_gO0JeWaBM4p3J', '_abaco_execution_id': '60YByl8WQlRY0', '_PROJ_CORRAL': '/corral', 'PATH': '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin', 'MSG': "{'text': 'Hello, Reactor. This is another Reactor calling.'}", 'HOME': '/', '_abaco_actor_state': '{}', 'execution_id': '60YByl8WQlRY0', 'raw_message_parse_log': '', '_abaco_api_server': 'https://api.sd2e.org', 'environment': 'x_src_execution_id', 'state': '{}', '_abaco_username': 'vaughn', '_USER_WORK': '', 'actor_id': 'gO0JeWaBM4p3J', 'x_src_execution_id': 'OmGPAq5arrlLo', 'username': 'vaughn', '_REACTOR_TEMP': '*****', 'raw_message': "{'text': 'Hello, Reactor. This is another Reactor calling.'}", 'content_type': None, '_PROJ_STOCKYARD': '/work/projects/', '_abaco_Content_Type': 'str', '_abaco_access_token': 'f38786f3605ba35edbb315a84e79e8f', 'message_dict': {'text': 'Hello, Reactor. This is another Reactor calling.'}, '_abaco_actor_dbid': 'SD2E_gO0JeWaBM4p3J', 'HOSTNAME': '3b4ba1516ace', 'x_src_actor_id': 'DkAVxzjYPqakV'}
2018-04-17T04:21:44Z [DEBUG] gO0JeWaBM4p3J:60YByl8WQlRY0 - Raw Message: {'text': 'Hello, Reactor. This is another Reactor calling.'}
2018-04-17T04:21:44Z [DEBUG] gO0JeWaBM4p3J:60YByl8WQlRY0 - Parse Log:
2018-04-17T04:21:44Z [DEBUG] gO0JeWaBM4p3J:60YByl8WQlRY0 - tag x_src_execution_id: OmGPAq5arrlLo
2018-04-17T04:21:44Z [DEBUG] gO0JeWaBM4p3J:60YByl8WQlRY0 - tag x_src_actor_id: DkAVxzjYPqakV
```

