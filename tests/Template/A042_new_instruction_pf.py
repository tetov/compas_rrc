from compas_rrc import *
from compas.geometry import Frame
from compas_fab.backends.ros import RosClient
import re
import time

if __name__ == '__main__':

    ros = RosClient()

    abb = AbbClient(ros)
    abb.run()
    print('Connected.')

    # Stop
    abb.send(Stop())
    result = abb.send_and_wait(Stop(feedback_level=1))

    # end of code
    print('Finished')

    abb.close()
    abb.terminate()

    time.sleep(3)
