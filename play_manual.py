from rl_game.racegame import RaceEnv

environment = RaceEnv()
# smoother controls
environment.car.ACCELERATION = 0.5
environment.car.TURN_ACCELERATION = 5
environment.init_render()
run = True

while run:
    # set game speed to 30 fps
    environment.clock.tick(30)
    # ─── CONTROLS ───────────────────────────────────────────────────────────────────
    # get pressed keys, generate action
    action = environment.pressed_to_action()
    # calculate one step
    new_state, reward, done = environment.step(action)
    # render current state
    environment.render()

pygame.quit()