import zmq

from volatilitybot.conf.config import DAEMON_ZMQ_FRONTEND, DAEMON_ZMQ_BACKEND


def launch_daemon():
    try:
        context = zmq.Context(1)
        # Socket facing clients
        frontend = context.socket(zmq.PULL)
        frontend.bind(DAEMON_ZMQ_FRONTEND)

        # Socket facing services
        backend = context.socket(zmq.PUSH)
        backend.bind(DAEMON_ZMQ_BACKEND)

        zmq.device(zmq.STREAMER, frontend, backend)
    except Exception as e:
        print('bringing down zmq device: '.format(e))
    finally:
        pass
        frontend.close()
        backend.close()
        context.term()


if __name__ == "__main__":
    launch_daemon()