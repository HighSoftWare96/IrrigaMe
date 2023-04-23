import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

class TankLevel:
    def __init__(self, min_distance, max_distance, trigger_pin_out, echo_pin_in, hc_speed=34300):
        self.trigger_pin_out = trigger_pin_out
        self.echo_pin_in = echo_pin_in
        self.distance_interval = max_distance - min_distance
        self.hc_speed = hc_speed
        
    def __del__(self):
        GPIO.cleanup()

    def measure_one(self):
        GPIO.output(self.trigger_pin_out, True)
        time.sleep(0.00001)
        GPIO.output(self.trigger_pin_out, False)

        start = time.time()

        while GPIO.input(self.echo_pin_in) == 0:
            start = time.time()

        while GPIO.input(self.echo_pin_in) == 1:
            stop = time.time()

        elapsed = stop - start
        distance = (elapsed * self.hc_speed) / 2

        return distance
      
    def measure_samples(self, samples_count = 5):
        result = 0
        for _ in range(0, samples_count):
          result += self.measure_one()
        return result / samples_count

    def measure_percentage(self, samples_count = 1):
        average = self.measure_samples(samples_count)
        return (average / self.distance_interval) * 100
