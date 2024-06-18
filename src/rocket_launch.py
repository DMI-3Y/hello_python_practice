import time

def rocket_launch():
    stages = [
        ("Beginning preparation for rocket launch", 3),
        ("Main systems online", 2),
        ("Fuel tanks full", 2),
        ("Engines online", 2),
        ("Initiating the launch sequence", 2),
        ("Beginning countdown", 2),
        ("And 5...", 1),
        ("4...", 1),
        ("3...", 1),
        ("2...", 1),
        ("1!", 1),
        ("Liftoff! We have a liftoff!", 3),
        ("Clearing the tower", 5),
        ("Stage one separation", 3),
        ("Stage two ignition", 5),
        ("Leaving atmosphere", 3),
        ("Reaching orbit", 3),
        ("Orbit speed esablished", 1),
        ("Mission success", 0),

    ]

    for stage, delay in stages:
        print(stage)
        time.sleep(delay)  # Simulate time delay for each stage

if __name__ == "__main__":
    rocket_launch()
