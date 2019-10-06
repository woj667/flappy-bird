class Settings:
    def __init__(self):
        # Screen properties
        self.screen_width = 400
        self.screen_height = 708
        self.screen_caption = "Flappy flap flap."
        self.frames_per_second = 60

        # time [ms] between frames, updated in main loop
        self.dt = 0

        # Bird properties
        self.flap_vel = 6.5  # [px/s]
        self.flap_angle = 90  # [degree]
        self.flap_time = 0.3  # [s]

        self.bird_centerx = 75
        self.bird_centery = int(0.75 * self.screen_height)

        # Pipes properties
        self.pipe_speed = 3
        self.pipe_interval = 3000  # [ms]
        self.pipe_gap = 150  # [px]

        # Environment properties
        self.gravity = 9.8  # [px/s^2]
