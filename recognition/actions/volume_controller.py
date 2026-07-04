from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL


class VolumeController:

    def __init__(self):

        devices = AudioUtilities.GetSpeakers()

        interface = devices.Activate(
            IAudioEndpointVolume._iid_,
            CLSCTX_ALL,
            None,
        )

        self.volume = cast(
            interface,
            POINTER(IAudioEndpointVolume),
        )

    def increase(self):

        current = self.volume.GetMasterVolumeLevelScalar()

        self.volume.SetMasterVolumeLevelScalar(
            min(current + 0.05, 1.0),
            None,
        )

    def decrease(self):

        current = self.volume.GetMasterVolumeLevelScalar()

        self.volume.SetMasterVolumeLevelScalar(
            max(current - 0.05, 0.0),
            None,
        )

    def mute(self):

        self.volume.SetMute(
            1,
            None,
        )